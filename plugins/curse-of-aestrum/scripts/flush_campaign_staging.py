#!/usr/bin/env python3
"""flush_campaign_staging.py — flush the active scene's staging file into the
campaign's monolith overlays + the transcript, then delete staging.

CoA analogue of Pandora's scripts/flush_staging.py. The shared *doctrine*
(staging mechanism, transcript carve-out, save = flush) lives upstream in
Calliope's scene_lifecycle.md (section 5a-bis) and Aria's story_lifecycle.md
("Staging (work-scoped)"). This script is CoA's concrete flush: it APPENDS to the
existing per-entity monolith overlays (CoA does NOT shard).

The append itself is fiction-host's runtime/state.py::append_delta, called rather
than reimplemented. This script used to be PowerShell, which put the overlay byte
format in two languages that could not share a test — and they had in fact
drifted. One implementation, in the language the rest of the play-time tooling
already requires, is the point of the port. CoA keeps what is CoA's (which domain
lands in which directory); the engine keeps the byte format.

Python is not a new dependency: the play-time epistemic-gate hooks already require
3.11+, so every machine that can play a scene can run this.

Usage:
  python3 scripts/flush_campaign_staging.py --campaign <campaign-id> [--dry-run]
  python3 scripts/flush_campaign_staging.py --campaign <id> --repo-root <path>

Staging file format (campaign_state/<C>/staging/<sid>.md):
  # Objective log                  -> append to timelines/saved/aestrum_events.md
  # Experience deltas
    ## party/<name>                -> append to party/saved/<name>.md
    ## npcs/<name>                 -> append to npcs/saved/<name>.md
  # Entity overlays
    ## factions/<id>               -> append to factions/saved/<id>.md
    ## items/<id>                  -> append to items/saved/<id>.md
    ## locations/<id>              -> append to locations/saved/<id>.md
  # Transcript                     -> write conversation_states/<sid>.md (verbatim)
Each h2 (and the objective log) body is a `### Day N - desc` block + bullets.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

EXP_DOMAINS = ("party", "npcs")
ENTITY_DOMAINS = ("factions", "items", "locations")

# Whitespace trimmed from section bodies. Includes CR so a CRLF staging file does
# not leave a stray carriage return at the end of every block it contributes.
_TRIM = "\r\n \t"

_FRONTMATTER_RE = re.compile(r"---\s*\r?\n.*?\r?\n---\s*\r?\n(.*)", re.DOTALL)
# The transcript boundary is matched as a whole line, so only a real section
# header can split there.
_TRANSCRIPT_RE = re.compile(r"^#[ \t]+Transcript[ \t]*\r?$", re.MULTILINE)
# Lookahead splits keep each header line attached to its own section. `#\s` cannot
# match `##`, so an h2 never reads as an h1 boundary.
_H1_SPLIT_RE = re.compile(r"(?=^#\s)", re.MULTILINE)
_H2_SPLIT_RE = re.compile(r"(?=^##\s)", re.MULTILINE)
_H1_RE = re.compile(r"#\s+([^\r\n]+)\r?\n(.*)", re.DOTALL)
_H2_RE = re.compile(r"##\s+([^\r\n]+)\r?\n(.*)", re.DOTALL)
_DOMAIN_RE = re.compile(r"([^/]+)/(.+)")


def fail(msg):
    """Abort with a nonzero status. Save is all-or-nothing by the caller's rule:
    the scene skill must not hand-write overlays as a fallback, so a bad staging
    file has to stop the flush loudly rather than half-apply it."""
    print(f"flush: {msg}", file=sys.stderr)
    raise SystemExit(1)


def load_append_delta():
    """Import fiction-host's append_delta from whichever layout we are in.

    Resolution is relative to THIS FILE, never to --repo-root: the test suite
    points --repo-root at a throwaway fixture while the script stays put, so the
    engine has to be found next to the script's own tree either way.
    """
    here = Path(__file__).resolve().parent
    candidates = (
        here.parent / "engines" / "fiction-host",   # installed plugin bundle
        here.parent.parent / "fiction-host",        # sibling source checkouts
    )
    for root in candidates:
        if (root / "runtime" / "state.py").is_file():
            sys.path.insert(0, str(root))
            from runtime.state import append_delta
            return append_delta
    looked = "; ".join(str(c) for c in candidates)
    fail(f"could not locate fiction-host runtime/state.py (looked in: {looked})")


def read_raw(path):
    """Read text with line endings untouched, so a flush never rewrites them."""
    with path.open(encoding="utf-8", newline="") as fh:
        return fh.read()


def write_raw(path, text):
    """Write UTF-8 with no BOM and no newline translation.

    Overlays and transcripts are parsed artifacts shared with fiction-host's own
    save path, so their bytes must not depend on which host wrote them.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def split_sections(text, split_re, header_re):
    """Split on a heading lookahead into ordered (header, body) pairs."""
    out = []
    for part in split_re.split(text):
        if not part.strip():
            continue
        m = header_re.match(part)
        if m:
            out.append((m.group(1).strip(), m.group(2).strip(_TRIM)))
    return out


