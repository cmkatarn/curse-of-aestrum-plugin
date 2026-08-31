# Correspondence — Asynchronous Written Exchange

A discipline reference loaded on demand when a scene runs in the
**`correspondence`** narration mode (see
[`{{PLUGIN_ROOT}}/engines/prose-engine/scene/narration_modes.md`]({{PLUGIN_ROOT}}/engines/prose-engine/scene/narration_modes.md)). Governs the **form** of
each written message and the **timing** of an exchange between parties
who are not in one another's presence.

Genre-neutral: the medium may be email, a letter, a note left on a
table, an in-world messaging system — anything sent at one moment and
read at another. "Email" is the common instance; the rules below use it
loosely and apply to any written, point-in-time artifact.

The discipline in one line: **a message is a subject and a body sent at
one point in time; replies relate a read time to a send time, the gap
between them is short, and the variable cost of correspondence is how
long a message waits to be read.**

---

## The message artifact

Each message has at least two parts:

- **Subject** — a short line naming what the message is about.
- **Body** — the message itself.

Nothing else is required, and there are **no other fields.** In
particular, a greeting ("Dear Bob," "Hi —") and a sign-off or
signature, *if the author uses them at all*, live **inside the body**.
The engine neither imposes nor strips them: some writers open and close
formally, some don't, and the presence or absence of a "hello" is
itself characterization. Do not add a salutation the author wouldn't
write, and do not lift one into a separate header.

The body is written in the author's **written register** (see
[`{{PLUGIN_ROOT}}/engines/prose-engine/scene/registers.md`]({{PLUGIN_ROOT}}/engines/prose-engine/scene/registers.md)), which may differ from how they
speak. The message **is the entire turn's output** — there is no
narration around it: no scene, no perceived environment, no action
beat, no description of the author writing it. Render the artifact and
nothing else.

---

## Point-in-time, no spans

Each message is **sent at a single point in time** — its **send time**,
T. A message has no duration; it is composed and sent at T and then
exists for whoever reads it later. An exchange is an **ordered sequence
of these point-in-time send events**, not a continuous span.

This is deliberately unlike a declared *event*
([time_and_events.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/time_and_events.md)), which carries a time, a
duration, and a catchup policy. A message has no duration to be early or
late *into* — it is sent, then read, and the only times that matter are
those two clock readings.

---

## Two clock stamps per reply

Every reply relates two moments:

- **read time** — when the replying author read the message they are
  answering.
- **send time** — when they sent the reply (its T).

The **opening message** of an exchange answers nothing and therefore
carries only a **send time.**

---

## Who supplies the clock stamps

- **Player-authored message.** The **player supplies the stamps** for
  their own character — the read time of the message they are answering
  and the send time of their reply (or, for an opening message, just the
  send time). The narrator does not invent these for a player-controlled
  author; if the player omits them, ask.

- **World-driven (engine-authored) message.** The **narrator determines
  them**: when the recipient **reads** the inbound message, and when
  they **send** their reply. Reason from plausibility — **time of day
  and time zone above all.** A message that lands at 03:00 in the
  recipient's local time is not read until they are plausibly awake; one
  that arrives in the middle of their working day may sit until a break;
  two correspondents in different time zones are reading and writing on
  different clocks. **State the determined read and send times** as part
  of the message so the exchange's sequence is explicit and resumable.

---

## The 30-minute read-to-send window

The interval between **reading** a received message and **sending** the
reply is assumed to be **at most 30 minutes.** That window absorbs
reading the message, composing the answer, and any real-time discussion
among co-authors of a joint reply.

The consequence: the variable latency in an exchange is the
**time-to-read** — how long a message waits unread before the recipient
opens it — *not* the read-to-send gap. When the narrator determines a
world-driven reply's timing, the **read time is the judgment call**
(driven by time of day and time zone, above); the **send time follows
within thirty minutes** of it.

---

## Co-authored messages — one writes for a group

A single author may write a message **on behalf of a group they speak
for** — two partners replying as one, a household answering together.
The message is authored from **one** author's seat, and **that author's
knowledge boundary governs** what the message may contain.

A co-author's *private* knowledge does **not** enter the message unless
the authoring party would actually have it — i.e., unless it was shared
between them. "Speaking for both" is a **voicing convention, not a
merging of what each knows.** If Alice writes for herself and Bob, the
message may contain what Alice knows (including whatever Bob has told
her) and not what Bob knows privately and never told her.

At the consuming layer's save time, note that *all* the represented
parties are participants in the exchange even though one held the pen —
but that is the consumer's record-keeping concern, not a drafting rule.

---

## The received message is an input channel

A reply may react **only to what the message it answers actually said**,
plus the author's own standing knowledge. It may not react to something
the author merely knows or suspects but was not told in the message, and
it may not pull in content from a different channel. The inbound message
is the **input**; the reply is **rendered against it**.

This is the same channel-attribution discipline that governs spoken and
overheard input in [player_input_channels.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_input_channels.md)
and [epistemic_discipline.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline.md), applied to
written correspondence: what a character may respond to is bounded by
the channel it actually arrived on. A fact that was never written into
the exchange is not available to a reply just because the author, out of
character, knows it.
