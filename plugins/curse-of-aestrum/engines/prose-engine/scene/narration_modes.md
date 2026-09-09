---
name: narration_modes
description: Narration modes for the scene skill — controls whose perceptual envelope the narrator is bound to, or, for the artifact modes, the form the turn's output takes. Orthogonal to register. Loaded by the skill on demand.
---

# Narration Modes

The narration mode governs **what the turn is allowed to put on the
page** — for most modes, by binding the narrator to a character's
perceptual envelope: which character's senses (if any) constrain what
the narration may describe. For the artifact modes it does so by fixing
the form the output takes instead (see *Two families of mode* below).
Orthogonal to register: register controls *how* the prose sounds;
narration mode controls *what the narrator is allowed to see, hear,
smell, taste, and touch on behalf of the reader* — and, where there is
no camera, what shape the turn's output has at all.

> **Register vs. narration mode.** *Register* (`{{PLUGIN_ROOT}}/engines/prose-engine/scene/registers.md`) and
> *narration mode* (this file) are orthogonal axes. Both apply at draft
> time. Register may switch mid-scene; narration mode is **locked at
> scene start.**

---

## Two families of mode

The modes divide into two families, and the division governs which of
this file's sub-rules apply to a given mode.

- **Camera modes** — `character_aligned`, `omniscient`, `split_anchor`.
  The turn's output is narrated prose, and the mode binds a
  **perceptual envelope**: whose senses (or none) constrain what the
  camera may render. The sense-availability sub-rule lives here.

- **Artifact modes** — `correspondence`, `dialog_only`, `screenplay`.
  The turn's output is not narrated prose at all but a **composed
  artifact** of a declared form — a written message, a spoken exchange,
  a page of screenplay. The mode binds the **form of what the turn
  emits**, and constrains perception only insofar as the form admits it
  (`correspondence` renders no environment; `dialog_only` renders only
  what is audible; `screenplay` renders only what a lens and a
  microphone could record).

Both families are locked at scene start, both are orthogonal to
register, and both leave the epistemic gate fully in force. What
differs is that a camera mode answers *what may the narrator see*, and
an artifact mode answers *what shape does the turn take.*

---

## Selection and lock

- The narration mode is selected once, at scene start, as one of the
  scene parameters in STEP 1.
- It is held for the entire duration of the scene. **No mid-scene
  switching.** A locked perceptual frame is a contract with the reader
  that cannot be rewritten mid-stream without breaking what the camera
  has already shown them it can see.
- To change narration mode mid-conversation: close the current scene
  via the save protocol and start a new one with the new mode declared
  at STEP 1.

---

## Default and override

This file declares a built-in default: **`character_aligned`.**

A consuming game's override may pin the default explicitly so that
future engine changes do not silently shift the consuming game. The
override pin supersedes the file-declared default.

The default is **silent** — STEP 1 does not prompt the user for a
narration mode if the default holds. The user may declare otherwise at
scene start or by explicit instruction:

> *"This scene is omniscient."*
> *"This scene is split-anchor between Alice and Bob."*

---

## Anchor declaration at scene start

The narration mode determines what (if any) character anchor must be
named at scene start:

| Mode | Anchor declaration |
|---|---|
| `character_aligned` | Implicit. Defaults to the PC. The user may name a different anchor (e.g., an NPC) at scene start. |
| `omniscient` | None. No anchor exists. |
| `split_anchor` | **Required.** The user names two or more anchors in their alternation order. Each section is labeled with its anchor. |
| `correspondence` | **Required.** Each message names its author. A message may be authored by one character on behalf of a group they speak for; the author's knowledge boundary governs (see [references/correspondence.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/correspondence.md)). |
| `dialog_only` | Implicit. Defaults to the PC. Governs **audibility only** — which lines reach the page — never description. The user may name a different anchor at scene start. |
| `screenplay` | None. No anchor exists. |

---

## The six modes

### `character_aligned`

The narrator's perceptual envelope is the named anchor character's.
The narration may describe only what the anchor can perceive through
their currently-available senses (see *Sense-availability sub-rule*
below).

