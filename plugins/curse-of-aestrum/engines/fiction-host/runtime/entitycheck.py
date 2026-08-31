"""Deterministic entity-graph checker for the markdown narrative stack.

``refcheck`` validates *markdown links*. It says nothing about the other reference
system these repos run on: frontmatter fields that name other entities by ``id``
(``connected_locations``, ``npcs_present``, ``parent``, ``members``). Those
references are invisible to a link checker, so a graph can rot in four ways that
still "load" — and each produces a *different world* depending on which file the
loader entered from:

  - **dangling reference** — a field cites an id no file defines;
  - **alias drift** — one entity acquires a second id, so half the graph points at
    a ghost;
  - **one-way edge** — A names B as a peer, B does not name A back;
  - **key drift** — the same relation spelled with two field names.

This module checks a work's entity tree against the *bindings it declares*, per
Aria's invariant/binding split (``story-engine/rules/authoring_entities.md``,
anchors ``entity-authoring.bindings`` / ``.relations`` / ``.integrity``). The
engine fixes the invariants; each work names its own spellings in an
``entitycheck.toml``. Nothing here knows any work's directory names, field names,
or id prefixes — a work that spells its peer link ``connects_to`` and scopes ids
per-directory is checked exactly as strictly as one using ``connections`` and
type-prefixed ids.

Read-only, stdlib only — matching refcheck.py and spec_drift.py.
"""

from __future__ import annotations

import fnmatch
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

if sys.version_info >= (3, 11):
    import tomllib
else:  # pragma: no cover
    import tomli as tomllib  # type: ignore

_FM = re.compile(r"\A---\r?\n(.*?)\r?\n---\s*$", re.S | re.M)
_KV = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")
_ITEM = re.compile(r"^\s*-\s+(.*)$")
# An indented `subkey: value` line beneath an empty `key:` — one level of map.
_MAP_ITEM = re.compile(r"^\s+([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")


# --------------------------------------------------------------------------- #
# Frontmatter — a deliberately small YAML subset (stdlib-only invariant).
# --------------------------------------------------------------------------- #


def _scalar(raw: str) -> str:
    s = raw.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        s = s[1:-1]
    return s.strip()


def _value(rest: str) -> object:
    """A frontmatter value: an inline ``[a, b]`` list, or a scalar."""
    if rest.startswith("[") and rest.endswith("]"):
        inner = rest[1:-1].strip()
        return [_scalar(p) for p in inner.split(",") if p.strip()] if inner else []
    return _scalar(rest)


def parse_frontmatter(text: str) -> dict[str, object]:
    """Parse a leading ``---`` block into {key: str | list[str] | dict}.

    Handles the shapes these repos actually use: ``key: scalar``, ``key: [a, b]``,
    a ``key:`` followed by indented ``- item`` lines (a list), and a ``key:``
    followed by indented ``subkey: value`` lines (a one-level map whose values are
    scalars or inline lists — e.g. the faction ``known_to`` secrecy graph). Deeper
    nesting is kept as a raw scalar rather than guessed at.
    """
    m = _FM.search(text)
    if not m:
        return {}
    out: dict[str, object] = {}
    pending: str | None = None       # an empty ``key:`` awaiting indented children
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        item = _ITEM.match(line)
        if item is not None and pending is not None and isinstance(out.get(pending), list):
            out[pending].append(_scalar(item.group(1)))          # list child
            continue
        mapitem = _MAP_ITEM.match(line)
        if mapitem is not None and pending is not None:
            cur = out.get(pending)
            if isinstance(cur, list) and not cur:
                out[pending] = cur = {}       # first indented `subkey:` → it is a map
            if isinstance(cur, dict):
                cur[mapitem.group(1)] = _value(mapitem.group(2).strip())
            continue
        kv = _KV.match(line)
        if kv is None:
            continue
        key, rest = kv.group(1), kv.group(2).strip()
        pending = None
        if rest == "":
            out[key] = []
            pending = key
        else:
            out[key] = _value(rest)
    return out


def as_ids(value: object) -> list[str]:
    """The id-valued references in a field, as a list (scalar fields count as one)."""
    if isinstance(value, list):
        return [v for v in value if v]
    if isinstance(value, str) and value:
        return [value]
    return []


# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #


@dataclass
class Domain:
    name: str            # config key, e.g. "locations"
    path: str            # directory relative to the scan root
    kind: str            # the Aria kind this domain holds
    prefix: str = ""     # required id prefix under the "prefix" uniqueness binding
    ref_fields: list[str] = field(default_factory=list)
    required_fields: list[str] = field(default_factory=list)
    enums: dict[str, list[str]] = field(default_factory=dict)
    # Globs (relative to the domain dir) for files that live in a domain tree but
    # are not entities — indexes, roster prose, reference tables.
    exclude_files: list[str] = field(default_factory=list)
    # Roster files: one markdown file holding MANY entities, one per heading
    # section, with fields on an inline field line rather than in frontmatter.
    # A digest is a legitimate shape for minor entities — cheaper to load than N
    # files — but it is invisible to a one-entity-per-file reader unless declared.
    exclusive: list["Exclusive"] = field(default_factory=list)
    scoped_maps: list["ScopedMap"] = field(default_factory=list)
    roster_files: list[str] = field(default_factory=list)
    roster_level: int = 2
    roster_field_pattern: str = r"\*\*([a-z_]+):\*\*\s*([^|]+)"


@dataclass
class Exclusive:
    """A group of fields where at most one may be set — typically a reference
    field and the status field that stands in when no referent exists (a wanderer
    with no location, a decision not yet made). Keeping them in separate fields is
    what stops a state from being written into a reference field, where it can
    only ever dangle."""

    name: str
    fields: list[str]
    required: bool = True     # exactly-one for full entities, at-most-one for digests


@dataclass
class ScopedMap:
    """A map-valued field whose keys and value-ids must all be ids listed in a
    sibling ``scope`` field on the same entity — e.g. a faction's ``known_to``
    secrecy graph, whose every endpoint must be one of the faction's ``members``.
    Directed by design (A-knows-B does not imply B-knows-A), so it is checked for
    containment within scope, never for reciprocity. A non-list value (a sentinel
    such as ``all``) is left unchecked; only list entries are id-validated."""

    field: str
    scope: str


@dataclass
class Reciprocal:
    name: str
    a_domain: str
    a_field: str
    b_domain: str
    b_field: str


@dataclass
class EntityConfig:
    root: Path
    exclude: set[str]
    kind_binding: str          # "directory" | "explicit"
    id_binding: str            # "prefix" | "directory"
    containment_key: str
    soft_ids: list[str]        # globs for intentionally unresolved references
    domains: dict[str, Domain]
    reciprocals: list[Reciprocal]


DEFAULT_EXCLUDE = {".git", "Photos", "badges", "__pycache__"}


def load_config(config_path: Path) -> EntityConfig:
    """Read an entitycheck.toml. Paths resolve relative to the config's directory."""
    base = config_path.resolve().parent
    with config_path.open("rb") as fh:
        data = tomllib.load(fh)
    scan = data.get("scan", {})
    bind = data.get("bindings", {})
    domains: dict[str, Domain] = {}
    for name, d in data.get("domains", {}).items():
        domains[name] = Domain(
            name=name,
            path=d.get("path", name),
            kind=d.get("kind", name),
            prefix=d.get("prefix", ""),
            ref_fields=list(d.get("ref_fields", [])),
            required_fields=list(d.get("required_fields", [])),
            enums={k: list(v) for k, v in (d.get("enums") or {}).items()},
            exclude_files=list(d.get("exclude_files", [])),
            exclusive=[
                Exclusive(name=x.get("name", "/".join(x.get("fields", []))),
                          fields=list(x.get("fields", [])),
                          required=bool(x.get("required", True)))
                for x in d.get("exclusive", [])
            ],
            scoped_maps=[
                ScopedMap(field=sm["field"], scope=sm["scope"])
                for sm in d.get("scoped_map", [])
            ],
            roster_files=list((d.get("roster") or {}).get("files", [])),
            roster_level=int((d.get("roster") or {}).get("section_level", 2)),
            roster_field_pattern=(d.get("roster") or {}).get(
                "field_pattern", r"\*\*([a-z_]+):\*\*\s*([^|]+)"),
        )
    recips = [
        Reciprocal(
            name=r.get("name", f"{r['a']['domain']}.{r['a']['field']}"),
            a_domain=r["a"]["domain"], a_field=r["a"]["field"],
            b_domain=r["b"]["domain"], b_field=r["b"]["field"],
        )
        for r in data.get("reciprocal", [])
    ]
    return EntityConfig(
        root=(base / scan.get("root", ".")).resolve(),
        exclude=set(scan.get("exclude", sorted(DEFAULT_EXCLUDE))),
        kind_binding=bind.get("kind", "explicit"),
        id_binding=bind.get("id_uniqueness", "prefix"),
        containment_key=bind.get("containment_key", "parent"),
        soft_ids=list(bind.get("soft_ids", [])),
        domains=domains,
        reciprocals=recips,
    )


