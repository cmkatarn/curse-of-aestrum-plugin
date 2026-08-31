---
name: narration_modes
description: Narration modes for the scene skill — controls whose perceptual envelope the narrator is bound to. Orthogonal to register. Loaded by the skill on demand.
---

# Narration Modes

The narration mode governs **whose perceptual envelope the narrator is
bound to** — which character's senses (if any) constrain what the
narration may describe. Orthogonal to register: register controls *how*
the prose sounds; narration mode controls *what the narrator is allowed
to see, hear, smell, taste, and touch on behalf of the reader.*

> **Register vs. narration mode.** *Register* (`{{PLUGIN_ROOT}}/engines/prose-engine/scene/registers.md`) and
> *narration mode* (this file) are orthogonal axes. Both apply at draft
> time. Register may switch mid-scene; narration mode is **locked at
> scene start.**

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

---

## The four modes

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

The sense-availability sub-rule is **inactive** under this mode.

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

---

## Sense-availability sub-rule

Applies to **`character_aligned`** and **`split_anchor`**. Inactive
under `omniscient` and `correspondence` (neither binds the narration
to a perceiving anchor — `omniscient` because the camera is
unconstrained, `correspondence` because there is no perceived
environment to render at all).

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
the message instead of the message alone) are caught in the same pass
that catches other drafting-constraint failures.
