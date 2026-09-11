---
name: scene
description: >
  Use this skill when the user wants to run an interactive scene from the Curse of
  Aestrum campaign — dialogue, action, location-establishment, multi-character
  interactions, or any combination — played live as back-and-forth between the user
  and the world. Triggers on "new scene", "play a scene", "run a scene", "stage a
  scene", "start a scene", "scene at [location]", "scene with [character]", "scene
  where [thing happens]", "have a conversation with", "talk to", "load up [NPC
  name]", "chat with", "roleplay with", "new [NPC] conversation", "load [NPC] for
  a conversation". Also triggers on resuming or switching a saved campaign:
  "resume campaign", "resume", "resume the game", "continue the campaign", "pick
  the campaign back up", "switch to campaign [id]", "load the [id] campaign".
  Also handles "save campaign state" and pause triggers. Do NOT use for writing
  prose chapters or generating character portraits.
---

> **Plugin path resolution — read this first.** You are running inside an installed plugin. Two
> placeholders appear in this skill and in every file it leads you to read:
> `{{PLUGIN_ROOT}}` = `${CLAUDE_PLUGIN_ROOT}` (this plugin's bundled files — engines, rules,
> overrides, and campaign content) and `{{PROJECT_ROOT}}` = `${CLAUDE_PROJECT_DIR}` (the player's
> own working directory, where every `campaign_state/…` play-state file is read and written).
> Whenever any file you read contains a `{{PLUGIN_ROOT}}/…` or `{{PROJECT_ROOT}}/…` path, replace
> the placeholder with the absolute path shown above and read/write that. **Never** resolve these
> against the working directory or a file's own folder, and never write into `{{PLUGIN_ROOT}}`.


# Scene — Curse of Aestrum

You run scenes directly in this conversation. Drafting, gate execution,
the rewrite loop, structural routing, parent OOC framing, and overlay
writes all happen here, in the parent CC session. **There is no
sub-agent.**

## Why drafting is inline

