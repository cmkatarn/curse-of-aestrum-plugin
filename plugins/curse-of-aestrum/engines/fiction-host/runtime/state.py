"""Deterministic state primitives — the thick-host core.

Game-agnostic. These functions own the bookkeeping the plan moves OFF the LLM:
parsing accumulated overlay files into time-tagged delta entries, filtering them
to a time anchor, merging base + overlay into a single block to hand the model,
and writing new delta entries back in the canonical format.

Nothing here knows about any specific campaign. The consuming game's layout
module (e.g. games/curse_of_aestrum/layout.py) decides *which* files to load for
a given character and *which* filter policy applies; it then calls these
primitives to do the actual work.

Format reference:
  - Delta entries are level-3 markdown headers: ``### <anchor> — <descriptor>``
    followed by ``- **Field:** value`` bullets.
  - Some anchors are numeric (``### Day 6 — ...``, ``### Day -31 — ...``) and can
    be ordered/filtered deterministically. Others are free-form
    (``### Pre-Aestrum (eve of crossing) — ...``) and can only be ordered by
    their position in the file (overlays are append-only / chronological).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal, Optional

# A "Day" tag in an entry header. Handles ASCII '-'/'+' and the Unicode minus
# sign (U+2212, '−') that appears in real campaign files (e.g. "### Day −31").
_DAY_RE = re.compile(r"\bDay\s*([+\-−]?\s*\d+)", re.IGNORECASE)
_ENTRY_HEADER_RE = re.compile(r"^###\s+(.*\S)\s*$", re.MULTILINE)

# Entries whose heading carries this prefix are the loop's deterministic
# recurrence repertoire (approach-keyed dialogue and event-experience reactions),
# not experience the character accumulates. Per scene.md :: "Time-filter format"
# they load in full regardless of the time anchor — the prefix is the machine
# contract. (Location overlays use "Cycle recurrence —" and carry no time-filter
# to begin with, so only the character-side prefix needs recognizing here.)
_CYCLE_RESPONSE_RE = re.compile(r"^cycle response\b", re.IGNORECASE)

FilterPolicy = Literal["continuous", "loop"]


def _is_cycle_response(header: str) -> bool:
    """True if a delta entry is a loop cycle-response block (never time-filtered)."""
    return bool(_CYCLE_RESPONSE_RE.match(header.strip()))


def parse_day(header: str) -> Optional[int]:
    """Extract the integer Day index from an entry header, or None if free-form.

    >>> parse_day("Day 6 — noon, the salon")
    6
    >>> parse_day("Day −31 — vestibule note")
    -31
    >>> parse_day("Pre-Aestrum (eve of crossing) — party formed")  # returns None
    """
    m = _DAY_RE.search(header)
    if not m:
        return None
    raw = m.group(1).replace("−", "-").replace(" ", "")
    try:
        return int(raw)
    except ValueError:
        return None


@dataclass
class DeltaEntry:
    """One ``### ...`` block from an overlay's accumulating state log."""

    header: str                 # text after "### ", e.g. "Day 6 — noon"
    body: str                   # the bullet lines beneath the header
    day: Optional[int]          # parsed numeric Day, or None for free-form anchors
    index: int                  # position in the file (0-based) — chronological order

    @property
    def text(self) -> str:
        return f"### {self.header}\n{self.body}".rstrip() + "\n"


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_without_fences, body). Frontmatter is '' if absent."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm = text[3:end].strip("\n")
            body_start = text.find("\n", end + 1)
            body = text[body_start + 1 :] if body_start != -1 else ""
            return fm, body
    return "", text


# MIRRORS: scene.md :: Overlay header conventions (asymmetric-aspect slots)
def parse_entries(text: str) -> list[DeltaEntry]:
    """Parse all ``### ...`` delta entries from an overlay file's text.

    Content before the first ``###`` header (overview prose, the base-sheet
    body, section headers like ``## Campaign State Log``) is ignored here — the
    caller decides how to present the base file. This function only extracts the
    accumulating, time-tagged log entries.
    """
    entries: list[DeltaEntry] = []
    matches = list(_ENTRY_HEADER_RE.finditer(text))
    for i, m in enumerate(matches):
        header = m.group(1).strip()
        body_start = m.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[body_start:body_end].strip("\n")
        entries.append(
            DeltaEntry(header=header, body=body, day=parse_day(header), index=i)
        )
    return entries


