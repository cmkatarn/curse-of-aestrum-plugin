#!/usr/bin/env python3
"""Curse of Aestrum plugin assembler.

Reads the five source repos (CoA + Calliope/Aria/Bailly/fiction-host), and emits a
self-contained, path-portable Claude Code plugin under ../plugins/curse-of-aestrum/.

Path portability (see the plan's M0 RESULT): an installed plugin's skills get
${CLAUDE_PLUGIN_ROOT} expanded, but transitively-read files do NOT — and relative paths inside
them resolve against the session CWD, not the file. So every cross-file reference in every
bundled file is rewritten to a sentinel — {{PLUGIN_ROOT}}/<plugin-relative-path> for bundle reads,
{{PROJECT_ROOT}}/campaign_state/... for play-state — and each skill gets a preamble mapping the two
sentinels to ${CLAUDE_PLUGIN_ROOT} / ${CLAUDE_PROJECT_DIR}. The model substitutes them at every hop
(validated by spike v2).

Reference resolution: a ref is resolved in SOURCE space against the right base — the CoA project
root for CoA skills (their documented convention), the file's own directory otherwise — then mapped
through SOURCE_MAP to its vendored plugin location. Refs that don't map to a bundled file are logged.

Run:  py build/assemble.py
"""

from __future__ import annotations

import hashlib
import os
import re
import shutil
from datetime import datetime
from pathlib import Path

# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #

HERE = Path(__file__).resolve().parent            # <plugin-repo>/build
# Source repos are siblings of the plugin repo (…/Documents/{curse-of-aestrum-plugin,CurseOfAestrum,
# prose-engine,…}); override with COA_SRC if they live elsewhere.
DOCS = Path(os.environ.get("COA_SRC") or HERE.parent.parent)
COA = DOCS / "CurseOfAestrum"
OUT = HERE.parent / "plugins" / "curse-of-aestrum"  # the generated installable plugin

# source-tree -> plugin-relative-root. Order matters (skills before the CoA catch-all).
SOURCE_MAP: list[tuple[Path, str]] = [
    (COA / ".claude" / "skills", "skills"),
    (COA, ""),                                    # CoA content at plugin root
    (DOCS / "prose-engine", "engines/prose-engine"),
    (DOCS / "story-engine", "engines/story-engine"),
    (DOCS / "rpg-5e-engine", "engines/rpg-5e-engine"),
    (DOCS / "fiction-host", "engines/fiction-host"),
]

# What to copy: (src_dir_relative_to_its_repo_root, repo_root, dst_relative_to_OUT).
# Chapter-2 + private state excluded via EXCLUDE_DIRS / the chapter filter.
COPY_SPECS: list[tuple[Path, str]] = [
    # (source path, plugin-relative destination)
    (COA / ".claude" / "skills", "skills"),
    (COA / "overrides", "overrides"),
    (COA / "rules", "rules"),
    (COA / "lore", "lore"),
    (COA / "timelines", "timelines"),
    (COA / "locations", "locations"),
    (COA / "npcs", "npcs"),
    (COA / "factions", "factions"),
    (COA / "items", "items"),
    (COA / "quests", "quests"),
    (COA / "party", "party"),
    (COA / "scripts" / "flush_campaign_staging.py", "scripts/flush_campaign_staging.py"),
    (DOCS / "prose-engine" / "scene", "engines/prose-engine/scene"),
    (DOCS / "prose-engine" / "CONTRACT.toml", "engines/prose-engine/CONTRACT.toml"),
    (DOCS / "story-engine" / "rules", "engines/story-engine/rules"),
    (DOCS / "story-engine" / "FRONTMATTER.md", "engines/story-engine/FRONTMATTER.md"),
    (DOCS / "story-engine" / "CONTRACT.toml", "engines/story-engine/CONTRACT.toml"),
    (DOCS / "rpg-5e-engine" / "create-character", "engines/rpg-5e-engine/create-character"),
    (DOCS / "rpg-5e-engine" / "create-party", "engines/rpg-5e-engine/create-party"),
    (DOCS / "rpg-5e-engine" / "rules", "engines/rpg-5e-engine/rules"),
    (DOCS / "rpg-5e-engine" / "CONTRACT.toml", "engines/rpg-5e-engine/CONTRACT.toml"),
    (DOCS / "fiction-host" / "claude_code_gate", "engines/fiction-host/claude_code_gate"),
    # Only what play-time tooling imports: runtime.lint for the gate hooks, runtime.state for the
    # save flush (+ the package marker). NOT the LLM backends / dispatch — those are for the
    # standalone host and are unneeded here.
    (DOCS / "fiction-host" / "runtime" / "__init__.py", "engines/fiction-host/runtime/__init__.py"),
    (DOCS / "fiction-host" / "runtime" / "lint", "engines/fiction-host/runtime/lint"),
    # state.py is stdlib-only and holds append_delta, the one writer of the overlay byte format.
    # scripts/flush_campaign_staging.py calls it rather than reimplementing it, so the format has
    # exactly one implementation across the plugin and the standalone host.
    (DOCS / "fiction-host" / "runtime" / "state.py", "engines/fiction-host/runtime/state.py"),
    # The integrity checkers: stdlib-only, so they vendor without pulling the host in.
    # Their CLI is build/assets/plugin_runtime_main.py (see emit_runtime_main), NOT
    # fiction-host's own __main__, which imports the whole engine/backends chain.
    (DOCS / "fiction-host" / "runtime" / "refcheck.py", "engines/fiction-host/runtime/refcheck.py"),
    (DOCS / "fiction-host" / "runtime" / "entitycheck.py", "engines/fiction-host/runtime/entitycheck.py"),
]
ROOT_FILES = ["entitycheck.toml", "refcheck.toml"]   # CoA root files -> plugin root

