# Create Party — RPG 5e Engine Core

The engine body of the `create-party` skill. Generic D&D 5e party
assembly, decoupled from any specific campaign. A consuming game wires
this in via a thin shell `SKILL.md` that loads:

1. This file (multi-PC orchestration + diversity).
2. The engine's `create-character/core.md` (the per-slot walkthrough).
3. The game's own override file (spoiler discipline, blood-relation
   restrictions, anti-conflict list, opening location, opening NPCs,
   state-directory and instance conventions).

This file knows nothing about specific settings, factions, or named
NPCs. Everything campaign-specific is supplied by the override.

---

## Hard Rules — Inherited and Reinforced

### Interaction style

**Never assume a desktop client.** Present all choices as plain
markdown — numbered lists, headings, code blocks. Do not use
structured-option pickers.

### Spoiler discipline

A new party arrives in the campaign region as outsiders. The override
file defines the canon boundary. **Apply the override's spoiler list
rigidly across all slots, not just the player-built ones.**

The opening scene (see STEP 5) describes the surface job and the public
faces of any NPC pitching the work — nothing about what's actually
happening inside the canon. "Recommend, don't leak." If a hook points
near a sensitive plot, recommend it without explaining why.

### Blood relations to canon-load-bearing NPCs

The override file lists NPCs whose arcs require that no new PC have a
blood tie. Never assign or suggest blood relation to anyone on that
list. Honor any narrow override-defined exceptions exactly as written
(typically: a lineage that is allowed *only* if the user volunteers it
without prompting).

### Claude-controlled party NPCs and PC harm
<!-- anchor: create-party.claude-controlled-party -->

When the user selects **Claude-Directed** NPC control (see STEP 2),
Claude plays every party NPC in character, per the NPC's profile —
including their flaws, frictions, and complications. **Inter-party
conflict is acceptable.**

**Hard limits — Claude-controlled party NPCs may NOT:**

1. Attempt to kill the PC without giving them a fair chance to defend.
2. Murder the PC while they sleep.
3. Come to blows with the PC absent obvious, previously surfaced
   relationship friction.

These limits apply to **party NPCs only**. **Non-party NPCs**
(antagonists, hostile factions, betrayed contacts, monsters) operate
under normal narrative rules and may take any action the fiction
supports.

The override may relax these limits where the setting provides a
structural softener (resurrection mechanics, time loops, narrative
resets, etc.). Any such override must specify the exact condition
under which the limit is relaxed.

### Canon PC arcs are fair game

A new dwarf can share a clan with a canon PC; a new warlock can have any
patron; the new PCs have no knowledge of the canon PCs. Allow the
overlap without comment.

### Outsider rule

No new PC may originate inside the campaign-internal region or carry
pre-knowledge of anything inside it. All hooks come from outside per
the override's "outside the region" hook tables.

---

## STEP 1 — Campaign and Instance Setup

A new party is being created. Decide whether this party belongs to a
**new campaign** or an **existing campaign** in the override's
state-directory convention.

Ask the user as a plain text block:

```
Let's set up a new party. I need:

1. Campaign — new or existing?
   - If new: pick a short slug (e.g., chapter_one_run, the_<X>_run).
     This becomes the campaign ID at the override's state-directory.
   - If existing: name the campaign slug to load. (List of existing
     campaigns shown below if any.)
2. Party size (1–5)
3. Starting level (default 1)
4. Instance name (short slug for the save folder inside this campaign;
   default: instance_<YYYYMMDD>). Instances are within-campaign save
   snapshots.
5. Content rating for this instance (the override defines the rating
   taxonomy and default).
```

If the user picks **new campaign**:

1. Confirm the slug does not already exist at the override-defined
   campaign path. If it does, error and ask for a different name (or to
   use the existing).
2. Scaffold the campaign directory tree per the override's spec. At
   minimum the override should require some combination of: per-campaign
   trees for NPCs, party, locations, factions, items, timelines,
   conversation-states, and any setting-specific overlay categories.
3. Set the override's active-campaign indicator (e.g., a `.active` file)
   to the new slug.
4. Acknowledge the new campaign on one line.

If the user picks **existing campaign**:

1. Verify the campaign directory exists. If not, error and re-ask.
2. Set the active-campaign indicator to that slug.

