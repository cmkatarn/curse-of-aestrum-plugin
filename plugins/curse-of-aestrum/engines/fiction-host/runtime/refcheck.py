"""Deterministic reference-integrity checker for the markdown engine stack.

The narrative stack keeps most of its behavior in markdown that the LLM reads
directly. Consumers (and engines) cross-reference each other with ordinary
markdown links — ``[text](../prose-engine/scene/core.md#some-anchor)``. Nothing
validates those references, so a renamed section or moved file "compiles" fine
and only fails when the model reads it mid-scene. This module closes that gap by
resolving every link statically: the target file must exist, and any ``#fragment``
must resolve to a real heading (GitHub-style slug) or an explicit anchor.

Resolution rule: markdown ``[](...)`` links are validated as **standard
file-relative links** (GitHub navigation semantics) — the target resolves
relative to the directory of the file that contains it. (The scene SKILL's
project-root convention governs its backtick ``Read`` *directives*, a separate
runtime channel that is not a markdown link and is not checked here.)

Fragments resolve against the target file's anchor index, which is the union of:
  - GitHub-style slugs computed from every ``#``..``######`` heading, and
  - explicit ``<!-- anchor: some-id -->`` markers (introduced in the contract
    work; tolerated-absent until then).

Read-only, stdlib only — matching spec_drift.py and the no-third-party invariant.
"""

from __future__ import annotations

import fnmatch
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote

if sys.version_info >= (3, 11):
    import tomllib
else:  # pragma: no cover
    import tomli as tomllib  # type: ignore

# Same heading grammar spec_drift.py uses; kept local so refcheck has no
# dependency on another module's private name.
_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
# Explicit, wording-independent anchor markers: <!-- anchor: core.load-order -->
_ANCHOR = re.compile(r"<!--\s*anchor:\s*([A-Za-z0-9._-]+)\s*-->")
# Inline markdown links/images: [text](target) and ![alt](target). Captures the
# target up to whitespace or ')', so an optional "title" after the URL is ignored.
_LINK = re.compile(r"!?\[[^\]]*\]\(\s*([^)\s]+)(?:\s+\"[^\"]*\")?\s*\)")
# Fenced code blocks (``` or ~~~) — their contents are not real links.
_FENCE = re.compile(r"^\s*(```+|~~~+)")
# Link targets we never resolve on disk.
_EXTERNAL = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//)", re.IGNORECASE)


def slugify(heading: str) -> str:
    """GitHub's heading-anchor slug: lowercase, drop punctuation except spaces
    and hyphens, then spaces -> hyphens. Reproduces e.g.
    "STEP 2 — Per-slot mode" -> "step-2--per-slot-mode"."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)  # \w keeps letters/digits/underscore
    return s.replace(" ", "-")


def _strip_fences(lines: list[str]) -> list[str]:
    """Blank out fenced-code lines (preserving line count) so example links in
    documentation are not validated. Inline code spans are also blanked."""
    out: list[str] = []
    fence: str | None = None
    for line in lines:
        m = _FENCE.match(line)
        if fence is None and m:
            fence = m.group(1)[:3]
            out.append("")
            continue
        if fence is not None:
            if line.strip().startswith(fence):
                fence = None
            out.append("")
            continue
        out.append(re.sub(r"`[^`]*`", "", line))
    return out


def anchor_index(text: str) -> set[str]:
    """Every fragment a link may target in this file: heading slugs + explicit
    anchors. Duplicate heading slugs get GitHub's -1/-2 suffixes."""
    anchors: set[str] = set()
    seen: dict[str, int] = {}
    for line in text.splitlines():
        m = _HEADING.match(line)
        if m:
            base = slugify(m.group(2))
            n = seen.get(base, 0)
            anchors.add(base if n == 0 else f"{base}-{n}")
            seen[base] = n + 1
        for am in _ANCHOR.finditer(line):
            anchors.add(am.group(1))
    return anchors


