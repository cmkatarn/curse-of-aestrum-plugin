---
id: loc_misty_forest_shrine
name: The Misty Forest Shar Shrine
type: religious_site
parent: loc_misty_forest
region: aestrum
curse_affected: true
loop_anchor: true
shar_controlled: true
connected_locations: [loc_misty_forest, loc_misty_forest_dead_zone, loc_mieke_mercenary_camp]
npcs_present: []
chapter: 1
---

## Overview

The second of Shar's two prayer anchors, and the reason the cycle holds — see
[rules/loop_anchors.md]({{PLUGIN_ROOT}}/rules/loop_anchors.md), where this shrine and the
[Shrine of Selûne]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/shrine_of_selune.md) are named together as the pair.

A ruined structure of dark stone with only **one wall still standing**. Two stained
glass windows remain in that wall, both stained deep magenta — intact, in a structure
that has lost everything else.

## Position — and why it matters

Approximately **100 yards west of the [dead zone]({{PLUGIN_ROOT}}/locations/chapter_1/misty_forest_dead_zone.md)
boundary**, and deliberately outside it. The distance is load-bearing, not scenery:
**Shar cannot hear anything spoken within an antimagic field**, so a prayer made
inside the dead zone reaches nobody. The shrine sits where it sits so that the prayers
made at it work.

The **hunting trail** runs roughly a quarter-mile west, between the shrine and the
road. When Jiasha has been taken captive in the Duchy,
[Mieke's mercenary camp]({{PLUGIN_ROOT}}/locations/chapter_1/mieke_mercenary_camp.md) occupies it — the nearest thing to
habitual trespassers on Rowan's ground.

## The Anchor Objects

Two, and they behave differently:

- **Hati's donated idol** — a carved Shar likeness left by Hati Heldrivver when she
  took the original forest statue to Duskwall. It **predates the loop**, resets each
  midnight, and qualifies as an anchor on its own. This is Shar's redundancy here, and
  it is **always present**.

  *Why the original went:* Shar needed a statue for the Duskwall shrine and had no
  time to obtain one — the lock was being rushed forward against Miri Amblecrown's
  itinerary (see [`{{PLUGIN_ROOT}}/factions/chapter_1/shar.md`]({{PLUGIN_ROOT}}/factions/chapter_1/shar.md),
  *Why Aestrum — and Why Then*). This was the only Shar statue already inside
  Aestrum, so this is the one that moved.
- **Rowan's hand-carved effigy** — a *conditional* additional anchor, and a crude
  personal replacement for the statue he lost. The resentment is visible in the
  construction. He only carves it once his fixation on Miri has been disrupted badly
  enough that Hati's idol no longer satisfies his need for a likeness of his own —
  specifically, driven from the Deckard Estate **and** having lost Miri to a party as
  a protected asset. Absent both, he prays through Hati's idol with habitual disdain
  instead. When present, the effigy postdates the snapshot, disappears at midnight,
  and is re-carved each cycle.

**Destroying an anchor object** removes Shar's ability to hear prayers through it
until the next reset — a **same-day window**, not a permanent fix. See
[breaking_the_cycle.md]({{PLUGIN_ROOT}}/quests/chapter_1/breaking_the_cycle.md).

## Who Is Here

Nobody lives at a ruin, and `npcs_present` is empty accordingly. **Rowan Deckard prays
here each morning**, facing the effigy — but his anchor is the
[Deckard Estate]({{PLUGIN_ROOT}}/locations/chapter_1/deckard_estate.md), which is where his sheet places him. He does not
know his prayer sustains the loop.

The shrine resets each morning along with the rest of Aestrum.

## DM Notes

**Rowan's werewolf nature is NOT seeded for discovery here — do not hint it at this
location.** There is no ambient wolf-spoor to find at the shrine or in the surrounding
wood: he has had no reason to transform in a long while, so there are no fresh tracks
to read, and any sign there ever was would reset with the cycle regardless. A party
searching the shrine finds the shrine.
