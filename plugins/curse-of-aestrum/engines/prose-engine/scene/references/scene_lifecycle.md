# Scene Lifecycle — Generic Protocol (Resume / Close / Save)

Reference loaded on demand from `scene/core.md`. Relevant when the user
**resumes** a saved scene, when a scene **ends**, when the user invokes a
**save** command, or when **switching the active overlay set** mid-session.

The consuming game's override file supplies the state-directory location,
the active-overlay-set indicator, the time-tag format, and any
game-specific overlay categories.

This engine knows only the **scene** as its unit. Any higher-level
grouping a consuming game layers on top of scenes (an RPG campaign, an
episodic arc, etc.) is the consuming layer's concept — it binds its own
command vocabulary to the generic operations below and supplies the
scope (which overlay set, which POV character, which time anchor).

---

# RESUME
<!-- anchor: scene-lifecycle.resume -->

The symmetric open to the close protocol below. A resume turns saved
state back into a **player-facing refresher** and hands off to live play.

The refresher is an out-of-character author-to-player block, but it is
**not** a freely-exempt OOC summary: it is a gated emission, bounded by
the POV character's knowledge. See the player-scoped OOC carve-out in
[epistemic_discipline_checklist.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline_checklist.md)
(Scope paragraph + row 1). The whole point of the resume operation is
that the refresher passes through the same single gate the scene does —
drafting it freehand from the saved files is exactly what leaks
DM-only/hidden state into the player's view.

## R1. Resolve scope

From the override, resolve:

- **The active overlay set.** The override supplies the indicator (e.g.,
  a single-line active-set file). If the indicator is missing, surface
  the override's error — do **not** guess the set, and do **not** pick by
  file modification time.
- **The POV character** — by default the player's PC.
- **The time anchor T** — the last-saved point for this overlay set
  (from the most recent overlay delta entry / saved frontmatter).

## R2. Build the POV character's working memory block at T

Use the STEP 2 procedure in
[character_memory_template.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/character_memory_template.md): load base +
overlay under the memory-mode policy, time-filtered to T. By construction
this block admits **only** the POV character's own knowledge and
perceptions; DM-only / author-facing sections and other characters'
private state are never admitted to it.

**The base file is a creation-time artifact, not a present-tense
record.** Its current-status statements — *first meeting, newly
arrived, currently lives at X, has not yet Y* — are baselines that play
accumulation can supersede. The build reconciles such claims against
accumulated state (overlay deltas + the per-§5d transcript-frontmatter
sweep) before treating any creation-snapshot phrase as live present-
tense. A live value wins over a superseded base-file phrase. See
`{{PLUGIN_ROOT}}/engines/prose-engine/scene/references/character_memory_template.md` §2b step 4 for the procedure.

For any other character the refresher will mention (a companion, a
recurring NPC), draw **only** on what the POV character has observed —
grounded in the POV block's perception log — never on that character's
own overlay's private/DM-only content.

## R3. Draft the refresher from the POV block

Compose the player-facing refresher strictly from the POV block: who the
PC is, where they are at T, what they know, the open threads they are
carrying, and what each present companion looks like *through the PC's
eyes*. If the PC has never observed a fact, it does not appear — and a
fact the PC specifically does **not** know is omitted entirely, never
surfaced by negation ("you don't know X", "you're not aware that Y",
"(player-side: …)").

## R4. Allowed out-of-character orientation

The refresher may additionally include explicitly OOC player-orientation
the override declares as permitted — typically:

- Player-meta / mechanics the player legitimately tracks (character
  level, stats, resources).
- The time anchor for bearings, in whatever OOC form the override allows.
- The active content rating.

These are player-facing scaffolding, not in-fiction knowledge, and are
exempt from the knowledge-boundary check (but everything in R3 still
applies to the in-fiction content of the refresher).

## R5. Gate, then display, then hand off

Run the drafted refresher through the single epistemic gate as the final
pass before display, treated as POV-anchored on the PC. After the
refresher posts, hand off to live play (STEP 4) at time anchor T.

## R6. Switch-then-resume

If the override's active-set indicator was just changed (see §5e), the
resume reads the **new** set. A consuming layer's "switch" command writes
the indicator first, then performs a resume against the new set.