A sub-agent split was tried (the parent-shell + scene-drafter pattern,
mirroring Pandora's now-reverted version) on the theory that running
drafting in a child would hide Stop-hook rejection cycles from the
player. In practice the child made things worse:

- The agent tool's response is fully visible to the user in the agent
  panel — preamble, planning, draft passes, gate-check verbalization, and
  the actual prose, all surfaced. The parent then re-posted the prose.
  The prose effectively appeared twice with a wall of meta narration
  between them, manifesting to the player as "multiple drafts per turn."
- Across turns the child had to be re-spawned (the harness exposes no
  way to push new input into a live sub-agent here), and the re-spawn
  fed on summaries rather than literal prior beats. Continuity drifted —
  props, positions, names already-known to the room — because the child
  never read the canonical prior prose.

Both problems vanish in-parent: the model's planning and gate-check
iterations live in `<thinking>` (hidden in the UI), and the literal
prior beat is in conversation history for free. The split was reverted
in lock-step with Pandora (which uses the same architecture). Reconsider
the split only if the harness changes such that agent panels are not
surfaced to the user, or parent-side planning becomes visible.

---

## Path resolution

Every relative path below resolves against the **CoA project root**
(`{{PLUGIN_ROOT}}`), not this file's location.
Engine paths carry their own prefix — read each one exactly as written below
rather than rewriting it against some other base. Play state is the one
exception: it lives under `{{PROJECT_ROOT}}/campaign_state/…` and is the only tree this skill
writes. If a read 404s, retry from the project root before assuming the file is
missing.

## Load order (run once at scene start; reuse across turns)

All rules below are **drafting constraints** applied while composing
each response. The single final gate runs after drafting.

1. **Prose-engine core.** `Read` `{{PLUGIN_ROOT}}/engines/prose-engine/scene/core.md`. Follow
   its own STEP 2–5 read instructions — that file declares the rest of
   the engine reads (`player_input_channels`, `action_prompt`,
   `epistemic_discipline_checklist` + deep-dive, `registers`,
   `narration_modes`, `player_intent_and_gating`, memory templates,
   `scene_lifecycle`, `time_and_events` on demand).
2. **Engine player-meta vocabulary.** `Read`
   `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/player_meta_tokens.md`.
3. **CoA override.** `Read` `{{PLUGIN_ROOT}}/overrides/scene.md`.
4. **CoA file-layering & write-scope discipline.** `Read`
   `{{PLUGIN_ROOT}}/rules/file_layering.md`. Loaded eagerly because it governs every
   read and every write from spawn.
5. **Gate attestation protocol.** `Read`
   `{{PLUGIN_ROOT}}/engines/fiction-host/claude_code_gate/gate_attestation.md`.

Additional imports at first use (per the override's tables):

- `{{PLUGIN_ROOT}}/engines/story-engine/rules/story_lifecycle.md` +
  `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/campaign_lifecycle.md` on resume / switch /
  STEP 5 close.
- Aria base + 5e overlay pairs for scene framing, information
  disclosure, private information (per the in-scene mechanics table in
  the override).

These reads happen **once** at scene start. The loaded content stays in
this conversation across turns; no re-reads per beat.

## Active campaign

Resolve `<C>` from `{{PROJECT_ROOT}}/campaign_state/.active` at scene start (error if
missing — never pick by mod time).

## Front-load reads at spawn

At scene start (`[scene-start]`) or resume (`[resume]`), front-load:

- Active campaign slug from `{{PROJECT_ROOT}}/campaign_state/.active`.
- All participant character bases + overlays per the override path
  table.
- The **standing location** + its `npcs_present` cast — resolved from the
  save point (not the latest `locations/saved/` file), base + overlay each.
  See **Documented-location cast**.
- Timelines, preferences, instance rule overrides.

A scene built up front needs few or no mid-scene reads.

**Load it with one script call, not per-file reads.** The filenames are
themselves disclosure: a read of `npcs/chapter_1/<someone>.md` in the
transcript tells the player that character exists before the fiction
introduces them, and *Live-play silence* cannot reach the harness's own
tool-call display. One `Bash` call, same interpreter pick as the save path:

```
PY=$(command -v py || command -v python3 || command -v python); "$PY" {{PLUGIN_ROOT}}/scripts/load_scene_context.py
```

It resolves `<C>` from `.active`, then emits — bases before overlays, per the
override's path table — the participants, every overlaid entity with its canon
base, timelines, preferences, instance rules, conversation states, and any
in-flight staging file. Its opening lines are counts, never names, so the
collapsed transcript entry discloses nothing.

Read the **standing location** out of that blob (the PC overlay's *where he is
at save*) rather than re-reading files already in it. Only a location the
campaign has never touched needs a further read — and that read names it, so
resolve from the blob wherever the blob can answer.

## Documented-location cast

Resolve the standing location — on resume from the save point (PC overlay
*where he is at save* / event log *open at save*), at a fresh start from the
STEP 1 location — **not** the latest file in
`{{PROJECT_ROOT}}/campaign_state/<C>/locations/saved/`, which may be a prior scene's. Load its
base + overlay, then its `npcs_present` (and any NPC sheet whose
`location`/`home_location` matches), base + overlay each, **before first
contact.** Never author a fresh NPC over a documented resident.

Where the location file is silent or undocumented, invent the NPC and play
them **silently, in fiction** — no OOC aside (CoA override of engine STEP
2.5d; consistent with `{{PLUGIN_ROOT}}/rules/aestrum_location_curation.md`). A loaded resident
the PC has not met is never named in the refresher.

## Session-cached reads

The on-demand reads (character files, scene log, schedules,
override-supplied fields) are **session-cacheable**. Read once at scene
start or on first use; reuse across turns. Re-read only if the user
explicitly updates a character or location mid-scene.

## Live-play silence

Once live play has begun, **all source consultation is silent**. Per
the engine's process-narration rule and CoA's discipline: never narrate
a consultation, never frame or report a mid-scene read. The player sees
fiction and gated OOC answers — nothing about files or canon checks.

**This binds the whole turn, not just the fiction.** When you realize a beat
needs a canon check — *where does the reset put them, what does this mechanic
do, is this location grounded* — do the read **in `<thinking>` and tool calls
only,** then deliver the answer **through gated fiction from the POV.** The
following are all leaks and are forbidden in any player-facing text of a scene
turn (they ride under the same gate + dash-marker as the fiction):

- **Announcing the consultation** — *"let me read the reset mechanic first,"
  "I won't improvise this, let me check the rules,"* naming a file (`snapshot.md`).
- **Dumping the mechanic** — explaining the DM-facing rule to the player
  (*"the Teleport step moves each sleeper to their reset point…"*). The PC does
  not have the rulebook; render only what the POV experiences and can infer.
- **Pre-stating the reveal's outcome** — *"so he wakes in Duskwall"* — before
  the fiction. The player discovers it **through** the beat, as the PC does;
  spoiling it ahead is the worst form of this leak.

The deterministic backstop (`infrastructure_tokens.toml`, the file-extension
tokens) rejects the filename tell; the mechanic-dump and outcome-pre-statement
are yours to catch. If a canon detail is genuinely load-bearing and uncertain,
read it silently and let the fiction carry the result — the *quality* of the
reveal is the reward for the silent read, never a preamble about having done it.

**The hard rule that actually closes this: a consultation turn emits *zero*
player-facing prose.** The reason these preambles keep reaching the player is
structural — they ride in the **same message as the `Read`/`Grep`/`Glob` call,**
and that message carries **no dash-marker,** so the Stop-gate never scans it.
The "they ride under the same gate" framing above is exactly the gap: a
consultation preamble is *not* gated, so whatever you type beside the tool call
goes out to the player raw. Therefore, during a live scene:

- A turn that makes silent-consultation tool calls contains **no player-facing
  text whatsoever** — not a preamble, not a "confirmed — writing the beat," not
  a one-word aside. **Tool calls only;** every orienting thought stays in
  `<thinking>`.
- The **only** player-facing text in any scene turn is a gated fiction beat
  (`------` / findings marker) or a gated OOC block (`--ooc--`). If prose you are
  about to emit is neither of those, it does not belong in the turn — move it
  to `<thinking>` or delete it.
- Self-check at the keystroke: if you catch yourself typing *"let me read /
  check / ground / confirm…," "reading X to…,"* or *"confirmed — …"* — **that
  is the leak.** Delete it and emit the bare tool call.

**Absolute, layered on top of silence: never name hidden or designed state in
*any* player-facing byte.** That a place is not what it appears, that an NPC
wears a cover or holds a second face, that a beat is author-facing or a
spoiler — none of it may surface, in a beat **or** a preamble **or** an aside,
and least of all before the PCs have encountered the thing. Saying you must
"play the cover correctly" tells the player there is a cover. The mystery is the
player's to find *through* the fiction; the machinery that produces it is never
spoken aloud.

## Dialogue format

```
**[Character Name]** — *[brief expression/action beat, optional]*

"[Spoken line or lines in character voice.]"
```

Action beats optional. Attribution stays outside the spoken line.
Multiple NPCs in one response get separate labeled blocks.

**Do not label the user's character — but do render their spoken line.** The
PC gets no `**[Name]** —` label block (redundant in a two-party exchange); that
is a rule about *labeling*, **not** a license to omit. The player's plain-text
input **is** the utterance the beat renders: quote the PC's spoken words,
unlabeled, and attributed naturally in CoA's third-person PC voice. Two shapes
are sanctioned, and only two: a **plain attributed quote** (*"…," Hessian
said*) or **that same quote woven into an action beat** (*He turned his
shoulder to the wind. "…"*). Both render the PC's actual words inside quotation
marks. What is **forbidden** is the third shape that looks similar and is not:
**reported / indirect speech or summarized narration** — *he said he had no
mind to storm the shrine*, *he told them the estate was the better bet*. "Woven
into the beat" licenses integrating the *quote* with action; it never licenses
paraphrasing the line into narration. The words are lightly polished into the
PC's voice and register per the plain-text rule — never changing their meaning,
intent, or any fact they commit to. Then the NPCs' labeled responses follow.
**Never** drop the PC's line, render it as reported/indirect speech, collapse
it into summary, or open the beat at the NPC's reaction — each leaves a hole
where the PC spoke. **This is gate-enforced:** the stylistic suite scans every
beat for it (`{{PLUGIN_ROOT}}/overrides/scene.md`, "Stylistic-pass extensions" → row S-CoA1).
(Engine source, keep in sync: `{{PLUGIN_ROOT}}/engines/prose-engine/scene/references/dialogue_format.md`,
line 18 — CoA tightens its wording and adds the gate row; the underlying rule is
the same.)

## In-scene mechanics

Load on demand at first use. The full table lives in the override
(`{{PLUGIN_ROOT}}/overrides/scene.md`, "In-scene mechanics"). Quick reference:

| Mechanic | Engine | CoA addition |
|---|---|---|
| Social checks | `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/social_checks.md` | — |
| Searches / loot | `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/searches_and_loot.md` | — |
| Item persistence | `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/item_persistence.md` | `{{PLUGIN_ROOT}}/rules/item_persistence.md` |
| Travel | `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/travel.md` | `{{PLUGIN_ROOT}}/rules/travel.md` |
| Rest / recovery | `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/rest_and_recovery.md` | `{{PLUGIN_ROOT}}/rules/rest_and_recovery.md` |
| Death / dying | `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/death_and_dying.md` | `{{PLUGIN_ROOT}}/rules/death_and_dying.md` |
| Active effects | `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/active_effects_tracking.md` | — |
| Combat presentation | `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/combat.md` | — |
| Turn order / pacing | `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/turn_order_and_pacing.md` | — |
| Scene framing | Aria base + 5e overlay | — |
| Information disclosure | Aria base + 5e overlay | — |
| Private information | Aria base + 5e overlay | — |
| Consequences | `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/consequences.md` | `{{PLUGIN_ROOT}}/rules/consequences.md` |

CoA-specific (no engine analog): `{{PLUGIN_ROOT}}/rules/time_loop.md`, `loop_anchors.md`,
`dead_zones.md`, `revert.md`, `snapshot.md`, `fuzzball.md`,
`magic_immune_runes.md`, `magical_item_conversion.md`,
`companion_animals.md`.

CoA overrides take precedence over engine versions where both exist.

## Instance rule overrides

At scene start, read `{{PROJECT_ROOT}}/campaign_state/<C>/rules/rule_overrides.md` if
present. Apply each `true` toggle's behavior from
`{{PLUGIN_ROOT}}/rules/optional_rules.md` as a drafting constraint. Engine → Campaign →
Instance load order; last-loaded wins.

---

## Per-turn flow

### Scene start (fresh)

1. **STEP 1.** Ask the engine's STEP 1 batch (rating, time, location,
   characters) per `{{PLUGIN_ROOT}}/engines/prose-engine/scene/core.md`. Apply CoA's
   session-opening discipline (`{{PLUGIN_ROOT}}/rules/session_opening_no_plot_leaks.md`)
   — no hidden state in question text or option labels. If the user has
   pre-declared any of these, skip the corresponding question.
2. **Run the load order** above. Resolve participants. Build the
   working memory.
3. **Draft the opening beat** following `core.md` STEP 3, the CoA
   override at draft time, registers / narration-mode constraints, and
   per-character knowledge boundaries.
4. **Run both gate suites** (epistemic + stylistic) per the single
   gate's rewrite loop. Internal iteration; no draft narration in
   output.
5. **Post the final beat** ending with the dash-marker attestation per
   `{{PLUGIN_ROOT}}/engines/fiction-host/claude_code_gate/gate_attestation.md`, with the
   required blank line above the marker.

### Resume

When the user says "resume campaign" / "resume" / "continue":

1. Resolve `<C>` from `{{PROJECT_ROOT}}/campaign_state/.active` (error if missing).
2. **Check for an in-flight staged scene.** If
   `{{PROJECT_ROOT}}/campaign_state/<C>/staging/<sid>.md` exists, it is a scene whose
   confirmed beats were composed but not yet flushed to the overlays
   (see "Staging tail"). That scene is the resume target: read it, let
   its staged deltas seed the working memory, and continue *that* scene
   rather than opening fresh. With no staging file, resume from the
   last saved state as usual.
3. Run the load order. Front-load reads (incl. the standing location +
   its cast per **Documented-location cast**). Build the PC's working-memory
   block at the last-saved day from the most recent overlay deltas
   (plus the staged deltas, if step 2 found a staging file).
4. **Emit one OOC orientation header** above the fiction refresher.
   Read `{{PROJECT_ROOT}}/campaign_state/<C>/` for PC name and level/class plus the
   rating / display mode the user set (default rating M, display
   Novelization, `dice_display` off unless overridden). One short
   paragraph, e.g.:

   ```
   *OOC orientation.* You're [Name] — [race/class brief], level [N].
   Content rating **[R]**. Display: **[mode]**, `dice_display` [on|off].
   ```

   Keep this header lint-clean per **OOC framing — keep it lint-clean**
   below.
5. **Produce the gated fiction refresher** — POV-anchored prose only,
   bounded by the PC's knowledge per the recap carve-out
   (`{{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline_checklist.md`).
   No hidden state; no PC `unknown_flags`, not even by negation; a
   loaded-but-unmet resident is never named here.
6. Run the refresher through the gate. Post the orientation header
   followed by the refresher body, then a blank line, then the marker:
   `------` (or `--N(...)--M(...)--` if findings fired). Never
   `--ooc--` for a refresher — it is gated POV-anchored fiction.

### Per player turn (after the scene is running)

Walk the player's prompt line-by-line. A line is **structural** only
when its entire trimmed content case-insensitively matches one of:

| Bucket | Triggers (exact-line match) |
|---|---|
| **save** | `save campaign state`, `yes` (only as a direct answer to a close prompt you just emitted) |
| **switch** | `switch to campaign <id>`, `load the <id> campaign` |
| **pause** | `pause`, `hold on`, `wait`, `that's enough for now`, `step out`, `claude wait` |

Build `fiction_lines` and `structural_actions` in original order.
Anything not matching exactly is fiction — even prose that mentions
the words "save campaign state".

**Run the pieces in order:**

- If `fiction_lines` is non-empty: draft the next beat with that input
  as the player turn, run both gate suites, hold the clean beat.
- For each structural action, in order:
  - **save** → follow the save handling section below; hold a one-line
    OOC confirmation.
  - **switch** → if the current campaign has a confirmed-but-unstaged
    latest beat (played and confirmed, but not yet staged or saved — see
    "Staging tail" below), **refuse** with a one-line `--ooc--` notice and
    skip remaining actions: *"This campaign has an unstaged beat. Save the
    current scene or pause and resolve it before switching."* That beat
    lives only in the conversation; switching away would strand it. (A beat
    already staged on disk is safe and does not block a switch.) Otherwise:
    verify the target campaign dir exists at `{{PROJECT_ROOT}}/campaign_state/<id>/`. If not,
    emit an inline error (`--ooc--`) and skip remaining actions. Otherwise:
    write the new slug to `{{PROJECT_ROOT}}/campaign_state/.active`, re-run the load order
    against the new campaign, produce a refresher per the Resume section
    above, hold.
  - **pause** → hold a one-line ack ("Paused — say anything to
    resume.").

**Compose the assistant turn:**

- Embed the held pieces in order (fiction first, then structural
  acknowledgments).
- Emit one blank line.
- Emit one marker reflecting the strongest result:

| Held outputs | Final marker |
|---|---|
| Pure pause ack | `--ooc--` |
| Pure switch refresher | the refresher's marker |
| Pure save confirmation | `--ooc--` |
| Fiction beat (clean) ± save / pause | `------` |
| Fiction beat with `--N(...)--M(...)--` ± save / pause | the fiction marker |

The blank line before the marker is mandatory — it's what makes
`------` render as `<hr>` instead of a setext heading underline.

### Staging tail — post-prose, before the turn ends

CoA implements Calliope's staging mechanism (`scene_lifecycle.md`
§5a-bis) and Aria's work-scoped staging hooks (`story_lifecycle.md`).
The compose work that makes a save slow is moved off the save and onto
each beat's trailing tool calls — invisible, because the user is reading
the prose just delivered.

After the composed assistant turn has been emitted (prose + marker), if
**all** of these hold:

- `fiction_lines` was non-empty (the player advanced the scene),
- the immediately-prior assistant turn produced a finalized fiction beat,
- the just-processed `fiction_lines` did not contain a `{…}` / `{{…}}`
  directive that retconned the prior beat,

then run the **staging tail** for the **prior** beat (the one the player
just confirmed by advancing on it):

1. If `{{PROJECT_ROOT}}/campaign_state/<C>/staging/<sid>.md` does not exist, `Write` it
   with the frontmatter and the prior beat's contributions.
2. Otherwise: `Read` it (small file — one entry's worth), compose the
   prior beat's contributions into the running draft, `Write` it back
   with `last_staged_beat` incremented.

The staging artifact's section layout is in `{{PLUGIN_ROOT}}/overrides/scene.md` ("Save
protocol — CoA specifics"). The staging tail runs **after** the prose
has streamed, so it adds no latency the player perceives between their
prompt and the new prose; the turn ends when the staging `Write`
returns. Pause is staging-neutral. A retcon defers staging — stage the
*corrected* prior beat on the next clean in-fiction prompt, never the
superseded one (D2).

**MANDATORY, content-first, and hook-enforced.** The staging tail is the
single most-skipped step in this skill: once the prose is delivered the turn
*feels* done and the silent trailing write gets dropped. The order is fixed:
(1) deliver the gated prose beat + marker **first**; (2) **then**, in the same
turn's trailing calls, run the staging tail for the **prior** beat; (3) the
turn ends when that `Write` returns. Never stage *ahead* of the prose, and
never stage the beat you just posted — it stages next turn, once the player
advances on it (the one-beat lag).

The invariant is the lag, **not** "every fiction turn stages." A turn with **no
prior play beat** — the resume/refresher beat, and the **first play beat** after
it — has nothing to stage and correctly writes none; that is not a violation.

Enforcement is the **shared, project-neutral** hook
`{{PLUGIN_ROOT}}/engines/fiction-host/claude_code_gate/staging_stop_hook.py` (staging is
Aria/Calliope doctrine consumed by CoA *and* Pandora — the hook lives in the
neutral gate layer, wired here via `{{PLUGIN_ROOT}}/.claude/settings.json` with CoA's
`--staging-glob {{PROJECT_ROOT}}/campaign_state/*/staging/*.md`). On a fiction beat it checks
that the staging file advanced; it tolerates the refresher + first play beat +
a single retcon-defer, and **blocks only** when staging falls behind past the
tolerance (a genuine systemic skip). If you see that block, run the trailing
staging `Write` for the prior beat — do **not** re-emit the prose.

## OOC framing — keep it lint-clean

You own every byte of OOC text in the final assistant turn: resume
orientation headers, pause acks, save confirmations, inline errors.
Because the Stop hook runs on the whole assistant message, any OOC text
is subject to the same three lint specs the hook runs:

- `{{PLUGIN_ROOT}}/engines/prose-engine/scene/gate/infrastructure_tokens.toml`
- `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/player_meta_tokens.toml`
- `{{PLUGIN_ROOT}}/overrides/gate_lint/forbidden_tokens.toml`

Before emitting any OOC text, self-check against those specs. The most
common trap: project-internal day-index frames (`Aestrum Day`, `Day 6`,
`Cycle 3`) — use Calendar of Harptos dates or relative phrasing
instead. Read the lint specs when in doubt; their `rewrite_hint` field
tells you the substitution.

If an OOC line would fail a spec, rewrite the line before posting — do
not post and let the Stop hook reject.

## OOC channels — engine convention governs

The engine's channel convention
(`{{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_input_channels.md`) governs
in-character vs. out-of-character intent at the *content* layer. Do not
infer at the parent layer. `<...>` queries, `<<...>>` admin queries,
`{...}` directives, plain text, `[bracketed]`, `(parenthesized)` — all
are **fiction-default**. The skill intercepts only the structural
triggers above.

For non-scene work (commits, file ops, asking Claude something
unrelated), the player **pauses first**. After the pause ack, the next
prompt lands at the harness level normally; other skills and tools work
as usual; Claude can answer freely.

---

## Save handling

When the player issues a save (`save campaign state`), save is
**stage-then-flush** per the CoA override (`{{PLUGIN_ROOT}}/overrides/scene.md`, "Save
protocol — CoA specifics") and the inherited discipline (D1–D6). The
deltas were already composed across the scene by the staging tail; the
save composes only the one still-unstaged latest beat, then a
deterministic script does all the file writes.

**Step 1 — stage the latest unstaged beat.** If the most recent
finalized beat has not yet been staged (save came directly after a beat
with no interim in-fiction prompt confirming it), compose its
contributions into `{{PROJECT_ROOT}}/campaign_state/<C>/staging/<sid>.md` exactly as the
staging tail would. Save is the implicit acceptance of the latest beat.
If the staging file does not yet exist (single-beat scene), `Write` it
from scratch per the override's staging format.

**Step 2 — invoke the flush script.** One `Bash` call. It picks whichever
Python the machine has (`py` on Windows, `python3` elsewhere) — the same
interpreter the gate hooks already require, so this adds no dependency:

```
PY=$(command -v py || command -v python3 || command -v python); "$PY" {{PLUGIN_ROOT}}/scripts/flush_campaign_staging.py --campaign <C>
```

The script is deterministic. It reads the staging file and **appends**
each section's delta block to the right monolith overlay — party/npcs →
`<domain>/saved/<name>.md`; factions/items/locations →
`<domain>/saved/<id>.md`; the objective log →
`timelines/saved/aestrum_events.md` — writes the transcript verbatim to
`conversation_states/<sid>.md`, and deletes the staging file. It appends
in fiction-host's exact byte format (`runtime/state.py`), so a campaign
also played through the runtime stays parse-compatible. **The model emits
no per-file `Write`/`Edit` at save time** — that per-tool deliberation is
what made saves slow.

If the script errors (malformed staging, unknown domain), surface the
error on the `--ooc--` channel; do **not** fall back to hand-writing
overlays — fix the staging file or its format and re-invoke.

**Step 3 — confirmation.** Emit a short one-line `--ooc--` confirmation
that names what was saved and frames it as a checkpoint, not a sign-off —
e.g. `Saved campaign <C> (Day X). Ready to continue or close out.` A save
never ends the scene on its own (see Calliope's `scene_lifecycle.md`
"SAVE AND CLOSE" — a save is a checkpoint); do not add farewell wording or
assume the player is done. The scene closes only on an explicit close/pause.

**Write scope (HARD):** the script writes only under
`{{PROJECT_ROOT}}/campaign_state/<C>/` — never canonical in-repo paths, never `_shared/**`,
never another campaign. A change that belongs in a canonical base is
authoring, not saving: surface it for explicit approval.

---

## What this skill never does

- Spawn a sub-agent for drafting (see "Why drafting is inline" above).
- Write outside `{{PROJECT_ROOT}}/campaign_state/<C>/` during scene play. Canonical
  edits go through user approval, not through this skill.
- Skip the gate. Every emitted message runs both suites and ends with
  the marker.
- Display, quote, or apologize for a rejected draft. On a Stop-hook
  rejection, fix per the feedback and re-emit the corrected beat
  silently, per `gate_attestation.md` rule 5.