This is the default and the most common mode. It produces close-third
prose anchored on a single character — typically the PC, but the user
may anchor on an NPC for scenes where the camera should sit inside a
non-player character (a private monologue, an NPC's perspective on the
party's arrival, a scene the PC is not present for).

**The anchor is named at scene start and held for the scene.** The
narration does not drift between characters' perceptions.

### `omniscient`

No anchor. The narrator's perceptual envelope is unconstrained — the
camera may render any **observable surface** in the scene, including
surfaces no character is currently perceiving.

The sense-availability sub-rule is **inactive as a rendering
constraint** under this mode. Its second job is not: what each
character perceives still follows the gates, and the camera's freedom
is exactly what lets it show a character failing to perceive something
the audience can see (see *Job 2 — perception as staged fact* below).

**Scope: external surfaces only.** The omniscient camera sees what an
ideally-positioned, sober eye and ear could register — bodies,
positions, gestures, weather, lighting, surfaces of objects, the
audible content of speech, the surfaces of expression (a smile, a
flinch, a stillness held). It does **not** see:

- **Interior states.** Thoughts, feelings, motives, fears, hopes,
  intentions, decisions, dread, relief, recognition — these are
  hidden state regardless of whose mind they belong to. Render the
  observable *tell* (a hand turned away, a smile resting like a tool,
  a stillness a body had to choose); never the named interior.
- **Intent, rehearsal, preparation, history.** A smile is *settled
  into place*, not *rehearsed into place*; a knock is *patient*, not
  *the patience of a person who has waited at thresholds before*.
  Imputing planning, training, or backstory to surfaces the camera
  observes is interior-state leakage dressed as description.
- **Future plans or expectations** of any character. (Same logic as
  the epistemic suite's row 7.)
- **Knowledge boundaries (epistemic suite) still bind.** The
  omniscient camera does not surface another character's hidden /
  factive state, does not name a person before any present character
  knows the name (see the epistemic suite's identity-before-introduction
  row), and does not contradict the saved-state grounding the
  grounding-family rows enforce. "Omniscient" widens the perceptual
  envelope; it does not relax the gate.

Useful for: prologue-style scene openings, ensemble beats where no
one character is central, scenes whose dramatic purpose requires the
reader to see surfaces the characters cannot — never to see *into*
them.

### `split_anchor`

Two or more character anchors, alternated by labeled section. Each
section's anchor's perceptual envelope governs that section. The
sense-availability sub-rule applies per-section, scoped to whichever
anchor is active.

Section labels must be visible to the reader (e.g., a short header
line naming the anchor, a stylistic break, or any convention the scene
establishes at its first transition).

Useful for: scenes with two simultaneously-present characters where
the dramatic interest is in *how each is reading the other*; scenes
that cut between two locations.

### `correspondence`

**No perceptual envelope.** The narrator renders no perceived
environment at all — no room, no senses, no action beats. The entire
output of a turn is a composed written **message** (a subject and a
body; see below). The parties are **not in one another's presence**;
they exchange messages across time, each sent at its own point in
time.

The mode's anchor is the **author of the current message.** Unlike
the sensory modes, that anchor governs not a camera but the message's
**voice and knowledge boundary** — the message is written in the
author's register and may contain only what the author knows. A
message may be authored by one character **on behalf of a group they
speak for** (two partners answering as one, a household replying
together); the single author's knowledge boundary still governs what
the message may contain (see *Co-authored messages* in
[references/correspondence.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/correspondence.md)).

The **form** of each message (subject + body; greetings and
signatures live inside the body, if at all) and the **timing** of the
exchange (each message is point-in-time; who supplies the read/send
clock stamps; how a world-driven reply's timing is determined from
time of day and time zone) are governed by
[references/correspondence.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/correspondence.md), loaded
on demand when this mode is active.

Useful for: scenes whose entire substance is the written exchange —
organizing or negotiating something by letter, email, or message —
with no in-person beat at all.

### `dialog_only`

**The auditory channel and nothing else.** The turn's entire output is
the spoken exchange. Three things reach the page and no fourth:

1. **Who spoke** — the speaker label.
2. **What they said** — the line, quoted, complete.
3. **How they said it** — the *audible* manner of the utterance.

There is no narrated environment: no room, no weather, no light, no
time of day, no furniture, no distance, no movement, no gesture, no
body language, no interior state. The reader hears the scene and does
not see it.

The anchor is implicit (the PC by default) and does **one** job:
it fixes **audibility** — which lines were within earshot and therefore
reach the page. It does not license description. The
sense-availability sub-rule applies to this mode **on the auditory
channel only** as a rendering constraint (see its Job 1 table below).
Its second job is unaffected: the characters' other senses are still
live world state, still shape what they know and how they answer, and
simply have no channel through which to reach the page except as
someone says so.

**The delivery beat.** The optional action-beat slot in
[references/dialogue_format.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/dialogue_format.md) narrows,
under this mode, to a **delivery beat**: the audible manner of the
utterance and nothing else. Volume, pace, a pause taken before the
line, a break or catch in the voice, a laugh riding under it, an accent
thickening, a shift into another language, a line delivered flat.

**The test: could it be heard with the eyes closed?** If not, it is not
a delivery beat. *A hand set flat on a table*, *a look away*, *a step
closer* — all out, however much they would sharpen the line. The
delivery beat is optional and is often best omitted; a line that
carries its own delivery does not need to be told how it sounded.

**Audible manner, not named interior.** The omniscient scope rule
applies with full force to the delivery beat, which is the one place in
this mode where interior state can leak. Render the sound, not its
meaning: *a laugh under the words*, not *bitterly*; *a half-beat before
the answer*, not *reluctantly*. A delivery beat that names what the
speaker felt is the interior-state leak of the `omniscient` scope rule
arriving through the only door this mode leaves open.

**The one environmental exception: deixis.** When a spoken line is
unintelligible without its referent — a deictic (*"this one," "that,"
"here," "again"*) pointing at something the words alone do not supply —
the referent may be carried in the **minimum** words needed to make the
line parse, and only there. This is the whole of the
"relevant-to-what-is-being-said" carve-out: it licenses the **referent
of a line**, never the room around it, and never a detail that merely
enriches. If the exchange can be followed without it, it does not go on
the page.

**Inaudibility is still rendered as inaudibility.** The
every-audible-line rule in `dialogue_format.md` binds unchanged: speech
the anchor received goes on the page complete, and speech the anchor
could **not** receive is rendered as the not-hearing — in the same
stripped register, as briefly as the fact can be stated.

**The handoff lives in the dialogue.** There is no prose in which to
write an in-register invitation, so the invitation is carried by the
**speech itself** — a question, a line that plainly waits, a marked
pause. This narrows
[references/action_prompt.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/action_prompt.md) rather than
suspending it: the invariant function (the player knows unambiguously
that control has passed) still binds; only the available surface form
is confined to what someone can say. Never append an out-of-fiction
prompt to close the beat.

**The PC's line is still rendered** — unlabeled, per `dialogue_format.md`.
Under this mode that rule is load-bearing rather than stylistic: the
spoken line is the only thing on the page, so dropping the PC's leaves
the exchange with a visible hole.

Useful for: interrogations, negotiations, and confrontations whose
whole substance is verbal; exchanges over a channel that carries voice
and nothing else (a phone, a radio, a door between the parties); scenes
written to be heard.

### `screenplay`

**No anchor; the camera is a camera.** The turn's output is a page of
screenplay — scene headings, action, character cues, dialogue — written
so it could be handed to a crew and shot as part of a larger picture.

The perceptual scope is **identical to `omniscient`**: observable
surfaces only, no interiors. Screenplay convention already enforces
exactly this, which is why the two fit together without friction — an
action line can describe only what a lens and a microphone could
record. **The camera cannot photograph a thought.** Every prohibition
in the `omniscient` scope rule above (interior states; intent,
rehearsal, preparation, history; future plans; the epistemic suite's
knowledge boundaries) applies here word for word.

**Sense availability is inactive only as a rendering constraint.** The
camera is not bound to anyone's senses, so nothing gates what the page
may show. What each character *perceives* is untouched by that, still
follows the gates, and is frequently the load-bearing fact of the beat:
that one character does not hear another come in, that a character
keeps talking to a room that has stopped listening. This is not a
second-order concern in this mode — it is the format's native
material, because non-perception is **blocking**, and blocking is what
a screenplay is for. Stage it in the action lines (see *Perception and
non-perception are blocking* in
[references/screenplay.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/screenplay.md)), and see *Job 2 —
perception as staged fact* below.

**The epistemic gate binds, and the format accommodates it natively.**
A character whose name is not yet established in the fiction is cued
descriptively (`MAN IN THE GREY COAT`) and switches to the name once
the page has earned it — which is standard screenplay practice, not a
concession the engine invented. The identity-before-introduction row
and the format's own convention want the same thing.

**Register still applies, on a short leash.** Action lines are lean by
convention. Register modulates what the camera is pointed at, how long
it holds, and the rhythm of the action lines — it never licenses them
to carry prose interiority.

**`dialogue_format.md`'s labeling convention is superseded.** That
file's rule that the PC gets no speaker label is a prose-format
convention; screenplay format cues **every** speaker, PC included. The
rule it does *not* supersede is the content rule underneath: the PC's
line still reaches the page, and every audible line is rendered
complete rather than summarized in an action line.

The **format** — scene headings, action lines, cues, parentheticals,
extensions, transitions, and the disciplines that keep the page
shootable — is governed by
[references/screenplay.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/screenplay.md), loaded on demand
when this mode is active.

Useful for: scenes authored as production material; scenes whose
interest is blocking, staging, and cutting rather than interiority; a
scene meant to sit inside a larger film or episode.

---

## Sense-availability sub-rule

### The sub-rule does two jobs — only one of them is mode-scoped

Sense availability is used twice, for different purposes, and the modes
switch **one** of them off and never the other.

**Job 1 — the rendering constraint.** Sense availability bounds *what
the narrator may put on the page*: the camera describes environment
only through the active anchor's currently-available senses. This job
is **mode-scoped**, per the table below.

**Job 2 — perception as staged fact.** Sense availability determines
*what each character in the scene actually perceives*, and therefore
what they know, how they behave, and what they can react to. This job
is **active in every mode, without exception.** A gated sense is world
state, not a camera setting. A character who did not hear someone come
in did not hear them, whatever the narration is free to describe — and
that non-perception is often the most important thing in the beat.

The two jobs are easy to conflate because in `character_aligned` they
collapse into one: the anchor's senses bound both the character and the
camera at once. In the modes where the camera is not a character's
senses, they come apart, and only Job 1 goes quiet.

### Job 1 — where the rendering constraint applies

| Mode | Rendering constraint |
|---|---|
| `character_aligned` | **In full.** The anchor's available senses bound the description. |
| `split_anchor` | **In full,** per section, scoped to whichever anchor is active. |
| `dialog_only` | **Auditory channel only.** The anchor exists solely to fix audibility, so the hearing gates below (deafness, magical silence, unconsciousness; the sleep, earplug, and loud-ambient threshold gates) determine which lines reach the page and which are rendered as the not-hearing. The other senses have no channel to reach the page through, so their gates are moot *for rendering* — see Job 2. |
| `omniscient` | **Inactive.** The camera is unconstrained; a lens and a microphone are not a character's senses. |
| `screenplay` | **Inactive,** for the same reason. |
| `correspondence` | **Inactive.** There is no perceived environment to render at all. |

### Job 2 — perception as staged fact, in every mode

What a character perceives still follows the gates below in **all six
modes.** Three consequences, and they bind regardless of what the
camera is allowed to show:

- **A character cannot react to what they did not perceive.** This is
  the sense-gate feeding the epistemic gate's knowledge boundaries: a
  gated sense is one of the ordinary ways a character fails to acquire
  a fact. A character who responds to a line they could not hear is a
  knowledge-boundary violation whose cause is a missed sense gate.
- **Non-perception is stageable, and often the point.** *Character A
  does not see Character B come in; Character B is looking straight at
  them* is a beat, not an omission — and in the anchorless modes the
  camera can show **both** halves of it, which is precisely the
  dramatic irony those modes exist to produce. Stage the failure to
  register: a head that does not turn, a conversation that continues,
  a hand that goes on writing.
- **The gate lifting is an event.** When a character finally registers
  the thing — the wake, the turn, the sentence stopping mid-word — that
  transition is staged the same way in an anchorless mode as it is
  narrated in an anchored one.

The rest of this sub-rule — the senses, the gate types, the tables, the
re-opening rule, attention, dreams — describes the gates themselves and
so feeds **both** jobs.

### The rendering rule

The narrator may describe environment only through the active anchor's
**currently-available** senses. When a sense is gated, the narration
must lean on the remaining channels until the gate lifts.

### The senses

Sight, hearing, smell, taste, touch / proprioception.

### Gate types

There are two kinds of gate.

**Full gate** — the sense is unavailable at any signal strength.

| Sense | Full gates |
|---|---|
| Sight | Lid closed; blindfold; hood; total darkness; blindness; unconsciousness |
| Hearing | Deafness; magical silence; unconsciousness |
| Smell | Anosmia (innate or condition); sealed airway; unconsciousness |
| Taste | Chemical block; numbed mouth. (Taste is not normally active outside eating / drinking / kissing; gating matters only when one of those is in play.) |
| Touch | Anesthesia; complete numbness in a region; unconsciousness |

**Threshold gate** — the sense is available only above an intensity
threshold. Below the threshold the sense is effectively gated; above
the threshold the sense registers and (for some gates) the registering
also ends the gated state.

| Gate | Effect |
|---|---|
| Sleep | Sight: full gate (lids closed, no visual processing). Hearing, smell, touch: threshold-gated — loud noise, strong smell, firm touch / pain *registers* and *wakes* the sleeper. Background ambient does not register. |
| Heavy intoxication / drugged state | High thresholds across one or more senses, often without the waking-effect — the anchor may register a strong signal but not act on it. |
| Earplugs / sealed-but-not-deafened ears | Quiet sounds gated; loud ones not. |
| Strong masking smell (smoke, perfume, char) | Raises the threshold for noticing a different smell underneath. |
| Loud ambient (crowd, storm, machinery) | Raises the threshold for noticing specific sounds within or beneath it. |

### The rule

For each gated sense on the active anchor, the narrator must not
describe environment through that channel from the anchor's
perspective **while it is gated.** For threshold gates, "while gated"
means at signal strengths below the threshold. Above-threshold signals
are rendered, and (when the gate state is one that wakes, such as
sleep) the rendering includes the wake / alert event as part of the
beat.

### Re-opening

When a gate lifts — a full gate ends, a threshold state is exited, the
anchor wakes or sobers — the narrator may resume describing through
the affected channels. The transition is often a natural beat for a
brief catch-up paragraph if the scene needs it.

### Not a gate

**Attention.** A character may not be paying attention to a thing they
can in principle perceive. This is **not** a sense-gate — but it still
bounds what the anchor perceives, and it bounds it **in both
directions:**

- A signal that **would land in peripheral awareness** may be rendered
  as ambient even while the anchor is focused elsewhere; the anchor's
  failure to *register* it is then its own narrative beat.
- A signal that would **not break through** the anchor's reallocated
  attention is, for that stretch, effectively below threshold and is
  **not the anchor's to perceive** — the narrator must not render it as
  something the anchor caught. When attention is heavily reallocated
  under strong competing demand — driving through a storm, severe pain,
  a task that swallows the whole focus — only signals strong enough to
  break that focus are perceived (and the narrator renders the break);
  subtler ones pass unregistered and stay off the anchor's channel.

This includes attention failure under strong competing input — *a
character in severe pain feels other tactile signals on the body, but
the brain ignores them; a hand on the shoulder lands and goes
unnoticed; a raised voice or a firm shake breaks the focus, and the
narrator renders the break.* The senses remain available; the
character's attention is what has been reallocated.

**Concealed signals compound this.** A tell another character is
*actively suppressing* — a micro-expression they catch and school, an
impulse checked before it shows, a hand that starts to move and is set
back down — sits below the perception threshold even at full attention,
and is doubly out of reach when the anchor's attention is elsewhere.
The narrator must not render such a suppressed signal as something the
anchor perceived (*e.g. "you watch them catch it"* right as they
school a tell). Doing so breaks the perceptual envelope **and** leaks
the other character's concealed interior state onto the page through a
camera that could not have seen it — the knowledge-boundary suite's
row-1 concern, reached by a perceptual back door. If the other
character successfully hides it, the anchor — and so the reader — does
not get it; it stays that character's alone, surfaced only in their own
POV or overlay.

### Dreams

A sleeping anchor may have internal perceptual content. The dream
counts as the anchor's perception for narration purposes: the narrator
may render the dream as the anchor experiences it, unconstrained by
the anchor's waking sense-gates (eyes closed under the lid still
"see" in the dream).

The anchor's waking sense-gates continue to apply to the **waking
environment.** A waking-environment signal above the sleeping anchor's
threshold (a noise, a smell, a touch) is rendered and, where
appropriate, triggers the wake event — the dream collapses, the waking
environment floods back in, and the gate state ends per the *Re-opening*
rule above.

---

## Out of scope

This file describes mundane human sensory channels (sight, hearing,
smell, taste, touch / proprioception) and their full and threshold
gates. Consuming games may extend an anchor's perceptual envelope
through their own rules — magical senses, supernatural attunements,
device-mediated perception. Those extensions are declared in the
consuming game's mechanics layer and apply on top of the rules here.

---

## Drafting-constraint placement

The narration mode is a **drafting constraint**, applied while
composing each response — alongside register, the override's other
drafting constraints, and the per-character knowledge boundaries from
STEP 2. The epistemic-pass gate runs *after* drafting and does not have
a separate row for narration-mode violations; the constraint is
enforced at draft time. Narration-mode violations (the narrator
describing through a gated sense, the narrator rendering a signal below
the anchor's attention threshold — a subtle or actively-concealed tell
the anchor's reallocated focus could not catch, per the *Attention*
sub-rule — a `character_aligned` scene drifting between characters'
perceptions, an unannounced section break in `split_anchor`, a
`correspondence` beat rendering perceived environment or action around
the message instead of the message alone, a `dialog_only` beat rendering
anything the eyes-closed test excludes — scenery, gesture, movement, a
delivery beat naming an interior — or a `screenplay` beat carrying an
unfilmable in an action line) are caught in the same pass that catches
other drafting-constraint failures.
