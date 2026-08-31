---
id: loc_misty_forest_dead_zone
name: The Misty Forest Dead Zone
type: dead_zone
parent: loc_misty_forest
region: aestrum
curse_affected: false
dead_zone: true
connected_locations: [loc_misty_forest, loc_misty_forest_shrine, loc_mieke_mercenary_camp]
npcs_present: []
chapter: 1
---

## Overview

The third significant dead zone in Aestrum, after the [Deckard Estate]({{PLUGIN_ROOT}}/locations/chapter_1/deckard_estate.md)
and the [Nahamkate]({{PLUGIN_ROOT}}/locations/chapter_1/nahamkate_desert.md). A magic-immune pocket in the forest's middle
band — **detectable at its boundary but unmarked.**

## Where

Northwest of Aliss Perisdottir's house — relative north and relative west of it, just
west of the Perisdottir path. It sits at roughly the same latitude as the shrine and
the hunting trail, in the forest's middle band. The
[Shar shrine]({{PLUGIN_ROOT}}/locations/chapter_1/misty_forest_shar_shrine.md) stands about **100 yards west of this
boundary**, deliberately outside it.

## What It Does

The same qualities as the Deckard Estate's: a slight change in the air, a stillness, a
torch that burns without flicker. **All magic fails within it**, and **the loop's reset
does not penetrate** — memory carried in survives the midnight boundary.

## Who Is Here

Empty by default. **Rowan Deckard does *not* sleep here** — his anchor is the Deckard
Estate and he returns there each night. This dead zone is his **fallback**: if a party
occupies the estate and forces him off it, he shelters here instead, where his memory
is still preserved and his lycanthropy still suppressed, but where he is off-rhythm,
more volatile, and aware that someone has taken the one place he was fully himself.

That displacement is a **triggered branch, not the baseline.** A campaign in which it
has fired records the actualized state in that campaign's
`{{PROJECT_ROOT}}/campaign_state/<C>/locations/saved/misty_forest.md` overlay; canon here stays
estate-anchored.

## Mechanical Significance

**Permanent removal of Rowan runs through a dead zone.** He resets each midnight
*unless his corpse is inside one by then* — the loop's resurrection cannot reach
within. He does not have to die inside it: a party can kill him anywhere and move the
body before midnight. This dead zone and the Deckard Estate's are both viable. **The
constraint is time, not place.**
