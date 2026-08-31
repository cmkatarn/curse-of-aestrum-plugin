---
id: rule_snapshot
name: The Snapshot
type: core_mechanic
related_rules: [rule_revert, rule_fuzzball, rule_time_loop, rule_dead_zones]
---

## Overview

The first night a subject is physically inside Aestrum at midnight, Shar takes a **snapshot** — a wholesale point-in-time assessment of the subject (memory, inventory, physical state). The snapshot is the baseline the [Revert step]({{PLUGIN_ROOT}}/rules/revert.md) reverts to each midnight thereafter.

---

## Established Rules

### When the snapshot is taken

- **Triggered at the first midnight the subject is physically inside Aestrum and outside a dead zone.** Not at the moment of border crossing, and not on first arrival in any other sense — the snapshot fires during the midnight reset, on the first cycle the subject is present for it and not sheltered by a [dead zone]({{PLUGIN_ROOT}}/rules/dead_zones.md). A subject who has only ever slept inside a dead zone since the loop began has no snapshot on file; one is taken the first midnight they sleep outside one.
- **Partial-presence cases are DM-ruled.** Scrying, astral projection, dream-entry, a limb across the border, and similar partial-presence scenarios are not codified; resolve at the table.

### What it captures

- **Wholesale point-in-time assessment.** The snapshot is not memory-only. It captures everything needed to revert the subject:
  - Memory (everything the subject knows at the moment of snapshot).
  - Inventory (carried items and their state).
  - Physical state (body, condition, prepared spells, class resources).
- Treat the snapshot as a complete restore point for the subject's reversion at midnight.

### Reset point