def iter_links(text: str):
    """Yield (line_number, raw_target) for each inline link/image, skipping
    fenced/inline code."""
    for i, line in enumerate(_strip_fences(text.splitlines()), start=1):
        for m in _LINK.finditer(line):
            yield i, m.group(1)


@dataclass
class RefIssue:
    file: str        # the file that contains the offending link
    line: int
    target: str      # the raw link target
    reason: str      # "missing file" | "unknown anchor" | "unresolved path"


@dataclass
class RefReport:
    issues: list[RefIssue] = field(default_factory=list)
    files: int = 0
    links: int = 0

    @property
    def clean(self) -> bool:
        return not self.issues


def _split_target(target: str) -> tuple[str, str | None]:
    """Split 'path#frag' into (path, frag). 'path' may be '' for a same-file
    '#frag'."""
    if "#" in target:
        path, frag = target.split("#", 1)
        return path, frag
    return target, None


def _anchors_for(path: Path, cache: dict[Path, set[str]]) -> set[str]:
    idx = cache.get(path)
    if idx is None:
        idx = anchor_index(path.read_text(encoding="utf-8"))
        cache[path] = idx
    return idx


def _ignored(path_part: str, ignore: list[str]) -> bool:
    """True if a link's path matches a consumer-declared soft-pointer glob (e.g.
    'saved/*' — instance overlay state that only resolves inside a campaign
    instance, intentionally dangling in the canon tree)."""
    return any(fnmatch.fnmatch(path_part, pat) for pat in ignore)


def expand_placeholder(
    token: str, placeholders: "dict[str, Path | None] | None"
) -> "tuple[str | None, bool]":
    """Resolve a leading `{{NAME}}/` sentinel in a link target.

    Assembled/packaged trees rewrite their link targets to sentinel form
    (`{{PLUGIN_ROOT}}/engines/...`) because the real base is only known at load
    time. Left alone, every such link reads as a literal directory named
    `{{PLUGIN_ROOT}}` and reports as a missing file — 600+ false positives on a
    tree whose links are all fine.

    Returns `(resolved, handled)`:
      * `(abs_path_str, True)`  — sentinel known; check against this base.
      * `(None, True)`          — sentinel deliberately unresolvable (e.g. a
                                  per-instance state root that does not exist at
                                  check time); skip the link, do not report it.
      * `(token, False)`        — no sentinel; caller proceeds as before.

    Callers that pass no `placeholders` get the original behaviour untouched.
    """
    if not token.startswith("{{"):
        return token, False
    end = token.find("}}")
    if end == -1:
        return token, False
    name = token[2:end]
    rest = token[end + 2:].lstrip("/")
    mapping = placeholders or {}
    if name not in mapping:
        return token, False          # unknown sentinel — leave it to normal resolution
    base = mapping[name]
    if base is None:
        return None, True            # known-but-uncheckable: a soft pointer by construction
    return str(base / rest) if rest else str(base), True


