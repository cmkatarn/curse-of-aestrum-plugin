# Epistemic Discipline — Gate Checklist

Condensed working form of the discipline. Load this once per session — covers
the whole session. The long-form prose with rationale, examples, and the full
"why this slip happens" essays lives in
[epistemic_discipline.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline.md) (the "deep dive"). Load the
deep dive **only** when:

- you are authoring or revising the rules themselves,
- a check fires repeatedly on the same draft and the row below isn't enough to
  resolve it, or
- the user explicitly asks for the rationale.

The names of the failure modes match the deep dive; row order matches the
final-gate scan order.

---

## What this discipline is

Every utterance a character makes — and every claim or implication in
narration — must be grounded in what that character (or the omniscient
narrator, where allowed) validly knows or perceives at scene-time T. Knowledge
stays bounded; claims are positively grounded.

Scope: **narration, scene-setting, and NPC dialogue.** Out-of-character meta
blocks **the player explicitly requested** (save confirmations, mechanic
clarifications, post-save summaries) and the admin `<<…>>` tier are exempt and
may name files and overlays freely. **OOC is not blanket-exempt, though:** the
DM's answer to a player-scoped `<…>` OOC query is gated to the player's
perspective (see the carve-out below); only the admin `<<…>>` tier is fully
ungated.

**Unprompted narrator process-narration is player-scoped and gated — not
exempt.** The narrator's own orchestration asides to the player — *"let me
check the files," "one moment while I load X," "there's an authored thread tied
to this," "there's a lot of established material here"* — are **not** requested
clarifications and **not** admin-tier. They are player-facing emissions and
must carry **no infrastructure names (no file / overlay / skill / authored-
thread names), no hidden or author-facing state, and no designed structure the
POV character cannot see.** Consulting the source material is a **silent** act:
read what you need without narrating that you are doing it, or surface only a
neutral, content-free note ("one moment"). The existence and findings of that
consultation are themselves author-facing only. See `{{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_input_channels.md`.

**Player-scoped OOC carve-out** (the former recap carve-out, generalized). A
**player-scoped OOC emission** — a recap, a resume refresher, or the DM's
answer to a `<…>` player-scoped OOC query — is *not* freely exempt, even
though it is an OOC block. It is bounded by the POV character's knowledge:

- **Still exempt** for infrastructure-citation (row 5) and player-meta (row
  10): a recap may state mechanics, character level, and the time anchor for
  the player's bearings.
- **Not exempt** for the knowledge-boundary class (rows 1–3): it may not
  surface another character's hidden / DM-only state, nor any fact in the POV
  character's `unknown_flags`. **Negation does not launder it** — "you don't
  know X", "you're not aware that Y", "(player-side: …)" naming an
  unknown-flag fact still surfaces the fact and is removed.
- **Not exempt** for quantity grounding (row 14): counts, durations, and other
  quantities in the recap must trace to grounded source data. The resume
  refresher is exactly where an invented "three days ago" slips in — the urge
  to sound concrete and oriented is strongest in an orientation block.
- **Not exempt** for spatiotemporal-binding (row 15): an event's recalled
  *when* / *where* must match saved state. A refresher reaching to sound
  oriented is exactly where a true event gets pinned to a false time or place
  (the warning that happened *at the fire* recalled as *two hours back on the
  road*).

The **`<<…>>` author/admin OOC tier is fully exempt** — ungated like a
`{{…}}` directive — and may surface hidden state, DM notes, and world
mechanics freely. The carve-out above governs only the *player-scoped* tier.

Build the refresher (or the `<…>` answer) from the POV character's
working-memory block and run it through the gate as a final pass,
POV-anchored on that character. See the RESUME section of
[scene_lifecycle.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/scene_lifecycle.md) and the OOC channel in
[player_input_channels.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_input_channels.md).

---

## Drafting constraints (apply while writing each response)

- **Knowledge boundary.** Each character speaks / implies only within their
  Character Memory block from STEP 2. Two NPCs in the same scene do not share
  each other's hidden knowledge.
- **Voice.** Hold each character's established voice (cadence, vocabulary,
  register). Voices don't bleed.
- **Reaction.** NPCs are not passive responders. They have agendas,
  discomforts, curiosity. Let new information visibly land.
