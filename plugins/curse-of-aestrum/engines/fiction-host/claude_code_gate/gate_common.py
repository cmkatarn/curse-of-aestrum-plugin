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
    (tool_use name=="Skill", input.skill=="scene") or by the user typing the
    slash command (a user line containing "<command-name>/scene</command-name>").

Substring prefilters are used for speed but every hit is JSON-verified —
tool RESULTS quoting these strings must not count as invocations.
"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

# Prefilter strings; cheap line screen before JSON parsing.
_SKILL_PREFILTER = '"Skill"'
_CMD_PREFILTER = "<command-name>/scene</command-name>"


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


def _line_invokes_scene(line: str) -> bool:
    """JSON-verified check that this transcript line starts the scene skill."""
    if _CMD_PREFILTER in line:
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
            return _CMD_PREFILTER in content
        if isinstance(content, list):
            return any(
                isinstance(b, dict)
                and b.get("type") == "text"
                and _CMD_PREFILTER in b.get("text", "")
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
                and block["input"].get("skill") == "scene"
            ):
                return True
    return False


def scene_active(event: dict) -> bool:
    """Scope guard: has the scene skill been invoked in THIS session?

    Positive results are cached in the session state file so the transcript is
    not rescanned on every hook firing. A negative result is never cached —
    the scene may start later in the session.
    """
    session_id = event.get("session_id", "")
    state = load_state(session_id)
    if state.get("scene_active"):
        return True

    transcript = event.get("transcript_path", "")
    if not transcript or not Path(transcript).exists():
        return False
    try:
        with open(transcript, encoding="utf-8") as fh:
            for line in fh:
                if _SKILL_PREFILTER not in line and _CMD_PREFILTER not in line:
                    continue
                if _line_invokes_scene(line):
                    state["scene_active"] = True
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
