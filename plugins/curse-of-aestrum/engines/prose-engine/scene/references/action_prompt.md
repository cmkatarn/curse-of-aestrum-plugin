# The Action Prompt — Handing Control Back to the Player

How a beat ends when control passes from the narrator to the player. The
counterpart to [player_input_channels.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_input_channels.md): that
file governs the player's *input*; this one governs the **invitation** that
elicits it. Loaded once per session.

> Working expectation. Treat as a strong guideline the consuming game may
> extend or override in its overrides file.

---

## Function vs. surface form

The handoff has one invariant **function**: the player must know,
unambiguously, that control has passed to them — and roughly what is being
asked of them right now.

Its **surface form is variable, and is never a fixed repeated token.** This is
the governing rule of the whole file: write a *fresh* handoff each beat, keyed
to what just happened. The generic *"What do you do?"* is one phrasing among
infinitely many — not a default, not a baseline, not a closing stamp to append
to every beat. A single prompt token, repeated turn after turn, reads as a
mechanical seam and breaks immersion as surely as a surfaced register tag does
— and it does so *however open the situation is.* An open situation licenses a
direct question; it never licenses the **same** direct question twice running.
The set of good handoffs is open-ended; write the one this moment wants.

---

## The invitation is written in-register, scaled to stakes

The handoff wears the same register as the beat it closes (see
[registers.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/registers.md)). It is part of the prose, not a fixture bolted
on after it:

- **neutral** — a plain, direct handoff — but still a *fresh* one each beat,
  keyed to what just happened, never a recycled stock question.
- **combat** — terse, immediate, keyed to the next decision. (See the
  combat constraint below — clarity is paramount; vary conservatively.)
- **intimate** — close, breath-held; the invitation can be the held moment
  itself. *"Her hand stays open between you, warm, waiting. Do you take it?"*
- **horror** — withholding; let the wrongness do the asking. End on the
  thing that is wrong and hold, rather than stamping a question on it.
- **investigation** — concrete, keyed to what's in front of the PC. *"The
  ledger, the locked drawer, the boot-scuff by the window — where do you
  look?"*
- **levity** — loose, conversational; the prompt can ride the banter.

Re-evaluate the form whenever the register or the stakes change, exactly as
register itself is re-evaluated.

---

## The closing need not be an explicit question

A spectrum of forms (illustrative, **not** a lookup list — the real set is
infinite; pick what the moment wants):

- **Direct question** — an open, direct ask when the situation is wide and
  nothing narrower fits. The generic open ask is one such phrasing — but it is
  not a default to fall back on, and asking it the same way beat after beat is
  exactly the repeated token this file forbids. Vary the wording and anchor it
  to the specific moment: *"How do you react?"* / *"Where to from here?"* /
  *"And you — what's your move?"*
- **Question narrowed to the moment** — *"Do you take the offered hand?"*
  When the beat has put one clear choice in front of the PC, name it.
- **A charged image the situation turns into an implicit prompt** — the beat
  ends on the live tension and waits, the question carried by the image
  rather than stated:
  > *The edge digs in. A thread of blood runs warm down your throat. He
  > watches your hands — ready to finish it the instant they move wrong.*

  No "what do you do?" is needed; the situation *is* the question.
- **Plain trailing handoff** — when the choice is obvious and a question
  would be noise, simply hand the floor back: *"The road forks here."* /
  *"She's waiting on your answer."*

---

## The handoff is gated like any other beat

Unlike the register (internal, never surfaced), the action prompt **is**
surfaced prose. So it runs through the epistemic gate POV-anchored, exactly
like the beat it closes:

- It may reference only what the PC could know — no hidden state, no
  off-screen fact, nothing in the PC's `unknown_flags`, smuggled in through
  the framing.
- It carries **no out-of-fiction or meta tag.** Do not label it (`[prompt]`,
  `[your turn]`) and do not emit a register tag with it — the same
  no-label rule as in [registers.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/registers.md).

---

## Variance never costs clarity *(the hard constraint)*

When the player could be uncertain whether it is their turn — async-text play,
a multi-character scene, combat — the invitation must carry an **unambiguous
turn signal** even while its phrasing varies. Naming the active character, a
clear question, or an evident hand-off beat all serve. If a flourish would
leave the player unsure they are up, drop the flourish. **Clarity wins over
texture, always.**

The implicit-prompt forms above (the charged image, the plain trailing
handoff) work only when it is *already obvious* the floor is the player's.
When it is not obvious, make it explicit.

---

## Anti-patterns

- **The repeated token.** The same closing phrasing beat after beat. The
  failure this file exists to prevent.
- **The bolted-on prompt.** Appending a generic stock closer to a beat
  that already implies the choice (the offered hand, the open door, the asked
  question). The beat already handed off; the stamp is redundant and breaks
  the spell.
- **The register break.** Dropping a flat, mechanical-sounding question into a
  scene whose register is anything but neutral — snapping the reader out of an
  intimate or dread-built moment to ask, tonelessly, what they do.

---

## Enforcement

This file is the **craft rule**; its enforcement lives at the gate. The
**stylistic-variance suite** ([stylistic_variance_checklist.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/stylistic_variance_checklist.md),
row S1) scans each drafted beat's handoff and fires on a stock or
repeated-token closer, funnelling it back for a fresh, in-register rewrite per
this file. The relationship mirrors `registers.md` and its gate enforcement:
the rule says *how* to write the handoff; the gate makes sure a draft that
ignored it does not post.

---

## Relationships

- Narrow the invitation toward what the player has been **reaching for**, per
  [player_intent_and_gating.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_intent_and_gating.md) — surface the
  choice they are already leaning into rather than a neutral open prompt.
- The invitation elicits the input channels in
  [player_input_channels.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_input_channels.md); phrasing a prompt as a
  question naturally invites a spoken or active reply, an open beat invites any
  channel.
