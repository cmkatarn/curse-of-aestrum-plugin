"""UserPromptSubmit hook — keeps the gate instruction adjacent to every turn.

When a scene is active in this session, print ONE reminder line to stdout
(exit 0 → appended to the model's context, ~30 tokens). When no scene is
active, print nothing (zero tokens). Never blocks a prompt.

Registered per consumer; see README.md in this directory.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gate_common import read_event, scene_active  # noqa: E402

REMINDER = (
    "[gate] Before posting: run BOTH suites (epistemic + stylistic) against the "
    "draft, then end the message with the dash-marker attestation on its own "
    "line, preceded by a blank line: `------` for a clean fiction beat, "
    "`--N(rN,...)--M(rN,...)--` if findings fired during drafting (row list "
    "required for any nonzero count; empty slots = clean for that suite), or "
    "`--ooc--` for non-fiction turns."
)


def main() -> int:
    event = read_event()
    if event and scene_active(event):
        print(REMINDER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
