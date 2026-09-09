# Screenplay — Shootable Page Format

A discipline reference loaded on demand when a scene runs in the
**`screenplay`** narration mode (see
[{{PLUGIN_ROOT}}/engines/prose-engine/scene/narration_modes.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/narration_modes.md)). Governs the **elements**
of the page and the **disciplines** that keep it shootable.

Genre-neutral. The target is a page a crew could work from as part of a
larger picture — not a prose scene with the descriptions taken out.

The discipline in one line: **an action line may contain only what a
lens and a microphone could record, and every element on the page is
one of six things.**

---

## The perceptual contract

This mode's camera has the same scope as `omniscient`: **observable
surfaces only.** The format enforces it natively — you cannot
photograph a thought — which is why screenplay is a natural fit for the
engine's interior-state discipline rather than a fight with it.

**The unfilmable test.** For every clause in an action line: *could a
camera and a microphone, well placed, record this?* If not, it does not
go on the page.

Unfilmable, and therefore forbidden:

- *He remembers the last time he stood here.*
- *She realizes she has been lied to.*
- *He has been waiting for this his whole life.*
- *She decides not to answer.*
- *He is a man who has learned not to hope.*
- *The room feels wrong.*

Filmable, and therefore the rewrite move — render the **tell**, not the
state behind it:

- *He stops in the doorway. Doesn't go in.*
- *She reads the line again. Sets the page down.*
- *He looks at the door. Looks at his hands. Looks at the door.*
- *She opens her mouth. Closes it.*

This is the same rewrite the `omniscient` scope rule asks for, arriving
with the format's own vocabulary. The prohibition on **intent,
rehearsal, preparation, and history** carries over unchanged: *a smile
settles into place*, never *a rehearsed smile*.

---

## Perception and non-perception are blocking

The camera is not bound to any character's senses. **The characters
still are.** Sense availability
([{{PLUGIN_ROOT}}/engines/prose-engine/scene/narration_modes.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/narration_modes.md), *Job 2 — perception as
staged fact*) governs what each person in the scene actually registers,
in this mode exactly as in every other, and that governance does not
weaken just because the page is free to show everything.

In this format it is not a constraint to work around — it is the
material. A screenplay's whole engine of tension is the gap between
what the audience can see and what a character has registered, and that
gap is **stageable**: unlike a prose scene bound to one anchor, the
page can show the thing *and* the person not noticing it, in the same
breath.

**Stage the non-perception; do not merely omit it.**

Forbidden — the interior report:

- *He doesn't notice her come in.*
- *She is unaware he is behind her.*
- *He can't hear them over the machinery.*

These are unfilmable in the ordinary way: *not noticing* and *being
unaware* are states, not images. Render the observable behavior that
constitutes the non-perception:

```
CAROL comes through the door behind him. Sets her bag down.

BOB doesn't turn. Keeps writing.
```

```
The press hammers. ALICE says something to him across it.

BOB nods along, three beats behind, answering a question
she didn't ask.
```

**The consequences that still bind:**

- **A character cannot react to what they did not perceive.** A gated
  sense is one of the ordinary ways a character fails to acquire a
  fact; a character answering a line they could not hear over the
  machinery is a knowledge-boundary violation, and the format gives it
  nowhere to hide.
- **A gate lifting is an event, and it is a *cut*.** The turn, the head
  coming up, the sentence stopping mid-word — that is the beat the
  scene has been building, and it wants its own action line rather than
  a clause tacked onto the previous one.
- **Blocking must make the perception plausible.** Where people are
  standing, what is between them, which way they face, how loud the
  room is — these are the reasons a character does or does not
  register something, and this format is the one that has to put them
  on the page in order to be shot. Establish the geometry in an action
  line before the non-perception depends on it.

`(O.S.)` is the format's own tool here: a speaker present but out of
frame is frequently a speaker some character on screen has not yet
located.

---

## The six elements

Everything on the page is one of these. Nothing else is an element.