def main():
    ap = argparse.ArgumentParser(description="Flush a scene's staging file into campaign overlays.")
    ap.add_argument("--campaign", required=True, help="campaign id under campaign_state/")
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would be written, write nothing")
    ap.add_argument("--repo-root", help="repo root (default: the parent of this script's directory)")
    args = ap.parse_args()

    append_delta = load_append_delta()

    repo_root = (Path(args.repo_root).resolve() if args.repo_root
                 else Path(__file__).resolve().parent.parent)
    campaign_root = repo_root / "campaign_state" / args.campaign
    if not campaign_root.is_dir():
        fail(f"campaign dir not found: {campaign_root}")

    staging_dir = campaign_root / "staging"
    if not staging_dir.is_dir():
        fail(f"staging dir not found: {staging_dir}")

    staging_files = sorted(p for p in staging_dir.glob("*.md") if p.is_file())
    if not staging_files:
        fail(f"no staging file found in {staging_dir}")
    if len(staging_files) > 1:
        names = ", ".join(p.name for p in staging_files)
        fail(f"multiple staging files in {staging_dir} - cannot flush ambiguously: {names}")

    staging_file = staging_files[0]
    scene_id = staging_file.stem
    content = read_raw(staging_file)

    # Strip the optional YAML frontmatter.
    m = _FRONTMATTER_RE.match(content)
    body = m.group(1) if m else content

    # Carve the Transcript off FIRST, before any section splitting. The transcript
    # is the terminal freeform-prose region: everything from the `# Transcript` h1
    # to EOF, verbatim. It is NOT sub-split, so a prose line that happens to begin
    # with `# ` (a read-aloud heading, a reproduced document, "# of bodies they
    # never found:") can never be mistaken for a section boundary and silently
    # truncate the save. (Calliope scene_lifecycle.md section 5a-bis carve-out.)
    transcript = None
    structural_body = body
    parts = _TRANSCRIPT_RE.split(body, maxsplit=1)
    if len(parts) == 2:
        structural_body = parts[0]
        transcript = parts[1].strip(_TRIM)

    sections = dict(split_sections(structural_body, _H1_SPLIT_RE, _H1_RE))
    if "Experience deltas" not in sections:
        fail("staging file is missing required section: '# Experience deltas'")

    def emit(path, block):
        if args.dry_run:
            print(f"[dry-run] would append -> {path}")
        else:
            append_delta(path, block)
            print(f"appended -> {path}")

    # --- Objective log -> timelines/saved/aestrum_events.md ---------------------
    objective = sections.get("Objective log", "").strip(_TRIM)
    if objective:
        emit(campaign_root / "timelines" / "saved" / "aestrum_events.md", objective)

    # --- Experience deltas -> party/saved or npcs/saved ------------------------
    for header, block in split_sections(sections["Experience deltas"], _H2_SPLIT_RE, _H2_RE):
        dm = _DOMAIN_RE.fullmatch(header)
        if not dm:
            fail("experience delta sub-section header must be '<domain>/<name>' "
                 f"(domain in {'|'.join(EXP_DOMAINS)}): '{header}'")
        domain, name = dm.group(1), dm.group(2)
        if domain not in EXP_DOMAINS:
            fail(f"experience delta domain must be one of [{', '.join(EXP_DOMAINS)}]: "
                 f"got '{domain}' in '{header}'")
        emit(campaign_root / domain / "saved" / f"{name}.md", block)

    # --- Entity overlays -> factions/items/locations saved ---------------------
    if "Entity overlays" in sections:
        for header, block in split_sections(sections["Entity overlays"], _H2_SPLIT_RE, _H2_RE):
            dm = _DOMAIN_RE.fullmatch(header)
            if not dm:
                fail(f"entity overlay sub-section header must be '<domain>/<id>': '{header}'")
            domain, entity_id = dm.group(1), dm.group(2)
            if domain not in ENTITY_DOMAINS:
                fail(f"entity overlay domain must be one of [{', '.join(ENTITY_DOMAINS)}]: "
                     f"got '{domain}' in '{header}'")
            emit(campaign_root / domain / "saved" / f"{entity_id}.md", block)

    # --- Transcript -> conversation_states/<sid>.md (verbatim, overwrite) -------
    if transcript:
        tx_path = campaign_root / "conversation_states" / f"{scene_id}.md"
        if args.dry_run:
            print(f"[dry-run] would write -> {tx_path}")
        else:
            write_raw(tx_path, transcript)
            print(f"wrote -> {tx_path}")
    else:
        print("[warn] no Transcript section in staging - skipping transcript write")

    # --- Delete staging ---------------------------------------------------------
    if args.dry_run:
        print(f"[dry-run] would delete {staging_file}")
    else:
        staging_file.unlink()
        print(f"deleted {staging_file}")

    mode = "DRY RUN" if args.dry_run else "DONE"
    print()
    print(f"{mode} - scene {scene_id} flushed for campaign {args.campaign}")


if __name__ == "__main__":
    main()
