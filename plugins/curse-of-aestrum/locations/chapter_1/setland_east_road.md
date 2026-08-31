---
id: loc_setland_east_road
name: The Setland East Road
type: corridor
region: setland
curse_affected: false
connected_locations: [loc_setland_city, loc_jiasha_hut, loc_aestrum_boundary]
npcs_present: []
chapter: 1
---

## Overview

The road east out of [Setland City]({{PLUGIN_ROOT}}/locations/chapter_1/setland_city.md) to the Aestrum boundary — the
route the campaign opens on. It runs through a **farmland belt** (~7 hours on foot),
then a stretch of **forested foothills** (~1 hour), to **[Jiasha's hut]({{PLUGIN_ROOT}}/locations/chapter_1/jiasha_hut.md)**
at the eastern edge of the foothills, and ~200 feet beyond the hut to the **boundary**
into Aestrum. Full segment distances and the onward Aestrum-side approach to 4WI are in
[routes.md]({{PLUGIN_ROOT}}/locations/chapter_1/routes.md).

The hut is the intended overnight stop before the crossing — the campaign uses
afternoon rain to motivate it, and the overnight is the built-in snapshot-positioning
lever for the party.

## Register — Chapter 1: peaceful and productive

At campaign start the corridor is **healthy and quiet.** Crops in the fields, smoke from
chimneys, kept fences, road-warden posts in good repair, fair-priced inns. Setland is on
a quiet footing — Malak conceals his war preparations (see [setland_city.md]({{PLUGIN_ROOT}}/locations/chapter_1/setland_city.md)) —
and the road shows it.

- **Farmsteads.** Independent smallholdings on Setland's standard agricultural tithe,
  south of the road. Farmers are used to travelers and treat them with **friendly
  indifference**: food and water at fair prices, short rests permitted, news passed along
  unfiltered.
- **Foothill forest.** North of the road, healthy and productive. Setland charcoal-burners
  and timber crews work the lower slopes on a sustainable rotation; deeper forest is left
  alone. Game plentiful. **Not the Misty Forest** — no antimagic strangeness — but dense.
- **Faction reach.** Setland's writ runs light along the corridor — a road-warden, an
  occasional patrol. The Black Arrows are opportunistic transients, not garrisoned.
  Aestrum has no Setland-side presence.

**Sell the peace.** The Chapter 2 contrast only lands because the party walked the
peaceful version with their own boots.

## Register — Chapter 2: devastated (one-way, triggered)

Once Setland's war effort reaches the corridor, the peaceful register is **gone for
good** — farms confiscated and stripped, forest clear-cut for materiel, the road churned
to mud under army columns, road-warden posts turned to supply depots. This is a
**one-way transition**, not a daily change: it does not revert.

The full devastated state is authored as a chapter overlay at
[chapter_2/setland_east_corridor.md]({{PLUGIN_ROOT}}/locations/chapter_2/setland_east_corridor.md), which
supersedes this file's Chapter 1 register when Chapter 2 is active. **Hold the peaceful
register until then**; do not pre-age the road.

## The Mercenary Encounter — conditional, Chapter 1

**Fire this only if no PC has learned of the Galadiil bounty by the time the party
reaches the forested foothills.** Its purpose is to put the bounty's existence in front
of the party before they meet Jiasha, so the Aestrum thread opens with the right
context. **It is not a scheduled ambush** — if the bounty is already carried, the road to
Jiasha is uneventful, and running it anyway is redundant.

**The encounter.**

- **A small group of mercenaries** (three to four; tune to party level) ambushes the
  party on the forest trail. Competent but not elite — Black Arrows-adjacent operators
  racing the party to Aestrum to claim the bounty themselves. **This is a forward scout
  team dispatched by [Mieke]({{PLUGIN_ROOT}}/npcs/chapter_1/mieke.md)**, the band's captain, who is
  not in this encounter — he is with the main band, still on the Setland side. If the
  party wipes the scout team, the chain into timeline B fires: Mieke regroups the main
  band, follows the same road, and kidnaps Jiasha for intel and retribution (see
  [the_abduction_of_jiasha.md]({{PLUGIN_ROOT}}/quests/chapter_1/the_abduction_of_jiasha.md)).
- **The combat is light.** Injure without seriously wounding — a few hit points, a clean
  strike or two that draws blood, perhaps one PC dropped to half. Nothing lethal. The
  encounter exists to surface the bounty document, not to threaten the party.
- **One mercenary attempts to flee** as the fight turns; let them escape if the party
  doesn't pursue hard. (Optional — they are reporting back, not relevant to the scene.)
- **Search the bodies.** A retrievable copy of the bounty is on the leader — a **standard
  Black Arrows writ**, small parchment sealed with a black-arrow stamp:

  > *Open writ. Target: Galadiil. Location: Aestrum. Proof: right eye, right hand, the
  > hand to bear the heirloom ring as identification. Payment on delivery to Charnelhold
  > contact, full and discreet. Issued through the standard channel.*

  No issuer name — the Black Arrows do not name commissioners — but a PC who has heard of
  Quellenna's "special assistance" can connect it. A PC who has not still has a target, a
  location, and the proof terms.
- **The injuries set up Jiasha.** She has the immediate, useful role of healing them when
  they reach her hut shortly after; her introduction lands better if she is doing
  something specifically for the party in the first beat.

**Flexible framing.** If a different delivery fits the table, the encounter bends — bandit
road-thieves carrying the writ incidentally, a single Black Arrows scout met less
violently, or a body already on the trail with the writ on it and no combat at all. **The
point is the writ in the party's hands.** The combat is the recommended vehicle, not a
requirement.

## DM Notes

- **The boundary crossing is silent, and stays silent.** A first-time party crosses into
  Aestrum with no in-fiction signal — no shift in the air, no threshold-feeling. See
  [routes.md]({{PLUGIN_ROOT}}/locations/chapter_1/routes.md) and [rules/time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md).
- **Jiasha's hut is the last waystation before the loop.** The corridor's design point is
  that proximity: the overnight there is where the party is positioned for their snapshot.

## Open Slots — To Develop in Play

- **[layout]** The corridor is a register and a route, not a mapped place. Specific
  farmsteads, the inn(s), road-warden posts, and named stretches are undetailed — the
  Chapter 2 overlay lists callback slots (a court-intelligence-drop farmer, a
  charcoal-burner, a road-warden sergeant, a foothill forester) that have Chapter 1 seed
  homes here and are not yet cast.
- **[relation]** Whether the Aestrum-side approach (boundary → 4WI) is part of this
  corridor or its own segment. It is currently held only as route entries in
  [routes.md]({{PLUGIN_ROOT}}/locations/chapter_1/routes.md); this file stops at the boundary.
