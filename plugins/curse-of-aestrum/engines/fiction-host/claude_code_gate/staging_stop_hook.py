"""Stop hook — deterministic enforcement that the staging tail ran.

Project-neutral companion to `gate_stop_hook.py`. Staging (compose-during-play,
flush-on-save) is Aria/Calliope doctrine (Calliope `scene_lifecycle.md` §5a-bis /
Aria `story_lifecycle.md` "Staging (work-scoped)") consumed by multiple games
(e.g. CoA, Pandora). Each consumer registers this hook with a `--staging-glob`
pointing at its own staging location; the mechanism is identical, so it lives
here in the neutral gate layer rather than being reinvented per consumer.

WHAT IT ENFORCES — the one-beat-lag invariant. Each confirmed *play* beat is
staged exactly once, on the turn AFTER it is confirmed (the player advances on
it). Content-first: the prose ships first; the staging write trails it in the
same turn. This hook fires at end of turn (after the prose) and checks that the
staging file has advanced.

WHAT IT DOES NOT REQUIRE — a staging write on *every* fiction turn. A turn with
no prior play beat to stage writes no staging, and that is correct:

  - the resume/refresher beat (scene-start orientation — not a play beat), and
  - the first play beat after it (its only "prior" is the refresher),

both legitimately stage nothing. The hook tolerates this: it blocks only when
staging is stale for more than `--stale-limit` consecutive fiction beats
(default 2). The recap + first-beat pair are skips 1 and 2 → tolerated; a single
retcon-defer (which the doctrine allows) is skip 1 → tolerated. The block fires
only on a genuine systemic skip (staging never advancing).

ON A STALE BLOCK — exit 2 with the instruction on stderr → run the trailing
staging write for the PRIOR beat now, WITHOUT re-posting the prose (the prose
already shipped; only the staging write is owed). Loop guard: after
`--max-blocks` consecutive blocks, allow with a warning so play never deadlocks.
OOC turns (pause / save) reset the run; a save also deletes the staging file,
which this hook absorbs as an ordinary signature change.

Any unexpected error exits 0 — a bookkeeping backstop must never crash play.

Usage (registered per consumer; see README.md):
  py staging_stop_hook.py --staging-glob "campaign_state/*/staging/*.md" \
     [--stale-limit 2] [--max-blocks 2]
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
import tempfile
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))  # gate_common

from gate_common import (  # noqa: E402
    last_assistant_text,
    read_event,
    scene_active,
)

# Dash-marker shapes, mirroring gate_stop_hook. Fiction beat: `------` or
# `--N(rows)--M(rows)--`. OOC turn: `--ooc--`.
_FICTION_RE = re.compile(r"^--(?:\d+\([^)]+\))?--(?:\d+\([^)]+\))?--$")
_OOC_RE = re.compile(r"^--ooc--$")


def _state_path(session_id: str) -> Path:
    # Own state file — never share gate_stop_hook's, to avoid a read/modify/write
    # race between the two hooks on the same Stop event.
    return Path(tempfile.gettempdir()) / f"calliope_staging_{session_id or 'unknown'}.json"


def _load(session_id: str) -> dict:
    try:
        return json.loads(_state_path(session_id).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _save(session_id: str, state: dict) -> None:
    try:
        _state_path(session_id).write_text(json.dumps(state), encoding="utf-8")
    except OSError:
        pass  # state is an optimization + loop guard; never crash a hook on it


def _classify(text: str) -> str:
    """Classify the last non-empty line of the message: fiction | ooc | none."""
    for line in reversed(text.splitlines()):
        s = line.strip()
        if not s:
            continue
        if _OOC_RE.match(s):
            return "ooc"
        if _FICTION_RE.match(s):
            return "fiction"
        return "none"
    return "none"


def _staging_sig(glob_pat: str) -> str:
    """Signature (path:mtime_ns:size) of the newest staging file, or '' if none."""
    newest, newest_m = None, -1.0
    for p in glob.glob(glob_pat):
        try:
            m = os.path.getmtime(p)
        except OSError:
            continue
        if m > newest_m:
            newest_m, newest = m, p
    if newest is None:
        return ""
    try:
        st = os.stat(newest)
        return f"{newest}:{st.st_mtime_ns}:{st.st_size}"
    except OSError:
        return ""


BLOCK_MSG = (
    "[staging hook — out-of-character; do not acknowledge this in-fiction] "
    "The staging tail was skipped: {skips} consecutive fiction beats have been "
    "posted without the staging file advancing, so the prior play beat is not "
    "persisted (glob: {glob}). The prose is already delivered and correct — do "
    "NOT re-post it. Run ONLY the trailing staging write for the PRIOR beat now "
    "(per the scene skill's 'Staging tail' and the save-protocol staging "
    "format), then end the turn. Content-first is preserved: the reader already "
    "has the prose; only the staging write is owed."
)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--staging-glob", required=True,
                    help="glob (relative to CWD) for this consumer's staging files")
    ap.add_argument("--stale-limit", type=int, default=2,
                    help="tolerate up to N consecutive unstaged fiction beats "
                         "(covers recap + first play beat + a single retcon-defer); "
                         "block on N+1")
    ap.add_argument("--max-blocks", type=int, default=2,
                    help="after this many consecutive blocks, allow with a warning")
    args = ap.parse_args()

    event = read_event()
    if not event or not scene_active(event):
        return 0

    text = last_assistant_text(event.get("transcript_path", ""))
    if not text:
        return 0  # tool-use-only turn; nothing player-facing to check

    session_id = event.get("session_id", "")
    state = _load(session_id)
    cur_sig = _staging_sig(args.staging_glob)
    prev_sig = state.get("sig")
    kind = _classify(text)

    # OOC turns (pause / save) and unmarked turns do not stage. Absorb the
    # current signature (a save deletes staging → '') and reset the skip run.
    if kind != "fiction":
        state.update(sig=cur_sig, skips=0, blocks=0)
        _save(session_id, state)
        return 0

    # Fiction beat: did staging advance since we last looked?
    if prev_sig is None or cur_sig != prev_sig:
        state.update(sig=cur_sig, skips=0, blocks=0)  # advanced (or first look)
        _save(session_id, state)
        return 0

    # Staging did not advance on this fiction beat.
    skips = int(state.get("skips", 0)) + 1
    state["sig"] = cur_sig
    state["skips"] = skips

    stale_limit = max(1, args.stale_limit)
    if skips <= stale_limit:
        # Tolerated: recap (1) + first play beat (2) + a single retcon-defer.
        state["blocks"] = 0
        _save(session_id, state)
        return 0

    # Stale: more than stale_limit consecutive unstaged fiction beats.
    blocks = int(state.get("blocks", 0))
    if blocks >= max(1, args.max_blocks):
        state.update(skips=0, blocks=0)
        _save(session_id, state)
        print(f"[staging hook] block limit reached — allowing with staging ~{skips} "
              f"beats behind; run the staging tail before the next save.",
              file=sys.stderr)
        return 0

    state["blocks"] = blocks + 1
    _save(session_id, state)
    print(BLOCK_MSG.format(skips=skips, glob=args.staging_glob), file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