# --------------------------------------------------------------------------- #
# Model
# --------------------------------------------------------------------------- #


@dataclass
class Entity:
    id: str
    domain: str
    file: Path
    fields: dict[str, object]
    line: int = 0            # non-zero for an entity declared inside a roster file


@dataclass
class EntityIssue:
    file: str
    reason: str      # short machine-ish label
    detail: str
    line: int = 0


def parse_roster(text: str, level: int, field_pattern: str) -> list[tuple[str, dict[str, object], int]]:
    """Parse a multi-entity roster into [(id, fields, line), ...].

    A section is one heading at the declared level; its fields come from the first
    matching field line inside it. A section with no id is **not** an entity — in
    practice it is a redirect stub ("moved to X", "elevated to its own sheet") or a
    sub-heading written one level too shallow. Skipping those is deliberate: a
    redirect names an entity that lives elsewhere, and minting an id for it here
    would fabricate a duplicate of the real one.
    """
    head = re.compile(rf"^#{{{level}}}\s+(?!#)(.*)$")
    fields_re = re.compile(field_pattern)
    out: list[tuple[str, dict[str, object], int]] = []
    cur: dict[str, object] | None = None
    cur_line = 0
    started = False        # have we seen this section's first field line yet?
    closed = False         # ...and have we passed the end of the field block?

    def flush() -> None:
        if cur and isinstance(cur.get("id"), str) and cur["id"]:
            out.append((str(cur["id"]), cur, cur_line))

    for i, line in enumerate(text.splitlines(), start=1):
        if head.match(line):
            flush()
            cur, cur_line, started, closed = {}, i, False, False
            continue
        if cur is None or closed:
            continue
        found = fields_re.findall(line)
        if found:
            # Fields may be pipe-delimited on one line or one-per-line; both are
            # the same block. Collect them, first spelling wins. A bracketed value
            # is a list, exactly as in frontmatter — without this a roster's
            # `[a, b, c]` reads as one long id and dangles.
            for k, v in found:
                v = v.strip()
                if v.startswith("[") and v.endswith("]"):
                    inner = v[1:-1].strip()
                    cur.setdefault(k, [_scalar(p) for p in inner.split(",") if p.strip()]
                                   if inner else [])
                else:
                    cur.setdefault(k, v)
            started = True
        elif started and line.strip():
            # First non-field, non-blank line after the block: the body starts
            # here. Stop, so a lowercase **bold:** run inside prose is not read
            # as an entity field.
            closed = True
    flush()
    return out


@dataclass
class EntityReport:
    issues: list[EntityIssue] = field(default_factory=list)
    files: int = 0
    entities: int = 0
    refs: int = 0

    @property
    def clean(self) -> bool:
        return not self.issues


def _excluded(path: Path, root: Path, exclude: set[str]) -> bool:
    return any(part in exclude for part in path.relative_to(root).parts)


def collect(cfg: EntityConfig) -> tuple[list[Entity], list[EntityIssue], int]:
    """Load every entity file under each declared domain directory."""
    entities: list[Entity] = []
    issues: list[EntityIssue] = []
    files = 0
    for dom in cfg.domains.values():
        d = (cfg.root / dom.path).resolve()
        if not d.exists():
            issues.append(EntityIssue(str(d), "domain missing",
                                      f"[domains.{dom.name}] path does not exist"))
            continue
        for md in sorted(d.rglob("*.md")):
            if _excluded(md, cfg.root, cfg.exclude):
                continue
            rel = md.relative_to(d).as_posix()
            if any(fnmatch.fnmatch(rel, g) for g in dom.exclude_files):
                continue
            files += 1
            text = md.read_text(encoding="utf-8")
            if any(fnmatch.fnmatch(rel, g) for g in dom.roster_files):
                for eid, fields, line in parse_roster(
                        text, dom.roster_level, dom.roster_field_pattern):
                    entities.append(Entity(id=eid, domain=dom.name, file=md,
                                           fields=fields, line=line))
                continue
            fm = parse_frontmatter(text)
            if not fm:
                continue          # prose-only file in a domain tree: not an entity
            eid = fm.get("id")
            if not isinstance(eid, str) or not eid:
                issues.append(EntityIssue(str(md), "missing id",
                                          "frontmatter declares no id"))
                continue
            entities.append(Entity(id=eid, domain=dom.name, file=md, fields=fm))
    return entities, issues, files