# Never copy these directory names, anywhere.
EXCLUDE_DIRS = {"chapter_2", "campaign_state", "__pycache__", ".git", "analysis",
                "Photos", "badges", "paper", "prior_art", "tests"}
# Never copy these exact file names.
EXCLUDE_FILES = {"settings.local.json", "settings.json"}
# Only these extensions are rewritten/copied as text; others copied as-is if under an allowed tree.
TEXT_EXT = {".md", ".toml", ".py", ".sh", ".json", ".txt"}

REWRITE_LOG: list[str] = []
UNMAPPED: dict[str, int] = {}


# --------------------------------------------------------------------------- #
# Source -> plugin mapping
# --------------------------------------------------------------------------- #

def map_source_to_plugin(abs_src: Path) -> str | None:
    """Return the plugin-relative path a source file will be vendored to, or None."""
    abs_src = abs_src.resolve()
    for root, dst in SOURCE_MAP:
        root = root.resolve()
        try:
            rel = abs_src.relative_to(root)
        except ValueError:
            continue
        return (dst + "/" + rel.as_posix()).lstrip("/")
    return None


def is_coa_skill(src_file: Path) -> bool:
    try:
        src_file.resolve().relative_to((COA / ".claude" / "skills").resolve())
        return True
    except ValueError:
        return False


# --------------------------------------------------------------------------- #
# Reference rewriting
# --------------------------------------------------------------------------- #

_PATH_EXT = (".md", ".toml", ".py", ".sh", ".json")
_SKIP_PREFIX = ("{{", "http://", "https://", "mailto:", "$")
_ENGINE_NAMES = "prose-engine|story-engine|rpg-5e-engine|fiction-host|CurseOfAestrum"


def resolve_ref(token: str, bases: list[Path]) -> str | None:
    """Turn one path token into its sentinel form, or None to leave it as-is.

    A ref is resolved against each base in turn (the file's own dir AND the CoA project root —
    CoA files mix both conventions: `../engine` is root-relative, `../../engine` link targets are
    file-relative) and the first candidate that is an existing source file wins. Play-state ->
    {{PROJECT_ROOT}}; bundled files -> {{PLUGIN_ROOT}}; anchors/urls/snippets/shorthand -> None.
    """
    frag = ""
    if "#" in token and not token.startswith("#"):
        token, _, rest = token.partition("#")
        frag = "#" + rest
    if not token or token.startswith(_SKIP_PREFIX):
        return None
    if token.startswith("campaign_state/") or token == "campaign_state":
        return "{{PROJECT_ROOT}}/" + token + frag
    if not (token.endswith(_PATH_EXT) or token.startswith("../")):
        return None                                       # not a file path (e.g. `groups: []`)
    cs = (COA / "campaign_state").resolve()
    for base in bases:
        target = (base / token).resolve()
        try:                                              # play-state via a relative path
            rel = target.relative_to(cs)
            return "{{PROJECT_ROOT}}/campaign_state/" + rel.as_posix() + frag
        except ValueError:
            pass
        # Directories count, not just files: prose cites trees as often as leaves
        # (`../rpg-5e-engine/rules/`, `../rules/`). An is_file() test silently left
        # every such mention pointing at a sibling layout that does not exist in the
        # bundle — the reader is told to look somewhere the plugin has no path to.
        if target.exists():
            plug = map_source_to_plugin(target)
            if plug is not None:
                return "{{PLUGIN_ROOT}}/" + plug + frag
    if token.startswith("../"):                           # looked like a ref, resolved to nothing
        UNMAPPED[token] = UNMAPPED.get(token, 0) + 1
    return None                                           # shorthand / display text — leave


_MD_LINK = re.compile(r"\[([^\]\n]*)\]\(([^)\s]+)\)")
_INLINE_CODE = re.compile(r"`([^`\n]+)`")
_BARE_ENGINE = re.compile(r"(?:\.\./)+(?:" + _ENGINE_NAMES + r")/[\w./-]+\.\w+")
# A fenced command block is not inline code and not a markdown link, so neither of the wrapped
# rewriters sees the script path in the save invocation. Left bare it resolved against the player's
# own working directory at play time, where `scripts/` does not exist — the save step pointed at
# nothing on every platform. Matched anywhere in the text, like the campaign_state rule below.
_BARE_SCRIPT = re.compile(r"(?<![\w/{`($.-])scripts/[\w.-]+\.py\b")
_BARE_STATE = re.compile(r"(?<![\w/{`($])campaign_state/[\w./<>*-]+")


