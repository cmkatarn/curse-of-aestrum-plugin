"""Stop hook — deterministic enforcement that the gate visibly ran.

Fires when the model finishes a turn. In scene-active sessions it verifies the
last assistant message:

  1. carries the attestation comment as its last non-empty line
     (<!-- gate: E# S# --> | <!-- gate: ooc -->), and
  2. for fiction beats, passes the closed-vocabulary token scan
     (runtime.lint.LintEngine over the consumer-supplied sidecar specs).

On failure: exit 2 with the correction on stderr → the model must redraft (the
hook never edits text; rejection re-enters the model's full drafting gate).
`ooc` turns skip the token scan — player-requested meta (save confirmations,
mechanics answers) is exempt from infrastructure-citation per the engine's
player-scoped OOC carve-out.

Loop guard: consecutive blocks are counted in the per-session state file; after
--max-redrafts the stop is allowed with a warning (mirrors on_exhausted="warn")
so play never deadlocks. Any clean pass resets the counter.

Usage (registered per consumer; see README.md):
  py gate_stop_hook.py --spec <token_sidecar.toml> [--spec ...] [--max-redrafts N]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))           # gate_common
sys.path.insert(0, str(_HERE.parent))    # fiction-host root → runtime.lint

from gate_common import (  # noqa: E402
    last_assistant_text,
    load_state,
    read_event,
    save_state,
    scene_active,
)
from runtime.lint import LintEngine, load_specs  # noqa: E402

# Dash-marker attestation. Three positional `--` separators with two
# optional slots (E, S). Each slot is empty (clean) or `<count>(<rows>)`
# (findings fired and were resolved during drafting). Clean both suites
# renders as a markdown horizontal rule (`------`); dirty cases are short,
# deliberately visible inline counts. OOC turns use `--ooc--`.
ATTESTATION_RE = re.compile(
    r"^--(?:(\d+)\(([^)]+)\))?--(?:(\d+)\(([^)]+)\))?--$"
)
_OOC_FORM_RE = re.compile(r"^--ooc--$")
# Loose shape-match for "the model tried to emit a marker but it's malformed."
# Matches `--<slot>--<slot>--` where each slot has no internal `-`. Distinguishes
# a malformed attempt (e.g. `--2----`, count without rows → ROWS_REQUIRED_MSG)
# from a missing attestation entirely.
_MARKER_SHAPE_RE = re.compile(r"^--[^-]*--[^-]*--$")
_STRIP_ATTESTATION_RE = re.compile(
    r"^(?:--[^-]*--[^-]*--|--ooc--)$",
    re.MULTILINE,
)

MISSING_MSG = (
    "Gate attestation missing — the single gate did not visibly run. Run BOTH "
    "suites (epistemic + stylistic) against your last beat, fix any findings, "
    "and re-emit the corrected beat ending with the dash-marker attestation: "
    "`------` for a clean pass (both suites zero findings), "
    "`--N(rN,...)--M(rN,...)--` if findings fired during drafting (row list "
    "required for any nonzero count), or `--ooc--` for non-fiction turns. "
    "The marker is on its own line, preceded by a blank line, as the last "
    "non-empty line of the message. Do not display or apologize for the "
    "rejected draft; simply emit the corrected beat.\n"
    "If your PREVIOUS message already posted a valid beat and marker and THIS "
    "message is just a trailing handoff, recap, or 'your move' line, that "
    "stray line is the failure — the beat was fine and already handed control. "
    "End the turn on your state-writes (staging/save) and emit no further "
    "player-facing prose; if a closing line is unavoidable, it is OOC and must "
    "end with `--ooc--`."
)

BLANK_LINE_MSG = (
    "Gate attestation present but missing the required blank line above the "
    "marker. The line immediately above the marker must be empty so the "
    "clean form `------` renders as a markdown horizontal rule rather than a "
    "setext heading underline. Re-emit the corrected beat with one blank "
    "line between the last paragraph and the marker."
)

ROWS_REQUIRED_MSG = (
    "Gate attestation form invalid — a nonzero count must be followed by the "
    "row list it resolved, e.g. `--2(r3,r13)----` not `--2----`. A "
    "findings-resolved pass is never collapsed to the clean form. Re-emit "
    "the corrected beat with the row list filled in for any nonzero count."
)


def _block(event: dict, state: dict, message: str) -> int:
    state["blocks"] = int(state.get("blocks", 0)) + 1
    save_state(event.get("session_id", ""), state)
    print(message, file=sys.stderr)
    return 2


def _allow(event: dict, state: dict, warning: str | None = None) -> int:
    if state.get("blocks"):
        state["blocks"] = 0
        save_state(event.get("session_id", ""), state)
    if warning:
        print(warning, file=sys.stderr)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", action="append", default=[],
                        help="token sidecar TOML (repeatable)")
    parser.add_argument("--max-redrafts", type=int, default=2)
    args = parser.parse_args()

    event = read_event()
    if not event or not scene_active(event):
        return 0

    text = last_assistant_text(event.get("transcript_path", ""))
    if not text:
        return 0  # tool-use-only turn; nothing player-facing to check

    state = load_state(event.get("session_id", ""))

    # Loop guard — never deadlock play.
    if int(state.get("blocks", 0)) >= args.max_redrafts:
        return _allow(event, state,
                      f"[gate hook] redraft limit ({args.max_redrafts}) reached — "
                      "allowing the beat with a warning.")

    lines = text.splitlines()
    marker_idx = next(
        (i for i in range(len(lines) - 1, -1, -1) if lines[i].strip()),
        None,
    )
    if marker_idx is None:
        return 0  # whitespace-only message; nothing to check
    marker = lines[marker_idx].strip()

    is_ooc = bool(_OOC_FORM_RE.match(marker))
    is_attest = bool(ATTESTATION_RE.match(marker))
    is_shape = bool(_MARKER_SHAPE_RE.match(marker))

    # 1. Attestation present and well-formed?
    if not (is_ooc or is_attest):
        # Distinguish "tried but malformed" (count without rows) from "missing".
        if is_shape:
            return _block(event, state, ROWS_REQUIRED_MSG)
        return _block(event, state, MISSING_MSG)

    # 2. Blank line above the marker (markdown <hr> invariant for `------`).
    if marker_idx > 0 and lines[marker_idx - 1].strip():
        return _block(event, state, BLANK_LINE_MSG)

    # 3. ooc turns: player-requested meta is exempt from the token scan.
    if is_ooc:
        return _allow(event, state)

    # 4. Deterministic closed-vocabulary scan (fiction beats only).
    specs = load_specs([Path(p) for p in args.spec])
    engine = LintEngine(specs, enabled=True)
    if engine.enabled:
        scan_text = _STRIP_ATTESTATION_RE.sub(" ", text)
        result = engine.validate(scan_text)
        if not result.is_clean:
            return _block(event, state, engine.correction_prompt(result))

    return _allow(event, state)


if __name__ == "__main__":
    raise SystemExit(main())