---

# SAVE AND CLOSE

**A save is a checkpoint, not an ending.** Persisting state and ending the
scene are **separate acts.** A save folds the play so far into durable state
and leaves the scene exactly where it stood — **ready to either continue or
be closed out.** The user may save mid-scene to checkpoint and keep playing,
save-then-stop, or play on and never save; saving commits to none of these.
Never treat a save as a sign-off, and never frame the confirmation as a
farewell: report that the state was saved and that the scene is ready to
continue or close, then wait for the user's next move (more fiction, another
save, or an explicit close). The one place a save and an ending coincide is
the **close prompt** (5a) — but even there the *ending* is what the user is
signaling; the save is the checkpoint offered alongside it.

The scene is **closed** only when the user signals an end ("end scene",
"that's enough", "fade out", "close the scene", "close the conversation"), or
reaches a natural dramatic conclusion and does not continue. Closing is the
user's call, never inferred from the fact that a save just happened.

Saving is split into two independent actions, with **strict write-scope
rules**. The goal: a future session can resume by reading only the
per-character overlay files — never the transcript — so reload stays
cheap. Six invariants — **D1–D6 below** — bind every save (5a and 5b
alike); a consuming game's override may tighten or extend them and supplies
the concrete state paths, but may not relax them.

## Save discipline (invariants D1–D6)
<!-- anchor: scene-lifecycle.save-discipline -->

These hold for any state write, under any consuming game. The override
supplies *where* state lives and *what categories* exist; these govern *when*
a save may write and *what it may contain*.

### D1. A save is explicit and user-initiated