def rewrite_text(text: str, src_file: Path) -> str:
    bases = [src_file.parent, COA]
    # Scrub the dev absolute CoA path — a username leak, and in the plugin the CoA content root
    # IS the plugin root.
    coa = str(COA)
    text = text.replace(coa, "{{PLUGIN_ROOT}}").replace(coa.replace("\\", "/"), "{{PLUGIN_ROOT}}")

    def repl(inner: str, wrap):
        r = resolve_ref(inner, bases)
        return wrap(r if r is not None else inner)

    def link_repl(m: "re.Match[str]") -> str:
        label, href = m.group(1), m.group(2)
        r = resolve_ref(href, bases)
        new_href = r if r is not None else href
        # Rewrite the LABEL too when it is itself a sibling-relative path. The href
        # is what the model follows, but the label is what a human reads — leaving
        # `[../rules/x.md]({{PLUGIN_ROOT}}/rules/x.md)` renders as a path that does
        # not exist in the bundle. Only `../`-style labels are touched: a plain
        # `[rules/x.md](…)` label is ordinary display text and stays readable.
        inner = label.strip("`")
        if inner.startswith("../"):
            # A label may be a bare path, or a path followed by a section title
            # ("…/core.md § Some Heading"). Rewrite only the leading path token so
            # the human-readable remainder survives intact.
            head, sep, tail = inner.partition(" ")
            lr = resolve_ref(head, bases)
            if lr is not None:
                inner = lr + sep + tail
                label = f"`{inner}`" if label.startswith("`") else inner
        return f"[{label}]({new_href})"

    text = _MD_LINK.sub(link_repl, text)
    text = _INLINE_CODE.sub(lambda m: repl(m.group(1), lambda s: f"`{s}`"), text)
    # belt-and-suspenders: un-wrapped engine escapes / campaign_state mentions in prose
    text = _BARE_ENGINE.sub(lambda m: resolve_ref(m.group(0), bases) or m.group(0), text)
    text = _BARE_STATE.sub(lambda m: "{{PROJECT_ROOT}}/" + m.group(0), text)
    text = _BARE_SCRIPT.sub(lambda m: "{{PLUGIN_ROOT}}/" + m.group(0), text)
    return text


SKILL_PREAMBLE = """\
> **Plugin path resolution — read this first.** You are running inside an installed plugin. Two
> placeholders appear in this skill and in every file it leads you to read:
> `{{PLUGIN_ROOT}}` = `${CLAUDE_PLUGIN_ROOT}` (this plugin's bundled files — engines, rules,
> overrides, and campaign content) and `{{PROJECT_ROOT}}` = `${CLAUDE_PROJECT_DIR}` (the player's
> own working directory, where every `campaign_state/…` play-state file is read and written).
> Whenever any file you read contains a `{{PLUGIN_ROOT}}/…` or `{{PROJECT_ROOT}}/…` path, replace
> the placeholder with the absolute path shown above and read/write that. **Never** resolve these
> against the working directory or a file's own folder, and never write into `{{PLUGIN_ROOT}}`.

"""


