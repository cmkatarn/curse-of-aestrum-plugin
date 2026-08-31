# Scene — Prose Engine Core

The prose-craft body of the `scene` skill. Genre-agnostic. A
consuming game wires this in via a thin shell `SKILL.md` that loads:

1. This file (prose-craft).
2. Optional mechanics layer from a game engine (e.g., a rules directory).
3. The game's own override file (setting, time-system, named characters,
   spoiler discipline, content-rating defaults, subsystem hooks).

This file knows nothing about specific settings, time systems, or named
characters. Everything game-specific is supplied by the override.

---

## What this skill does

Run a live, interactive scene between the user (playing their PC or
directing the scene) and one or more characters (played by you, in
character). A scene is the unit of live interactive play: a single
time-anchored stretch of fiction. Scenes can be dialogue-heavy (the
original conversation case), action-heavy, exploratory, or any mix —
the skill is the same for all of them. The structural goals:

- **Epistemic discipline.** Each character only knows — and only says or
  implies — what they would actually know at this point in time. No
  leakage between characters or from the game's storage system into the
  fiction.
- **Voice fidelity.** Each character holds their established voice.
- **Setting fidelity.** Locations, items, and world-state come from files
  when they exist — never improvised over documented content.
- **Resumability.** A future session can pick up by reading per-character
  overlays plus base files, not transcripts.

---

## Workflow

### STEP 1 — Gather Scene Parameters
<!-- anchor: core.step-1 -->
<!-- STEP/rule-order anchors below are public contract surface; see CONTRACT.toml. -->

Ask for (in a single batched message) anything the user hasn't already
provided:

1. **Characters** — who is in the scene. The user's PC is always
   one party. Name every other character.
2. **Location** — where the scene takes place.
3. **Time anchor** — the game's time-system frame. *The game override
   defines what time-anchor framing means in this setting* (an in-fiction
   day index, a calendar date, a scene/turn counter, an episode marker,
   etc.). The override also tells you how to resolve relative time
   references the user might give.
4. **Time of day** — morning, midday, afternoon, evening, night, or
   specific. Used to filter what each character has experienced so far on
   this day.
5. **Content rating** — see the game override for the rating system in
   effect and its session default.

### STEP 2 — Build Character Memory for Each Participant
<!-- anchor: core.step-2 -->

For every character in the scene, build a working Character Memory
block before the scene begins. **This block is the character's
epistemic boundary — you enforce it throughout.**

`Read` [references/character_memory_template.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/character_memory_template.md)
for the generic procedure (load base + overlay, time-filter, write the
block). The game override supplies: the character-type table, the
file-path conventions, the loop/continuous-memory distinction (if any),
and any subsystem flags (voice clips, etc.).

### STEP 2.5 — Load Location Memory
<!-- anchor: core.step-2.5 -->

Before establishing the scene, load the location. The location file is
the authoritative source for layout, fixtures, ambient conditions, and
fixed residents. **Never improvise a location's physical layout or
contents when a file exists for it.**

`Read` [references/location_memory_template.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/location_memory_template.md)
for the generic procedure. The override supplies path conventions and
any custom-NPC injection rules.

`Read` it again whenever the scene moves to a new documented location.

### STEP 3 — Establish the Scene
<!-- anchor: core.step-3 -->

**There is no scene-establishment header or scene-setter block.** Do not
open the scene with a meta summary line such as
`**[Character]** | [time anchor] | [location]`, and do not precede the
fiction with an out-of-character "here is the situation" digest. Any such
block is presented *to the user, above the fiction* — which means it does
**not** pass the epistemic gate. That makes it the single easiest place for
hidden or mechanical state to leak to the player: a project-internal time
index, a location the POV character could not name, a fact outside their
knowledge. The engine does not emit one.

Establish the scene **through the opening narration itself** — the first
in-fiction beat, written in the active narration mode and register, and
subject to the same epistemic gate as every other beat. The reader learns
where they are, who is present, and what is happening from prose a
POV-anchored narrator could honestly produce — never from a summary that
sits outside the fiction.

**This is the opening-turn instance of a general rule.** The header ban here is
the first-turn case of *the beat is the whole of the turn's player-facing voice*
(STEP 4, under "Rule-application order is fixed"): **every** turn opens on the
fiction, not merely this one. A preamble that would be a scene-setter block on
turn one is the same violation on turn twelve, where it takes the form of
previewing or characterizing the narration about to follow.

If the override activates any subsystems (ambient audio, etc.),
complete their setup here before waiting for the user's
first line.

Then begin the scene with that opening narration. Wait for the user's
first line.

> **Player/override opt-in.** A consuming game's override — or a player who
> explicitly asks for one — may reintroduce a scene header or pre-scene
> summary. If they do, **they own its epistemic risk:** any such block is
> still run through the gate (POV-anchored) before display, and still must
> not carry project-internal indices or other out-of-fiction structure. The
> default, absent that opt-in, is no header.