# MIRRORS: scene.md :: Time-filter format
def time_filter(
    entries: list[DeltaEntry],
    policy: FilterPolicy,
    anchor_day: Optional[int],
    *,
    replay: bool = False,
) -> tuple[list[DeltaEntry], list[str]]:
    """Filter overlay entries to a time anchor.

    Returns (kept_entries, notes). ``notes`` surfaces anything the host could
    NOT decide deterministically, so the caller can pass that judgment to the
    model rather than silently guessing.

    Policy:
      - "continuous": include everything (Player PCs, non-loop NPCs accumulate
        linearly), UNLESS ``replay`` is set — then apply the loop rule to
        re-stage an earlier moment.
      - "loop": drop entries whose numeric Day is strictly greater than the
        anchor. Entries tagged with the same Day are kept (time-of-day
        plausibility within a day is a semantic call left to the model — flagged
        in notes). Free-form (None-day) entries cannot be compared numerically;
        they are kept in file order with a note.

    Exempt regardless of policy/anchor: entries whose heading is prefixed
    "Cycle response —" are the loop's deterministic recurrence repertoire, not
    accumulated experience, so they always load in full (no day comparison, no
    undated note).
    """
    notes: list[str] = []

    if policy == "continuous" and not replay:
        return list(entries), notes

    if anchor_day is None:
        notes.append(
            "No numeric Day anchor supplied; loop/replay filter could not run — "
            "all entries included in file (chronological) order."
        )
        return list(entries), notes

    kept: list[DeltaEntry] = []
    same_day_present = False
    undated_present = False
    for e in entries:
        if _is_cycle_response(e.header):
            kept.append(e)  # deterministic loop recurrence — never time-filtered
        elif e.day is None:
            kept.append(e)
            undated_present = True
        elif e.day < anchor_day:
            kept.append(e)
        elif e.day == anchor_day:
            kept.append(e)
            same_day_present = True
        # e.day > anchor_day: dropped (future knowledge)

    if same_day_present:
        notes.append(
            f"Entries tagged Day {anchor_day} are included; whether each has "
            "plausibly occurred by the requested time of day is a judgment call — "
            "treat anything later in that day as not-yet-known."
        )
    if undated_present:
        notes.append(
            "Some entries use free-form time anchors (no numeric Day); they were "
            "kept in file order and could not be filtered numerically."
        )
    return kept, notes


@dataclass
class MergedMemory:
    """The product handed to the model for one character/location."""

    name: str
    base_text: str
    kept_entries: list[DeltaEntry] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    base_path: Optional[str] = None
    overlay_path: Optional[str] = None

    def render(self) -> str:
        """Render base + time-filtered overlay as one block for the model."""
        parts = [self.base_text.rstrip(), ""]
        if self.kept_entries:
            parts.append("## Accumulated State (time-filtered by host)\n")
            for e in self.kept_entries:
                parts.append(e.text)
        else:
            parts.append("## Accumulated State (time-filtered by host)\n")
            parts.append("*(no overlay entries within the time anchor)*\n")
        if self.notes:
            parts.append("\n---\n*Host filter notes (for your judgment, not for the player):*")
            for n in self.notes:
                parts.append(f"- {n}")
        return "\n".join(parts).rstrip() + "\n"