def inject_preamble(text: str) -> str:
    """Insert the sentinel preamble just after a skill's YAML frontmatter."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            nl = text.find("\n", end + 1)
            head, tail = text[: nl + 1], text[nl + 1 :]
            return head + "\n" + SKILL_PREAMBLE + tail
    return SKILL_PREAMBLE + text


# --------------------------------------------------------------------------- #
# Copy + transform
# --------------------------------------------------------------------------- #

def excluded(p: Path) -> bool:
    parts = set(p.parts)
    return bool(parts & EXCLUDE_DIRS) or p.name in EXCLUDE_FILES


def process_file(src: Path, dst: Path, is_skill_md: bool) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    # Only Markdown is model-read, so only Markdown gets sentinel-rewritten. Executed code
    # (.py/.sh) and tool configs (.toml/.json) ship verbatim — their paths come from CLI args /
    # env at invocation (hooks.json, --config), handled when those are wired, not by substitution.
    if src.suffix.lower() == ".md":
        text = src.read_text(encoding="utf-8")
        text = rewrite_text(text, src)
        if is_skill_md and src.name == "SKILL.md":
            text = inject_preamble(text)
        dst.write_text(text, encoding="utf-8", newline="\n")
    else:
        shutil.copy2(src, dst)


def copy_spec(src: Path, dst_rel: str) -> int:
    n = 0
    dst_base = OUT / dst_rel
    if src.is_file():
        if not excluded(src):
            process_file(src, dst_base, is_skill_md=False)
            n += 1
        return n
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        rootp = Path(root)
        for f in files:
            sp = rootp / f
            if excluded(sp):
                continue
            rel = sp.relative_to(src)
            dp = dst_base / rel
            is_skill = dst_rel == "skills"
            process_file(sp, dp, is_skill_md=is_skill)
            n += 1
    return n


import json

PLUGIN_NAME = "curse-of-aestrum"

# Version scheme: <major>.<minor>.<YYYYMMDD><NN>  e.g. 0.2.2026090901
#
# Claude Code caches an installed plugin under
# .claude/plugins/cache/<marketplace>/<plugin>/<version>/, so the version IS the cache key: a
# rebuild that reuses it lands in a directory already holding the old files and `/plugin update`
# has nothing new to key on. Deriving the patch from the build date + a daily counter means every
# rebuild is uniquely keyed without anyone having to remember to bump anything.
#
# Date and build are deliberately concatenated into ONE component rather than split into a fourth.
# The field is not semver-validated (Anthropic's own claude-security ships "0.10.2.3"), but a
# 3-component numeric form stays sortable under BOTH a real semver comparison and a naive string
# comparison — and the leading year digit guarantees no leading zero. A 4-component form would read
# better and parse as semver not at all.
#
# MAJOR/MINOR are the hand-set part: bump them for a real release. The patch takes care of itself.
#
# The version moves ONLY when the bundle's content actually moved. A rebuild that reproduces a
# byte-identical bundle keeps the version it had: the version is the installed side's cache key, so
# bumping it for an unchanged bundle makes every consumer re-download the same 200-odd files, and
# it turns "did this rebuild do anything?" into a question only a diff can answer. To make that
# comparison possible the build runs with the PRIOR version in the manifest, and the real version
# is decided at the end, in finalize_version(), once the content is known.
PLUGIN_MAJOR_MINOR = "0.2"
_VERSION_RE = re.compile(r"\d+\.\d+\.(\d{8})(\d{2})\Z")
PLUGIN_VERSION = ""          # set by main(), before OUT is cleared


def read_prior_version() -> str | None:
    """The version the previous build wrote, or None if there is no readable prior bundle.

    Must be called before main() clears OUT.
    """
    prior = OUT / ".claude-plugin" / "plugin.json"
    if not prior.exists():
        return None
    try:
        return json.loads(prior.read_text(encoding="utf-8")).get("version") or None
    except (OSError, ValueError):
        return None                                   # malformed prior manifest -> treat as absent


def next_version(prior: str | None) -> str:
    """Same day -> increment the counter; new day, or no parseable prior -> start at 01.

    Restarting the count on an absent, legacy, or malformed prior is safe: the date component
    alone already distinguishes this build from every build before today.
    """
    today = datetime.now().strftime("%Y%m%d")
    build = 1
    m = _VERSION_RE.match(prior or "")
    if m and m.group(1) == today:
        build = int(m.group(2)) + 1
    if build > 99:
        raise SystemExit("assemble: 99 builds today already; bump PLUGIN_MAJOR_MINOR to continue")
    return f"{PLUGIN_MAJOR_MINOR}.{today}{build:02d}"


def fingerprint(root: Path) -> dict[str, str]:
    """plugin-relative path -> sha256 of its bytes, for every file under root.

    The assembler is deterministic — nothing but the version carries a timestamp — so two
    fingerprints differ if and only if the sources did.

    Bytecode caches are excluded. The build clears OUT, so a __pycache__ only exists because
    something RAN the bundled Python between builds — testing a hook or the flush script does it.
    Counting those made the next build report a change and bump the version with no source edit
    behind it, which is exactly the question this fingerprint exists to answer.
    """
    if not root.exists():
        return {}
    return {f.relative_to(root).as_posix(): hashlib.sha256(f.read_bytes()).hexdigest()
            for f in sorted(root.rglob("*"))
            if f.is_file() and "__pycache__" not in f.parts}


def finalize_version(prior_fp: dict[str, str], prior_version: str | None) -> bool:
    """Compare the fresh bundle against the previous one; bump the version only if it moved.

    The build wrote the prior version into the manifest, so an unchanged bundle is already
    byte-identical and needs no further action. A changed one gets the next version stamped into
    plugin.json, the only file this rewrites. Returns True if the bundle changed.
    """
    global PLUGIN_VERSION
    new_fp = fingerprint(OUT)
    changed = sorted(p for p in new_fp.keys() & prior_fp.keys() if new_fp[p] != prior_fp[p])
    added = sorted(new_fp.keys() - prior_fp.keys())
    removed = sorted(prior_fp.keys() - new_fp.keys())

    if prior_fp and not (changed or added or removed):
        print("\n  NO CHANGES - this rebuild reproduced the previous bundle exactly.")
        print("  Nothing in the plugin was modified by this run.")
        print(f"  Version stays {PLUGIN_VERSION}. There is nothing to commit, publish, or")
        print("  update on an installed copy.")
        return False

    for label, paths in (("changed", changed), ("added", added), ("removed", removed)):
        if not paths:
            continue
        print(f"\n  {len(paths)} {label}:")
        for path in paths[:10]:
            print(f"    {path}")
        if len(paths) > 10:
            print(f"    ... and {len(paths) - 10} more")

    PLUGIN_VERSION = next_version(prior_version)
    manifest = OUT / ".claude-plugin" / "plugin.json"
    data = json.loads(manifest.read_text(encoding="utf-8"))
    data["version"] = PLUGIN_VERSION
    manifest.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"\n  VERSION  {prior_version or '(new bundle)'} -> {PLUGIN_VERSION}")
    return True
DESCRIPTION = ("Curse of Aestrum — an interactive Dungeons & Dragons 5e campaign. Arrive in the "
               "duchy of Aestrum, where something is deeply and secretly wrong. Chapter 1. "
               "For adults: mature themes throughout, with a content rating chosen per session "
               "(T / M / AO; M by default, T the floor).")
AUTHOR = "Cody Mallonee"
AUTHOR_URL = "https://github.com/cmkatarn"
REPOSITORY = "https://github.com/cmkatarn/curse-of-aestrum-plugin"
# HOMEPAGE is where a player lands for requirements, the rating scale, and how to start a game;
# REPOSITORY is the source tree and the issue tracker. Distinct targets, so both fields earn a slot.
HOMEPAGE = f"{REPOSITORY}/tree/main/plugins/curse-of-aestrum"
ISSUES_URL = f"{REPOSITORY}/issues"
MARKETPLACE_DESCRIPTION = ("Home of Curse of Aestrum — an interactive Dungeons & Dragons 5e "
                           "campaign played in Claude Code, with the prose, story, and 5e engines "
                           "it runs on bundled in.")
DONATION_URL = "https://ko-fi.com/cmkatarn"   # empty suppresses the README's Support section entirely


def _cmd(s: str) -> dict:
    return {"type": "command", "command": s}


NOTES_RE = (r"^\*\*Content notes \(subject, not intensity\)\.\*\*"
            r".*?(?=\n\s*\n\*\*)")


def extract_rating_block() -> tuple[str, str, str]:
    """Lift the T/M/AO table, hard limits, and content notes verbatim from CoA's scene override.

    overrides/scene.md is the single source of truth for the rating scale. The plugin README
    restates it for anyone deciding whether to install, so it is *extracted* rather than
    paraphrased — a paraphrase drifts the moment the scale is edited. Hard-fails if the section
    shape changes, so the README can never ship with a hole where the ratings should be.
    """
    src = COA / "overrides" / "scene.md"
    section = re.search(r"^## Content rating system$(.*?)^## ", src.read_text(encoding="utf-8"),
                        re.M | re.S)
    if not section:
        raise SystemExit(f"assemble: no '## Content rating system' section in {src}")

    table = re.search(r"^\| Rating \|.*?(?=\n\s*\n)", section.group(1), re.M | re.S)
    if not table:
        raise SystemExit(f"assemble: no '| Rating |' table under 'Content rating system' in {src}")

    limits = re.search(r"^\*\*Hard limits regardless of rating:\*\*.*?(?=\n\s*\n\*\*)",
                       section.group(1), re.M | re.S)
    if not limits:
        raise SystemExit(f"assemble: no hard-limits list under 'Content rating system' in {src}")

    notes = re.search(NOTES_RE, section.group(1), re.M | re.S)
    if not notes:
        raise SystemExit(f"assemble: no content-notes block under 'Content rating system' in {src}")

    return table.group(0).strip(), limits.group(0).strip(), notes.group(0).strip()


_DECL_ID = re.compile(r"^\s*(?:\*\*)?id:?(?:\*\*)?:?\s*([a-z][a-z0-9_]*)", re.M | re.I)


def ids_declared_in_excluded_trees() -> list[str]:
    """Entity ids that exist in CoA canon but are not bundled.

    Chapter-1 content forward-references Chapter-2 entities as a matter of correct
    authoring — a faction's roster names the pieces it will play, a Chapter-1 duchy
    names its duke. Those ids are declared under `npcs/chapter_2/…`, which
    EXCLUDE_DIRS keeps out of a Chapter-1 bundle, so entitycheck sees the reference
    with no declaration behind it.

    Neither alternative is acceptable: bundling Chapter-2 stubs would ship next-chapter
    identities into a Chapter-1 plugin (against the campaign's own spoiler discipline),
    and stripping the references would make the bundle assert something false about its
    own canon — a faction with fewer members than it has.

    So the ids are declared as intentional soft pointers. Derived, not hand-listed, so
    it cannot drift; and because only ids that genuinely ARE declared in an excluded
    tree are collected, a typo'd reference still fails the check rather than being
    quietly absorbed.
    """
    found: set[str] = set()
    for md in COA.rglob("*.md"):
        parts = set(md.relative_to(COA).parts)
        if not (parts & EXCLUDE_DIRS) or "campaign_state" in parts:
            continue
        try:
            found.update(_DECL_ID.findall(md.read_text(encoding="utf-8")))
        except OSError:
            continue
    if not found:
        return []
    # Keep only what the bundle actually points at. An excluded chapter declares far
    # more than Chapter 1 reaches for, and a soft_id nothing references is dead
    # config that quietly widens what the checker will forgive.
    bundled = "\n".join(
        p.read_text(encoding="utf-8", errors="ignore") for p in OUT.rglob("*.md"))
    return sorted(i for i in found if i in bundled)


def emit_runtime_main() -> None:
    """Install the plugin-only checker CLI as `runtime.__main__`.

    fiction-host's own `__main__` dispatches the entire host (engine, backends,
    config, spec_drift) and imports that whole chain. The plugin vendors only the
    two stdlib-only checkers, so it gets a purpose-built entrypoint exposing just
    `refcheck` and `entitycheck`. Kept as a build asset rather than inlined here so
    it stays readable and lintable as ordinary Python.
    """
    src = HERE / "assets" / "plugin_runtime_main.py"
    dst = OUT / "engines/fiction-host/runtime/__main__.py"
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"  emitted        engines/fiction-host/runtime/__main__.py")


def retarget_checker_configs() -> None:
    """Rewrite the copied refcheck.toml for the bundled layout.

    refcheck.toml is authored for the SOURCE workspace, where the engines are
    sibling repos (`../prose-engine`). In the bundle they are vendored beneath the
    config itself, so the roots and every engine pin must be retargeted — and the
    scan roots collapse to "." because the engines are now inside it.

    Also declares what is dangling *by design* here: chapter_2 content is excluded
    from a Chapter-1 plugin (EXCLUDE_DIRS), so chapter_1 links into it cannot
    resolve and must not be reported as breakage.
    """
    # Both configs document how to invoke them, against the SOURCE checkout
    # ("--config ../CurseOfAestrum/..."). In the bundle the config sits at the
    # plugin root and the runtime is vendored beneath it.
    for name in ("refcheck.toml", "entitycheck.toml"):
        c = OUT / name
        if not c.exists():
            continue
        s = c.read_text(encoding="utf-8")
        s = s.replace(
            f"# Run:  py -m runtime {name[:-5]} --config ../CurseOfAestrum/{name}",
            "# Run, from the plugin's engines/fiction-host directory:\n"
            f"#   py -m runtime {name[:-5]} --config <plugin-root>/{name}")
        s = s.replace("(../story-engine/rules/authoring_entities.md",
                      "(engines/story-engine/rules/authoring_entities.md")
        if name == "entitycheck.toml":
            extra = ids_declared_in_excluded_trees()
            if extra:
                block = "\n".join(f'  "{i}",' for i in extra)
                s = s.replace(
                    '  "loc_aestrum", "loc_setland", "loc_aestrum_boundary",\n',
                    '  "loc_aestrum", "loc_setland", "loc_aestrum_boundary",\n'
                    '  # Declared in CoA canon but not bundled here: Chapter-1 content\n'
                    '  # forward-references Chapter-2 entities, and chapter_2/** is excluded\n'
                    '  # from this bundle. Generated by build/assemble.py - do not hand-edit.\n'
                    + block + "\n")
                print(f"  soft-declared  {len(extra)} ids from excluded chapters")
        c.write_text(s, encoding="utf-8")

    cfg = OUT / "refcheck.toml"
    if not cfg.exists():
        return
    t = cfg.read_text(encoding="utf-8")
    t = t.replace(
        'roots = [".", "../prose-engine", "../rpg-5e-engine", "../story-engine"]',
        '# Engines are vendored beneath this file, so "." already covers them.\nroots = ["."]')
    for eng in ("prose-engine", "rpg-5e-engine", "story-engine"):
        t = t.replace(f'path = "../{eng}"', f'path = "engines/{eng}"')
    # Anything in EXCLUDE_DIRS is deliberately absent from the bundle, so links
    # into it dangle by design rather than by error. Derive the soft-pointer globs
    # from that set so the two cannot drift apart: add a directory to EXCLUDE_DIRS
    # and its inbound links stay correctly unreported without a second edit here.
    # (campaign_state is already covered by the saved/* conventions.)
    soft = [f'"*{d}/*"' for d in sorted(EXCLUDE_DIRS)
            if d not in {"campaign_state", "__pycache__", ".git"}]
    t = t.replace(
        'ignore_targets = ["saved/*", "*/saved/*"]',
        '# Trees excluded from this bundle (see EXCLUDE_DIRS in build/assemble.py):\n'
        '# links into them are intentional soft pointers, not breakage.\n'
        'ignore_targets = ["saved/*", "*/saved/*", ' + ", ".join(soft) + ']')
    cfg.write_text(t, encoding="utf-8")
    print("  retargeted     refcheck.toml (bundled engine layout)")


def write_meta() -> None:
    root = "${CLAUDE_PLUGIN_ROOT}"
    proj = "${CLAUDE_PROJECT_DIR}"
    gate = f"{root}/engines/fiction-host/claude_code_gate"

    (OUT / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    (OUT / ".claude-plugin" / "plugin.json").write_text(json.dumps({
        "name": PLUGIN_NAME,
        "version": PLUGIN_VERSION,
        "description": DESCRIPTION,
        "author": {"name": AUTHOR, "url": AUTHOR_URL},
        "homepage": HOMEPAGE,
        "repository": REPOSITORY,
        "keywords": ["dnd", "dnd5e", "ttrpg", "rpg", "interactive-fiction", "campaign"],
    }, indent=2) + "\n", encoding="utf-8")

    # Every hook goes through run_hook.sh rather than naming an interpreter: one manifest string is
    # shared by every platform, and `py` exists only on Windows while `python3` exists only off it.
    # The wrapper resolves it at play time on the machine that knows. See its header for the detail.
    launch = f'sh "{gate}/run_hook.sh"'
    hooks = {
        "hooks": {
            "UserPromptSubmit": [{"matcher": "*", "hooks": [
                _cmd(f'{launch} "{gate}/gate_prompt_hook.py"')]}],
            "Stop": [{"matcher": "*", "hooks": [
                _cmd(f'{launch} "{gate}/gate_stop_hook.py"'
                     f' --spec "{root}/engines/prose-engine/scene/gate/infrastructure_tokens.toml"'
                     f' --spec "{root}/engines/rpg-5e-engine/rules/player_meta_tokens.toml"'
                     f' --spec "{root}/overrides/gate_lint/forbidden_tokens.toml"'),
                _cmd(f'{launch} "{gate}/staging_stop_hook.py"'
                     f' --staging-glob "{proj}/campaign_state/*/staging/*.md"'),
            ]}],
        }
    }
    (OUT / "hooks").mkdir(parents=True, exist_ok=True)
    (OUT / "hooks" / "hooks.json").write_text(json.dumps(hooks, indent=2) + "\n", encoding="utf-8")

    # marketplace.json lives at the plugin-repo root, not inside the plugin.
    repo_root = HERE.parent
    (repo_root / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    (repo_root / ".claude-plugin" / "marketplace.json").write_text(json.dumps({
        "name": PLUGIN_NAME,
        "description": MARKETPLACE_DESCRIPTION,
        "owner": {"name": AUTHOR, "url": AUTHOR_URL},
        "plugins": [{"name": PLUGIN_NAME, "source": "./plugins/curse-of-aestrum",
                     "description": DESCRIPTION,
                     "author": {"name": AUTHOR, "url": AUTHOR_URL},
                     "homepage": HOMEPAGE,
                     "repository": REPOSITORY}],
    }, indent=2) + "\n", encoding="utf-8")

    # An installed player has no repo context — the marketplace id they typed is long gone from
    # their scrollback - so the bundled README is the only place a bug channel can reach them, and
    # the only place the model can read one out of when they ask mid-session.
    bugs = f"""