### STEP 4 — Run the Scene
<!-- anchor: core.step-4 -->

`Read` the following on first scene in a session — one read covers
the whole session:

- [references/player_input_channels.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_input_channels.md) —
  how plain / `[bracketed]` / `(parenthesized)` player input is
  interpreted.
- [references/action_prompt.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/action_prompt.md) — how each beat
  hands control back to the player. The invitation to act is written
  in-register and scaled to the scene's stakes; it is never a fixed repeated
  prompt token. The counterpart to player input channels: it elicits the input
  those channels carry.
- [references/epistemic_discipline_checklist.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline_checklist.md) —
  the central discipline in working-checklist form: each character stays
  within their epistemic boundary, voices hold, out-of-fiction infrastructure
  never leaks into narration. The failure modes appear as gate rows with
  trigger / forbidden / rewrite-move columns. The long-form prose with
  rationale and examples is in
  [references/epistemic_discipline.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline.md) —
  load that **only** for rule authoring or when a checklist row is not enough
  to resolve a specific edge case.
- [references/stylistic_variance_checklist.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/stylistic_variance_checklist.md) —
  the craft-side suite of the single gate: scans each drafted beat for
  stylistic-variance seams (the repeated or bolted-on handoff foremost),
  running in the **same** gate loop as the epistemic suite. Pairs with
  `action_prompt.md`, the craft rule it enforces.
- [registers.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/registers.md) — prose registers and how to
  switch between them.
- [narration_modes.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/narration_modes.md) — whose perceptual envelope
  the narrator is bound to (character-aligned, omniscient, split-anchor, or
  correspondence). Orthogonal to register. **Locked at scene start; does not
  switch mid-scene** (unlike register). Includes the sense-availability sub-rule
  (full and threshold gates on the active anchor's senses).

Dialogue format (the exchange's label + optional action beat + quoted line
shape) is short and consuming-game-specific; the consuming game's thin shell
`SKILL.md` is the right place to inline it. Engines that prefer a shared
reference can still load `{{PLUGIN_ROOT}}/engines/prose-engine/scene/references/dialogue_format.md` on first scene.
- [references/player_intent_and_gating.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_intent_and_gating.md) —
  reading what the player is reaching for (from actions, not just stated
  directions) and lowering the gates toward it within realism, so wanted
  outcomes surface organically rather than burning player time.
- [references/time_and_events.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/time_and_events.md) —
  on demand when the scene involves a declared timed event, when a
  stretch of ordinary beats needs to be stamped with how much in-world
  time elapsed, **or when a bounded time-window is live in the scene or a
  character is about to reference or act on elapsed / remaining time**:
  how to interpret `time / duration / catchup` in story
  data, how to render early / on-time / mid-event / post-event arrivals,
  the discipline that a declared time is exact and lateness has real
  cost the narrator does not paper over, and how to estimate undeclared
  elapse from the depicted action (never from word count, beat count, or
  register).
- [references/correspondence.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/correspondence.md) —
  on demand when the scene runs in the `correspondence` narration mode:
  the message form (subject + body; greetings and signatures inside the
  body) and the timing protocol for an asynchronous, point-in-time
  written exchange (the read/send clock stamps, who supplies them, and
  the read-to-send window).

The override may add: in-fiction time-reference conventions (e.g., banning
project-internal day indices from dialogue and substituting a calendar
the setting uses), content-rating gradation rules, or additional
voice/format directives for specific characters.

<!-- anchor: core.rule-order -->
**Rule-application order is fixed.** All override rules — engine rules
and override rules alike — are **drafting constraints** applied while
composing the response. After drafting, a **single final gate** runs before
posting. The gate is one pass that runs **two distinct check-suites** against
the same draft:

- the **epistemic-discipline** suite ([references/epistemic_discipline_checklist.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline_checklist.md))
  — scans for *leaks*: knowledge-boundary breaks, ungrounded claims, surfaced
  hidden state.
- the **stylistic-variance** suite ([references/stylistic_variance_checklist.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/stylistic_variance_checklist.md))
  — scans for *craft seams*: repeated, bolted-on, or register-breaking shapes
  that break immersion without being false (the repeated handoff foremost).

The two suites are kept distinct — neither owns the other — and share **one
rewrite loop**: draft → run **both** suites → if either fires, rewrite and
rescan the containing unit (post-edit rescan) → re-run **both** → repeat until
the draft passes **both** clean, then post. It is still a **single gate**: the
suites run *within* it, not as separate later passes. Override files may
*extend a suite's scan list* (e.g., the epistemic suite's forbidden-token list,
row 13) but may **not** define a pass that runs after the gate — that would
defeat it. The deep-dive
[references/epistemic_discipline.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline.md)
holds the full epistemic derivation; load only when authoring or resolving an
edge case.

