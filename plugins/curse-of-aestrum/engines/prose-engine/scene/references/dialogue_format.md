# Dialogue Format

The exchange format for NPC responses during in-character conversation.

---

## Format

```
**[Character Name]** — *[brief expression/action beat, optional]*

"[Spoken line or lines in character voice.]"
```

- **Action beats are optional.** Use when body language or expression
  meaningfully shapes the line. Keep them short.
- **Multiple NPCs in one response** get separate labeled blocks.
- **Do not label the user's character, but do render their spoken
  line.** The PC gets no `**Name** —` label block — in a two-party
  exchange the label is redundant. That is a rule about *labeling*, not
  a license to omit: the PC's spoken words still appear as quoted
  dialogue in the prose, in the PC's voice, the same as any other
  utterance in the scene. The player's plain-text input is not
  "already said and therefore skipped" — it is the utterance the beat
  renders, and the reader must see it land as spoken words. Dropping
  it, collapsing it into summary, or opening the response at the NPC's
  reaction leaves the exchange with a hole where the PC spoke. Render
  the line (lightly polished into voice per the plain-text rule in
  [player_input_channels.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_input_channels.md)), unlabeled,
  then the NPCs' labeled responses to it.

---

## Example

Player input: `The seal was broken before I ever touched it.`

```
"The seal was broken before I ever touched it," you say.

**Mara** — *a single eyebrow lifting*

"That is a remarkable claim. Repeat it for me, slowly."
```

The PC's line appears first, quoted and unlabeled; Mara's labeled
response follows. The response has something visible to answer.

---

## Every audible line reaches the page — no elided speech

The rule above binds the **player's** utterances. This one is its
counterpart and binds every **character's**: any line a present
character speaks within the perceptual reach of the POV anchor (or, in
`omniscient`, of any present character) is rendered **with its content
complete.** The narrator never references an utterance it does not
deliver.

**Forbidden — speech gestured at rather than rendered:**

- *"She says something into his ear that has nothing to do with the
  weather."*
- *"He tells her exactly what he wants."*
- *"Whatever she said, it landed."*
- *"A line too low to carry"* — when the anchor is the person it was
  carried to.
- Any summary that reports the **fact** of an utterance, or its
  **effect**, while its **content** stays off the page.

**Why this is not a style preference.** The prose is the reader's only
access to the fiction. An utterance the anchor heard and the prose
withheld is a fact the POV character now holds and the player does
not — which inverts the whole contract: the player is left knowing
*less* than the character they are playing, and cannot quote it back,
act on it, hold the speaker to it, or reference it three beats later.
It reads as atmosphere and functions as deleted information. Where the
epistemic suite guards against the reader being told **too much**, this
guards the opposite failure, and the cost is player agency rather than
immersion.

**The form is quoted dialogue, and reported speech is not a
substitute.** Content-completeness is not the bar — the *words* are.
A report that carries the whole substance is still a paraphrase in the
narrator's voice, and it costs the reader both things the utterance
actually carried: the speaker's own phrasing, and a line the player can
quote back exactly, hold someone to, or answer word for word. So this
is not good enough either:

> Carol turned the second offer down flat: the price was the price,
> and he could take the smaller order at it or take nothing.

The line goes on the page as spoken:

> **Carol** — *sliding the invoice back across the table*
>
> "The price is the price. Take the smaller order at it, or take
> nothing."

**The one thing summary is still for: a compressed span, not a
withheld line.** The rule binds every utterance in the beat's **live,
staged action**. It does not outlaw compressing a *passage of time* in
which no particular utterance is being pointed at — *"they talked the
whole way in, and gave as good as they got"* is a montage, not an
elision, because it indicates no specific line the reader is being kept
from. The moment such a passage reaches for a specific one — *"and
somewhere in there she told him what the arrangement was"* — that line
has become staged action and must be rendered. **The test is not how
much time the sentence covers; it is whether a particular utterance is
being referred to.**

**The one genuine exception is inaudibility, and it is rendered as
inaudibility.** Speech the anchor cannot receive — out of earshot,
behind a door, drowned by ambient, in a language outside their
comprehension set, below an active threshold gate (see
[{{PLUGIN_ROOT}}/engines/prose-engine/scene/narration_modes.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/narration_modes.md)) — does not go on the
page, and the beat renders **the not-hearing**: *"Bob says something to
her at the far end of the room; the crowd takes all of it."* That is
the sense-availability rule working. It is categorically different from
heard-and-withheld.

**Volume and discretion are not exceptions.** A line murmured at the
anchor's ear is the *most* audible speech in the scene, not the least;
the intimacy of the delivery is a reason to render it precisely, never
a licence to summarize it. Nor does content — a line being crude,
tedious, or awkward to write is not grounds to elide it.

**The test:** did the anchor receive the words? If yes, the words are
on the page.

---

## Attribution-shape conventions stay outside the spoken line

Speaker attribution belongs in the **labeled block** preceding the
line and in the surrounding narration — never inside the quoted
dialogue itself. The conventions that mark *who said what* — em-dash
+ name (*"— Carol"*), parenthetical speaker-tag (*"(Carol)"*),
trailing *"— she said"* clauses, dash-and-attribution at the end of a
quoted string — are bookkeeping. They read as stage-direction
regardless of authorial intent.

The slip arises most often when the writer wants a **vocative**
inside a long quoted line and reaches for the em-dash + name shape:

> "I have heard your concerns. Every one of them. The shipment.
> The escort. The seal. — Captain. None of these is the real
> issue."

The intent may have been a vocative addressing the Captain at the
list's end; the format reads as attribution of the listed concerns
to the Captain-as-speaker. Either reading places a
bookkeeping-shape inside the quoted speech, where it does not
belong.

The fix:

- **For a vocative**: place the addressee's name in a normal sentence
  position within the spoken line.
  > "I have heard your concerns, Captain. Every one of them. The
  > shipment. The escort. The seal. None of these is the real
  > issue."

  Or drop the vocative — if the speaker has been addressing the
  addressee throughout the labeled block, repeating the name may be
  unnecessary.
- **For attribution**: rely on the speaker label preceding the block
  and on the surrounding narration. The reader knows who is speaking;
  the quoted line does not need internal attribution.

The test: any string inside quoted dialogue that — if lifted out and
read on its own — would read as a speaker-tag or stage-direction is a
slip. Move it out of the quoted speech, or recast it as a
sentence-position element of the spoken line.

---

## When a subsystem is active

If the override activates a per-response subsystem (audio cue, etc.),
perform its update **before** delivering the response
text. The subsystem update is silent — do not mention it to the user.