State is written **only** in response to an explicit save — a save command
(5b) or the user's affirmative answer to the close prompt (5a). Nothing else
writes state. **Pausing is not saving.** A paused scene, an interrupted turn,
a context switch, an OOC aside, a mid-scene question — none of them trigger a
state write, and the narrator never writes overlays proactively "to be safe."
A pause leaves state exactly as the last explicit save left it; resume rebuilds
working memory from the files, and if the player wants the interim folded in,
they save it. (Reaching a natural ending may *offer* the close prompt — but the
prompt only asks; the write happens on the player's yes, never before.)

### D2. Save the corrected fiction, not what was rewound over

A running scene can be revised in flight — the player re-prompts a beat,
corrects a detail, or bends the fiction with a director's directive
(`{…}` / `{{…}}`; see [player_input_channels.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_input_channels.md)).
What reaches state at save time is the **fiction as it actually stands now**,
never a passage that was superseded. Before writing a delta, reconcile against
in-session retcons:

- a beat that was rewound over **did not happen** and is not recorded;
- a beat the player amended is recorded **in its amended form**;
- a directive that bent the fiction is recorded by its **resulting state**
  (the caught hand stays caught), because that outcome is now what happened.

When it is unclear whether a contested beat still stands, **ask the player**
rather than guess — a wrong fact written to state outlives the session.

### D3. Overlays hold in-scene experience only — never meta

State overlays record **what happened in the fiction and what the character
experienced of it**. They never record out-of-fiction material. Anything that
arrived on a non-spoken / out-of-character channel is meta-knowledge and is
**excluded from every overlay**: an OOC query or its answer
(`<…>` / `<<…>>`), the *wording* of a director's directive, a save
confirmation, a mechanic clarification, the player's meta-discussion. The test
is channel attribution (see [player_input_channels.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_input_channels.md)
and the channel-attribution gate row): **only what was rendered into the
fiction is eligible to be saved.** A directive's *outcome* did enter the
fiction and is saved per D2; the directive's *text*, and any OOC exchange
around it, are not.

### D4. The latest entry is the latest event; conflicts resolve toward it

A character's timeline is ordered: **the most recent entry is the latest
event, and every earlier entry happened before it.** When an earlier entry —
in any overlay (timeline, the subjective per-character overlay, or an entity
overlay) — contradicts the latest event, the **latest event wins**, and the
stale entry is **flagged for correction or removal** so the record stays
coherent. Writing a new latest event is therefore also a reconciliation pass:
surface conflicting earlier text and fix it (or flag it for the user) rather
than leaving two records that disagree about the same fact. A timeline that
contradicts itself cannot be resumed from reliably — D4 is what keeps resume
honest, and a multi-file save must leave **all** of a scene's artifacts
agreeing on the latest state, not just some of them.

### D5. Record only what changed (true-delta)

A delta entry records **what changed in the scene that produced it.** State
that persists unchanged from a prior entry is conveyed by **silence**, not
re-asserted: a fact a character already knew, a relationship reading that did
not shift, a secret still held, an open thread still open — none of these earn
a bullet merely for continuing to be true. Working state is reconstructed by
applying entries in order atop the base file; the **absence** of a transition
delta means the prior state persists. Only **transitions** get bullets — a fact
newly learned, a disposition that moved, a secret acquired or disclosed, a
thread opened or closed.

Why this is an invariant and not a style preference: in an append log — and
especially once each entry is its own file — a line repeated across many
entries is noise that buries the one entry where something actually changed.
Re-asserting unchanged state is the most common way an overlay bloats and a
save slows. (Example: an entry that says "still does not know X" every scene
until the scene X is revealed should instead say nothing until the reveal,
then record the reveal once.)

### D6. The objective record stays terse (entry-size)

An overlay that records **objective events** (a timeline / event log, as
distinct from the subjective per-character overlay) is an **index, not a
transcript.** Its bullets are terse facts: who did what, who was present, what
changed. Never put into it:

- **paragraph-length bullets** — one sentence, two only if the second is
  genuinely necessary;
- **verbatim dialogue** — the transcript carries the exact words; the objective
  record summarizes *what was exchanged* in the third person;
- **atmospheric / sensory prose** — that is transcript-grade;
- **"standing threads forward" / "carried forward" summary bullets** that
  re-assert open state — these are working-state snapshots and are already
  forbidden by D5.

A useful canary: if the objective entry for a scene is **longer** than the
subjective entry for the same scene, the objective record has absorbed work it
should not be doing. The objective record is smaller by nature — fewer
dimensions, no interiority.

## 5a. Default close prompt — "Save scene state?"

When the scene ends, ask: **"Save scene state?"** (A consuming layer may
re-supply player-facing wording — e.g., an RPG layer may show "Save
campaign state?" — but the operation is the same.)

If yes, update the **active overlay set only** for everything that
changed during the scene. All overlay writes go to the active overlay
tree, as defined in the override's path table — never to in-repo
canonical files, never to cross-set shared paths, never to another
overlay set's subtree.

The override's path table specifies which overlay categories are
available (characters, locations, timelines, and any game-specific
categories like factions, items, custom subsystems).

For each overlay update, write a **per-time-tagged delta entry**
containing only what changed — *not* a transcript excerpt. The
time-tag format follows the override's time-anchor system.

The entry **envelope is fixed** for every consuming layer: a level-3
header — `### [time anchor] — [short descriptor]`, never `##` — followed
by `- **Label:** value` bullets, appended after all prior entries
(overlays are append-only and chronological). The **field labels** inside
the entry are vocabulary, not envelope: a consuming override may
re-supply its own ordered field list; absent an override list, use this
default:

```markdown
### [Time anchor per override] — [short descriptor]

- **Now knows:** [fact, fact, fact]
- **Now believes / suspects:** [inference, with source]
- **Relationship shift:** [character → character: what changed and why]
- **Emotional / situational state:** [if meaningfully altered going into next scene]
- **Unresolved:** [open threads this character is carrying forward]
- **Items / changes:** [for locations or inventory]
```

Drop any line that doesn't apply. Keep entries terse — a future load
should reconstruct the character's state from these bullets plus the
base file, without needing the transcript.

**Mechanism — cost-flat appends.** Two layouts satisfy the cost-flat
invariant; the consuming game's override picks one.

*Monolith layout (default).* Each overlay is one file accumulating
entries. Append by `Edit` with the file's existing trailing entry as
`old_string` and `old_string + <new entry>` as `new_string`. Glance at
the last ~6 lines first (one entry's worth: the `### header` + its
bullets) to pick the anchor, honor the latest-entry-wins invariant
where the override defines one, and avoid duplicate headers. Never
`Read` the whole overlay file and `Write` it back to append — that
scales with file size and turns a small delta into a multi-thousand-
token round-trip on overlays that accumulate across a long campaign or
anthology. For a brand-new overlay (no prior entry), `Write` the
initial content once; thereafter, `Edit`-append.

*Sharded layout.* A consuming game MAY shard the overlay across
one-file-per-entry under a per-character (or per-entity) directory —
`<overlay-dir>/<id>/<NNNN>.md`, zero-padded for lexical-chronological
sort. In that layout the trailing-`Edit` prerequisite does not apply:
an append is a `Write` of the next entry file, and the cost-flat
invariant is satisfied by construction (no growing file to read or
edit against). Determine the next ordinal by listing the directory
(`ls | wc -l` or equivalent); a brand-new overlay starts at `0001.md`
without a special-case branch. D1–D6 apply per entry, and the
latest-entry-wins reconciliation applies across the directory's
chronological order.

Both layouts admit the same entry envelope (level-3 header + bullets)
and the same D1–D6 invariants. The override declares the layout and
the on-disk paths; the rest of this protocol is layout-agnostic.

## 5a-bis. Staging — amortizing the save cost (optional)
<!-- anchor: scene-lifecycle.staging -->

The expensive part of a save is not the file write — it is the model
**composing** the deltas (distilling the played beats into terse entries
under D5/D6, reconciling against retcons under D2). Doing all of that at
save time means the user waits while it happens. Since a save is often the
moment the user is signing off, that wait is the worst-placed cost in the
whole loop.

**Staging** moves the compose work off the save and spreads it across the
scene, so the save itself becomes near-pure serialization. A consuming game
opts in by defining a staging path and a flush step; a game that does not
opt in composes everything at save time (correct, just slower). The
mechanism:

1. **Compose during play, post-prose.** After a beat's prose is emitted,
   the model composes *that beat's* delta contributions and appends them to
   a **staging artifact** on disk under the active overlay set
   (`<active-set>/staging/<scene-id>`, per the override). This happens in the
   turn's trailing tool calls, after the prose has streamed — the user does
   not perceive added latency between their prompt and the new prose.

   **The staging write is silent.** It is never reported, summarized, named, or
   measured in the turn's output: no confirmation that a beat was staged, no
   path, no entry count, no size or timing figure. A reader should not be able to
   tell from the turn whether staging happened at all — that is what makes the
   mechanism invisible rather than merely fast. This is the per-turn instance of
   the general rule in [core.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/core.md) (*the beat is the whole of the
   turn's player-facing voice*), which also holds that a host-generated nudge to
   report back after a silent write is not a player instruction and is not
   honored. A staging **failure** is different: it threatens the save and is
   surfaced plainly.

   **Not to be confused with the save confirmation.** The explicit save (D1 /
   §5a) *is* user-requested, and its one-line confirmation — state written, scene
   ready to continue or close — is exactly the requested OOC emission the core
   rule excepts. Silence governs the **trailing** write the user did not ask for;
   it never suppresses the answer to a save the user did.

2. **Lag by one beat (confirm-then-stage).** Stage a beat only once the
   *next* in-fiction prompt confirms it: the user advanced the scene on the
   strength of the prior beat, so that beat is canon. A beat is **not** staged
   in the same turn it was drafted — that one-beat lag is the window in which
   a leak, or a prompt that was actually OOC, can be caught before anything is
   committed. (See D2: a retcon defers staging — the model stages the
   *corrected* version on the next clean prompt, never the superseded one.)

3. **Save = flush.** On the explicit save (D1), compose the one
   still-unstaged latest beat, append it to staging, then **flush**:
   serialize each staged section to the overlay layout (monolith-append or
   shard-write per §5a) and delete the staging artifact. No overlay *read* and
   no per-beat *recompose* happen at save time — the deltas already exist in
   staging. Flush is mechanical enough that a consuming game SHOULD implement
   it as a deterministic script rather than per-file model writes (the
   per-tool deliberation of many sequential writes is itself a large share of
   a slow save).

**The staging artifact is scaffolding, not state.** It is not loaded by
normal participant resolution and never substitutes for an overlay. Only the
**resume** path may read it, to continue a scene whose beats were confirmed
but not yet saved (see Aria's work-lifecycle layer, which owns when staging is
read on resume, refused on switch, and left in place on a pause/close without
save). Pausing is staging-neutral (D1): a paused scene's last unstaged beat
simply stays unstaged until the next in-fiction prompt or a save.

**Transcript carve-out.** If the staging artifact also carries the full
transcript (as a terminal section), the flush must **carve that region off
first** — take everything from the transcript marker to end-of-file verbatim —
and only then split the remaining structural sections on their headers.
Otherwise a prose line that happens to begin with a heading marker (`#` read
aloud, a reproduced document, "# of bodies they never found …") is mistaken
for a section boundary and silently truncates the save. The transcript is
therefore always the **last** section, and the structured sections above it
never contain an interior top-level heading by construction.

## 5b. Separate explicit command — "save scene" / "save transcript"

Saving the full transcript is **opt-in and never bundled with the
default close prompt**. The user triggers it with an explicit command
("save scene", "save transcript", "save the scene markdown", or the
legacy phrasings "save conversation" / "save the conversation
markdown").

When invoked, write to the override-defined `conversation_states/`
path:

```markdown
---
id: [character_name]_conversation_[short_descriptor]
participants: [list all characters]
location: [location]
time_anchor: [per override]
time_of_day: [time]
content_rating: [per override]
status: complete
---

## Summary

[Two to four sentences. What was the point of this scene? What happened?]

## Key Information Exchanged

[Bullet list. What did each character learn or reveal? What changed as a result?]

## Knowledge Updates

[For each NPC in the scene: any new knowledge they now carry that should be added to their saved overlay. If significant, note which overlay file needs updating.]

## Transcript

[Full scene transcript, formatted as it was during play.]
```

The conversation-states directory is itself a saved-style location and
may be written without extra approval.

## 5c. Write-scope rule (HARD)

A save action — whether 5a or 5b — may **only** write to paths under the
override-defined active overlay tree. Specifically:

- The active overlay set's `**/saved/**` paths defined by the override.
- The active overlay set's `conversation_states/` path.

Any proposed write under in-repo canonical paths (the game's base
content), under cross-set shared paths, or under another overlay set's
subtree is **out of scope for save**. If the scene surfaced
something that genuinely belongs in a canonical file (a permanent change
to who lives at a location, a correction to a character's baseline), do
**not** edit it during save. Instead, surface it to the user:

> **"This change looks like it belongs in [path] (a canonical reset-state
> file, not an overlay). Want me to make that edit? It requires your
> explicit approval."**

Wait for explicit approval before editing any canonical file or any
shared file. Listing the diff in the prompt is encouraged.

## 5d. Reload model (what 5a is feeding)

Future sessions resuming these characters should load: base file from
the canonical tree (or the active overlay set's custom tree for
characters added by this set) + overlay from the active overlay path
(with the time-filter logic from the character-memory template). This is
the data side of RESUME above; the refresher is built on top of it.

The transcript **body** is not part of the reload path; resume avoids
the multi-thousand-token cost of replaying scenes from prose. The
transcript **frontmatter** (the YAML block: id/participants/location/
time_anchor/time_of_day/content_rating per 5b) is a cheap exception:
a resume MAY — and, when the base file carries creation-time current-
status claims, MUST — read the frontmatter of past scene transcripts
to anchor the structural shape of accumulated history (engagement /
trip / location-history, time-since-key-event, whom-the-PC-has-already-
met) that base-file creation-snapshots do not carry forward. See
[character_memory_template.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/character_memory_template.md) §2b step 4
on reconciling base-file claims against accumulated state.

The user may additionally ask to load the most recent conversation-
states entry explicitly for tonal continuity — otherwise transcript
bodies stay on disk as reference, not context.

## 5e. Switching the active overlay set mid-session

If the override defines multiple overlay sets and the user invokes the
consuming layer's switch command (which the consuming layer maps onto
this operation), treat it as a directive to:

1. Verify the target overlay set exists per the override's path
   convention. If not, surface to the user per the override's wording.
2. If it exists, update the override-defined active-set indicator to the
   new set.
3. Acknowledge the switch on one line.
4. Discard any in-memory character / location state from the previous
   set — the next scene load (or a resume per §R6) re-reads from the new
   set's overlays.