Then create the within-campaign instance directory per the override's
convention.

Track all values internally as you work — they feed into create-character
for each slot.

---

## STEP 2 — Per-Slot Mode
<!-- anchor: create-party.per-slot-mode -->

For each of the N slots, ask as plain markdown:

```
Slot <i> of <N> — how do you want this one?

1. Player build — you make all the choices (calls create-character).
2. Guided random — you give me hints (sex, race, class, archetype,
   background) and I fill the rest.
3. Fully random — I roll the whole thing.
```

Let the user batch the decision: they may say "slot 1 player, slots 2–4
random, slot 5 guided random with a wizard" in one go. Accept that.

**Track which slots are random.** This decides the opening sequence
(STEP 5).

The convention is that **slot 1 is the player's primary character**. If
the user marks slot 1 as random, ask them to confirm — at least one slot
should typically be player-built. If they confirm an all-random party,
slot 1 is still the "anchor" character for the opening location.

### NPC control mode

After slot modes are picked, **before generating any character**, check
whether the party contains NPCs. The convention:

- Mode 1 (player build) slots are PCs by default.
- Mode 2 (guided random) and Mode 3 (fully random) slots are NPCs by
  default.

If the resulting party contains one or more NPC party members, ask the
user as plain markdown:

```
Your party has <N> NPC member<s>. How do you want them controlled
during play?

1. Player-Directed — I prompt you for direction whenever an NPC would
   take a meaningful action or reaction (responding to a question,
   choosing a side in a dispute, taking a combat action, sharing
   information). Trivial ambient behavior (swatting at flies, shifting
   weight, looking at the fire) I narrate without asking.
2. Claude-Directed — I play every NPC in character through Calliope,
   per their profile, including frictions and complications. The hard
   limits on PC harm apply (see Hard Rules above). You direct your
   PC only.
```

Record the choice. It is the campaign default; the user can take
temporary control of an NPC at any later point in play without
re-asking. Do not program around mid-campaign control swaps — let them
happen.

**This choice affects override-driven generation.** Setting overrides
may gate secret NPC state on the control mode — seeding differently,
or not at all, depending on whether the player or Claude will be
controlling those NPCs (e.g., hidden bounties, prophecies, faction
ties whose contents shouldn't reach the player). The override's
seeding logic reads the choice recorded here.

If only mode-1 (player build) slots exist, skip the NPC control
question — there are no NPCs to control.

---

## STEP 3 — Per-Slot Generation

### Player builds (mode 1)

Invoke the **create-character** skill for that slot. Pass the instance
name and starting level. Let create-character handle the full
walkthrough.

### Guided random (mode 2) and Fully random (mode 3)

The per-character roll procedure — guided vs. fully random, the diversity
bias, and the override's anti-conflict list — lives in Aria's
`{{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_random.md`, with the 5e party role coverage
and build line in its overlay `rules/random_character_generation.md`. `Read`
both and apply them per slot,
walking the create-character stages silently and writing each file in the
standard format. Surface each rolled slot briefly:

```
Slot 2 — <Name>
<Race> <Class> (<Subclass>), <Background>.
Hook: <one-line of how they tie into the region per the override hook table>.
```

### Multi-Slot Layer (party-only)

The shared module covers the per-character roll. On top of it, the party
builder adds the **cross-slot** concerns that only exist with multiple
characters:

- **Cross-slot diversity comparison.** Apply the module's Diversity Bias
  *party form* — compare each new roll against the slots already filled:
  reject a race already present (unless duplicates requested), reject a
  class already present.
- **Role-coverage matrix.** Aim for at least one of each role across the
  whole party — **frontline melee**, **ranged / skirmisher**, **arcane
  caster**, **divine caster or support**, **skill / utility** — weighting
  uncovered roles higher as slots fill.
- **Hook spread.** Prefer backgrounds with strong override hooks for at
  least 2/5 of randomized slots.

The anti-conflict list applies identically to every slot; it is defined
in the module and the override, not duplicated here.

---

## STEP 4 — Roster Review

After all slots are filled, present the full party in compact plain
markdown:

```
Party — <instance>, level <N>
─────────────────────────────
1. <Name>  —  <Race> <Class>, <Background>  —  <hook>
2. ...
```

Then ask:

```
Any adjustments? You can swap a character, retune one, rename,
or accept as-is.
```

Loop on adjustments until the user accepts. Each adjustment that changes
a sheet rewrites the corresponding file.

---

## STEP 5 — Open the Campaign

Once the party is accepted, start an in-fiction cold open. The structure
depends on whether any random characters exist.

The **opening location**, the **opening NPCs**, and the **public pitch**
are all defined by the override. The engine provides the structure of
the cold open; the override fills in the concrete content.

### Case A — All slots were player-built (no random characters)

Open at a **single location** chosen to fit the strongest background
hook in the party. The override supplies a candidate list of opening
locations keyed to background categories (noble, criminal, sailor,
acolyte, outlander, etc.). Pick the one that best fits the party's
strongest hook.

Open with prose: the PCs in this location, naturally converging. Let
the player drive from there.

### Case B — Any slot is random

Run this in two beats:

**Beat 1 — Player-crafted PCs converge at slot 1's location.**

- Slot 1 is the player's anchor PC. Pick the opening location from the
  override's location list based on slot 1's background.
- All other **player-built** PCs join slot 1 at this location as part of
  the cold open. They are present from the start of the scene — their
  convergence is a brief moment of recognition or assembly, not a long
  setup.
- **Randomized PCs are NOT present yet.** They do not appear in this
  beat.
- The scene ends when the player-built PCs see, hear of, or are pointed
  toward **the campaign's public pitch** (the override defines what
  this is — a posting, a herald's announcement, a contact pulling them
  toward a specific location, whatever fits). They learn the pitch is
  being presented in person by the override-defined pitching NPCs. Hand
  control to the user.