## Bugs & feedback

Found a bug, a dead link, or a scene that went sideways? Open an issue:
**[{ISSUES_URL.split("://", 1)[-1]}]({ISSUES_URL})**

A useful report names the skill you were running (`scene`, `create-party`, …), the version from
`claude plugin details {PLUGIN_NAME}`, and what you expected instead. Your play-state lives in your
own `campaign_state/` folder, so paste from it only what the report needs — an issue is public.
"""
    # Tip jar, not a paywall: the link gates nothing, and saying so in the README is what keeps
    # it readable as a thank-you rather than a storefront.
    donation_label = DONATION_URL.split("://", 1)[-1].rstrip("/")
    support = f"""
## Support

The campaign is free and will stay that way. That being said, it is a one-person project — the
campaign, the (massive) bundled engines, and the build that assembles them — so if you enjoy your
time in Aestrum and want to say thanks, consider donating here:
**[{donation_label}]({DONATION_URL})**. Any contribution is entirely optional and unlocks nothing,
because nothing is locked.
""" if DONATION_URL else ""
    rating_table, rating_limits, content_notes = extract_rating_block()
    (OUT / "README.md").write_text(f"""# Curse of Aestrum

An interactive Dungeons & Dragons 5e campaign. Arrive in the duchy of Aestrum, where something is
deeply and secretly wrong. This is **Chapter 1**.