### 1. Scene heading (slug line)

```
INT. KITCHEN - NIGHT
EXT. LOADING DOCK - DAY
```

- `INT.` or `EXT.` (or `INT./EXT.` for a vehicle or a threshold).
- A location name in CAPS.
- A time-of-day tag after a hyphen.

**Permitted time tags only:** `DAY`, `NIGHT`, `DAWN`, `DUSK`,
`MORNING`, `EVENING`, `CONTINUOUS`, `LATER`, `MOMENTS LATER`,
`SAME TIME`. A slug line **never** carries a clock time or a
project-internal index — a day number, a session count, an internal
scene id. Those are infrastructure tokens and the gate catches them
here exactly as it catches them anywhere else. The time tag is a
lighting instruction, not a timestamp.

**A new slug is required** when the camera moves to a new place, or
when time is discontinuous. It is **not** required for a new beat in
the same place at the same time; that is what the action lines are for.

Sub-headers (`CLOSET`, `BACK OF THE HOUSE`) may be used on their own
line for a move within a location that does not warrant a full slug.

### 2. Action

Prose paragraphs, **present tense, active voice**, describing what is
seen and heard.

- Short paragraphs. Three or four lines each at the outside; white
  space is the format's rhythm, and a wall of action reads as
  unshootable.
- A character's **first appearance** puts their name in CAPS —
  `A MAN IN A GREY COAT, forty, sets a case on the table.` Subsequent
  mentions are in normal case.
- Sound cues may be CAPS for emphasis: *A door SLAMS somewhere below.*
  Use sparingly; every capitalization spends emphasis.
- **No dialogue inside action.** A line someone speaks is a dialogue
  element, always.

### 3. Character cue

The speaker's name, in CAPS, on its own line above their dialogue.

**Naming and the epistemic gate.** The cue names a character by what
the fiction has established, not by what the engine knows. Before a
name is established on the page, the cue is descriptive and consistent:

```
MAN IN THE GREY COAT
```

Once the name is established in the fiction, the cue switches to it —
and the switch is standard practice, not a compromise the engine
invented. The **cue stays stable within a scene** once chosen, so the
page reads cleanly; a name established mid-scene switches at the point
of establishment and holds from there.

**Extensions** go in parentheses after the cue and mean specific
things:

| Extension | Meaning |
|---|---|
| `(V.O.)` | Voice-over — the source is not in the scene's physical space at all (a recording, a letter read aloud, a narrator). |
| `(O.S.)` | Off-screen — the speaker is present in the scene's space but outside frame (through a door, from the next room). |
| `(CONT'D)` | The same character continues speaking after an intervening action line. |

**`(V.O.)` is not a back door for interior state.** A voice-over is
another character's audible speech, displaced in space or time — not a
channel for narrating what someone is thinking. Interior monologue
delivered as V.O. is the `omniscient` interior-state prohibition evaded
by format, and it is forbidden unless the consuming game has
established an actual narrating character whose voice the picture uses.

### 4. Dialogue

The spoken line, beneath its cue.

The **content-completeness rule** from
[dialogue_format.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/dialogue_format.md) binds unchanged and is easy to
violate here, because an action line makes summarizing speech feel
natural. It is not:

**Forbidden:**

```
They argue about the money.
```

**Required:**

```
                    CAROL
          The price is the price. Take the
          smaller order at it, or take nothing.
```

An action line may describe *that* people are talking when no
particular utterance is being pointed at (`The room is loud with
argument.` as an establishing beat). The moment a specific line is
referred to, it is dialogue and must be rendered.

### 5. Parenthetical

A short direction in parentheses between the cue and the line.

```
                    CAROL
              (not looking up)
          The price is the price.
```

**Use rarely.** A parenthetical earns its place only when the delivery
is **not inferable** from the line and its context — usually because
the line means the opposite of its surface, or is directed at someone
other than the obvious listener.

