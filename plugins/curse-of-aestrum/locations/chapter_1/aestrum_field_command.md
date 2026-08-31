---
id: loc_aestrum_field_command
name: Aestrum Field Command
type: military_camp
region: setland → aestrum (moves)
mobile: true
exists_from: nortmunde_day_0
curse_affected: false
npcs_present: [npc_aidra_calemthor]
chapter: 1
---

## Overview

[Aidra Calemthor]({{PLUGIN_ROOT}}/npcs/chapter_1/aidra_calemthor.md)'s forward command for the
Aestrum invasion — the seat of [the Setland Army]({{PLUGIN_ROOT}}/factions/chapter_1/setland_military.md)
in the field.

**It does not exist at campaign start.** There is no camp, no command, and no front
until the King of Nortmunde dies. Do not render it, reference it, or let a character
know of it before then.

## It Moves

This is the campaign's one **mobile** location, and its position is a sequence rather
than a place:

| Phase | Where | When |
|---|---|---|
| **Does not exist** | — | campaign start → Nortmunde Day 0 |
| **Staging** | the road from Setland to Aestrum, **on the Setland side** | forms once the King dies (Day 0); Aidra receives formal orders the same day |
| **Inside Aestrum** | **Tine Cross (3WI)** — the three-way junction ~20 minutes northeast of Duskwall, where the road west to Quarterways and the Setland road meets the roads to Duskwall and Dunleaven | a few days later — roughly Day +2 to the border, **Day +5 across** |

**Tine Cross is the position, and it is well chosen.** The junction holds the road back
to Setland, the road into Duskwall, and the southern road past the Deckard Estate gate
toward Dunleaven — an army sitting on 3WI has its supply line behind it and its hand on
every land approach to the capital. Once camped it is **visible from Duskwall as a large
smoke column**, and it becomes the army's **loop reset position**.

## The Crossing Is a Campaign Event

**When the Command moves into Aestrum, it destabilizes the curse.** The influx exceeds
Shar's capacity to hold the cycle cleanly; she refuses to release it, and the strain
produces cascading failures — memory failures, teleportation failures, sleep failures —
and hairline fractures in her control. Major destruction inside a given day's loop
becomes genuinely hard to reset and compounds the strain.

So this camp is not scenery moving on a map. **Its border crossing is the mechanism by
which the loop starts to come apart**, and it happens on a schedule the party does not
control and may not know about. See
[setland_military.md]({{PLUGIN_ROOT}}/factions/chapter_1/setland_military.md) for the march
profile and the full failure list.

## DM Notes

**Check the outside clock before rendering this at all.** Aestrum days and Nortmunde
days advance together; a party deep in the loop can be several days past the King's
death without knowing he is dead.

**In `die_a_hero` the army is already here.** It crossed on **Aestrum Day 12 / Nortmunde
Day +5 / Kythorn 30**, and Duskwall Castle is partially destroyed. The run stands at
Aestrum Day 13 — Nortmunde Day +6 — with the Command established at 3WI and the curse
already taking strain. Do not play this as a coming event in that campaign; it has
happened.

**Aidra is here only from Day 0.** Her anchor is this camp from the day the orders come. Before that
her anchor is [her own house]({{PLUGIN_ROOT}}/locations/chapter_1/aidra_house.md) outside Charnelhold's wall, and this
location does not exist to point at.

**She argued against the invasion and lost.** A blockade achieved the same strategic
result; once Malak decided, she closed the argument and executed. Play her as competent
and committed, not reluctant — the reluctance is spent.