## Content rating

**Written for adults.** Occult horror, violence, manipulation, and intimate themes run through the
campaign, and **T is the floor** — it does not play lighter than that.

You choose a rating when a session starts; **M** is the default, and a saved campaign resumes at
whatever it was last set to. The rating governs the whole scene, not just sex — injury granularity,
innuendo, threat bluntness, NPC anger.

{rating_table}

Say *"switch to M"*, *"drop to T"*, or *"go AO for this scene"* at any point; it takes effect on the
next response.

{rating_limits}

{content_notes}

## Requirements

- **Claude Code** and your own Claude access (Pro/Max/API).
- **Python 3.11+** on your PATH — `py`, `python3`, or `python`, whichever your platform provides;
  the play-time epistemic-gate hooks find it for you. (3.9 also works if you have the `tomli`
  package installed; the gate reads TOML lint specs.)

## Install

```
/plugin marketplace add <owner>/{PLUGIN_NAME}
/plugin install {PLUGIN_NAME}@{PLUGIN_NAME}
```

## Start playing

Open Claude Code in a **fresh, empty folder** (your play-state is written there, under
`campaign_state/`). Then:

- `/{PLUGIN_NAME}:create-party` — build your party, then
- `/{PLUGIN_NAME}:scene` — begin play.

`/{PLUGIN_NAME}:mex` loads the core cycle mechanics if you want the how-it-works first.
{bugs}{support}
## Credits & license

