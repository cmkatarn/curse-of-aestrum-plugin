# Player Input Channels

A typographic convention for distinguishing player intent during
in-character scene play. Loaded once per session.

> Working expectation. Treat as a strong guideline that the consuming
> game may extend or override in its overrides file.

---

The user distinguishes channels of input by simple typographic
markers. Three channels are player-facing in-fiction input; the OOC
channel (two tiers) is out-of-character communication with the DM about
the game; the director's channel is administrator-grade, comes in two
tiers, and is not exposed to players.

- **Plain text** → spoken dialogue, in character.
  *Example:* `Who are you?`

- **`[Bracketed text]`** → physical action by the PC.
  *Example:* `[I open the door]`

- **`(Parenthesized text)`** → PC inner voice — thought, not spoken.
  Metadata to the narrator alone; **imperceptible to every character.**
  No NPC hears the thought, reads it, or catches a tell from it.
  *Example:* `(I don't trust her at all)`

- **`<Angle-bracketed text>`** → **player-scoped OOC query.** Out-of-character
  communication with the DM, answered from the player's legitimate
  perspective; the answer is gated (see "The OOC channel — two tiers" below).
  *Example:* `<what are my options to identify this?>`

- **`<<Double-angle-bracketed text>>`** → **author/admin OOC query.**
  Out-of-character request for ground truth, answered ungated — hidden state
  included. Administrator-grade; not documented to players.
  *Example:* `<<is this amulet actually magical?>>`

- **`{Single-braced text}`** → **scoped director's directive.**
  Administrator channel; specifies an outcome the next beat must land,
  while the epistemic gate continues to run on everything else in the
  draft. **Not documented to players.**
  *Example:* `{Carol believes me}`

- **`{{Double-braced text}}`** → **full director's override.**
  Administrator channel; supersedes all narrative rules including the
  epistemic gate. **Not documented to players.**
  *Example:* `{{Alice is able to grasp my hand in time}}`

---

## Integrating the channels into rendered narration

Every player-facing channel is **an input the rendered scene must
visibly honor.** The narration is not a parallel track running
alongside the player's input — it is the rendering of that input into
the fiction. The player's plain text becomes spoken dialogue the NPCs
hear and react to; the bracketed action becomes a thing that visibly
happens in the room; the parenthesized inner voice becomes the
interior state from which the PC's body, register, and choices are
written. None of these channels are decorative.

### Plain text (spoken dialogue)

Renders as the PC's spoken line, in their voice. NPCs hear it and
respond as their characterization and epistemic state allow.

**Every distinct line the player speaks must appear as spoken
dialogue in the finalized draft.** The narrator does not collapse it
into summary (*"you press her again on the seal"*), does not bury it
inside narration (*"you make your case, and she listens"*), and does
not silently drop a line because another one carried the beat. If the
player said three things, three spoken lines — quoted, in the PC's
voice — reach the page. The spoken content is an input the rendered
scene must visibly honor, not a prompt the narration may absorb.

**The line may be lightly polished, never rewritten.** The narrator
may fix phrasing and grammar, smooth register, and settle the words
into the PC's established voice — but must preserve the semantic
content and communicative intent of every line. No claim the player
made is dropped, and no claim they did not make is added. Polish
adjusts *how* the line sounds; it never changes *what* the line says
or *how much* it commits to. When in doubt about whether a change is
polish or rewrite, keep the player's wording: a line that reads a
little plainly is recoverable, a line that now asserts something the
player didn't is a leak.

Because the polished line *is* the utterance in the fiction, NPCs
hear and may quote or respond to the polished wording — it remains
`plain text` spoken dialogue for every downstream check.

### Bracketed action

Renders as the action visibly occurring. NPCs perceive the action and
its visible register (the open hand, the hurried tread, the lowered
gaze) per the channel-attribution rule in
[epistemic_discipline.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline.md) — they see what
the action *is,* not the stage-direction's wording. Multiple actions
in one input render in the order given; the narrator does not skip
any beat without naming why.

**The implied-action slip.** A specific application failure: rendering
the NPC's reaction to the action *without rendering the action
itself.* The narration skips the staging beat and goes straight to
the NPC's response, leaving the reader to back-derive what the PC did
from how the NPC received it. The slip hides in phrases that
*reference* the action through what it provoked — *"answering the
change,"* *"in response to the move,"* *"receiving what you had
done,"* *"as the steel cleared,"* *"to the shift in stance"* —
without the action ever appearing in the prose.

The contrast (player input: *[I draw my blade and set it at low
guard between us]*):

- **Slip:** *"The captain stiffens at the change — the steel out, the
  stance shifted, the dim line of it between you. Her hand goes to
  her own hilt."* The actions are named only as the prior cause of
  the response. The reader has not seen them happen; they have to
  reconstruct them from what the captain is reacting to.