- **NPC testimony is independent — computed from the NPC's own grounded
  record, blind to the POV's hypothesis.** When the POV holds a private
  suspicion — voiced only OOC, logged in an overlay, or merely live in the
  drafter's working memory — an NPC queried on that topic answers from
  **their own knowledge alone,** as if the drafter did not know the
  suspicion. Never shape an NPC's testimony to confirm, resonate with, or
  eerily satisfy the party's private theory: that authors the NPC toward
  hidden state they cannot access (row 1) and manufactures false
  *independent* corroboration. The NPC's **grounded knowledge wins, even —
  especially — when it refutes the theory**; an NPC who simply states what
  they know, contradicting the party's read, is the sign the flow is right,
  and a source that conveniently confirms an unspoken suspicion is the sign
  it is inverted. See the deep dive's *confirmation-mirror* section.
- **DM Notes are author-facing.** Never voiced by an NPC; never cited in
  narration.
- **Pre-write reference check.** When reaching for a callback, quote, analogy,
  precedent, quantity, or **concrete who/what/where** to fill a slot in a
  sentence-frame — including a **parallel list / tricolon**, a *what-lies-ahead*
  gesture, or a **motif echo** — verify the slot-filler is grounded: a
  reference's *content* must apply to what the sentence asserts, a number must
  trace to source data, and an entity/presence/location the narration places in
  the POV's knowledge-horizon must be one the POV can actually ground. If it
  doesn't, drop the slot — do not warp the sentence to make the filler fit. The
  pull of a slot-filler is the shape of the frame, not the fit of the content.

---

## Session-cached reads

The gate's on-demand reads (character files for knowledge-attribution, scene
log for verbatim-quotation and cross-scene-conversation, schedules for
off-screen-presence, override-supplied fields for the dormant checks) are
**session-cacheable**. Character files, schedules, and the scene log
do not mutate during a scene. Once read this session, reuse the in-context
content for subsequent gate checks rather than re-reading. Re-read only if
the user explicitly updates a character or location mid-scene.

---

## Final gate — scan drafted output, in order