# --------------------------------------------------------------------------- #
# Checks — one per Aria invariant
# --------------------------------------------------------------------------- #


def _soft(ref: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(ref, g) for g in globs)


def _issue(e: Entity, reason: str, detail: str) -> EntityIssue:
    """An issue against one entity, carrying its roster line when it has one —
    without it, thirty entities in one roster file all report the same location."""
    return EntityIssue(str(e.file), reason, detail, e.line)


def check_ids(cfg: EntityConfig, ents: list[Entity]) -> list[EntityIssue]:
    """Uniqueness (always) + the work's declared uniqueness binding."""
    issues: list[EntityIssue] = []
    seen: dict[str, Entity] = {}
    for e in ents:
        prior = seen.get(e.id)
        if prior is not None:
            # A roster digest alongside a dedicated sheet is ONE entity documented
            # twice, not two entities colliding: the sheet is the entity, the
            # roster line is a summary of it. Only a collision within the same
            # tier is a real duplicate.
            digest_pair = (e.line == 0) != (prior.line == 0)
            if not digest_pair:
                issues.append(_issue(
                    e, "duplicate id",
                    f"{e.id} is also declared by {prior.file}"
                    + (f":{prior.line}" if prior.line else "")))
        else:
            seen[e.id] = e
        if cfg.id_binding == "prefix":
            pre = cfg.domains[e.domain].prefix
            if pre and not e.id.startswith(pre):
                issues.append(_issue(
                    e, "id prefix",
                    f"{e.id} does not start with '{pre}' (domain {e.domain})"))
    return issues


def check_kinds(cfg: EntityConfig, ents: list[Entity]) -> list[EntityIssue]:
    """Under the explicit binding, `type` must name the domain's kind. Under the
    directory binding the placement already carries it, and `type` is free."""
    if cfg.kind_binding != "explicit":
        return []
    issues: list[EntityIssue] = []
    for e in ents:
        want = cfg.domains[e.domain].kind
        got = e.fields.get("type")
        if got != want:
            issues.append(_issue(
                e, "kind",
                f"type is {got!r}, expected {want!r} for domain {e.domain}"))
    return issues


def check_containment(cfg: EntityConfig, ents: list[Entity]) -> list[EntityIssue]:
    """One containment key, work-wide. Any sibling spelling is key drift."""
    key = cfg.containment_key
    drift = re.compile(rf"^{re.escape(key)}_\w+$|^\w+_{re.escape(key)}$")
    issues: list[EntityIssue] = []
    for e in ents:
        for k in e.fields:
            if k != key and drift.match(k):
                issues.append(_issue(
                    e, "containment key drift",
                    f"{k!r} alongside the declared containment key {key!r}"))
    return issues


def check_refs(cfg: EntityConfig, ents: list[Entity]) -> tuple[list[EntityIssue], int]:
    """Every id-valued reference resolves, or matches a declared soft-id glob."""
    known = {e.id for e in ents}
    issues: list[EntityIssue] = []
    count = 0
    for e in ents:
        fields = list(cfg.domains[e.domain].ref_fields)
        if cfg.containment_key not in fields:
            fields.append(cfg.containment_key)
        for f in fields:
            for ref in as_ids(e.fields.get(f)):
                count += 1
                if ref in known or _soft(ref, cfg.soft_ids):
                    continue
                issues.append(_issue(
                    e, "dangling reference",
                    f"{f}: {ref} (no entity declares this id)"))
    return issues, count


def check_required(cfg: EntityConfig, ents: list[Entity]) -> list[EntityIssue]:
    """An empty relation is a statement; an absent one is a hole. Declared
    required fields must be present — `[]` is fine, missing is not."""
    issues: list[EntityIssue] = []
    for e in ents:
        if e.line:
            # A roster digest is an abbreviated record by design. Demanding the
            # full field set from it would force a work to either bloat the
            # digest or split it into one file per entity — which is exactly the
            # tradeoff the digest exists to avoid.
            continue
        for f in cfg.domains[e.domain].required_fields:
            if f not in e.fields:
                issues.append(_issue(
                    e, "missing required field",
                    f"{f} is absent (author it empty if it is genuinely empty)"))
    return issues