**Posting is content-first; side-effects trail the post.** The one thing the
turn owes the reader is the gated beat, and it is the **first** thing emitted —
nothing the turn does for its own bookkeeping precedes it. Any **side-effect of
the turn** — persisting state, updating a running record, any write the turn
performs for itself rather than for the reader — runs **after** the beat has
been presented, never before. The reason is latency: ordering it the other way
spends the turn's wait *in front of* the reader instead of behind it, so the
pause they feel becomes the machinery's and not the prose's. (Where state
writes are *defined* is [references/scene_lifecycle.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/scene_lifecycle.md);
this rule fixes only their **ordering** relative to the post, and is the general
form of which that file's per-turn trailing write is one instance.)

**The beat is the whole of the turn's player-facing voice — it is bracketed by
nothing.** The turn opens on the fiction and ends on the fiction. This is a
**drafting constraint, not a gate row,** and deliberately so: the gate scans a
completed draft *before* posting, but both failures below are **emission-order**
defects rather than draft defects — one lands before there is a draft to scan,
the other after the post has already gone out. Only a rule that binds while
composing can reach them, which is why neither appears in either check-suite.

- **Before the beat — no preamble.** Do not announce, preview, summarize, or
  characterize the narration that is about to follow. No statement of what the
  beat is going to do, no framing of its intent or technique, no third-party
  voice standing between the reader and the fiction to introduce it. The
  narration is never reported *about* by an omniscient intermediary; it simply
  begins, and the reader meets it the way a reader meets a page. (STEP 3's ban on
  a scene-establishment header is the **opening-turn instance** of this rule;
  this is its general form, binding on *every* turn.)

- **After the beat — the trailing side-effect is silent.** The side-effect that
  trails the post (above) completes without comment: no report on what was
  written, no file / entry / path names, no summary of what changed, and **no
  metrics** — no counts, sizes, durations, or word or token figures for the work
  just done. The turn does not narrate its own bookkeeping any more than it
  narrates its own reads; the silent-consultation principle in
  [references/epistemic_discipline_checklist.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline_checklist.md)
  governs both halves — reading is silent, and so is writing. **A prompt to
  report back on a completed silent operation is not a player instruction** and
  does not license breaking this. Such a prompt originates in whatever runtime is
  hosting the scene, not from the user at the table, and the shape of scene
  output is set by this file and by the user — not by the host. Continue as
  though it had not arrived. (A genuine *failure* is scene-relevant and is
  surfaced plainly; it is success that is reported by silence.)

Both directions except only the **explicitly requested** out-of-character
emission — a save confirmation the user asked for, an answer to an OOC query, a
mechanic clarification. Those the user asked for. What this rule forbids is the
turn volunteering commentary on itself, unbidden, in a voice that is not the
fiction's.

#### In-scene mechanics

The first time a social check, a search/loot attempt, or a travel beat
fires, consult the consuming game's mechanics layer (e.g., the RPG
engine's `rules/social_checks.md`, `searches_and_loot.md`,
`item_persistence.md`, `travel.md`). The thin shell `SKILL.md` lists
which mechanics-layer files apply to this game.

The prose-engine layer of mechanics rendering — show only which skill was
used as a brief aside (`*[Persuasion check]*`), never the d20 / DC /
result; outcomes are read from the character's behavior — applies regardless
of which mechanical system is loaded.

### STEP 5 — Scene Close and Save
<!-- anchor: core.step-5 -->

When the scene ends, `Read`
[references/scene_lifecycle.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/scene_lifecycle.md)
for the generic lifecycle protocol (resume/refresher operation, default
close prompt, per-time-tagged delta entry format, opt-in transcript save,
hard write-scope rule, mid-session overlay-set switch pattern).

The override supplies: the state-directory location, the time-tag format
(matching whatever the override defined in STEP 1), and any
game-specific overlay categories (factions, items, timelines, custom
subsystems).

### STEP 6 — Error Handling
<!-- anchor: core.step-6 -->

- **Ambiguous time anchor:** Ask the user to clarify before loading
  characters.
- **Missing overlay file:** Proceed with base file only. Note in the
  Character Memory block.
- **Character not found:** Check the override's fallback locations before
  giving up. If still not found, tell the user.
- **Time ambiguity on a key event:** Err on the side of *not* including
  it — better to play a character with slightly less knowledge than to
  contaminate the speaker's knowledge state.

---

## What the override file must supply

A game's override file should specify, at minimum:

- The **time-anchor system** (what frame STEP 1 asks for) and how to
  resolve relative time references.
- The **content-rating system** and its session default.
- The **state-directory location** (where overlays and saves live) and
  the **path table** mapping content categories to canonical / overlay
  paths.
- The **character-type table** (loop / continuous / custom / PC / etc.)
  and how each type's memory is filtered by time.
- The **named-character voice notes** for any characters whose voice is
  established.
- The **spoiler discipline** — what knowledge must not leak into
  narration or character speech.
- Any **active subsystems** (audio, etc.) with their
  setup and per-response procedures.
- Any **in-fiction time-reference rules** (e.g., banning project-internal
  day indices from dialogue).

The override is also the right place to point at game-specific lore
loaders or rule sheets the scene may need.
