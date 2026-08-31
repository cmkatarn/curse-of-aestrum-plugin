---
id: faction_aestrum_court
name: The Court of Aestrum
type: ruling_house
base: loc_duskwall_castle
members: [npc_evandur_tallwood, npc_galadiil_ilphekiir]
cycle_aware: false
---

## Overview

The ruling house of Aestrum, seated at [Duskwall Castle]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/duskwall_castle.md):
Duke Evandur Tallwood and his wife Galadiil Ilphekiir, Duchess. Both are loop subjects,
and both are killed in the castle every night by the
[trapped Setland expedition]({{PLUGIN_ROOT}}/factions/chapter_1/agents_of_setland.md) in the thirty-minute window before
midnight, and reset with everyone else.

## Membership

*`known_to` = the members who know this person belongs. Directed; member-to-member only.*

| Member | Role | `known_to` |
|---|---|---|
| [Evandur Tallwood]({{PLUGIN_ROOT}}/npcs/chapter_1/evandur_tallwood.md) | Duke of Aestrum | **all** |
| [Galadiil Ilphekiir]({{PLUGIN_ROOT}}/npcs/chapter_1/galadiil_ilphekiir.md) | Duchess | **all** |

A ruling house is the **maximally public** case — the whole duchy knows who sits at
its head. Everything interesting about this court is therefore *not* in the
membership column.

## What the Table Deliberately Does Not Say

**Galadiil is the Shrikes' inside contact for the vault**, and that does **not** make
her a Shrike. She provides the magical key and the bronze vault token; her motivation
is spite; she believes she is facilitating a robbery to embarrass her husband. She does
not know an assassination is intended, and it has never occurred to her that vault
access is also castle access.

That is not a secret membership — it is **a relationship she misunderstands.** It stays
prose, and it stays out of any `known_to` column, because putting it in one would
assert she has an allegiance she does not have. `known_to` records *who knows a person
belongs to a group*; it is not a general-purpose store for what characters know about
each other.

**She is also Quellenna Ilphekiir's older sister**, and was substituted into Evandur's
marriage contract after the northern prince she was arranged to marry died. Per the
[timeline]({{PLUGIN_ROOT}}/timelines/chapter_1/nortmunde_regional.md), that substitution and
Quellenna's displacement to Setland were deliberate and coordinated, and Galadiil was
placed inside Aestrum "far enough ahead of the cycle's creation to develop a visible
identity" — meaning her presence at this court predates the lock by design.

**She is not on [Shar's roster]({{PLUGIN_ROOT}}/factions/chapter_1/shar.md), and she does not belong on it.** Shar
maneuvered her into this marriage, but Galadiil is not an agent, a piece, or an
instrument — she serves Shar no function here at all.

**The target of the maneuver was Quellenna.** Shar placed Galadiil in her sister's
intended life *because taking it from Quellenna would drive her toward Shar and make
her pliable.* The displacement was the point — but the fracture it widened was already
there. **The sisters never got along**, and Quellenna resented Galadiil from the moment
the change to her engagement was announced. Shar did not invent the bad blood; she
arranged the injury that hardened it.

Galadiil is the means by which a wound was deepened in someone else, and she has no
idea she was used to do it — she simply married a duke.

That is the cleanest illustration in the campaign of **why "placed by Shar" and "works
for Shar" are different facts**, and why a roster of members is not a roster of people
Shar has moved. If it listed everyone she has arranged the position of, it would list
half the duchy.

## Open Slots — To Develop in Play

- **[relation]** Edwy Murn holds a post at the castle (archetype: *The Burdened
  Keeper*) with no stated affiliation. Whether he is court, guard, or household staff
  is unassigned.
- **[relation]** The rest of the household — chamberlain, correspondence clerk, the
  people who make a castle run. The clerk sitting on Dunleaven's bridge petition is
  named as a callback slot in the Duskwall index and has never been cast.