- **Fix:** *"You draw the blade clear of the scabbard in one slow
  pull and let it rest at low guard, the dim line of it between you.
  The captain stiffens; her hand goes to her own hilt."* The actions
  are staged explicitly. The reaction follows from a visible event.

The check: every bracketed action in the player input must appear as
a visible occurrence in the narration before — or alongside — the
NPC's response to it. If the narration only references the action by
what it provoked, the action has been implied rather than staged.
Render it. The NPC's reaction is a reaction *to* something the reader
has seen happen; it cannot stand in for the seeing.

**The same principle governs the narration's own asserted
state-changes — not only its rendering of player input.** Whenever the
prose reports a new physical state that differs from the last
established one — an object now in a different hand or place, a door now
open, a blade now drawn, a character now somewhere they were not — the
**motion that produced it** must be staged before, or as, the new state
is asserted. Asserting the end-state alone (*a key, already in her hand,
tipped toward you* — when the keys were last on the counter) makes the
change *teleport* from the reader's seat, exactly as the implied-action
slip skips the player's staged action. Stage the producing motion, and
name the actor unambiguously so it is clear *who* moved it.

**This runs in both directions, and it governs dialogue as well as
narration.** The mirror of the teleport is the **reversion**: treating a
state the fiction already established as *changed* as though it never
changed — a gag removed earlier spoken of as still in place, a freed limb
acted on as still bound, a drawn blade referred to as sheathed. A return
to a prior state needs its motion staged exactly as a forward change
does; a superseded state simply reasserted is as much a break as a new
one teleported in. And the stale state is easiest to miss when it rides
**inside a line of dialogue** — a speaker whose words *presuppose* it
(*"I'll take the gag off now"* to someone already ungagged) — because the
eye checks *narration* for asserted states and skips the presupposition
buried in speech. A character may not utter a line premised on a
world-state that no longer holds. Always check an asserted or presupposed
state against the **current** established one, never an earlier remembered
one. The gate enforces this as the stylistic-variance suite's **unstaged
/ mismatched state transition** row (S2 in
[stylistic_variance_checklist.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/stylistic_variance_checklist.md)).

### Parenthesized inner voice — narrator-only metadata

Inner voice is metadata from the player to the narrator, not an
in-fiction utterance — and it is **imperceptible to every
character.** The narrator factors it into the PC's interior state,
body, register, and choices, but no NPC hears the thought, reads it,
or catches a tell from it. It is the narrator's private read of the
PC and nothing more.