- **The location where the snapshot was taken becomes the subject's permanent reset point** — the destination of the Teleport step at 3 AM during every subsequent reset they are caught by. A subject who is moved by the Teleport step always lands at this single location, regardless of where in Aestrum they ended the day.
- **The reset point does not update.** Like all other snapshot data, it is set once on the first non-dead-zone midnight and is permanent for the duration of the loop.
- **Strategic consequence.** Where a subject spends their first non-dead-zone midnight is materially important. A subject snapshotted deep inside Aestrum has a useful reset point; a subject snapshotted near the border has a reset point at the border, which is inconvenient or punishing depending on where they expect to be operating. This is one of the few permanent strategic facts about a subject's relationship to the loop.
- **Delaying the snapshot** is possible by spending the first night inside a dead zone (no snapshot fires that night) or outside Aestrum entirely. The canonical example is the overnight stop at [Jiasha's hut]({{PLUGIN_ROOT}}/locations/chapter_1/jiasha_hut.md), which is on Setland soil 200 feet outside the boundary — a party that stays there their first night gains a full additional Aestrum-day of travel before their first non-dead-zone midnight catches them, allowing them to position their reset point further into the duchy.

### Persistence

- **One per subject, ever.** If a snapshot already exists from a prior cycle, no new snapshot is taken. The snapshot is **permanent** and does not update.
- **Survives dead zones.** A subject who is inside a [dead zone]({{PLUGIN_ROOT}}/rules/dead_zones.md) at midnight is not reverted that night, but their snapshot remains on file. The next midnight they sleep outside a dead zone, the revert fires.
- **Survives death and resurrection.** A resurrected subject reverts to their **original, singular snapshot** — resurrection does not create a new snapshot, and the snapshot is on the subject, not the body.
- **No exit during the cycle.** Subjects cannot leave Aestrum while the cycle continues, so snapshot persistence across exits is moot until the loop breaks.

### Moon Amulet interaction

- Moon Amulets block **Modify Memory** only. They do **not** prevent the snapshot from being taken.
- A subject who enters Aestrum wearing a Moon Amulet still has a snapshot taken at their first midnight. If they ever lose or remove the amulet, the snapshot is on file and revert will fire normally at the next midnight.
- Functionally these are "Amulets of Protection from Modify Memory" — the name *Moon Amulet* is preserved for table roleplay, since players will not know what the amulet does until they attune or pry the answer from Jiasha.

### Readability

- **Snapshots cannot be examined as a source of information about the subject.** Neither Shar nor any agent can read a snapshot to learn what the subject knows, carries, or has done. The snapshot is a revert target only — it is invoked at midnight, not queried.
- This rules out using a captured subject's snapshot as an intelligence source, and it rules out Quellenna or any cultist offering snapshot-readout as a service.

### Forensic value in-fiction

- The snapshot still serves as **circumstantial evidence of intent** at the time it was taken — what gear a subject carried, what orders they bore, what they had prepared. Malak's decade-old assassins are the standing example: their snapshots preserve orders on which Malak authorized the death of Evandur Tallwood, kit included ([malak_du_leon.md]({{PLUGIN_ROOT}}/npcs/chapter_1/malak_du_leon.md)).

---

## Behavioral Tells

A subject whose snapshot is being applied will, the morning after revert, behave exactly as they did the morning after their first midnight in Aestrum. Players who interact with the same NPC across multiple cycles should notice consistent re-arrival behavior — the same questions, the same jokes, the same fears.

---

## Boundary-Bubble Mechanic

*This section codifies* **how** *the snapshot binds the subject to the bubble. It lives here, in `{{PLUGIN_ROOT}}/rules/snapshot.md`, because the binding is a property of the snapshot itself — not of Aestrum's geography — per the canon line above: "The snapshot is the binding mechanism, not the boundary itself." Anything a future author writes about how the bubble holds a subject belongs with the snapshot, because the snapshot is the thing that holds them. A discoverable stub at [boundary_bubble.md]({{PLUGIN_ROOT}}/rules/boundary_bubble.md) routes readers here.*

### What the snapshot does, mechanically

The snapshot is a **divinely-sustained personal curse** of the *Geas* / *Bestow Curse* class, modeled with the conditional-permeability logic of *Forbiddance* and the mark-keyed triggering of *Symbol*. Imposed by Shar at the subject's first midnight inside Aestrum, the curse's sole prohibition is: *the subject may not cross Aestrum's territorial line.* The curse is **on the subject**, not on the duchy boundary — there is no wall in the world.

5e mechanical assembly (RAW components):

- **Mark:** a divine-tier curse on the creature (*Geas* / *Bestow Curse* family), inseparable from the snapshot itself.
- **Trigger:** the marked subject's body, voice, or effects reach the territorial-boundary coordinate of Aestrum.
- **Effect:** a *Wall of Force*-equivalent refusal manifests **personal to that subject** at the line. Other marked subjects walking beside them encounter their own copies of the refusal at the same coordinate. Non-marked creatures encounter nothing in the world there.

### What the refusal stops

The refusal is **total to all outbound aspects of the marked subject** at the line:

- **Body.** The subject cannot pass. Contact at speed produces Wall-of-Force-class impact (bloody nose at a brisk walk; broken bones at a full sprint). No save; no spell pierces it from the inside.
- **Voice.** Sound originating from the marked subject does not cross outward. An outsider standing on Setland soil at the line hears nothing from a subject pressed against the inside.
- **Thrown objects.** Anything cast by the marked subject — coin, dagger, written note, projectile — strikes the refusal and falls. Carried objects cannot be relinquished across the line.
- **Magical effects originated by the subject.** Spells, effects, and ranged magical attacks cast from inside do not cross the line outward.

### What the refusal does *not* stop

- **Light, inbound or outbound.** The refusal is transparent. A marked subject at the line can see Setland soil and any person on it; an outsider can see the marked subject through clear air. The canonical case: Jiasha's hut, 200 ft outside the territorial line, is visible from inside the bubble.
- **Outsiders crossing inward.** Non-marked creatures cross the territorial line freely in either direction. The boundary itself is not magical — only the curse on snapshotted subjects produces refusal. An outsider entering Aestrum encounters no wall. (They become snapshotted only if they stay past their first midnight inside; passing through Aestrum within one day's window does not bind them — see [time_loop.md § Snapshot Receipt and the Boundary Bubble]({{PLUGIN_ROOT}}/rules/time_loop.md).)
- **Sound, inbound.** A voice from outside the line carries normally into the bubble. A trapped subject hears an outsider's voice; the outsider hears nothing from inside.

### What the subject can infer from the experience

A party encountering the refusal at the line **cannot validly infer that the wall is subject-bound** from their own evidence base alone. Three marked subjects walking abreast and each meeting an invisible wall at the same coordinate reads, on its face, as *"there is a wall at this line."* The natural in-fiction reading is a wall on the duchy boundary — not a wall on themselves.

The subject-bound nature of the curse is discoverable only through:

- **A non-marked traveler crossing through their line of refusal** while a marked subject stands at it — direct disproof of the area-wall reading.
- **A divination specifically targeted at the subjects themselves**, of the *Identify* / *Detect Magic* / *Remove Curse* family. Such divination reveals only that *a curse of divine tier is on each subject*; it does not name Shar, the snapshot, or the binding's nature.
- **Out-of-fiction information from a knowing source** — Jiasha may know; Shar's agents do; a god of opposing aspect might intervene.

**DM discipline.** Do not let the party reach the *"the wall is on us"* realization without one of these confirming observations. The standalone experience of *"all three of us hit a wall at the line"* is consistent with a duchy-wide barrier and does not select for the subject-bound mechanic. Surfacing the subject-bound truth without confirming evidence is a knowledge-boundary leak (Variant C — hypothesis-as-inference; see Calliope's `epistemic_discipline_checklist.md` Row 1).

### What removes the curse

Mortal magic does not. *Remove Curse*, *Greater Restoration*, and equivalent effects fail against the divine-tier binding. The two routes off the snapshot are:

1. **Completion of the Breaking-the-Curse arc** — taking down Shar's hold on Aestrum dissolves the curse on all snapshotted subjects, who may then leave the way they came. The campaign's intended exit.
2. **A negotiation with Shar herself** — technically a route, narratively the wrong door, but a route. Any party member who reaches Shar with an offer she finds interesting could in principle bargain their own snapshot off. The DM should not foreclose this in principle, however unlikely it is in practice.
