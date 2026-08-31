# Time and Events — Declared Times, Durations, and Catchup

A discipline reference loaded on demand. Governs how the narrator
interprets declared times in story data and how players who arrive
early, on time, late-during, or late-after relate to those events.

The discipline in one line: **a declared time is exact, and an event
is a thing that starts at its declared time, runs for its declared
duration, and is over when that duration ends.** Late arrival is a
real cost; the narrator does not paper over it.

It also governs **undeclared elapse** — when no event is declared, how
the narrator estimates the in-world time a stretch of ordinary beats
consumed. That discipline in one line: **elapsed time follows the
depicted action at a natural pace, never the word count, beat count, or
register.** The final two sections cover it.

This file is loaded by the scene skill's thin shell when timed events
appear in story data. The consuming game's override may extend the
schema (additional fields, setting-specific event types) but should not
loosen the discipline.

---

## The schema

Every declared event in story data carries three fields:

- **`time:`** the exact moment the event begins (T). A specific clock
  time, a named bell, a calendar moment, or an in-fiction trigger
  ("at the next reset," "when the sun crosses the ridge"). T is
  exact unless a tolerance is declared in the field itself
  (`time: 7 AM ± 15 min`). Bare values are not approximate.

- **`duration:`** the time the event takes to play out (D). May be
  `instant` (the bell tolls; the assassin's blade lands; the door
  closes), a clock interval (`~5 minutes`, `~1 hour`), or a phase
  description (`until the petitioners disperse`, `until the prayer
  is complete`). Default if omitted: treat as `instant` and flag the
  omission to the author when noticed.

- **`catchup:`** how a player who arrives mid-event relates to what
  they missed. One of:
  - **`full`** — the missed content is recoverable in fiction through
    normal effort. The player can listen to the rest, ask a neighbor,
    catch a recap from a clerk or bystander after the fact. The
    narrator does *not* summarize the missed content; the player
    surfaces it in character.
  - **`partial`** — only some of the missed content is recoverable.
    The author declares which parts in a brief note (e.g.,
    `catchup: partial — the verdict is recoverable; the testimony is
    not`). The narrator treats the unrecoverable parts as gone.
  - **`none`** — the missed content cannot be recovered in fiction.
    The moment occurred at T and cannot be re-entered. The player can
    investigate *that* it happened — through evidence, witness
    accounts, aftermath — but cannot re-enter the moment itself.

Default if `catchup` is omitted: **`none`**. The discipline favors
exact declared times being load-bearing; ambiguous-by-omission events
should err toward closing the door, not propping it open.

---

## How the narrator applies the schema

For each declared event the player relates to, identify their arrival
time T' relative to the event's T and D.

### T' < T — arrived early

The event has not begun. Render the room/scene as it is *before* the
event — the empty audience hall, the gathering crowd, the speaker not
yet on the dais. The player is present, waiting, and may use the
waiting time as ordinary scene material.

### T' = T — present at the start

Full access. Render the event from its first beat.

### T < T' < T + D — arrived mid-event

The event is in progress. Render exactly what is happening at T' —
the line the speaker is mid-sentence on, the move the duelist is
mid-strike on, the prayer the supplicant is mid-phrase on. No
narrator summary of what came before. The player picks up from
wherever the event actually is.

What the player can do with the missed content depends on `catchup`:

- **`catchup: full`** — they can listen to the rest, watch the room,
  and ask in character after the event ends. The recovery costs an
  in-fiction beat (a question to a neighbor, a clerk pulled aside, a
  follow-up to the speaker) but is reliable.
- **`catchup: partial`** — they can recover what the author declared
  as recoverable; the rest is gone.
- **`catchup: none`** — the missed content is gone. The player can
  investigate aftermath but cannot recover the moment.

In every case the player's late arrival is **visible state** in the
room. Other characters notice; reactions are honest. The narrator
does not silently smooth the lateness away.

### T' ≥ T + D — arrived after the event ended

The event is over. Render the aftermath — the dispersing crowd, the
closed door, the body, the silence after the bell. The event itself
is no longer accessible at any tier. Catchup applies to *what the
player can still learn about it*, on the same `full / partial / none`
gradient, surfaced through aftermath rather than mid-event presence.

---

## What `catchup: full` does *not* mean

`catchup: full` does **not** mean the narrator summarizes what the
player missed in a meta aside. That breaks frame.