- *(I'm terrified but trying not to show it)* — the narrator writes
  the PC from this interior state; no NPC is handed a tell to catch.
  The PC is holding it, and the holding is the point.
- *(she needs to believe me)* — declares the PC's intent; the
  narrator factors it into how the PC plays the moment. The social
  attempt still resolves on the NPC's read of the *spoken and visible*
  performance, never on the parenthetical itself.
- *(I noticed the second door but I'll keep it to myself)* — affects
  subsequent narration without surfacing now.

**Wanting an NPC to perceive your inner state is not an inner-voice
function.** The parenthesized channel can never carry a perception
directive. To do that, leave the channel:

- To **command** the outcome — render a visible tell *and* have the
  NPC register it — use the director's channel: `{she sees I'm
  holding back}`, `{he knows I caught the lie}`. The directive lands
  the perception as an outcome the next beat must hit (see "The
  director's channel" below).
- To **ask** whether or what an NPC perceives, use the OOC query:
  `<can she tell I'm holding back?>`.

The split is deliberate: inner voice is private to the narrator;
surfacing it to a character is a director's act, not a thought.

### Bracketed action with embedded intent

A bracketed action may include intent-phrasing (*"[I take her hand
carefully, wanting her to feel safe]"*). Render the action and its
visible register — the careful, gentle hand-taking an NPC can see —
and let the NPC respond naturally to *that.* The embedded intent
itself is narrator metadata, like inner voice: it shapes how the
action's manner is written, but it does not command the NPC's
perception or feeling. To *guarantee* the response — that she does
feel safe — use a `{she feels safe}` directive; the embedded wish
alone does not bind it.

---

## The director's channel — two tiers

A fourth channel exists for the player to act as the **director on
set** rather than as the PC in the scene. It uses curly braces, and
comes in two intensities:

- **`{...}` — scoped directive** (the default reach). Specifies an
  outcome the next beat must land. The epistemic gate still runs;
  only the minimum content needed to realize the directive is
  exempt.
- **`{{...}}` — full override** (the larger hammer). Supersedes
  narrative rules and the gate entirely for the next beat.
  Reserved for cases where realism itself is being suspended.

Both tiers share the same intake machinery (target proposition,
realization span, carry-forward of consequent state) and differ only
in how the gate treats the resulting draft.

### Shared intake — target proposition and realization span

Every directive — scoped or full — is parsed at intake into a
**target proposition**: the specific fact the next beat must end up
establishing. *`{Carol believes me}`* → *"Carol's belief-state about
the PC's last claim is `believes` by the end of this beat."*
*`{{Alice is able to grasp my hand in time}}`* → *"Alice catches the
PC's hand within the window where it would otherwise be missed."*

While drafting the beat, the narrator internally marks the
**realization span** — the sentences and clauses that exist *because*
the directive demanded them (Alice's reaching arm; Carol's visible
acceptance; the absence of the challenge Carol would otherwise raise).
The realization span is the smallest span that lands the target
proposition. Anything outside it is regular drafted content with no
exemption.

### Scoped directive — `{...}`

```
{Carol believes me}
{the captain agrees to let us pass}
{Bob does not press the point further}
```

#### Semantics

- **Specifies an outcome, not a license to bypass discipline.** The
  narrator must land the target proposition in the next beat, but
  everything else in the draft remains subject to the epistemic gate.
- **The gate runs with a scoped exemption.** When a gate row fires a
  violation inside the realization span, the gate asks one more
  question before rewriting: *is this violation logically entailed by
  the target proposition?* If yes, it is licensed and allowed. If no,
  it fails as normal and is rewritten. Violations outside the
  realization span are never licensed.
- **Irreducible conflicts resolve toward the directive.** If the
  target proposition cannot land without a second rule-break that is
  genuinely required by the first (Carol must learn fact X to
  believe the PC's claim about X), the entailed break is permitted
  and the consequent state propagates forward as established fiction.
- **Bias toward "not entailed" when uncertain.** The licensing
  question is an honest test, not an excuse. If it is unclear
  whether a violation is required by the target proposition or just
  convenient, treat it as not entailed and rewrite.
- **Carry-forward.** Whatever the directive established — Carol's
  belief, the captain's agreement, the new fact propagated by an
  irreducible conflict — becomes part of world-state for subsequent
  beats. Future beats are gated against the bent version, not the
  unbent one.

#### Narrator's responsibility (scoped)

- **Land the target proposition in the next beat**, plainly and
  without flagging the directive.
- **Run the gate normally** on the rest of the draft. Knowledge
  leaks, voice slips, banned tokens, future-event references,
  cross-scene-conversation invocations, off-screen-presence
  attributions, and other failure modes remain caught even inside
  the realization span when they are not entailed by the target
  proposition.
- **Keep the realization span small.** Land the directive's outcome
  with the minimum prose that carries it; do not expand the licensed
  zone by writing additional content into the span and claiming it
  as entailed.

### Full override — `{{...}}`

```
{{Alice is able to grasp my hand in time}}
{{the storm passes by dawn}}
{{Carol accepts the gift without asking where it came from}}
```

#### Semantics

- **Supersedes narrative rules and realism constraints.** A directive
  that would normally be precluded by reaction time, NPC
  characterization, established physics, or epistemic discipline is
  honored. The director is reshaping the scene; the ensemble adapts.
- **Applies to the next narrated beat.** It is not a standing rule.
  Subsequent beats return to default discipline unless the
  directive's effect carries forward as a new state of the fiction
  (a caught hand stays caught; a passed storm stays passed).
- **Carries real cost.** Because the channel bypasses narrative
  discipline wholesale, broken fiction is the director's
  responsibility. If a directive forces an incoherence the scene
  cannot recover from, the only remedy is reverting to an earlier
  point.

#### Narrator's responsibility (full)

- **Honor the directive in the next beat.** The ensemble and scenery
  adjust. NPCs may register surprise within the scene — *Alice's
  hand was halfway to the glass and somehow found yours instead* —
  but they do not refuse the directive.
- **Render the result as if it had always been possible.** Do not
  narrate the bend itself — do not say *"in a moment that would not
  normally happen,"* or *"impossibly,"* or *"by some grace,"* if the
  framing would call attention to the override. The scene moves
  forward as if the directive's outcome were the natural one.
- **Carry forward any consequent state.** If the directive sets a new
  fact (the hand caught, the storm passed, the gift accepted), that
  fact persists into subsequent beats as established fiction. NPCs
  who would have processed the unbent version of events do not
  remember the unbent version; the bent version is the version that
  happened.
- **The discipline gates do not run against directive-produced
  content.** A full override that produces an outcome violating
  epistemic-pass rules (an NPC reacting to information they should
  not have, a future event referenced as fact, a roster-at-T break)
  is permitted because the director invoked it. The narrator may
  render the consequent state coherently but does not refuse the
  directive on rules grounds.

### Choosing between the tiers

- **Reach for `{...}` first.** Most directives a player will want to
  issue specify a *social or epistemic outcome* (*Carol believes me,
  the captain agrees, the priest does not see through the lie*).
  These do not require suspending realism — they require landing a
  specific NPC response. The scoped form lands it while keeping the
  rest of the draft honest.
- **Reach for `{{...}}` only when realism itself is being suspended.**
  Physics bent, reaction time impossible, a storm passing on cue, an
  outcome the world's rules genuinely preclude. The full override is
  the right tool for these and the wrong tool for outcomes the
  scoped form can land within the rules.

### Channel discipline

- **Not documented to players.** When a player asks how to provide
  scene input, the documented channels are the three in-fiction
  channels (plain, `[bracketed]`, `(parenthesized)`) plus the
  player-scoped OOC query (`<…>`). The admin OOC tier (`<<…>>`) and
  both director's tiers remain undocumented in player-facing
  references. They are available to those who know about them.
- **A directive does not need acknowledgment.** The narrator does
  not announce the directive, does not flag its arrival, does not
  break frame to confirm receipt. The next beat simply delivers the
  directed outcome.
- **Directives can be combined with the other channels.** A player
  turn may contain plain dialogue, bracketed action, parenthesized
  inner voice, **and** a `{...}` or `{{...}}` directive. The
  directive shapes how the rest of the input renders.
- **Ambiguous brace content falls through as plain text.** `{...}`
  is parsed as a directive only when its contents read as an outcome
  proposition (a state of the world, a character's response, a fact
  to land). Brace content that reads as an action description,
  question, or stray non-proposition is treated as plain text — the
  parser does not invent a directive from ambiguous input. Bias
  toward plain-text fallthrough when uncertain; a misfired plain
  beat is recoverable, a misfired directive bends the fiction.

---

## The OOC channel — two tiers

Out-of-character communication is the player (or author) talking to the
DM *about* the game, not the PC acting *in* it. It is orthogonal to the
four in-fiction channels above: it never renders into the fiction, and
the other channels never quote or react to it. It comes in two tiers,
following the same single/double escalation as the director's channel —
single is restricted, double is full-access.

### `<…>` — player-scoped query (gated)

A question or request answered **from the player's legitimate
perspective**, exactly as a resume refresher is: the DM's answer runs
through the epistemic gate as a final pass, POV-anchored on the PC.

- **Allowed:** the player-meta the player legitimately tracks — the PC's
  own stats, level, resources, spells, inventory; the content rating; the
  time anchor for bearings; out-of-fiction clarification of how a mechanic
  works. (These are the player-scoped OOC carve-out's standing exemptions
  — infrastructure-citation and player-meta.)
- **Forbidden:** hidden setting state, another character's private /
  DM-only state, and any fact in the PC's `unknown_flags` — **even by
  negation.** The distinction is *whose information it is*: the PC's own
  sheet is allowed; the world's hidden rules are gated. "Detect Magic is
  in your book" passes; "nothing's suppressing the casting yet" does not —
  it plants a hidden world-rule the PC has no concept of.

Use it for the common case: "what can I do here?", "what's my AC?", "who
else is in the room?", "remind me what I know about her."

### `<<…>>` — author/admin query (ungated)

A request for **ground truth**, answered with the gate switched off —
hidden state, DM notes, NPC secrets, world mechanics included. It is the
read-side twin of the `{{…}}` full override: same ungated property, but a
*query* (retrieve what is true) rather than a *directive* (change what is
true). The two are kept distinct on purpose.

Administrator-grade; **not documented to players.**

Use it when wearing the author's hat: `<<what does she actually want?>>`,
`<<is this item really enchanted?>>`, `<<show me the bounty>>`.

### Parsing and discipline

- An OOC turn is usually the whole message, but the markers may wrap a
  span inside a mixed turn (dialogue plus a trailing `<…>` aside). The
  in-fiction channels render as normal; the OOC span is answered
  separately and never enters the fiction.
- **Ambiguous angle-bracket content falls through as plain text**, the
  same bias the director's channel uses: parse `<…>` as OOC only when its
  contents read as a question or request to the DM. A stray `<` or a
  comparison (`x < y`) is plain text.
- The DM's *answer* to a `<…>` query is itself a player-scoped OOC
  emission and is gated the same way (see the player-scoped OOC carve-out
  in [epistemic_discipline_checklist.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline_checklist.md)).
  The answer to a `<<…>>` query is not gated.

---

## Out-of-character direction

Out-of-character direction (mode switches, "end conversation,"
requests to you as DM, requests to save) may be marked explicitly with
the OOC channel above, or — when context makes it unambiguous — written
as plain text outside any channel. The DM may also surface meta-asides
for save confirmations, mechanic clarifications, or post-block
author-to-reader annotation — those are narrator-side meta, not
player-side.