Curse of Aestrum by {AUTHOR}. Built on the Calliope (prose), Aria (story), and Bailly (5e)
engines, bundled here. See each `engines/*/` subtree for its own license/contract.
""", encoding="utf-8")


# Link targets that legitimately do not ship. The plugin deliberately excludes some
# trees (later chapters, the badge tier) that Chapter 1 files still point at as
# forward-references. Everything here is intentional; anything dangling and NOT
# listed is a build error. Prune an entry when its target starts shipping.
ALLOWED_DANGLING = {
    "locations/chapter_2/setland_east_corridor.md",  # chapter-2 overlay of a chapter-1 road
    "locations/chapter_2/mireval/vesper_hall.md",    # chapter-2 venue
    "npcs/chapter_2/remaining_npcs.md",              # chapter-2 secrets overlay
    "timelines/chapter_2/nortmunde_regional.md",     # chapter-2 half of the succession timeline
    "factions/chapter_2/shar.md",                    # chapter-2 half of Shar's board
    "lore/chapter_2/key_lore_summary.md",             # chapter-2 half of the lore summary
    "badges/side_quests.md",                         # badge tier is not bundled
}

_PLUGIN_LINK = re.compile(r"\]\(\{\{PLUGIN_ROOT\}\}/([^)#]+)(?:#[^)]*)?\)")


def check_dangling_refs() -> None:
    """Fail the build on any {{PLUGIN_ROOT}} link whose target was never copied.

    This is the one check that runs against the *bundle's* own link graph, and it
    exists because nothing else can catch this class. SOURCE_MAP resolves refs into
    chapter_2 (and other excluded trees) perfectly well, so they are rewritten to
    {{PLUGIN_ROOT}} form and never appear in the UNMAPPED log — mapping succeeds,
    copying does not. refcheck runs against the source repo, where those targets do
    exist, so it is blind here too. Deliberate forward-references live in
    ALLOWED_DANGLING; anything else means a ref points at a file the plugin ships
    no copy of, and the model will hit a dead path at play time.
    """
    missing: dict[str, list[str]] = {}
    for f in sorted(OUT.rglob("*")):
        if not (f.is_file() and f.suffix in TEXT_EXT):
            continue
        for target in _PLUGIN_LINK.findall(f.read_text(encoding="utf-8", errors="ignore")):
            target = target.strip()
            if target in ALLOWED_DANGLING or (OUT / target).exists():
                continue
            missing.setdefault(target, []).append(str(f.relative_to(OUT)))

    if missing:
        lines = [f"\n  BROKEN REFERENCES - {len(missing)} target(s) referenced but not shipped:"]
        for target, srcs in sorted(missing.items()):
            lines.append(f"    {target}")
            for s in sorted(set(srcs)):
                lines.append(f"        from {s}")
        lines.append("\n  Either add the target to COPY_SPECS, retarget the reference in the")
        lines.append("  source repo, or (if it is a deliberate forward-reference to content")
        lines.append("  this release does not ship) add it to ALLOWED_DANGLING with a reason.")
        raise SystemExit("\n".join(lines))

    stale = sorted(t for t in ALLOWED_DANGLING if (OUT / t).exists())
    if stale:
        print(f"\n  NOTE: {len(stale)} ALLOWED_DANGLING entr(y/ies) now ship and can be pruned:")
        for t in stale:
            print(f"    {t}")
    print(f"\n  bundle links resolve ({len(ALLOWED_DANGLING)} allowed forward-reference(s)).")


def main() -> None:
    global PLUGIN_VERSION
    # Snapshot the previous bundle before it is cleared: its content is what "did anything change?"
    # is measured against, and its version is what an unchanged rebuild keeps.
    prior_fp = fingerprint(OUT)
    prior_version = read_prior_version()
    # Build carrying the prior version so the manifest is not itself a difference. finalize_version
    # replaces it at the end if — and only if — the content moved.
    PLUGIN_VERSION = prior_version or next_version(None)
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    total = 0
    for src, dst_rel in COPY_SPECS:
        if not src.exists():
            print(f"  WARN missing source: {src}")
            continue
        c = copy_spec(src, dst_rel)
        total += c
        print(f"  copied {c:4d}  {dst_rel}")
    for rf in ROOT_FILES:
        sp = COA / rf
        if sp.exists():
            process_file(sp, OUT / rf, is_skill_md=False)
            total += 1

    emit_runtime_main()
    retarget_checker_configs()
    total += 1

    write_meta()
    print(f"\n  {total} files written to {OUT} (+ manifest / hooks / marketplace / README)")
    check_dangling_refs()
    if UNMAPPED:
        print("\n  UNMAPPED references (left untouched — review):")
        for k, v in sorted(UNMAPPED.items(), key=lambda x: -x[1]):
            print(f"    {v:3d}  {k}")
    else:
        print("\n  all references mapped.")
    finalize_version(prior_fp, prior_version)


if __name__ == "__main__":
    main()