def check_exclusive(cfg: EntityConfig, ents: list[Entity]) -> list[EntityIssue]:
    """Mutually exclusive field groups. Setting two of them is always an error;
    setting none is an error only for full entities — a roster digest is
    abbreviated by design (see check_required)."""
    issues: list[EntityIssue] = []
    for e in ents:
        for x in cfg.domains[e.domain].exclusive:
            present = [f for f in x.fields if f in e.fields]
            if len(present) > 1:
                issues.append(_issue(
                    e, "exclusive fields",
                    f"[{x.name}] {' and '.join(present)} are both set; exactly one applies"))
            elif not present and x.required and not e.line:
                issues.append(_issue(
                    e, "exclusive fields",
                    f"[{x.name}] none of {x.fields} is set"))
    return issues


def check_enums(cfg: EntityConfig, ents: list[Entity]) -> list[EntityIssue]:
    """Closed-vocabulary fields (status, and anything else a work closes)."""
    issues: list[EntityIssue] = []
    for e in ents:
        for f, allowed in cfg.domains[e.domain].enums.items():
            v = e.fields.get(f)
            if v is None:
                continue
            for one in as_ids(v):
                if one not in allowed:
                    issues.append(_issue(
                        e, "enum",
                        f"{f}: {one!r} not in {allowed}"))
    return issues


def check_reciprocity(cfg: EntityConfig, ents: list[Entity]) -> list[EntityIssue]:
    """Declared peer relations must be authored on both ends."""
    # When one entity has both a dedicated file and a roster digest, the FILE is
    # authoritative. Letting the digest win here would skip the reciprocity check
    # against it (digests are exempt) and silently drop a real finding.
    by_id: dict[str, Entity] = {}
    for e in ents:
        prior = by_id.get(e.id)
        if prior is None or (prior.line and not e.line):
            by_id[e.id] = e
    issues: list[EntityIssue] = []
    for r in cfg.reciprocals:
        for e in ents:
            if e.domain != r.a_domain:
                continue
            for ref in as_ids(e.fields.get(r.a_field)):
                other = by_id.get(ref)
                if other is None or other.domain != r.b_domain:
                    continue      # dangling / cross-domain: check_refs owns that
                if other.line:
                    continue      # the far end is a digest — see check_required
                if e.id not in as_ids(other.fields.get(r.b_field)):
                    issues.append(_issue(
                        e, "one-way edge",
                        f"[{r.name}] {e.id}.{r.a_field} names {ref}, but "
                        f"{ref}.{r.b_field} does not name it back"))
    return issues


def check_scoped_maps(cfg: EntityConfig, ents: list[Entity]) -> tuple[list[EntityIssue], int]:
    """A scoped map field (a faction's ``known_to``) is a directed graph whose every
    endpoint must lie inside the entity's scope field (``members``). A key that is
    not a member, or a value-id that is not a member, is the secrecy graph naming
    someone outside the group — the same dangling/ghost failure ``check_refs``
    catches for flat fields, one structure up. Non-list values are sentinels and
    are not id-checked; ``[]`` (known to nobody) is valid."""
    issues: list[EntityIssue] = []
    count = 0
    for e in ents:
        for sm in cfg.domains[e.domain].scoped_maps:
            mp = e.fields.get(sm.field)
            if not isinstance(mp, dict):
                continue
            scope_ids = set(as_ids(e.fields.get(sm.scope)))
            for key, val in mp.items():
                count += 1
                if key not in scope_ids:
                    issues.append(_issue(
                        e, "scoped-map key",
                        f"{sm.field}: {key} is not in {sm.scope}"))
                if not isinstance(val, list):
                    continue          # a sentinel (e.g. `all`) — not id-checked
                for ref in val:
                    if not ref:
                        continue
                    count += 1
                    if ref not in scope_ids:
                        issues.append(_issue(
                            e, "scoped-map reference",
                            f"{sm.field}[{key}]: {ref} is not in {sm.scope}"))
    return issues, count


def check(cfg: EntityConfig) -> EntityReport:
    """Full entity-graph check. The single entry point for the CLI."""
    ents, issues, files = collect(cfg)
    report = EntityReport(files=files, entities=len(ents))
    report.issues.extend(issues)
    report.issues.extend(check_ids(cfg, ents))
    report.issues.extend(check_kinds(cfg, ents))
    report.issues.extend(check_containment(cfg, ents))
    ref_issues, nrefs = check_refs(cfg, ents)
    report.refs = nrefs
    report.issues.extend(ref_issues)
    report.issues.extend(check_required(cfg, ents))
    report.issues.extend(check_exclusive(cfg, ents))
    report.issues.extend(check_enums(cfg, ents))
    report.issues.extend(check_reciprocity(cfg, ents))
    map_issues, nmaps = check_scoped_maps(cfg, ents)
    report.refs += nmaps
    report.issues.extend(map_issues)
    return report