def check_file(
    md: Path,
    cache: dict[Path, set[str]],
    ignore: list[str] | None = None,
    engines: "list[EngineContract] | None" = None,
    placeholders: "dict[str, Path | None] | None" = None,
) -> tuple[list[RefIssue], int]:
    """Validate every link in one markdown file. Returns (issues, link_count).

    When `engines` is supplied, a fragment citation from a *consumer* file (one not
    inside any engine root) into an engine file must target a **public** anchor —
    one listed in that engine's CONTRACT.toml. Engine-internal links are exempt:
    they only need to resolve."""
    ignore = ignore or []
    engines = engines or []
    md_in_engine = any(_is_under(md, ec.root) for ec in engines)
    issues: list[RefIssue] = []
    text = md.read_text(encoding="utf-8")
    self_anchors: set[str] | None = None
    count = 0
    for line, raw in iter_links(text):
        if _EXTERNAL.match(raw) or not raw:
            continue
        count += 1
        path_part, frag = _split_target(unquote(raw))
        if _ignored(path_part, ignore):
            continue

        if path_part == "":
            # Same-file fragment.
            if self_anchors is None:
                self_anchors = anchor_index(text)
            if frag and frag not in self_anchors:
                issues.append(RefIssue(str(md), line, raw, "unknown anchor"))
            continue

        expanded, handled = expand_placeholder(path_part, placeholders)
        if handled and expanded is None:
            continue                      # sentinel maps to an uncheckable root
        if handled:
            path_part = expanded

        target = (md.parent / path_part).resolve()
        if not target.exists():
            issues.append(RefIssue(str(md), line, raw, "missing file"))
            continue
        if frag and target.suffix.lower() == ".md":
            if frag not in _anchors_for(target, cache):
                issues.append(RefIssue(str(md), line, raw, "unknown anchor"))
            elif not md_in_engine:
                # A consumer citing into an engine must hit a public anchor.
                ec = _engine_of(target, engines)
                if ec is not None and frag not in ec.public_anchors:
                    issues.append(RefIssue(
                        str(md), line, raw,
                        f"non-public anchor (not in {ec.name} CONTRACT.toml)"))
    return issues, count


def _excluded(path: Path, root: Path, exclude: set[str]) -> bool:
    rel_parts = path.relative_to(root).parts
    return any(part in exclude for part in rel_parts)


def gather_markdown(roots: list[Path], exclude: set[str]) -> list[Path]:
    """All *.md under the given roots, skipping any path with an excluded part.
    Deduplicated and sorted (roots may overlap)."""
    seen: set[Path] = set()
    for root in roots:
        if not root.exists():
            continue
        for md in root.rglob("*.md"):
            if _excluded(md, root, exclude):
                continue
            seen.add(md.resolve())
    return sorted(seen)


# Sensible defaults: generated state and binary/asset dirs carry no contract refs.
DEFAULT_EXCLUDE = {".git", "campaign_state", "Photos", "badges", "__pycache__"}


def check_roots(
    roots: list[Path],
    exclude: set[str] | None = None,
    ignore_targets: list[str] | None = None,
    engines: "list[EngineContract] | None" = None,
    cache: dict[Path, set[str]] | None = None,
    placeholders: "dict[str, Path | None] | None" = None,
) -> RefReport:
    """Resolve every markdown link under `roots`. The single entry point both the
    selfcheck step and the standalone CLI call."""
    ex = DEFAULT_EXCLUDE if exclude is None else exclude
    files = gather_markdown(roots, ex)
    if cache is None:
        cache = {}
    report = RefReport(files=len(files))
    for md in files:
        issues, n = check_file(md, cache, ignore_targets, engines, placeholders)
        report.links += n
        report.issues.extend(issues)
    return report


# --------------------------------------------------------------------------- #
# Engine contracts — the versioned, wording-independent public surface (Item 3).
# --------------------------------------------------------------------------- #


@dataclass
class EngineContract:
    """A loaded CONTRACT.toml: an engine's public anchors and its version."""

    name: str
    root: Path
    version: int
    public_anchors: set[str]
    anchor_files: dict  # id -> file relpath (for the integrity check)


def load_contract(name: str, root: Path) -> "EngineContract | None":
    cp = root / "CONTRACT.toml"
    if not cp.exists():
        return None
    with cp.open("rb") as fh:
        data = tomllib.load(fh)
    anchor_files = {a["id"]: a.get("file", "") for a in data.get("anchor", [])}
    return EngineContract(
        name=name,
        root=root.resolve(),
        version=int(data.get("contract_version", 0)),
        public_anchors=set(anchor_files),
        anchor_files=anchor_files,
    )


