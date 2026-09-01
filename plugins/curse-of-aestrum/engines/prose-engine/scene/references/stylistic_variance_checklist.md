# Stylistic Variance — Gate Checklist

The craft-side suite of the single scene gate. Where the
**epistemic-discipline** suite ([epistemic_discipline_checklist.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline_checklist.md))
scans the drafted output for **leaks** — knowledge-boundary breaks, ungrounded
claims, surfaced hidden state — this suite scans the *same draft* for
**stylistic-variance** failures: the mechanical seams that break immersion not
because anything is *false* but because the prose has fallen into a repeated,
bolted-on, or register-breaking shape.

The two suites are **distinct and separate by design.** Keep epistemic
concerns out of this file and craft concerns out of the epistemic file —
neither suite owns the other. They share only the gate's single
scan→rewrite→rescan loop (see [core.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/core.md), "Rule-application order is
fixed"): the gate runs **both** suites against the draft, funnels any rewrite
back through **both** until both are satisfied, and posts only when the draft
passes both clean. **One gate, two suites — never a separate later pass.**

Load this once per session, alongside the epistemic checklist. It covers the
whole session.

---

## What this suite is

A stylistic-variance failure is a prose-craft seam, not a factual error. The
content can be perfectly grounded and still trip this suite: a beat that ends
on the same stock handoff as the last one, a generic closer bolted onto a
moment that already implied the choice, a flat mechanical question dropped into
a register that was anything but neutral. These are immersion breaks of
*texture* — the reader feels the machine, not a falsehood.

A **continuity seam** is the same class of break from a different angle: the
prose asserts a new physical state — an object in a new hand, a door now open, a
blade now drawn — without staging the motion that produced it, so from the
reader's seat the change *teleports*. Grounded, not false; still a machine-seam
the reader feels. The suite is the craft-side gate, so it catches both the
*variance* seams (repeated / bolted-on / register-breaking shapes) and these
*continuity* seams (an end-state asserted with its staging skipped).

A **withholding seam** is the third class, and it runs the other way: the prose
*refers to* something the reader was entitled to receive — most often a line of
dialogue the POV anchor heard — and delivers only the fact of it. Nothing is
false and nothing is repeated; information the player needed simply never
reached the page, and they cannot act on what they were not given. The suite
catches this alongside the other two because the failure surfaces the same way —
as prose that reads finished and leaves the reader short.

The fix is never to delete the function (a beat still has to hand off; a scene
still has to breathe). It is to **render the function freshly**, keyed to the
moment, the way the relevant craft-rule file directs. Each row below names that
file in its last column; consult it for the in-register rewrite.

---

## Final gate — stylistic suite (scan drafted output, in order)

Runs in the **same** gate pass as the epistemic suite, against the same draft.
A row firing inside a `{...}` realization span gets the same scoped-exemption
treatment the epistemic suite uses (license only violations entailed by the
directive's target proposition); a `{{...}}` full override skips this suite on
directive-produced content, exactly as it skips the epistemic suite.

| # | Check | Trigger surface | Forbidden | Rewrite move | Rule source |
|---|---|---|---|---|---|
| S1 | **Repeated / bolted-on handoff** | The beat-closing action prompt — the sentence(s) that hand control back to the player | A **stock closer** used as a default (*"What do you do?"* and near-equivalents) appended to a beat that already implies the choice (the offered hand, the open door, the just-asked question); **or** a handoff substantially the **same as the previous beat's** closer — the same phrasing or the same shape, turn after turn (the repeated token). An open situation licenses a direct ask; it never licenses the *same* direct ask twice running. | Write a *fresh* handoff keyed to what just happened, in the beat's register, scaled to its stakes; or let a charged image / plain trailing handoff carry it where the floor is already obviously the player's. Vary the form whenever register or stakes change. | [action_prompt.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/action_prompt.md) |
| S2 | **Unstaged / mismatched state transition** (the teleport, and its mirror) | Narration asserting — **or a character's dialogue or action presupposing** — a physical state that differs from the **current** established one: an object now in a different place or hand; a door / lid / blade / restraint / gag now open / drawn / closed / removed / replaced; a character now somewhere they were not; **or a state established as *changed* being treated as though it never changed** (a gag removed earlier spoken of as still on; a freed limb acted on as still bound; a drawn blade referred to as sheathed) | The state asserted or presupposed **without the motion that produced it** staged in the prose, in **either direction**: a *forward* transition (the new end-state reached with the intervening action skipped, so a thing that was *here* is suddenly *there* or in a hand — the **teleport**), **or** a *reversion* (a **superseded** state treated as current with no staged return to it — the **mirror teleport**: the prose, or a character, speaks or acts on a world-state the fiction already established was left behind). **The stale state carried inside a line of dialogue is the easiest form to miss** — a speaker's words *presupposing* it (*"I'll take the gag off now"* to an already-ungagged partner; *"once your hands are free"* to someone already unbound) — because a scan that reads only for *narration asserting* a state skips presuppositions embedded in speech. Often compounded by an **ambiguous actor** (a bare *"she"* whose nearest antecedent is the wrong character) so even *who* moved it is unclear. | Check the asserted/presupposed state against the **current** established one, not a remembered earlier one. If a transition was intended, stage the producing motion (forward or reverting) before — or as — the new state is asserted, and name the actor unambiguously. If **no** transition was intended, the line has drifted onto a stale state — correct it to the state that actually holds. **A speaker may not utter a line premised on a superseded state.** Never assert or presuppose an end-state alone when a visible action had to occur to reach it. | [player_input_channels.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_input_channels.md) (implied-action slip, generalized) |
| S3 | **Setting-register drift** (vocabulary / orthography mismatch with declared setting) | Narration and dialogue lexical choices: spelling conventions, everyday-object names, idiomatic phrasings, units of measure, vocatives, casual food / clothing / building / road vocabulary | Word choices that belong to a different regional or cultural register than the scene's declared setting — *kerb / pavement / biscuit / lift / mum / motorway* surfacing in an American-suburb scene; *sidewalk / cookie / elevator / mom* in a London scene; metric measures in a 1950s-American piece; the wrong vocative culture (*love, mate, pet, hon, ma'am*) for the place. **Authorial register drift is the usual route:** the genre's prose tradition (Shirley Jackson by way of Hill House, British procedural, Southern Gothic) carries a vocabulary the *story-tradition* lives in, even when the *setting* does not. The check is against the setting, not the tradition. | Substitute the setting-correct word (*curb, cookie, elevator, freeway, mom*; *kerb, biscuit, lift, motorway, mum*; *yard, foot, mile* vs. *metre, kilometre*); drop the misplaced vocative or replace with one local to the setting. If the setting genuinely permits a code-switch (a British character visiting Ohio, a regional outlier in the cast), license only their dialogue, never the narration. | The anthology's setting note — under Pandora: `anthologies/<A>/world/setting.md` (or its override) — for the region / period / cultural register; for consuming games with a richer setting layer, that game's setting / world file |
| S4 | **Salience-grounded ambient detail** (the Chekhov omission) | Narration surfacing a concrete ambient detail (an object, sound, smell, change-of-state, conspicuously absent thing) that would land in the salience field of at least one present character given their established relationship to it | The detail surfaced and then **left un-reacted-to** by every character it would matter to — a wife's husband's car parked outside her home when she does not know he's been there; a faint sharpness of bleach under domestic kitchen smells with no character orienting toward it; an ordinarily-open hallway door now shut with no character registering the wrongness. The reader's eye lands on the detail, registers that *someone in this room would notice this*, and is then yanked when no one does. Compounds especially with the omniscient camera, which can surface ambient detail without an anchor's salience to discipline what gets surfaced. | Either (a) render the salience-react: stage the relevant character's noticing — a head turning toward the window, a sentence trailing off mid-hum, an unmotivated glance at the door; the reaction can be small but it must occur; or (b) drop the detail. **Do not surface and abandon.** A surfaced detail is a promise of attention. | The participants' resolved knowledge blocks for the relationships that establish salience (whose car / whose door / whose ordinary scent layer); typically already in working memory |
| S5 | **Repeated sentence-opener / subject-drop drift** | Sentence and paragraph openers across consecutive sentences within a beat AND across consecutive beats; especially subject-dropped fragments (a bare verb-headed clause with the actor implicit: *Set the bottle down. Came back to the working side. Took her three-count.*) | More than two consecutive sentences using the **same syntactic frame** — most commonly subject-drop on a transitive verb (*Verb-ed X. Verb-ed Y. Verb-ed Z.*), but also any other repeating opener shape (*Adv-comma + clause; bare-NP fragment; participial phrase + clause*) — used as a **default beat-mode** rather than a chosen one for a specific intensifying / staccato / interior-stripping effect. The surface texture has fallen into a fixed cadence the reader registers as a tic instead of as service to the moment. Compounds especially in long action-procedural beats where each action gets its own short clause; the *Set X. Took Y. Came back.* march becomes the default and the prose loses the register it was supposed to be in. | Reintroduce subjects on most sentences (*He set the bottle down. Came back to the working side and took her three-count.*); vary opener form within the paragraph (subject-led, subordinate-clause-led, occasional fragment) so the frame changes from sentence to sentence. **The fix is register-discipline:** subject-drop and short fragments are *tools* with specific effects (urgency, internal-stripping, staccato shock); used as defaults they flatten the prose. Restore the register the scene is in — if the moment is tender / unhurried / reflective, the sentences carry their subjects and breathe their full shape. Reserve the fragment-pile for moments that earn it. | [registers.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/registers.md) |
| S6 | **Elided audible speech** (the withheld line) | Any narration that **refers to** an utterance by a present character rather than delivering it — *"says something," "tells him what she wants," "whatever she said," "a line too low to carry," "murmurs something into his ear"* — and **any** reported / free-indirect construction standing in for a staged utterance, including one that carries the full substance (*"Carol turned the offer down flat: the price was the price, and he could take the smaller order or take nothing"*) | An utterance the POV anchor **received** referenced but not rendered **as quoted speech**. Content-completeness does not rescue a paraphrase: the words themselves are the thing owed, because they are what the player can quote back, hold the speaker to, and answer exactly. **Volume is not a defence** — a line murmured at the anchor's ear is the most audible speech in the scene, not the least; nor is content — crude, tedious, or awkward-to-write is not grounds to elide. Distinguish sharply from **inaudible** speech (out of earshot, behind a door, drowned by ambient, outside the anchor's comprehension set, below an active threshold gate) — that is legitimately absent, and is rendered as *the not-hearing*, which is a different sentence and a different beat | Put the line on the page as **quoted dialogue in the speaker's voice** — there is no reported-speech fallback. Summary survives for exactly one purpose: compressing a **span of time** in which no particular utterance is pointed at (*"they talked the whole way in"*); the instant such a passage reaches for a specific line (*"and somewhere in there she told him the terms"*), that line is staged action and gets quoted. If the anchor genuinely could not hear it, rewrite to render the not-hearing instead | [dialogue_format.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/dialogue_format.md) |
| S7 | **Reaction to an established fact as though it were news** (knowledge-state kin of S2) | A character's reaction beat — surprise, delight, outrage, an exclamation, a *wait, she's in it?* — aimed at a fact this scene already established **in front of that character**. Fires hardest on **group** beats, where the reaction is written for the room rather than per-person | The reaction treats as new something the character watched happen, was told, or took part in. Nothing false is asserted — which is exactly why it slips past the epistemic suite — but the room is responding to the wrong fact, and a reader who was paying attention is thrown out of the scene. The usual cause is **the reaction being written before its referent is checked:** the drafter knows the moment wants a detonation, writes the detonation, and attaches it to whatever is nearest, which turns out to be common knowledge (*"Carol's name is in the hat!"* — when the whole room watched Carol put it in). Compounds with the **cheer chorus**, where three or four characters exclaim in sequence and only the first one's referent was ever checked | Find the fact that is **actually new in this beat** and aim the reaction at that — it is nearly always present and usually better (not *that Carol is in the hat*, but *that the one who has been enforcing the rules all night is now subject to them*). If no such fact exists, the beat does not warrant a detonation: render the reaction at the size the event actually is. **Check every voice in a chorus separately** — each speaker's line needs its own grounded referent, not a share of the first one's | [player_intent_and_gating.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_intent_and_gating.md) (reading what the moment is actually about) |