It also does **not** mean characters in the world re-perform the
event for the player's benefit. The speaker does not restart the
speech; the duelist does not restart the duel; the prayer is not
re-said. The world continues at the cost the lateness imposed.

What `catchup: full` *does* mean: the missed content is **available
through reasonable in-fiction action.** Listen to the rest, ask a
bystander, request the brief from a clerk, find someone after. The
player recovers it through their own character's effort, in dialogue
and action, the way they recover any other piece of information.

The cost of being late is preserved at every catchup tier:

- **`full`** — costs a beat of in-fiction work and surfaces the
  player as the obvious latecomer.
- **`partial`** — costs the same plus permanent loss of the parts
  the author declared unrecoverable.
- **`none`** — the event is gone; only aftermath remains.

---

## Two event shapes to keep distinct

The schema applies to both, but the application differs:

### Participation events

Events the player chooses whether to attend — an audience, a meeting,
a market, a public ritual, a private rendezvous. The player's
presence is the variable. The schema governs whether they made it,
how much of it they got, and what they can still recover.

The eleventh-bell recruitment pitch is this kind:
`time: 11:00, duration: ~5 minutes, catchup: full`.

### World-state moments

Events that occur regardless of the player — a bell tolling, a reset
firing, a planned assassination, a star crossing the horizon, a
caravan leaving the gate. The player's presence does not affect
whether the event happens. The schema governs whether the narrator
renders it at T (yes, exactly), and whether the player who arrived
mid-event or post-event can recover what happened.

A world-state moment with `catchup: none` is the strictest case: it
happened at T, it cannot be re-entered, and only aftermath is
available. Most instantaneous world-state moments default to this.

The discipline applied to either shape is identical: **T is exact, D
is what was declared, and the narrator does not soften lateness with
voiceover.**

---

## Authoring discipline (for story data)

When writing story data that includes a timed event, declare all
three fields explicitly. The schema is small enough that omitting it
is rarely an efficiency gain and frequently a future ambiguity. In
particular:

- **Do not write "around eleventh bell"** unless you mean it. Write
  `time: 11:00` if eleventh bell is exact (the usual case), or
  `time: 11:00 ± 5 min` if the event genuinely floats. "Around"
  without a declared window reads as authorial vagueness, and the
  narrator will resolve it as exact.

- **Do not write "shortly after midnight"** for a reset step. Write
  `time: 12:00 AM, duration: instant`. The reset steps are
  load-bearing across the entire setting; a player crossing a
  boundary at 12:00:01 has materially different outcomes than one
  crossing at 11:59:59, and the rules must support that distinction
  cleanly.

- **Do not omit `catchup` for events the player might miss.** The
  default is `none`, which is correct for most world-state moments
  but is a real loss for participation events the author actually
  wants the player able to recover. Decide and write the value.

- **For events with a tolerance**, prefer `time: T ± window` to a
  prose hedge. The tolerance is part of the time, not a separate
  flexibility note.

---

## Worked example — an eleventh-bell recruitment pitch

```yaml
event: expedition recruitment pitch
time: 11:00 (eleventh bell)
duration: ~5 minutes
catchup: full
catchup_notes: |
  A late arrival walks into the speech in progress. The recruiter is
  mid-sentence on the framing of the offer; she does not restart. The
  player picks up the speech from wherever it actually is. After the
  pitch ends, a neighbor, a clerk, or the recruiter's brief
  can surface the missed framing. The player is visibly the latecomer;
  the recruiter's read of them includes that fact.
```

A player who arrives at 10:55 stands with the other applicants and
waits. A player at 11:00 hears the pitch from the first word. A
player at 11:03 walks into the recruiter mid-framing and catches the
remainder; the missed two minutes are recoverable through in-fiction
effort after the audience. A player at 11:08 enters an empty
chamber; the pitch is over and what they can learn about it depends
on whom they find and ask.

---

## Worked example — a world-state moment

```yaml
event: The dawn bell
time: 6:00 AM (local)
duration: instant
catchup: none
catchup_notes: |
  The dawn bell tolls once at exactly 6:00 AM. Subjects within
  earshot hear it; subjects shielded from sound (sealed chambers,
  distant locations) do not. The moment itself is not re-enterable
  — only its consequences are observable from 6:00:01 AM onward.
```

The player cannot arrive "during" the bell; the duration is instant.
They either heard it (and reacted), were shielded (and did not), or
were awake nearby (and observed others react). There is no mid-event
arrival because there is no middle. The discipline of declaring the
schema explicitly still applies — the fields are what tell the
narrator the moment is instantaneous and unrecoverable.