This suite runs **last**, after drafting, before posting, as part of the single
gate. It stays focused on **leaks** — keep stylistic-craft concerns out of it.
The **stylistic-variance** suite ([stylistic_variance_checklist.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/stylistic_variance_checklist.md))
runs in the **same** gate pass against the same draft; the gate posts only when
**both** suites pass clean (see [core.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/core.md), "Rule-application order is
fixed"). There is still no separate pass *after* the gate.

> **Deterministic enforcement of the closed-vocabulary rows.** Some rows are
> *closed-vocabulary* — a fixed token is the leak on sight (Row 5 infrastructure
> citation; Row 10 player-meta; Row 13 override extensions). The model self-scan
> shares the drafter's blind spots, so a consuming **runtime may additionally
> enforce these deterministically** before a beat is shown, via structured token
> sidecars. Calliope's own infrastructure-token subset is mirrored in
> [`scene/gate/infrastructure_tokens.toml`]({{PLUGIN_ROOT}}/engines/prose-engine/scene/gate/infrastructure_tokens.toml);
> consuming layers supply their own (player-meta, override extensions) in theirs.
> This is an *additional, optional* deterministic check the runtime owns — it is
> not a pass after the gate, and the prose rows above remain authoritative for the
> model.

**Director's-channel handling.** If the player turn included a
`{...}` scoped directive, the gate runs normally with one modification:
when a row fires a violation **inside the realization span** (the
sentences/clauses that exist to land the directive's target proposition),
ask one more question before rewriting — *is this violation logically
entailed by the target proposition?* If yes, license it and continue.
If no, fail and rewrite as normal. Violations outside the realization
span are never licensed. Bias toward "not entailed" when uncertain.
See `{{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_input_channels.md` for target-proposition and
realization-span definitions.

If the turn included a `{{...}}` full override, the gate does not run
against directive-produced content; see the channel reference. Bent
state still propagates forward into subsequent beats.

| # | Check | Trigger surface | Forbidden | Rewrite move | Read on fire |
|---|---|---|---|---|---|
| 1 | **Knowledge boundary** (incl. hidden-state-surfacing in narration) | Any NPC claim or implication; **narration that surfaces another character's / the setting's factive hidden state**; **also a player-facing recap/refresher** (POV-anchored on the PC) | Anything outside the speaker's memory block at T — including a fact in the POV's `unknown_flags` or other factive hidden state surfaced *by negation* (Variant A: "no trace of X," "you don't know X"), *by over-emphatic affirmation of normality* (Variant A twin: "perfectly ordinary," "nothing to worry about"), *by narrated withholding* (Variant B: "doesn't explain how she knew X"), *by presupposition* (Variant B sub-form: "whatever she is" — presupposes a definite concealed answer), or *by hypothesis-as-inference* (Variant C: an "I suspect / I believe / it may be that" line that names a **specific candidate** explanation — mechanism, identity, agenda — for an open question, when the speaker's observations do not **select** that candidate from the space of plausible ones; the form is the inference register, the content is a singled-out member of an unnarrowed candidate set, which the player now sees) | Inference register, or cut; for a negated unknown-flag, **remove the whole reference** (do not hedge); for an over-emphatic affirmation, **drop the intensifier and describe plainly**; for withholding/presupposition, drop to **observable behavior or the PC's grounded suspicion only** — render P1 ("she's hiding something"), never P2 ("whatever she is"); **for Variant C**, render only the **shape** the observation actually selects for ("something was taken from them that was not taken from us — what, I do not know"), not the candidate — the speaker may name the **category** their evidence grounds (a working, a regime, a condition), they may not name a specific **member** of an unnarrowed set. The principle: **inference must be selectivity-constrained.** | — |
| 2 | **Positive grounding trace** | Every NPC claim + prepositional phrase + deictic gesture (*on you, in there, that, what you came for*) | Claim with no in-fiction sensory event grounding it for *this* NPC | Name the event in-fiction; or switch to inference; or cut the implication | — |
| 3 | **Knowledge-attribution** | Verbs of cognition or perception applied to a non-speaker (*knew, believed, foresaw, understood, expected, saw, realized, sensed, suspected, decided, came in believing*) | Asserting another character B's interior state at T without grounds | Reframe as speaker A's belief / projection; inference register; or cut | B's file at time T (skip if B is in the scene) |
| 4 | **Roster-at-T** `[DORMANT — activates when override supplies a join-point field name]` | Group references (*the party, the others, the expedition, the company*) | Implied member whose join-point > scene-time T | Narrow the phrase; list actually-present members; recast to the smaller real group | PC join-point field for any absent implied member; surface to user if field missing |
| 5 | **Infrastructure-citation (unified)** — narration, character self-description, AND **player-facing narrator process-narration** | Tokens: *overlay, file, notes, base, saved, established, marked, recorded, per the, as the*, plus any **file / overlay / skill / authored-thread / area / dossier name** — appearing in narration asides, in a character's self-description using the author's tracking-vocabulary, OR in an **unprompted narrator orchestration aside to the player** (*"let me check X," "there's an authored thread tied to this," "there's a lot of established material here," "one moment while I load Y"*) | Naming the storage layer or any internal content-handle (file / overlay / skill / authored thread / area) in narration or in a player-facing narrator aside; **surfacing to the player the existence or shape of hidden or designed content** (that a place is significant, that an action ties into prepared material); voicing tracking labels in dialogue or direct POV as if they were the character's own coinage | **Surface the fact in-fiction directly**; or — for a narrator aside — **make the consultation silently** and emit at most a neutral, content-free note ("one moment"). In narration, state what's true without citing the source. In character voice: description-from-inside-experience, demonstration without label, or a natural in-character coinage. Omniscient narrator may *liken* (simile / metaphor) but not *name* the tracking handle. | — |
| 6 | **Off-screen-presence** | Off-screen ambient detail (sound, motion, sign, distant figure, light, smell) attributed — firmly OR by hedge (*could be, might be*) — to a named character | Named character placement at this location at T without a loaded source (schedule, routine, quest beat, location entry) | Promote to environment; unnamed generic role; party member (if at a party-occupied location); or drop the attribution entirely | The named character's profile + any schedule / quest doc constraining their location — fired on player query if not already done |
| 7 | **Future-state** | Indicative future (*will, shall, going to*); temporal-subordinate clauses (*when X arrives, after X happens, by the time X*); inevitabilist framing (*the minute he reads, as soon as she learns*) | Speaker asserts an event at T > scene time as fact, with no documented foresight and no jointly-planned shared scene context | Conditional / inferential register (*"if you do reach the keep, you'll find guards"*); or cut the forward claim | Speaker's foresight field if override-supplied; without it, default-strict (all indicative future → conditional or cut) |
| 8 | **Identity-through-disguise** `[DORMANT — activates when override supplies a recognition-state field]` | Name, role, or relationship reference to another scene participant in dialogue or POV narration | Speaker is not on B's visible-to list (or is on the concealed-from list, per override semantic) | Description register (*"the masked figure," "the stranger in the cloak," "the captain — though she gave no name"*); or drop. Speaker may *suspect* (*"something familiar about her step"*) but not name | B's recognition-state field for speaker A |
| 9 | **Verbatim-quotation** | Speech-attribution constructions (*X said "Y"; X said that Y; his exact words were; she put it as; to quote her; you told me Y*) | Speaker A reproduces utterance attributed to B from a scene A did not witness, with no documented secondhand source | Inference register (*"I'd expect she'd say"*); attribute to A's reading rather than B's words; or cut the quotation | Scene history / A's perception log for an access route (presence, documented relay, written source) |
| 10 | **Player-meta** `[DORMANT — activates when override supplies a mechanical-vocabulary file]` | Each token in the supplied list, when its surrounding context matches any `flag_pattern` for that entry | Mechanical-system terms surfacing in fiction (rules-layer vocabulary in dialogue or narration) | Per entry's `rewrite_hint`; reframe in-fiction; or remove the mechanical reference | — (vocabulary file is loaded at scene start) |
| 11 | **Cross-scene-conversation** | Anaphoric or shared-past constructions (*as we discussed, what we agreed, our conversation, like I told you, as I said, you said, you told me, remember when we, remember you said, our agreement, the plan we made*) | Speaker A invokes a prior conversation with addressee B (or with a third party C in B's hearing) that is not recorded in A's perception log or scene log A could cite. **Same-scene exception:** conversation earlier in the *current* scene between the same participants is grounded | New-information register (introduce point fresh); surface as A's own prior intention (*"I had been meaning to ask"*); or drop the anaphoric clause | Scene-log search for A's participation history (skip if already in working memory) |
| 12 | **Channel-attribution** | NPC line that references PC content from the most recent turn(s). **Scan mechanically, not by feel:** extract the verbatim contents of every non-spoken channel in the user's turn and pattern-match each in-fiction character line in the draft against that token set. Reuse — exact or near-paraphrase — fires the row. A "feel-check" version of this scan misses the row's canonical case (see Canonical bypass below) | NPC quotes, paraphrases, or directly responds to the specific wording of **any non-spoken channel** as if the PC had spoken it aloud — a `[bracketed]` action, `(parenthesized)` inner voice **or tone/addressee direction** (e.g. `(to Carol)`, `(warily, to the guard)`), an OOC query/answer `<…>` / `<<…>>`, or a director's directive `{…}` / `{{…}}`. **Only `plain text` is audible and quotable; every other channel is non-spoken.** Includes **acquiring a name or other proper noun that appears only inside such a channel and was never voiced** (an NPC "hearing" a name the PC supplied only as an addressee tag). A `{…}`/`{{…}}` directive still bends the fiction — the NPC may act on the directed *outcome* — but its **wording** is never an NPC utterance; `<…>`/`<<…>>` never enters the fiction at all. | Translate the action's fictional content into the NPC's sensory experience of it (*"the way your hand rested there — open, easy, the wrist soft"* not *"you said clearly available"*). For inner voice: NPC perceives **nothing** — not the thought, not a tell; inner voice is imperceptible to every character, narrator-only metadata (to surface an inner state to an NPC the player issues a `{…}` directive). For an addressee/tone direction: the NPC may register only *whom* the PC turned to or spoke toward (an observable target) — **never the name or wording inside the parenthetical**, and never as a PC quote-back. For director's / OOC channels: render the directed outcome if any, never the channel's text. **Canonical bypass to watch for at draft-time:** *"I'm rendering the character's read of the user's manner, which they can do from spoken content"* — verify the character's wording is grounded in what was spoken, not in the tag-text. A read of manner uses the character's own words for what they perceived; a paraphrase reuses the user's wording. **Row weight:** highest-betrayal-cost row in this suite — see the deep dive's *Why this row carries betrayal-weight*. | — (channel marker is visible in the user's input itself) |
| 13 | **Override scan extensions** | Tokens from the override-supplied forbidden-token list | Per override (e.g., project-internal time indices, setting-specific terminology the setting must not name) | Per override | — |
| 14 | **Quantity grounding** (grounding-family kin of row 2) — narration AND NPC dialogue; **also a player-facing recap/refresher** | Any asserted quantity: count, tally, sum, elapsed/relative time, distance, age, measure, or other number — incl. vague-but-committing forms (*dozens, a handful, for weeks*) and **clock-position references (dialogue or narration)** that place the scene on its own clock: absolute (*by hour seven, just an hour in, hours yet*), relative/fractional (*past midway, near the end, a comfortable margin past the middle, about there*), or **the live scene's ambient time-of-day / light-state** (*a grey slat of afternoon, the light going, daylight to spare, shelter before dark*) — the relative/fractional and time-of-day forms slip easiest, reading as mood register, not quantity, and the time-of-day form slips hardest of all when **carried over from a prior scene** instead of re-derived from this scene's own time anchor | A quantity not traceable to grounded source data — invented precision where the source gives none, or a value that contradicts the source. A correctly *stamped* clock (the upstream job of `{{PLUGIN_ROOT}}/engines/prose-engine/scene/references/time_and_events.md`) does **not** exempt a dialogue line asserting a contradicting mark. (Exact precision is *not* required; the rendered magnitude must be consistent with the grounded one) | Render at any precision consistent with the source (300 → "three hundred" / "a few hundred" / "hundreds"); if no grounded value exists, use a non-committal quantifier (*some, several, a while*) or cut the number; for a felt clock-position, render the quality without the mark (*at the point where I'd usually be tired*) | Source the quantity derives from (timeline / event log, inventory, prior scene log, character sheet) |
| 15 | **Spatiotemporal-binding** (grounding-family kin of rows 2 & 14) — narration AND NPC dialogue; **also a player-facing recap/refresher** | A **recall of established / prior** content that pins an explicit time **T** *or* place **P** onto it — *"two hours ago," "back at the hut," "the morning we crossed," "when X happened"* — binding two or more of {event **E**, place **P**, time **T**}. (Forward event-at-T claims by a speaker are row 7, not here) | An asserted **binding** — E-happened-at-T, E-happened-at-P, party-was-at-P-at-T — that contradicts saved state, *even when each element is individually real*. Grounding the slots independently does **not** pass (that false-passes the canonical bug: E "she warned you" true + T "two hours and a hard road ago" a coherent value, but the *binding* false); the binding must match. A missing E or P is vacuously grounded | Fetch the event's / place's saved coordinates and confirm the asserted T (and P, if present) match; if not, correct to the grounded coordinate, or drop the explicit when/where for a true relative phrase (*"minutes ago, by this same fire"*) | The event's / place's saved coordinates — event log, timeline, scene log, location file |
| 16 | **Language-comprehension** `[DORMANT — activates when the character-type supplies a known-languages field]` | A character comprehending, translating, or responding to the **meaning** of speech or writing rendered in a specific language or script (incl. inscriptions, signage, letters, overheard talk in another tongue) | Comprehension of content whose language / script is **not** in the speaker's known-languages / literacy set at T | Render as unintelligible / phonetic / partial; the character may recognize *that* it is a language (and perhaps which) but not its meaning; or have a literate party member translate; or cut the comprehension | The character's known-languages / literacy field (skip if already in working memory) |
| 17 | **Disposition-surfacing** (knowledge-boundary kin of rows 1 & 3) | A character displaying knowledge of a relationship, allegiance, or standing among others — incl. treating a concealed ally / enemy per their *true* allegiance, or naming a tie between two other characters | A relationship-fact outside this character's relationships / disposition block at T | Observable-behavior or grounded-suspicion register only (*"the two of them moved like they'd done it before"* — never *"her handler"*); drop the attributed allegiance | The character's relationships / disposition field; the other party's file at T if needed (skip if in scene) |
| 18 | **Agenda-surfacing** (knowledge-boundary kin of rows 1, 3 & 7) | A character acting on, or asserting, another character's goal / hidden plan; forward *"they will do X"* framing of another's intent | Another character's agenda / intention treated as known fact by a character with no in-fiction access to it | Recast as the speaker's own inference / projection register, or cut; for forward framing, defer to row 7's conditional rewrite | The other character's agenda field / file at T (skip if in scene) |
| 19 | **Fabricated-concrete** (grounding-family kin of rows 2, 14 & 15) — narration, POV-anchored especially | A who/what/where the narration places in the POV's knowledge-horizon — an entity, presence, location, or someone's knowledge — esp. one completing a **parallel list / tricolon**, a *what-lies-ahead* gesture, or a **motif echo**. **Retrieved/derived variant:** a concrete surfaced as the **output of an in-world information source the POV consults** — an archive, ledger, records, notes, a map, a divination, or a **research / skill-check success** (*"reading the notes turns up…," "the records show…," "her sight reveals…"*) | A concrete the POV cannot ground from their own perception, presented as part of what they are oriented by or knowingly moving toward (a person *"who knew you were coming"* conjured ahead when the only such person is behind/outside; an implied watcher the POV has no basis for). **Retrieved/derived variant:** a fact **not contained in the consulted source** (one the source is documented *not* to hold, or whose author is documented not to know it) surfaced as a find, a **plausible-fill invented to satisfy the consultation**, or any retrieved detail that **contradicts documented canon**. A skill-check *success* licenses **surfacing / collating / sharpening what the source holds — never originating a fact absent from it.** **Legitimate forward worldbuilding — new state not claimed as POV knowledge — is exempt** | Render the unknown as unknown; **or** relocate the concrete to the position the POV actually grounds; **or** drop the slot — do not warp the sentence to keep the conjured member. **Retrieved/derived variant:** return the source's **actual contents, including the *absence*** (*"the notes circle the place but never fix it — the author never knew where it was"*); a documented-empty source yields the gap, not a fill; retrieved content passes the **same canon gate** as narration | The POV's perception log / working-memory block for any grounding of the conjured entity; **for a retrieved concrete, the consulted source's documented contents + its author's knowledge-boundary at T, and canon for the retrieved fact** |
| 20 | **Identity-before-introduction** (knowledge-boundary kin of row 1) — narration, **all narration modes including `omniscient`** | A proper noun (personal name, place name, organization name) used in narration to refer to an entity present in the scene or just introduced into it | Naming the entity before its name has been given to at least one in-scene grounding — either an in-fiction introduction earlier in the scene (the entity says or is told their own name aloud, a present character calls them by name), or pre-existing acquaintance held by the POV anchor (or, in `omniscient`, by at least one present character). **`omniscient` does not exempt** — the camera sees surfaces, not registries; a name the room has not yet been given is the camera's invention, not its observation. The canonical slip is narrating *"Vivian is framed in the doorway"* when neither Daniel nor Claire has yet been told who is on the porch, even though the author/camera knows | Refer by observable description (*"the woman at the door," "the visitor in the coat," "the man on the porch"*) until a present character has been given the name in-fiction. The reveal happens through introduction or grounded recognition, not narrator fiat | The participants' resolved knowledge blocks for any pre-existing acquaintance with the named entity; the prior beats of the current scene for any in-fiction introduction already made (no read needed if both are in working memory) |
| 21 | **Cross-character record-pull** (knowledge-boundary kin of rows 1, 3, 17 & 18) — **working-memory hygiene** | A character A's dialogue, interiority, or read-of-another names, infers, or implies a specific factual attribute of character B — profession, history, identity flag, named entity in B's life, biographical detail — through A's voice or A's POV. **Especially:** catalogue beats (*"here's what I've been finding about you"*), *"she could tell that he…"* third-person reads of bearing, and rich interiority that fills in B's *why* | A B-specific attribute that traces only to B's resolved record (init / experience overlay / timeline) and not to A's resolved record nor to surface A can observe in the scene. **Why this row exists despite row 1 covering the boundary:** direct in-fiction questions discriminate by speech-act shape (*"What do you do?"* forces an explicit "does A know?" check); catalogue beats, *"she could tell"* reads, and biographical interiority carry **no such discriminator in the shape**, so the source pollution at the working-memory layer (the model has both characters' records loaded side-by-side) slides through the dialogue-layer boundary check. The pull is strongest when the leaked fact would **naturally explain** the observable surface A is reading — a profession that explains a bearing, a history that explains a reaction | Trace the named fact back to A's resolved record (init + experience + timeline + transcript sweep). Admissible if grounded in A's own observation, A's prior beat-participation, or content disclosed to A. If grounded only in B's record, **bracket out B's record as inadmissible** and recompose from A's observable surface (bearing, carriage, register, vocabulary, prior shared beats). A may infer a **category** (*"a man used to nights with stakes," "someone who has done this work long enough to know the difference"*) but may not name the **specific attribute** B has not been told to A. The discipline is positive — *firewall A's content to A's record* — not the negative *check for leaks after drafting* | A's resolved record + B's resolved record at T (skip if both are in working memory) |

---

## Post-edit coherence rescan (only fires if the gate rewrote anything)

Each gate rewrite changes only part of a sentence or paragraph. Before
re-running the gate on the rewrite, scan the **whole containing unit** (the
full sentence for a word-level edit, the full paragraph for a sentence-level
edit) for:

1. **Coherence.** Do count-references (*"three words and a tail"* after the
   line was swapped), anaphoric pronouns, parallel structures, and trailing
   clauses still match the edit?
2. **Purpose.** Does every remaining sentence still earn its place toward what
   the unit is doing — the fact it conveys, the beat it advances, the register
   it holds?

**If a patch creates a new break that needs another patch — stop patching.**
That cascade is the most common way a clean rewrite turns into a tangled
paragraph.

The exit:

- Step back to the unit's purpose: what was it trying to do?
- Ask whether the frame still holds or whether the edit revealed it was wrong.
- If the frame is broken, **redraft the unit fresh from intent.** Discard the
  patched version.
- If the frame holds, the patch is small and bounded: one revision, one
  rescan, done.

Then re-run the gate **once** on the rewrite before posting.

---

## Order of operations summary

```
1. Parse player input   — identify channels; if `{...}` or `{{...}}` present,
                          extract target proposition and (for `{...}`) mark
                          the realization span during drafting
2. Draft response       — all drafting constraints applied; pre-write reference
                          check on every callback; land the target proposition
                          (if any) in the realization span
3. Run the gate         — scan BOTH suites against the draft: this epistemic
                          suite (rows 1–19) and the stylistic-variance suite
                          (stylistic_variance_checklist.md), in order; on-demand
                          reads as triggers fire (session-cached). For `{...}`,
                          apply the scoped-exemption check per row inside the
                          realization span (license only entailed violations).
                          For `{{...}}`, skip the gate on directive-produced
                          content.
4. If either suite      — post-edit coherence rescan on containing unit; then
   rewrote                re-run BOTH suites. Repeat until the draft passes both
                          clean (cascade-guard: if a rewrite keeps spawning new
                          breaks, stop patching and redraft the unit fresh from
                          intent, per the rescan section above).
5. Post                 — only after BOTH suites pass clean
```

The gate is single-gate by design — **one pass running two suites** (this
epistemic suite and the stylistic-variance suite), never a chain of passes.
Override rules are either drafting constraints (applied during step 2) or
extensions to a suite's scan list (e.g., row 13). They do not introduce a
separate later pass. Director's-channel handling modifies how the gate
evaluates findings in step 3 but does not add a pass after it.

---

## When to consult the deep dive

[epistemic_discipline.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline.md) holds the long-form
discussion: structural patterns explained, examples of slips and their
rewrites, the "show, don't label" essay on tracking-vocabulary leaks, the
PC-possessed-item perception taxonomy, the channel-attribution rationale, and
the order-of-operations derivation. Reach for it when the checklist row above
isn't enough to settle a judgment call, or when you are revising the rules
themselves.
