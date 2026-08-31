# claude_code_gate — deterministic gate enforcement for Claude Code play

When a consumer's scene skill runs inside **Claude Code** (instead of the
standalone runtime), the single gate is model-executed and can silently decay
over a long session. This directory makes "the checks ran" deterministic, at
near-zero token cost, using Claude Code hooks. It never edits model text — it
only accepts or rejects; a rejection re-enters the model's full drafting gate
(single-gate compliant: redraft, not mutate).

Components (all project-neutral; stdlib-only, reuses `runtime.lint`):

| File | Role |
|------|------|
| `{{PLUGIN_ROOT}}/engines/fiction-host/claude_code_gate/gate_attestation.md` | Model-facing protocol: end every scene-session message with a dash-marker attestation (`------` clean, `--N(rN,...)--M(rN,...)--` resolved, `--ooc--` non-fiction) on its own line, preceded by a blank line. |
| `{{PLUGIN_ROOT}}/engines/fiction-host/claude_code_gate/gate_prompt_hook.py` | `UserPromptSubmit` hook: injects a one-line gate reminder each player turn while a scene is active (~30 tokens; silent otherwise). |
| `{{PLUGIN_ROOT}}/engines/fiction-host/claude_code_gate/gate_stop_hook.py` | `Stop` hook: blocks the turn (exit 2) if the marker is missing, malformed, or missing its required blank line above, or if a fiction beat trips the closed-vocabulary token scan; bounded by `--max-redrafts` (default 2), then warn-and-allow. |
| `{{PLUGIN_ROOT}}/engines/fiction-host/claude_code_gate/staging_stop_hook.py` | `Stop` hook: enforces that the **staging tail** ran. Staging (compose-during-play, flush-on-save) is Aria/Calliope doctrine consumed by multiple games; each registers this hook with its own `--staging-glob`. Enforces the one-beat-lag invariant — **not** "every fiction turn stages": a turn with no prior play beat (the resume/refresher beat, the first play beat after it, a single retcon-defer) correctly stages nothing and is tolerated. Blocks (exit 2) only when staging is stale past `--stale-limit` (default 2) consecutive fiction beats; bounded by `--max-blocks` (default 2), then warn-and-allow. |
| `{{PLUGIN_ROOT}}/engines/fiction-host/claude_code_gate/gate_common.py` | Shared stdin/transcript/scope-guard/state helpers. |

Scope guard: hooks act only in sessions where the scene skill was actually
invoked (JSON-verified `Skill` tool use or `/scene` command in the session
transcript); all other sessions see zero behavior and zero tokens.

## Wiring a consumer (once per project)

1. **Hooks** — in the consumer's `{{PLUGIN_ROOT}}/.claude/settings.json` (or
   `settings.local.json`), with `--spec` listing that game's token sidecars
   (mirror its lint spec set; paths relative to the consumer project root):

```json
"hooks": {
  "UserPromptSubmit": [{ "matcher": "*", "hooks": [{ "type": "command",
    "command": "py {{PLUGIN_ROOT}}/engines/fiction-host/claude_code_gate/gate_prompt_hook.py" }]}],
  "Stop": [{ "matcher": "*", "hooks": [{ "type": "command",
    "command": "py {{PLUGIN_ROOT}}/engines/fiction-host/claude_code_gate/gate_stop_hook.py --spec {{PLUGIN_ROOT}}/engines/prose-engine/scene/gate/infrastructure_tokens.toml" }]}]
}
```

2. **Protocol** — one line in the consumer's scene skill load order:
   *"Read `{{PLUGIN_ROOT}}/engines/fiction-host/claude_code_gate/gate_attestation.md` and follow it
   for every beat."*

3. **Staging enforcement** *(if the consumer stages)* — add a second `Stop`
   command with that game's staging glob (paths relative to the consumer root):

```json
"Stop": [{ "matcher": "*", "hooks": [
  { "type": "command", "command": "py {{PLUGIN_ROOT}}/engines/fiction-host/claude_code_gate/gate_stop_hook.py --spec {{PLUGIN_ROOT}}/engines/prose-engine/scene/gate/infrastructure_tokens.toml" },
  { "type": "command", "command": "py {{PLUGIN_ROOT}}/engines/fiction-host/claude_code_gate/staging_stop_hook.py --staging-glob \"<staging-glob>\"" }
]}]
```

   CoA uses `{{PROJECT_ROOT}}/campaign_state/*/staging/*.md`; Pandora uses
   `local/anthologies/*/staging/*.md`.

That's all. The shared scripts carry no consumer data; everything
game-specific arrives via `--spec` / `--staging-glob`.

## Notes

- The dash-marker attestation is renderer-safe by design: the clean form
  (`------`) renders as a markdown horizontal rule in every CommonMark
  renderer, and the dirty forms (`--N(rN,...)--M(rN,...)--`, `--ooc--`) are
  short inline text that signals "the gate caught and resolved something."
  No MessageDisplay strip is needed; the prior `gate_display_hook.py` has
  been retired.
- The marker requires a **blank line above it** so `------` renders as
  `<hr>` rather than as a setext heading underline of the preceding
  paragraph; the Stop hook enforces this.
- `ooc`-attested turns skip the token scan (player-requested meta is exempt
  from infrastructure-citation per the engine's player-scoped OOC carve-out).
- **Sub-agent shells — tried, reverted; cautionary note.** A consumer's
  scene skill *could* in principle route drafting through a session-scoped
  sub-agent (e.g. `.claude/agents/scene-drafter.md`) on the theory that
  Stop-hook rejection cycles would happen inside the child's conversation
  rather than on screen. CurseOfAestrum and Pandora both tried this shape
  and **reverted** it. Two problems made it net-worse than in-parent
  drafting:
  1. *Agent panels are visible.* The agent tool's response is fully
     surfaced to the player in the UI — preamble, planning, draft passes,
     gate-check verbalization, and the actual prose, all in the panel.
     The parent then re-posted the prose. The prose effectively appeared
     twice with a wall of meta narration between them, manifesting as
     "multiple drafts per turn." Stop-hook *rejections* did stay inside
     the child, but the model's normal pre-posting reasoning did not, and
     that reasoning fires every turn.
  2. *Cross-turn continuity drifts.* The harness here exposes no way to
     push new input into a live sub-agent, so the child has to be
     re-spawned per turn. The re-spawn's briefing is a summary, not the
     literal prior beat — so the new child confabulates against summary
     priors (the wineglass that was a cloth; the half-step behind that
     was the foyer). Continuity drift is the recurring failure mode.

  Both problems vanish when drafting runs in the parent: the model's
  planning and gate-check iterations live in `<thinking>` (hidden in the
  UI by default), and the literal prior beat is in conversation history
  for free. Reconsider the sub-agent split only in a harness that does
  not surface agent panels to the user *and* exposes a SendMessage-style
  primitive that pushes new input into a live child.
- Per-session state (scope-guard cache + block counter) lives in
  `%TEMP%/calliope_gate_<session_id>.json`. `{{PLUGIN_ROOT}}/engines/fiction-host/claude_code_gate/staging_stop_hook.py` keeps its
  own separate state (`%TEMP%/calliope_staging_<session_id>.json`) so the two
  Stop hooks never race on a shared file.
- This is complementary to the standalone runtime's in-loop lint
  (`runtime/lint/`): same matcher, same sidecars, different host.
