#!/usr/bin/env python3
"""load_scene_context.py — emit the scene skill's front-load state as one blob.

Why this exists is a disclosure problem, not a performance one. The front-load
reads name story resources: `npcs/chapter_1/<someone>.md` in the transcript tells
the player that character exists before the fiction introduces them, and the
overrides' *Live-play silence* rule ("never narrate a consultation ... nothing
about files or canon checks") cannot reach the harness's own tool-call display.
Twelve reads naming twelve files leak twelve facts.

One invocation with a neutral name leaks none. The command line carries no entity
name, and the first lines of output — which is all the transcript previews before
collapsing — are counts, not names.

This is the *state* front-load only: the participants, the overlaid entities and
their canon bases, timelines, instance rules, conversation states, and any
in-flight staging file. The engine stack (Calliope core, registers, narration
modes) is read normally; those filenames disclose nothing.

Base resolution follows the override's path table rather than a list kept here,
so a table change does not silently drift from a hardcoded copy:

  party/saved/<n>.md    -> party/<n>.md               (canonical PC)
                        |  campaign_state/<C>/party/<n>.md  (custom PC)
                        |  npcs/chapter_1/<n>.md      (PC companion)
  npcs/saved/<n>.md     -> npcs/chapter_1/<n>.md      (absent => self-contained sheet)
  locations/saved/<n>.md-> locations/chapter_1/**/<n>.md
  timelines/saved/<n>.md-> timelines/chapter_1/<n>.md
  factions/saved/<n>.md -> factions/chapter_1/<n>.md
  items/saved/<n>.md    -> items/chapter_1/<n>.md
  quests/saved/<n>.md   -> quests/chapter_1/<n>.md

Python is not a new dependency: the gate hooks and the save flush already require
it, so every machine that can play a scene can run this.

Usage:
  python3 scripts/load_scene_context.py [--campaign <id>]
  python3 scripts/load_scene_context.py --state-root <path> --canon-root <path>

The standing location is deliberately NOT resolved here. It is recorded as prose
("**Where he is at save:** ...") in the PC overlay, not as frontmatter, so a
script can only guess at it. The PC overlay is emitted below, and the model reads
the standing location from it; every location the campaign has already touched
arrives with its base and overlay anyway.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# domain under campaign_state/<C>/ -> canon directory holding its base files.
# None means the overlay is always self-contained (no canon tier).
CANON_TIER = {
    "npcs": "npcs/chapter_1",
    "locations": "locations/chapter_1",
    "timelines": "timelines/chapter_1",
    "factions": "factions/chapter_1",
    "items": "items/chapter_1",
    "quests": "quests/chapter_1",
}


def find_base(canon_root: Path, domain: str, stem: str) -> Path | None:
    """Locate the canon base for an overlay, or None if the overlay stands alone."""
    tier = CANON_TIER.get(domain)
    if tier is None:
        return None
    direct = canon_root / tier / f"{stem}.md"
    if direct.is_file():
        return direct
    # A city is a directory whose own entry is _index.md (locations/chapter_1/duskwall/
    # holds the city's venues; locations/saved/duskwall.md overlays the city itself).
    index = canon_root / tier / stem / "_index.md"
    if index.is_file():
        return index
    # Venues nest one level down inside their city directory.
    matches = sorted((canon_root / tier).rglob(f"{stem}.md"))
    return matches[0] if matches else None


def pc_base(canon_root: Path, campaign_root: Path, stem: str) -> Path | None:
    """A party/saved/ overlay layers on one of three bases, per the path table."""
    for cand in (canon_root / "party" / f"{stem}.md",
                 campaign_root / "party" / f"{stem}.md",
                 canon_root / "npcs" / "chapter_1" / f"{stem}.md"):
        if cand.is_file():
            return cand
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description="Emit the scene front-load state as one blob.")
    ap.add_argument("--campaign", help="campaign id (default: read campaign_state/.active)")
    ap.add_argument("--state-root",
                    help="root holding campaign_state/ (default: the working directory if it "
                         "has one, else the parent of this script's directory)")
    ap.add_argument("--canon-root",
                    help="root holding npcs/, party/, locations/ ... "
                         "(default: the parent of this script's directory)")
    args = ap.parse_args()

    # Campaign prose carries em dashes, arrows and minus signs; a Windows console
    # defaults to cp1252 and dies on the first one. The content is UTF-8 on disk and
    # the model reads UTF-8 — say so rather than inheriting the console's codepage.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

    script_root = Path(__file__).resolve().parent.parent
    if args.state_root:
        state_root = Path(args.state_root).resolve()
    elif (Path.cwd() / "campaign_state").is_dir():
        state_root = Path.cwd().resolve()
    else:
        state_root = script_root
    canon_root = Path(args.canon_root).resolve() if args.canon_root else script_root

    campaign = args.campaign
    if not campaign:
        active = state_root / "campaign_state" / ".active"
        if not active.is_file():
            print("load: no active campaign set (campaign_state/.active missing)", file=sys.stderr)
            return 1
        campaign = active.read_text(encoding="utf-8").strip()
    if not campaign:
        print("load: campaign_state/.active is empty", file=sys.stderr)
        return 1

    campaign_root = state_root / "campaign_state" / campaign
    if not campaign_root.is_dir():
        print(f"load: campaign dir not found: {campaign_root}", file=sys.stderr)
        return 1

    # (label, absolute path) in load order. Bases precede their overlays so the
    # merge reads top-down the way the layering rules describe it.
    picked: list[tuple[str, Path]] = []
    seen: set[Path] = set()

    def add(path: Path | None, label: str) -> None:
        if path is None or not path.is_file():
            return
        resolved = path.resolve()
        if resolved in seen:
            return
        seen.add(resolved)
        picked.append((label, resolved))

    add(canon_root / "party" / "preferences.md", "canon preferences")
    add(campaign_root / "preferences.md", "instance preferences")
    for f in sorted((campaign_root / "rules").glob("*.md")):
        add(f, "instance rule")

    for f in sorted((campaign_root / "party" / "saved").glob("*.md")):
        add(pc_base(canon_root, campaign_root, f.stem), "party base")
        add(f, "party overlay")

    for domain in ("npcs", "locations", "timelines", "factions", "items", "quests"):
        for f in sorted((campaign_root / domain / "saved").glob("*.md")):
            add(find_base(canon_root, domain, f.stem), f"{domain} base")
            add(f, f"{domain} overlay")

    for f in sorted((campaign_root / "conversation_states").glob("*.md")):
        add(f, "conversation state")
    for f in sorted((campaign_root / "staging").glob("*.md")):
        add(f, "staging (in-flight scene)")

    # Header first: the transcript previews the opening lines before collapsing the
    # rest, so nothing here may name an entity.
    total = sum(p.stat().st_size for _, p in picked)
    print("===== SCENE CONTEXT =====")
    print(f"campaign: {campaign}")
    print(f"files: {len(picked)}  bytes: {total}")
    print("=========================")
    print()

    for label, path in picked:
        try:
            rel = path.relative_to(state_root)
        except ValueError:
            rel = path.relative_to(canon_root)
        print(f"----- {label}: {rel.as_posix()} -----")
        print(path.read_text(encoding="utf-8", errors="replace").rstrip())
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