- **Never an interior:** `(bitterly)`, `(hopeful)`, `(realizing)` are
  unfilmable directions, forbidden by the same test as action lines.
  `(quietly)`, `(overlapping)`, `(to Bob)`, `(in Language A)` are
  filmable and permitted.
- **Never an action:** a character crossing the room is an action line,
  not a parenthetical.
- Actors and directors resent them; the page is usually better without.

### 6. Transition

```
CUT TO:
SMASH CUT TO:
DISSOLVE TO:
MATCH CUT TO:
```

**Use rarely.** A cut between scenes is implied by the next slug line;
writing `CUT TO:` before every one is noise. Reach for a transition
only when the *kind* of cut is the story point.

---

## Camera direction — spec discipline

Default to **spec format: no shot calls.** The director and the DP own
the shot list, and a page thick with `ANGLE ON` and `PUSH IN` reads as
an author doing someone else's job.

Direct the camera only when the story beat is **unreadable without
it** — most often when the point of the beat is what the audience is
allowed to see and when: `ANGLE ON`, `CLOSE ON`, `PUSH IN`, `PAN TO`,
`REVEAL:`, `OFF her look`. If the beat survives without the call, cut
the call.

The same restraint governs `INTERCUT` (cross-cut simultaneous action),
`SUPER:` (on-screen text), and `MONTAGE` / `SERIES OF SHOTS` (a
compressed passage of time — see
[time_and_events.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/time_and_events.md) for how much elapsed time a
compressed passage may be treated as covering).

---

## Layout in a plain-text medium

The engine emits into a text channel, not onto a page with industry
margins. Use the following convention, which is unambiguous, readable
in a chat, and **compatible with Fountain** — so the output can be
pasted into a screenwriting application and formatted correctly:

- Scene headings, character cues, and transitions on their own lines,
  in CAPS.
- Transitions right-aligned in spirit; a trailing `TO:` is enough to
  mark them.
- Action as ordinary paragraphs.
- Parentheticals on their own line, in parentheses, directly under the
  cue.
- A blank line between every element.

Indentation of cues and dialogue is **optional** — helpful where the
channel renders it stably, harmless to omit. An element's identity is
carried by CAPS, position, and blank lines, not by column position.
Do not wrap the page in a code fence unless the user asks; the
screenplay is the scene's prose, not a code sample.

---

## Interactive play under this format

Screenplay mode is still a played scene, and three things adapt:

- **The PC is cued like anyone else.** `{{PLUGIN_ROOT}}/engines/prose-engine/scene/references/dialogue_format.md`'s
  no-label-for-the-PC rule is a prose convention and does not survive
  into this format. The PC gets a cue and a dialogue element.

- **The player's plain-text input becomes the PC's dialogue,** lightly
  polished into voice per
  [player_input_channels.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_input_channels.md), rendered under
  the PC's cue. It is not skipped as already-said, and it is not
  compressed into an action line.

- **The handoff is the page running out.** There is no prose in which
  to write an in-register invitation, so the beat ends on the action
  line or the cue that leaves the PC's next move unwritten — a question
  landing on them, an action line that puts the decision in front of
  them and stops. This narrows
  [action_prompt.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/action_prompt.md) rather than suspending it: the
  invariant function (the player knows control has passed) binds; the
  surface form is confined to what a page can carry. **Never append an
  out-of-fiction prompt** below the last element.

Keep beats short. A played turn is a fragment of a scene, not a whole
one — a slug (when the location changes), a few action lines, and the
exchange that gets to the handoff.

---

## What this mode does not do

- **No prose interiority**, in any element, by any route — action line,
  parenthetical, or V.O.
- **No scene-setter header.** The slug line *is* the establishment, and
  it is in-fiction page content. An out-of-fiction summary above the
  page is the same violation it is in every other mode (see
  [{{PLUGIN_ROOT}}/engines/prose-engine/scene/core.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/core.md), STEP 3).
- **No register tag, no mode label, no element key.** The format is the
  output; nothing annotates it.
