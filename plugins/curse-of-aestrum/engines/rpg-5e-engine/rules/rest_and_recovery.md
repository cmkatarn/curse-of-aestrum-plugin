---
id: rule_rest_and_recovery
name: Rest and Recovery
type: core_mechanic
related_rules: [rule_active_effects_tracking]
---

## Overview

Standard 5e rest rules apply. Settings with reset / loop / time-rewind / memory-wipe mechanics may modify what recovery a long rest actually grants (and where it can be taken) — those modifications live in the game override, not in this file.

---

## Short Rests

- **RAW timing.** A short rest is one hour of in-fiction light activity.
- **Player-declared.** The DM does not auto-offer short rests. The party calls for them; the DM resolves availability based on the scene (combat ongoing, pursuit, time pressure).
- **Hit dice spending and short-rest abilities** (Warlock slots, Action Surge, Channel Divinity uses, etc.) follow RAW.

---

## Long Rests

- **RAW timing.** 8 hours, at least 6 of which must be sleep (or species-equivalent rest).
- **RAW recovery.** Full HP restored. All expended spell slots restored. Half the PC's total hit dice (minimum one) restored. Exhaustion reduced by one.
- **One long rest per 24-hour period.**
- **RAW interruption rules apply** (1+ hour of strenuous activity breaks the rest).

---

## Setting Modifications

If the consuming game has reset / loop / shelter-zone / snapshot mechanics, the game override specifies how (and where) long rests function. The override is the single place to look for rules like:

- "A long rest only counts if taken in a specific kind of location."
- "HP / slots / hit dice / exhaustion follow a snapshot-revert model rather than a long-rest recovery model."
- "Resources granted by a long rest evaporate at the next setting-defined cut."
- "Sleep is forced regardless of player choice at a specific time."

Absent any such override, RAW applies.

---

## Exhaustion

Exhaustion tracking follows [active_effects_tracking.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/active_effects_tracking.md) and RAW reduction-by-long-rest. The override may modify reduction conditions for settings with snapshot mechanics.