def merge_memory(
    name: str,
    base_text: str,
    overlay_text: str,
    *,
    policy: FilterPolicy,
    anchor_day: Optional[int],
    replay: bool = False,
    base_path: Optional[str] = None,
    overlay_path: Optional[str] = None,
) -> MergedMemory:
    """Merge a base sheet with a time-filtered overlay into one memory block.

    The base text is taken as-is (it is the reset-state / canonical sheet). The
    overlay's ``### ...`` entries are parsed, filtered to the anchor under the
    given policy, and appended. Pre-entry prose in the overlay (its own intro /
    "merge with base" note) is intentionally dropped — it is scaffolding, not
    character knowledge.
    """
    _, overlay_body = split_frontmatter(overlay_text) if overlay_text else ("", "")
    entries = parse_entries(overlay_body) if overlay_body else []
    kept, notes = time_filter(entries, policy, anchor_day, replay=replay)
    return MergedMemory(
        name=name,
        base_text=base_text,
        kept_entries=kept,
        notes=notes,
        base_path=base_path,
        overlay_path=overlay_path,
    )


# --------------------------------------------------------------------------- #
# Writing new delta entries (the save side of the thick host).
# --------------------------------------------------------------------------- #

# Default field order for a delta entry, per scene_lifecycle.md §5a. Field
# vocabulary is consumer-owned (see CONTRACT.md §4): a consumer plugin may pass
# its own ordered (key, label) list to format_delta; this is the engine default.
# MIRRORS: scene_lifecycle.md :: 5a. Default close prompt — "Save scene state?"
DELTA_FIELDS = [
    ("now_knows", "Now knows"),
    ("now_believes", "Now believes / suspects"),
    ("relationship_shift", "Relationship shift"),
    ("emotional_state", "Emotional / situational state"),
    ("unresolved", "Unresolved"),
    ("items_changes", "Items / changes"),
]


# MIRRORS: scene.md :: Save protocol — CoA specifics
def format_delta(
    time_tag: str,
    descriptor: str,
    fields: dict[str, object],
    *,
    field_order: list[tuple[str, str]] = DELTA_FIELDS,
) -> str:
    """Build one ``### <time_tag> — <descriptor>`` delta block.

    ``fields`` maps any of the ``field_order`` keys to a string or list of
    strings. ``field_order`` defaults to the engine vocabulary (DELTA_FIELDS);
    a consumer with its own vocabulary passes its ordered (key, label) list.
    Lines with no value are dropped, per the format spec ("Drop any line that
    doesn't apply").
    """
    lines = [f"### {time_tag} — {descriptor}", ""]
    for key, label in field_order:
        val = fields.get(key)
        if not val:
            continue
        if isinstance(val, (list, tuple)):
            rendered = "; ".join(str(v) for v in val if v)
            if not rendered:
                continue
        else:
            rendered = str(val)
        lines.append(f"- **{label}:** {rendered}")
    return "\n".join(lines) + "\n"


def append_delta(path: Path, block: str) -> None:
    """Append a delta block to an overlay file, creating it if needed.

    Exactly one blank line separates the new entry from prior content, and the
    file ends with a single newline. The caller (game layout) is responsible for
    write-scope enforcement — this is a raw append once the path has been
    validated.

    The separator is rebuilt rather than conditionally added, because an overlay
    is appended to over and over by more than one writer and arrives in whatever
    state the last one left it: three trailing newlines, or CRLF endings after
    someone opened it in a Windows editor. Both would otherwise survive into the
    file and drift it off the documented format, so trailing newlines and
    carriage returns are stripped before the separator goes back on.

    Both the read and the write open with ``newline=""`` so this function is
    byte-faithful: it changes the seam and the final newline and nothing else.
    The default text mode would translate on both ends — writing ``\n`` as
    ``\r\n`` on Windows, which silently gave an overlay different bytes
    depending on which machine appended to it, and rewriting every interior line
    ending of a file it was only supposed to append to. An overlay is a parsed
    artifact shared across save paths, so its bytes cannot depend on the host.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = ""
    if path.exists():
        with path.open(encoding="utf-8", newline="") as fh:
            existing = fh.read()
    if existing:
        existing = existing.rstrip("\r\n") + "\n\n"
    with path.open("w", encoding="utf-8", newline="") as fh:
        fh.write(existing + block.rstrip("\r\n") + "\n")
