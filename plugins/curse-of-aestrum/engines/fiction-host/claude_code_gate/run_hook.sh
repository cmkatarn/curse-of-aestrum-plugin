#!/bin/sh
# Launch a gate hook under whatever Python 3 this machine actually has.
#
# Hook commands in a plugin manifest are one fixed string shared by every platform, so naming an
# interpreter directly there picks a winner: `py` exists only on Windows, `python3` only off it.
# Either choice leaves the gate silently not running for half the users — the worst failure mode
# available to a tool whose whole job is catching what the narration got wrong.
#
# So the manifest invokes `sh run_hook.sh <script> [args...]` instead, and the resolution happens
# here, at play time, on the machine that has the answer. Claude Code provides `sh` on every
# platform it supports (on Windows via the Git Bash it already requires), which is why this is a
# POSIX shell script and not a Python one: a Python launcher would need the interpreter it is
# looking for.
#
# Candidates are probed by running them, not by testing for a file: Windows ships a `python3`
# App Execution Alias that is a Microsoft Store stub, and some systems carry an unrelated `py`.
# Both fail the probe and are skipped, which a -x test would not catch.
#
# The probe demands TOML parsing rather than a bare import, because the gate's lint specs are TOML:
# stdlib tomllib (3.11+) or the tomli backport both satisfy it, and an interpreter with neither
# cannot load a spec no matter how new it is.
set -u

PROBE='import importlib.util as u, sys; sys.exit(0 if (u.find_spec("tomllib") or u.find_spec("tomli")) else 1)'

for cand in "py -3" "python3" "python"; do
    # Intentionally unquoted: $cand carries the interpreter plus its flags as separate words.
    # shellcheck disable=SC2086
    if $cand -c "$PROBE" >/dev/null 2>&1; then
        # exec, so the hook inherits this process: stdin (the event JSON) passes through untouched
        # and the script's own exit code reaches Claude Code rather than this wrapper's.
        # shellcheck disable=SC2086
        exec $cand "$@"
    fi
done

# No usable interpreter. Say so loudly and let the turn proceed: the alternative is blocking every
# prompt in the session, and a gate that cannot run is a reason to warn, not to confiscate the game.
# Exit 0 with a systemMessage — a nonzero exit here would read to Claude Code as a gate verdict.
printf '%s\n' '{"systemMessage":"\n[gate] No Python 3 with TOML support found on PATH, so the play-time epistemic gate did NOT run this turn. Narration is unchecked until this is fixed. Install Python 3.11+ (or 3.9+ with the tomli package) and start a new session.\n"}'
exit 0
