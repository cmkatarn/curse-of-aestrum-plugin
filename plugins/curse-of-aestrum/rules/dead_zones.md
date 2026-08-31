---
id: rule_dead_zones
name: Dead Zones
type: core_mechanic
related_rules: [rule_time_loop, rule_revert, rule_fuzzball, rule_magic_immune_runes]
---

## Overview

Dead zones are **antimagic field equivalents** — no magic functions within them. They are immune to the loop's reset effects and to all other magic.

Historical origin and specific locations are documented in [key_lore_summary.md]({{PLUGIN_ROOT}}/lore/key_lore_summary.md#the-dead-zones--origin). This file codifies how dead zones interact with the loop mechanics at the table.

---

## Core Rule

Inside a dead zone, **no magical effect functions** — including:
- The cycle's Sleep, Modify Memory, Recreate, and Teleport steps.
- The [fuzzball]({{PLUGIN_ROOT}}/rules/fuzzball.md), which is itself a magical construct.
- Spells cast by characters.
- Active properties of magic items (until removed from the dead zone).

This makes dead zones the only reliable shelter from the loop.

---

## Interaction With the Reset Sequence

A subject physically inside a dead zone at the moment each step fires is unaffected by that step:

Per [time_and_events.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/time_and_events.md):
each step is a world-state moment with `time:` exact, `duration:
instant`, `catchup: none`. Shelter is determined at the exact moment
of firing — a subject inside the dead zone at the declared time is
sheltered for that step; a subject outside it at that moment is not.
There is no shelter "around" 12:00 AM; a subject who steps inside the
dead-zone boundary at 12:00:00 AM exactly is a DM ruling on the
boundary's resolution at that instant.

| Reset Step | Time | Inside a dead zone |
|---|---|---|
| **Sleep** | 12:00:00 AM | Not put to sleep |
| **Recreate** | 1:30:00 AM | Body / objects not recreated |
| **Teleport** | 3:00:00 AM | Not teleported |
| **Modify Memory** | 4:30:00 AM | Not reverted; no fuzzball planted |
| **Wake** | 6:00:00 AM | N/A (was never asleep from this cycle) |

A subject who is only *partly* covered (e.g., asleep across the boundary) is a DM ruling — default to: if the head is inside, the mind is sheltered; the rest follows the magic's normal area rules.

---

## The Persistent-Snapshot Rule

Sheltering in a dead zone does **not** erase a subject's [snapshot]({{PLUGIN_ROOT}}/rules/snapshot.md). It only postpones the revert. If a long-term dead-zone resident ever sleeps outside one, the revert fires the following midnight and the fuzzball reasserts.

This means dead-zone shelter is a holding pattern, not a cure. Rowan Deckard exploits this exactly — sleeping inside a dead zone at night to preserve memory, then coming out during the day to operate in the loop world.

---

## Item Interactions

- **Magic items inside a dead zone:** Their magical properties are suppressed while inside. They function normally once removed.
  - Notable case: the Pendant of Waking Hours' *irremovable* property is suppressed inside a dead zone — see [magical_item_conversion.md]({{PLUGIN_ROOT}}/rules/magical_item_conversion.md).
- **Magic-immune (runed) items:** These are essentially portable dead zones — see [magic_immune_runes.md]({{PLUGIN_ROOT}}/rules/magic_immune_runes.md).
- **In-progress enchantment work:** Must be stored in a dead zone before midnight or it resets. This is how loop-aware crafters operate.

---

## Dead-Zone Locations Are Curated — Never Surfaced From a Source That Doesn't Hold Them

Dead-zone locations are authored canon (the three majors — Deckard Estate,
Nahamkate Desert, Misty Forest — plus scattered pockets, in
[key_lore_summary.md]({{PLUGIN_ROOT}}/lore/key_lore_summary.md#the-dead-zones--origin), with
geography in [routes.md]({{PLUGIN_ROOT}}/locations/chapter_1/routes.md); the DM does not
invent new ones — see [aestrum_location_curation.md]({{PLUGIN_ROOT}}/rules/aestrum_location_curation.md)).
They are also the campaign's hardest-won, highest-stakes secret, which makes
them the sharpest case of Calliope's **retrieved-concrete** rule
([epistemic_discipline_checklist.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline_checklist.md)
Row 19, retrieved/derived variant): an in-world information source yields a
dead-zone location **only if that source canonically holds it.**

In particular, an in-Aestrum intelligence source that documents the dead places
**only from their thresholds, or as gaps in its own reach** — a seer's archive,
a scholar's records, a diviner's notes — does **not** contain their map
positions and cannot be made to under any research or skill-check success. The
honest result of mining such a source is the **absence** (the source circles a
dead place, names its character, and never fixes *where* it is), plus whatever
true leads the source genuinely holds. A dead-zone location is learned only
through canon-authored discovery — footwork and on-site detection at the real
coordinates, or a canon lead that legitimately carries the position — never
fabricated, and never surfaced through a source that lacks it. A location
surfaced this way that contradicts the canon geography (routes.md, the location
files) is a canon-violating leak the party will spend real, wasted effort
acting on.
