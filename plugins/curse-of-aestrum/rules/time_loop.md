---
id: rule_time_loop
name: The Time Loop — Reset Sequence
type: core_mechanic
related_rules: [rule_snapshot, rule_revert, rule_fuzzball, rule_dead_zones, rule_loop_anchors]
---

## Overview

Aestrum is trapped in a magical daily cycle. Every midnight, the day resets. Memory-bearing subjects are reverted (see [revert.md]({{PLUGIN_ROOT}}/rules/revert.md)); creatures and objects are restored to their start-of-day state.

The current in-game year is **1490**. The cycle began in approximately **1480**, meaning NPC residents believe it is still that year.

The loop is sustained by qualifying prayers at two anchor shrines — see [loop_anchors.md]({{PLUGIN_ROOT}}/rules/loop_anchors.md).

---

## Reset Sequence (timed)

Each step is a **world-state moment**. The schema follows
[time_and_events.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/time_and_events.md):
every step fires at its declared `time:` exactly; every step's
`duration:` is `instant`; every step's `catchup:` is `none`. There is
no "around midnight" — Sleep fires at 12:00:00 AM Aestrum-local. A
subject inside the affected area at the moment of firing is subject;
a subject outside it (across the boundary, inside a dead zone, or
otherwise sheltered per the per-step rules) is not. There is no
mid-event arrival because every step is instantaneous.

| Time (Aestrum-local) | Step | Duration | Catchup | Effect |
|---|---|---|---|---|
| 12:00 AM | **Sleep** | instant | none | Forces unconsciousness on all affected creatures |
| 1:30 AM | **Resurrect / Recreate** | instant | none | Restores creatures and objects to start-of-day state |
| 3:00 AM | **Teleport** | instant | none | Moves sleeping individuals to their reset point |
| 4:30 AM | **Modify Memory** | instant | none | Wipes the day's memories — see [revert.md]({{PLUGIN_ROOT}}/rules/revert.md) and [fuzzball.md]({{PLUGIN_ROOT}}/rules/fuzzball.md). **Must run after Recreate** so resurrected subjects do not retain memory of having died. |
| 6:00 AM | **Wake** | instant | none | Removes Sleep effect |

At midnight (12:00:00 AM), affected individuals fall asleep, collapse,
freeze rigid facing their intended direction of travel, then vanish to
their reset point. The Sleep step itself is instantaneous; the
collapse-and-freeze tableau plays out in the seconds after.

**Boundary-crossing precision.** *"After the morning Wake step"* means
strictly after 6:00:00 AM. *"Before the following midnight Sleep
step"* means strictly before 12:00:00 AM. A subject who crosses the
border at 11:59:59 PM departs as a non-snapshot subject; a subject
inside the boundary at 12:00:00 AM is snapshotted. The cycle does not
round, and neither does the discipline that surfaces it.

---

## Recreate Mechanics

- **Physical objects** ARE recreated (jewelry in a tomb reappeared after reset).
- **Magical enchantments** are NOT recreated. A magical pendant was recreated as a non-magical copy.
- **Magic-immune items** (runed) are not recreated — they were never erased. See [magic_immune_runes.md]({{PLUGIN_ROOT}}/rules/magic_immune_runes.md).
- **Creatures** are fully restored, even if parts were missing (the Runic Skeleton's femur was perfectly recreated).
- **Animals** are excluded from the loop's transformative steps. They are not
  Resurrected/Recreated (an animal that dies stays dead — see
  [death_and_dying.md]({{PLUGIN_ROOT}}/rules/death_and_dying.md)); they are not subject to Modify
  Memory, so an animal retains **continuous memory across resets**, accumulating
  real experience while the looped residents around it revert to start-of-day;
  and they are not **Teleported** — having no reset point, a sleeping animal
  simply remains where it lay while the looped party is scattered to their reset
  points. (This is why a companion animal caught outside a dead zone at midnight
  is separated from the party at reset.) The looped population re-meets each
  animal "for the first time" every morning; the animals do not. The lived
  consequence — animals enduring years inside Aestrum, unremembered and
  uncared-for — and the two adoptable companions built on it (including how they
  handle separation at a reset) are developed in
  [companion_animals.md]({{PLUGIN_ROOT}}/rules/companion_animals.md).
- **Newcomers who die before their first midnight** have no reset point and stay dead permanently — the loop can only restore a creature to a prior state it established within Aestrum.

---

## Protection from Reset Steps

The party can convert existing magic items into per-step protections (Sleep, Teleport) via the essence-extraction rule. See [magical_item_conversion.md]({{PLUGIN_ROOT}}/rules/magical_item_conversion.md).

Inside a dead zone, none of the reset steps apply — see [dead_zones.md]({{PLUGIN_ROOT}}/rules/dead_zones.md).

Moon Amulet bearers are not affected by the Modify Memory step but are still subject to Sleep, Recreate, and Teleport unless otherwise protected.

---

## Snapshot Receipt and the Boundary Bubble

The reset sequence and the boundary bubble both act only on subjects who have received a Modify Memory snapshot. A subject who enters Aestrum strictly after the morning Wake step (after 6:00:00 AM) and leaves strictly before the following midnight Sleep step (before 12:00:00 AM) never receives a snapshot and is therefore:

- **Not subject to the reset sequence** at the midnight they would otherwise have been caught by, and
- **Not contained by the boundary bubble** for the duration of their stay — they can leave Aestrum the same way they entered.

**Implication — same-day cross-border traffic is possible.** Border traders who enter Aestrum in the morning, conduct business, and leave before midnight pass in and out without becoming loop subjects. They observe Aestrum residents (who *are* snapshot subjects) failing to remember previous visits, but the traders themselves carry continuous memory and accumulate observations across many visits. This is why Setland-side knowledge of Aestrum exists at all — and why all of it is second-hand, anecdotal, and uniformly strange.

**A subject who stays past midnight becomes a loop subject permanently.** Receiving even one snapshot is sufficient to bind them to the bubble; they cannot then leave the way they came. The snapshot is the binding mechanism, not the boundary itself.
