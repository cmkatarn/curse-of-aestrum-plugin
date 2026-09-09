# Cycle Recurrences — the loop's deterministic replay layer

## What this is

Aestrum's residents reset every midnight (Modify Memory) and re-live the same
day. A resident's behavior is therefore **deterministic from baseline**: the
same stimulus, on any cycle, produces the same reaction — the same gate-guard's
half-challenge, the same shopkeeper's greeting, the same line of dialogue in
answer to the same opening. The party, who **retain** memory across the reset,
experience these repetitions as an uncanny recording.

**Cycle recurrences** capture those deterministic beats so they replay
faithfully and their repetition pays off over multiple cycles. This is the
*emergent* cousin of the authored **Daily Routine / Daily Pattern** sections in
NPC and location files (Rowan's routine, Mieke's camp): those are pre-authored
recurring scripts; a cycle recurrence is one that **arose in play** and must now
recur because loop physics demand it.

## What can trigger a recurrence

A recurrence is keyed to a **situation pattern**, not necessarily a place. Three
kinds:

1. **Ambient / place** — being at or entering a location under given
   circumstances (the bored landward-gate guard's half-challenge). The place is
   the trigger. Stored on the **location** overlay (`## Cycle Recurrences`).
2. **Interaction / approach** — the party opens with a resident a certain way and
   draws a set response; a different opening branches. Stored on the **NPC**
   overlay (`## Cycle Responses`).
3. **Event-experience — location-independent.** The actor witnesses or undergoes
   an event of a given **type**, and gives the same response *wherever it
   happens.* This is the Westworld texture: Lawrence's flat, repeated
   *"Motherfucker…"* every time he watches William gun down several people while
   Lawrence is tied up — the trigger is the **experience** (helpless witness to a
   sudden slaughter by his companions), not the saloon it happens in. Match by
   **situation-type**, not location; store on the **NPC** overlay
   (`## Cycle Responses`).

So the same basic event can warrant the same response **in a different place** —
match on what the actor *experiences*, not on where they stand.

## The two invariants

1. **Same stimulus → same beat.** When the party reproduces the circumstances of
   a stored recurrence — enter the same place the same way, approach the same NPC
   with the same opening, **or put the actor through the same kind of experience**
   (anywhere) — the drafter **reproduces the stored beat faithfully** (behavior
   and any line near-verbatim). The resident is reset; the determinism is the
   loop's physics, not a coincidence to be freshly improvised each time.
2. **Different stimulus → new branch.** Change the input — enter unarmed, open
   with a different line, approach from a different footing — and the beat
   **branches**: the drafter authors the new response (consistent with the
   actor's baseline), and that new `(stimulus → response)` pair is **itself
   stored** as a recurrence. Over cycles the party maps the tree by probing it.

The actor never remembers; **the party does.** So the payoff is POV-side: the
drafter surfaces the party's growing recognition of the repetition ("the same
guard, the same half-step, the same three words") — the *beat* is constant, the
*accumulation* is in the party's awareness. Let that recognition stack; it is one
of the loop's most legible textures, and the whole point of storing these.

## Perturbation and expiry

A recurrence holds **until the party changes the world that produces it.** If the
producing condition is removed — the NPC is killed and their body dead-zoned so
they no longer reset, a standing change is made to the place — the recurrence
**lapses**: mark it lapsed, do not replay it. A recurrence is a function of
current standing conditions, not an immortal script.

## Where recurrences are stored (per-campaign overlays)

Cycle recurrences are **per-campaign** — they arise from a specific party's
specific inputs — and live in that campaign's overlays, **never** the canonical
base. (A base file's recurring beats are its authored Daily Routine / Daily
Pattern; those are shipped for every campaign. A cycle recurrence is this
party's.)

- **Place-triggered** (fires on entering / being at a location under given
  circumstances): the **location overlay**,
  `{{PROJECT_ROOT}}/campaign_state/<C>/locations/saved/<loc>.md`, under `## Cycle Recurrences`.
- **NPC-triggered** (fires on approaching / opening with an NPC a certain way,
  **or on the NPC experiencing an event of a stored type — anywhere**): the
  **NPC overlay**, `{{PROJECT_ROOT}}/campaign_state/<C>/npcs/saved/<name>.md`, under
  `## Cycle Responses`. Holds both approach-keyed dialogue branches and
  location-independent event-experience reactions (the Lawrence case).

> **`## Cycle Responses` is NOT time-filtered.** It is baseline determinism — the
> resident's response repertoire, not retained experience. The loader includes it
> in full regardless of Aestrum Day, unlike the character's `### Day X —`
> experience entries (which *are* time-filtered per `{{PLUGIN_ROOT}}/overrides/scene.md`). A
> resident's deterministic reaction to a given opening or situation-type does not
> "accumulate"; it is always available because the loop always reproduces it.

An incidental actor with no file of its own — a nameless gate guard — is carried
as a **role** inside the *location* recurrence, not given an NPC file.

## Entry schema

Each recurrence records:

- **trigger:** the circumstances that fire it — a place+circumstance, an
  approach/opening, or an **event-experience type** (location-independent).
  Precise enough to know when it recurs *and when it does not* (which different
  inputs would branch instead).
- **actor:** the NPC (name) or role (*"the landward-gate guard"*).
- **beat / lines:** the deterministic behavior and any dialogue, stored
  near-verbatim so it recurs verbatim.
- **first seen:** the cycle-day / context of first occurrence — anchors the
  party's "Nth time" recognition.
- **branches:** known alternate stimuli and their responses (each a
  sub-recurrence); the **default** branch replays when no alternate input
  matches. New branches are appended as the party discovers them.
- **status:** `active`, or `lapsed` (with the reason) once the producing
  condition is removed.

## Capture — during staging, flushed on save

Recurrences are captured through the **normal staging pipeline**, not by any
separate mechanism. When a deterministic, loop-repeatable beat first occurs (or a
new branch is discovered), it is written into the in-flight **staging file**
(`{{PROJECT_ROOT}}/campaign_state/<C>/staging/<sid>.md`) as part of that beat's deltas — the same
compose-during-play staging tail that carries every other delta — and **flushed to
the overlay on `save campaign state`** by `flush_campaign_staging.py`. The D1
explicit-save discipline holds: nothing reaches an overlay until an explicit save.

**Staging routing + entry format.** A recurrence is staged as a self-identifying
`###` block under the entity's staging section, so the flush appends it to the
right overlay exactly like any delta:

```markdown
# Entity overlays
## locations/duskwall
### Cycle recurrence — <short name>
- **trigger:** ...
- **actor:** ...
    (schema below)
```
```markdown
# Experience deltas
## npcs/<name>
### Cycle response — <short name>
- **trigger:** ...
    (schema below)
```

- **Location recurrence:** `### Cycle recurrence — <name>` under `## locations/<id>`.
- **NPC recurrence** (approach *or* event-experience): `### Cycle response — <name>`
  under `## npcs/<name>`.

The `### Cycle recurrence —` / `### Cycle response —` **prefix is the load-time
marker.** The loader gathers these entries as the location's `## Cycle
Recurrences` / the NPC's `## Cycle Responses` regardless of where in the monolith
the flush appended them, and — critically for NPCs — treats a `### Cycle
response —` entry as **baseline determinism, exempt from the time-filter,** never
a `### Day X —` time-filtered experience entry. The `## Cycle Recurrences` /
`## Cycle Responses` heading in a hand-written overlay is human-readable grouping;
the machine contract is the entry **prefix**.

**One-time vs recurrence:**

- A **one-time event** (happened once, changed the world) → objective log
  (`timelines/saved/aestrum_events.md`), as before.
- A **recurrence** (the loop will reproduce it) → a `### Cycle recurrence —` /
  `### Cycle response —` entry per above.
- Some beats are **both** — logged once *and* seeded as a recurrence.

**Updating a recurrence** (a newly discovered branch, or marking one lapsed) is
just another staged entry the next save appends — the latest entry for a given
recurrence name wins, per the overlays' standing latest-entry-wins convention.

## Draft-time application

Loaded as a drafting constraint (see `{{PLUGIN_ROOT}}/overrides/scene.md`, *Cycle recurrences*).
On entering a location, opening an NPC conversation, or putting an NPC through an
event of a stored type (anywhere), check the relevant overlay's recurrence /
response section against the current circumstances:

- **Match** → replay the stored beat faithfully, and surface the party's
  recognition of the repetition.
- **New input** → author the new branch (consistent with the actor's baseline),
  render it, and stage it as a new stored branch.
- **Producing condition removed** → treat the recurrence as lapsed; do not
  replay it.