**Read on fire (S1):** the **previous beat's** closing handoff — available from
the immediately prior turn already in context (no file read needed). The check
is comparative: a closer is a violation when it is the stock default *or* when
it repeats the shape of the one before it.

**Read on fire (S2):** the **current established physical state** of the object /
feature / character whose state the draft asserts **or presupposes** — available
from the prior narration already in context (no file read needed). The check is
comparative and **bidirectional**: a state is a violation both when reaching a
*new* one required a visible action the prose did not stage (the teleport) **and**
when a *superseded* one is treated as still current with no staged return to it
(the reversion) — **including when the stale state is carried only inside a
character's line of dialogue as a presupposition** (scan speech, not just
narration). Compare against the *latest* established state, never an earlier
remembered one.

**Read on fire (S3):** the anthology's declared setting (region, period,
cultural register) — typically a one-time read at scene start, then in working
memory. Re-read only if the user re-pins the setting mid-scene.

**Read on fire (S4):** the participants' relationships and knowledge blocks for
the surfaced detail's salience anchors — typically already in working memory
from STEP 2.

**Read on fire (S5):** the **previous N sentences** within the current beat and
the previous beat's closing paragraph — already in context from the in-flight
draft and the prior turn; no file read needed. The check is comparative and
local: count consecutive sentences sharing the same opener-frame; if the count
exceeds two without intentional effect, the row fires.