**Beat 2 — The public pitch.**

- This beat fires when the user has the player-built PCs **attend the
  pitch presentation**. The pitch is delivered by the override-defined
  pitching NPCs — this is the invitation event where contractors are
  sought.
- The **randomized PCs are present in the audience**, attending the
  same open call. They are not pre-vetted, not pre-assigned, not
  handpicked — they are attendees who came on their own initiative,
  drawn by the same posting or rumor that drew the player-built PCs.
- Run the pitch per the override. Apply spoiler discipline rigidly.
  Nothing about the canon-internal state. The pitching NPCs speak as
  the public personas a citizen would see — composed, confident,
  formal. Do not show their private agendas.
- When the call for contractors goes out, the **randomized PCs step
  forward and accept alongside** the player-built PCs. Introduce each
  one organically — a name, a glance, a brief in-character moment of
  taking the contract. Their backstories do not surface here; only
  their names, surface impressions, and the fact that they accepted.
- End the open when the contract is signed by all PCs and the full
  party has effectively been formed by the act of accepting. Hand
  control to the user.

**Before writing Case B beats**, read the override-specified location
file(s) for the opening location and the pitch venue so the scene is
accurate.

### Scene Style (both cases)

- 200–500 words of prose per beat.
- Third person, present or past tense — pick one and stay consistent.
- Establish each present PC visually within the scene.
- End on a beat that hands narrative control to the user.
- Apply spoiler discipline. NPCs at the opening location do not know
  what is happening inside the canon. They speak of it as outsiders
  speak of it: rumor, wariness, contract risk premium.

---

## STEP 6 — Hand Off

After the cold open is complete and the party is assembled, hand off to
the user. Give them their bearings (where the party is) and then an
invitation to act phrased per the consuming narration layer's action-prompt
convention — written to the opening's register, not a fixed token. The
generic form is one option, not the default:

```
The party is in <opening region>. <invitation to act, in-register>
```

From here, the campaign is live. Other skills (scene,
write-chapter) handle ongoing play. This skill is done.

---

## What This Skill Does NOT Do

- Does not edit the canonical roster paths (the override's write-scope
  restrictions are absolute).
- Does not touch other instances' saved folders.
- Does not initialize per-instance timeline files unless the override
  instructs. If the user wants ongoing event tracking, mention it once
  at handoff — do not auto-create.
- Does not save portraits, transcripts, or scene states.
- Does not run combat. The opening scene is narrative only — first
  initiative roll belongs to the user.
- Does not assume a desktop client. All interaction is plain
  text/markdown.