def _is_under(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _engine_of(target: Path, engines: list[EngineContract]) -> "EngineContract | None":
    for ec in engines:
        if _is_under(target, ec.root):
            return ec
    return None


def contract_integrity_issues(ec: EngineContract, cache: dict[Path, set[str]]) -> list[RefIssue]:
    """Every anchor a CONTRACT promises must actually exist (heading slug or
    explicit marker) in its declared file — a stale public promise is a defect."""
    issues: list[RefIssue] = []
    cpath = str(ec.root / "CONTRACT.toml")
    for aid, rel in ec.anchor_files.items():
        f = (ec.root / rel).resolve()
        if not f.exists():
            issues.append(RefIssue(cpath, 0, f"{aid} -> {rel}", "contract file missing"))
        elif aid not in _anchors_for(f, cache):
            issues.append(RefIssue(cpath, 0, f"{aid} in {rel}", "contract anchor not in file"))
    return issues


@dataclass
class EnginePin:
    """A consumer's declared dependency on an engine contract: which version it
    was written against. Mismatch with the engine's live contract_version fails."""

    name: str
    path: Path
    version: int


@dataclass
class RefConfig:
    """Resolved refcheck.toml: which roots to scan, the consumer's soft-pointer
    conventions, and its engine-contract pins. Both entrypoints build one of these
    (the CLI from a file, the selfcheck step from host.game + an optional file)."""

    roots: list[Path]
    exclude: set[str]
    ignore_targets: list[str]
    engines: list[EnginePin] = field(default_factory=list)
    # Sentinel -> base dir for assembled trees; None means "known but uncheckable".
    placeholders: "dict[str, Path | None]" = field(default_factory=dict)


def load_config(config_path: Path) -> RefConfig:
    """Read a refcheck.toml. `roots`/`exclude`/`ignore_targets` live under [scan];
    `[engines.<name>]` tables carry `path` + `version`. Paths resolve relative to
    the config file's directory."""
    base = config_path.resolve().parent
    with config_path.open("rb") as fh:
        data = tomllib.load(fh)
    scan = data.get("scan", {})
    roots = [(base / r).resolve() for r in scan.get("roots", ["."])]
    exclude = set(scan.get("exclude", sorted(DEFAULT_EXCLUDE)))
    ignore = list(scan.get("ignore_targets", []))
    engines = [
        EnginePin(name=name, path=(base / e["path"]).resolve(), version=int(e.get("version", 0)))
        for name, e in data.get("engines", {}).items()
    ]
    # Sentinel bases for an assembled tree. `[scan].placeholders` maps a sentinel
    # name to a path relative to this config (or the literal "unresolvable" for a
    # root that does not exist at check time, e.g. per-instance play state). The
    # defaults describe the standard packaged layout: the bundle root is the
    # config's own directory, and project state is not checkable from here.
    raw = scan.get("placeholders") or {}
    placeholders: dict[str, Path | None] = {
        "PLUGIN_ROOT": base,
        "PROJECT_ROOT": None,
    }
    for name, val in raw.items():
        placeholders[name] = None if val == "unresolvable" else (base / val).resolve()
    return RefConfig(roots=roots, exclude=exclude, ignore_targets=ignore,
                     engines=engines, placeholders=placeholders)


def check(config: RefConfig) -> RefReport:
    """Full reference check: engine-contract version match + integrity, then link
    resolution with public-anchor enforcement on consumer→engine citations."""
    cache: dict[Path, set[str]] = {}
    contracts: list[EngineContract] = []
    pre: list[RefIssue] = []
    for pin in config.engines:
        ec = load_contract(pin.name, pin.path)
        cpath = str(pin.path / "CONTRACT.toml")
        if ec is None:
            pre.append(RefIssue(cpath, 0, pin.name, "engine pinned but no CONTRACT.toml"))
            continue
        if ec.version != pin.version:
            pre.append(RefIssue(
                cpath, 0, f"{pin.name}: consumer pinned v{pin.version} != engine v{ec.version}",
                "contract version mismatch"))
        pre.extend(contract_integrity_issues(ec, cache))
        contracts.append(ec)
    report = check_roots(config.roots, config.exclude, config.ignore_targets,
                         engines=contracts, cache=cache,
                         placeholders=config.placeholders)
    report.issues = pre + report.issues
    return report
