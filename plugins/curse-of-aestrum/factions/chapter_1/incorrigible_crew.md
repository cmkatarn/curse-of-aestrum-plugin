---
id: faction_incorrigible_crew
name: The Crew of the Incorrigible
type: ship_crew
base: loc_the_incorrigible
members: [npc_rylin_tsarran, npc_baldric, npc_rick_hastley, npc_emmo_durast, npc_wren_calvert]
cycle_aware: false
---

## Overview

The working crew of *[The Incorrigible]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/the_incorrigible.md)*,
a Calimshan brigantine built for speed over cargo volume — normally a captain and 7–8
hands, currently running lean. It is a **gang-controlled shipping operation**, and the
crew are sailors rather than criminals in their own right.

## Membership

*`known_to` = the members who know this person belongs. Directed; member-to-member only.*

| Member | Role | `known_to` |
|---|---|---|
| [Rylin T'Sarran]({{PLUGIN_ROOT}}/npcs/chapter_1/rylin_tsarran.md) | first mate; de facto captain | **all** |
| [Wren Calvert]({{PLUGIN_ROOT}}/npcs/chapter_1/wren_calvert.md) | helmsman | **all** |
| [Emmo Durast]({{PLUGIN_ROOT}}/npcs/chapter_1/emmo_durast.md) | topman | **all** |
| [Baldric]({{PLUGIN_ROOT}}/npcs/chapter_1/baldric.md) | able seaman | **all** |
| [Rick Hastley]({{PLUGIN_ROOT}}/npcs/chapter_1/rick_hastley.md) | ordinary seaman | **all** |

A ship's company is the **transparent case**: they live at close quarters and every one
of them knows exactly who else is aboard. Every row is `all`, and that is what an open
group looks like in this notation.

## The Exception That Isn't On This Table

**Rylin is also an Erethezra operative**, embedded in this shipping operation — and
none of the crew knows it. That fact does not belong here: it is a membership in
[Erethezra]({{PLUGIN_ROOT}}/factions/chapter_1/erethezra.md), and its secrecy is recorded in *that* faction's `known_to`,
where his row is visible only to the Commander.

This is the model working as intended. **A person can be openly in one group and
secretly in another**, and neither file has to know what the other says. Reading his
crew row tells you nothing about his second allegiance, which is exactly the property
his cover depends on.

## DM Notes

The crew are not loop subjects at campaign start — *The Incorrigible* anchors offshore
on Day 9 (see the ship's location file for the arrival sequence and what happens to a
vessel that tries to cross Aestrum's boundary).
