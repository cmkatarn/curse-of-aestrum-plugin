"""Shared helpers for the Claude Code gate hooks.

Project-neutral: knows nothing about any consumer. Both hooks need the same
three things — the stdin event payload, the "is a scene active in this
session?" scope guard, and the small per-session state file used to cache the
scope-guard result and count consecutive blocks (loop guard).

Transcript shape (verified against real session files):
  - one JSON object per line; relevant `type`s are "assistant" and "user"
  - assistant lines: {"type":"assistant","message":{"content":[blocks...]}}
    where a block is {"type":"text","text":...} or
    {"type":"tool_use","name":...,"input":{...}}
  - a scene is started either by the Skill tool
    (tool_use name=="Skill", input.skill==<name>) or by the user typing the
    slash command (a user line containing "<command-name>/<name></command-name>").
  - <name> is recorded as the skill is addressed: bare ("scene") for a
    project skill, namespaced ("<plugin>:scene") for a plugin skill.

The scope guard therefore never assumes a name. Each consumer's hook
registration passes its own entry point(s) via --scene-skill, so a consumer's
hooks arm only in sessions that loaded that consumer's scene — not in a sibling
project that happens to have a skill with the same bare name, and not never
(a hardcoded bare name can't match a plugin's namespaced one).

Substring prefilters are used for speed but every hit is JSON-verified —
tool RESULTS quoting these strings must not count as invocations.
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path

# Prefilter string; cheap line screen before JSON parsing. The slash-command
# prefilters are per-consumer (built from --scene-skill), see _cmd_markers.
_SKILL_PREFILTER = '"Skill"'


class HookArgumentParser(argparse.ArgumentParser):
    """argparse for hooks: a bad registration warns loudly instead of blocking.

    Stock argparse exits 2 on a usage error, and to a Stop hook exit 2 IS a
    block — a typo in a hook registration would surface as a bogus gate
    rejection with argparse's usage text as the "reason". Instead: exit 0 and
    say so via systemMessage, every turn, until the registration is fixed. A
    gate that cannot run is a reason to warn, not to confiscate the game.
    """

    def error(self, message: str) -> None:  # type: ignore[override]
        print(json.dumps({"systemMessage": (
            f"\n[gate] Hook misconfigured ({self.prog}): {message}. The gate did "
            "NOT run this turn, so narration is unchecked. Fix the hook "
            "registration, then start a new session.\n")}))
        sys.exit(0)


def add_scene_skill_arg(parser: argparse.ArgumentParser) -> None:
    """The scope-guard identity. Required, no default — see module docstring."""
    parser.add_argument(
        "--scene-skill", action="append", required=True, metavar="NAME",
        help="skill name that starts this consumer's scene, as the transcript "
             "records it: 'scene' for a project skill, '<plugin>:scene' for a "
             "plugin skill (repeatable)")


def scene_skills(parser: argparse.ArgumentParser, args: argparse.Namespace) -> tuple[str, ...]:
    """Validated, de-duplicated --scene-skill values (errors via parser.error)."""
    names = tuple(sorted({s.strip() for s in args.scene_skill}))
    if not names or "" in names:
        parser.error("--scene-skill must be a non-empty skill name")
    return names


def _cmd_markers(skills: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(f"<command-name>/{s}</command-name>" for s in skills)


def read_event() -> dict:
    """Parse the hook event JSON from stdin; empty dict on any failure."""
    try:
        return json.loads(sys.stdin.read() or "{}")
    except (json.JSONDecodeError, OSError):
        return {}


def state_path(session_id: str) -> Path:
    return Path(tempfile.gettempdir()) / f"calliope_gate_{session_id or 'unknown'}.json"


def load_state(session_id: str) -> dict:
    try:
        return json.loads(state_path(session_id).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def save_state(session_id: str, state: dict) -> None:
    try:
        state_path(session_id).write_text(json.dumps(state), encoding="utf-8")
    except OSError:
        pass  # state is an optimization + loop guard; never crash a hook on it


def _line_invokes_scene(line: str, skills: tuple[str, ...]) -> bool:
    """JSON-verified check that this transcript line starts one of `skills`."""
    markers = _cmd_markers(skills)
    if any(m in line for m in markers):
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            return False
        if obj.get("type") != "user":
            return False
        content = obj.get("message", {}).get("content")
        # Only the user's own typed text counts. A tool RESULT (also a "user"
        # line, content = list of tool_result blocks) that merely quotes the
        # command string must NOT register as a scene start.
        if isinstance(content, str):
            return any(m in content for m in markers)
        if isinstance(content, list):
            return any(
                isinstance(b, dict)
                and b.get("type") == "text"
                and any(m in b.get("text", "") for m in markers)
                for b in content
            )
        return False
    if _SKILL_PREFILTER in line:
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            return False
        if obj.get("type") != "assistant":
            return False
        for block in obj.get("message", {}).get("content", []) or []:
            if (
                isinstance(block, dict)
                and block.get("type") == "tool_use"
                and block.get("name") == "Skill"
                and isinstance(block.get("input"), dict)
                and block["input"].get("skill") in skills
            ):
                return True
    return False


def scene_active(event: dict, skills: tuple[str, ...]) -> bool:
    """Scope guard: has one of `skills` been invoked in THIS session?

    Positive results are cached in the session state file so the transcript is
    not rescanned on every hook firing. The cache key includes the skill set:
    two consumers' hooks can share a session (a project skill and a plugin
    skill side by side), and one arming must not arm the other. A negative
    result is never cached — the scene may start later in the session.
    """
    session_id = event.get("session_id", "")
    state = load_state(session_id)
    cache_key = "scene_active:" + ",".join(skills)
    if state.get(cache_key):
        return True
    markers = _cmd_markers(skills)

    transcript = event.get("transcript_path", "")
    if not transcript or not Path(transcript).exists():
        return False
    try:
        with open(transcript, encoding="utf-8") as fh:
            for line in fh:
                if _SKILL_PREFILTER not in line and not any(m in line for m in markers):
                    continue
                if _line_invokes_scene(line, skills):
                    state[cache_key] = True
                    save_state(session_id, state)
                    return True
    except OSError:
        return False
    return False


def last_assistant_text(transcript: str) -> str:
    """The text of the most recent main-chain assistant message with any text
    blocks (tool-use-only messages are skipped). Empty string if none."""
    result = ""
    try:
        with open(transcript, encoding="utf-8") as fh:
            for line in fh:
                if '"assistant"' not in line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if obj.get("type") != "assistant" or obj.get("isSidechain"):
                    continue
                blocks = obj.get("message", {}).get("content", []) or []
                texts = [
                    b.get("text", "")
                    for b in blocks
                    if isinstance(b, dict) and b.get("type") == "text"
                ]
                joined = "\n".join(t for t in texts if t).strip()
                if joined:
                    result = joined
    except OSError:
        return ""
    return result