**Read on fire (S7):** what this scene has already put **in front of the
reacting character** — the prior beats already in context; no file read needed.
The check is one question asked of every reaction beat, and asked **per
speaker**: *what, specifically, is this character reacting to, and did they
already know it?* If the referent turns out to be common knowledge, the
reaction is aimed at the wrong fact — find the one that is genuinely new in
this beat and re-aim it there.

**Read on fire (S6):** the active anchor's **sense-availability state** for
hearing — from the working-memory block and `{{PLUGIN_ROOT}}/engines/prose-engine/scene/narration_modes.md`; already in
context, no file read needed. The check is a single question asked of every
utterance in the draft: *did the anchor receive these words?* If yes, they must
appear. The row does **not** fire on speech the anchor could not receive; it
fires on speech they could and the prose kept back.

---

## Post-edit rescan and the shared loop

A stylistic rewrite is subject to the **same post-edit coherence rescan** as an
epistemic one (the canonical description lives in the epistemic checklist's
"Post-edit coherence rescan" section). After this suite rewrites any span,
rescan the containing unit for coherence and purpose, then the gate re-runs
**both** suites. Repeat until the draft passes both clean.

**Cascade-guard.** If a handoff rewrite keeps spawning new breaks, stop
patching and **redraft the closing unit fresh from intent** — what was this
beat trying to hand off, and in what register? A clean fresh handoff beats a
tangled patched one.

---

## Extending this suite

This suite seeds with the repeated-handoff check because it is the most
frequent craft seam in turn-by-turn play. It is **open to extension** with
further stylistic-variance checks in the same row shape (`Check`, `Trigger
surface`, `Forbidden`, `Rewrite move`, `Rule source`). Candidate future rows,
not yet live (add only when a real, recurring seam justifies the false-fire
risk):

- **Bolted-on register break** beyond the handoff — a flat mechanical line
  dropped into a non-neutral register mid-beat (the craft rule is
  [registers.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/registers.md)).
- **Motif / image overuse** — the same sensory motif recycled until it reads as
  a tic rather than a thread.

A consuming game's override may also add craft tokens specific to its setting,
in the same shape. The override **extends a suite's scan list; it never
introduces a pass that runs after the gate.**