---

## Undeclared elapse — estimating time from depicted action

Most scene time is **not** a declared event. It is the free-running
back-and-forth of ordinary beats, and the narrator still has to know
how much in-world time has passed — to advance the time of day, to
stamp saved state, to keep any spoken clock reference honest, and to
keep honest any deadline the characters are working against. The
discipline here is the counterpart to declared-time exactness:

**In-world elapsed time is a function of the depicted action at a
natural pace — not of word count, beat count, or register.** A register
sets *prose density* (how many words render a second of fiction). It
does not set the clock. Lingering prose is reading-time; it is not
story-time.

### When the estimate is mandatory

The estimate is easy to skip in a flowing scene, and skipping it
is how felt time — inflated by prose volume in a dilated register
— silently becomes the scene's clock. Treat it as **required, not
optional**, at any of these triggers:

- **A bounded window or deadline is live in the scene.** Whenever
  the characters are working inside a finite span — time before
  someone arrives, a meeting that ends, a ride that leaves, any
  "we have until X" — the elapsed-versus-window estimate must be
  current. Recompute it (per the procedure below) from the
  depicted action before any beat where the remaining time bears
  on what a character perceives, says, or does.
- **A character is about to reference elapsed or remaining
  time** — aloud or in interiority, in absolute form ("it's been
  an hour") or the mood forms that slip easiest ("we're nearly
  out of time," "past the midpoint," "the window's closing"). The
  reference must match the action-based estimate, not the feel of
  the passage.
- **A character is about to act on elapsed or remaining time** —
  cutting a conversation short, forcing a decision, calling the
  window spent, raising the urgency. This is the most
  consequential trigger and the easiest to miss: the pressure
  reads as drama, not as a quantity claim. A decision driven by
  inflated felt-time is the same error as a spoken wrong number —
  it just enters through behavior instead of dialogue. Estimate
  first; let the action follow the real clock.

Nothing here is stored or emitted. The estimate is derived on
demand from the scene already in context and spent immediately on
the beat that needed it. The discipline is *when to run it*, not
*what to keep*.

### The procedure

When stamping how much time a stretch of beats consumed:

1. **Bound the span** — from the last time stamp (or scene start) to
   now.
2. **List what was actually depicted in it** — the lines of dialogue
   actually spoken, the physical actions actually taken.
3. **Estimate the natural duration of *those*** — how long it takes to
   speak those lines at a conversational pace and perform those
   gestures or movements at a real, unhurried tempo.
4. That estimate **is** the elapse. The number of beats and the length
   of the prose are **not inputs.** Four beats of quiet exchange and
   four beats of a duel produce wildly different clocks from the same
   beat count.
5. **Correct against the register's known pull** (below): most
   registers tempt over-counting; travel tempts under-counting.
6. Feed the result to the time system the override defines (units and
   storage are override-owned). Any spoken clock reference must match
   it.

### The per-register pull

The pull is not a multiplier to apply — it is the direction the prose
will mislead the estimate if step 3 is skipped:

- **neutral / levity** — roughly 1:1; least illusion. Banter runs close
  to real time.
- **intimate / horror / investigation** — *dilated.* Much prose, little
  clock: moments held, beats let to breathe, granular slow-noticing.
  The passage *feels* long; the action is short. Strong over-count
  risk.
- **combat** — *extreme.* Many beats over seconds. The largest
  over-count risk in the system: a flurry of exchanges across several
  beats is tens of seconds, not tens of minutes.
- **travel** — *compressed.* A sentence can be hours; the prose is
  shorter than the time. Under-count risk — though travel usually
  carries its own stated duration, which takes precedence.

---

## Worked example — undeclared elapse in a dilated register

Two characters share a quiet exchange rendered across four beats in the
intimate register: roughly eight lines of unhurried dialogue and a few
small gestures — a hand moved, a held look, a shift closer. The prose
"lets moments hold," so the passage *reads* long.

Spoken and done at a natural pace, that exchange is about **five
minutes.** The narrator stamps ~5 minutes — not the ~40 minutes the
lingering prose tempts. The 40-minute feel is reading-time; the
depicted action is what advances the clock.

Had the same four beats been a duel in the combat register, the
depicted action — a half-dozen strikes and counters — would be on the
order of **twenty seconds.** Same beat count; the clock follows the
action, not the count.
