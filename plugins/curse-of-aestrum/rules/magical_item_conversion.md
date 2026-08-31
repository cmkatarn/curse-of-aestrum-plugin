---
id: rule_magical_item_conversion
name: Magical Item Conversion (Essence Extraction)
type: homebrew_rule
related_items: [misc_items (Loadstone), pendant_of_waking_hours, akadis_abarkas]
related_npcs: [npc_aliss_perisdottir (husband), npc_mazikeen]
---

## Overview

A skilled enchanter can extract the magical essence of an item and bind it to one or more new vessels. The source item is **consumed** in the process. The resulting items carry either the full effect (if undivided) or a weakened protective form (if split among multiple wearers).

This rule exists to allow the party to convert existing magic items into protection against specific steps of Shar's reset cycle.

---

## The Core Tradeoff

An undivided conversion produces **one item with full immunity** to the relevant cycle step — the step simply does not apply to that wearer.

Splitting the essence among N items means each wearer has only **partial protection** — they must succeed on a Constitution saving throw at the moment the cycle step triggers each night. The more ways the essence is split, the harder the save. A failed save means the step applies to that wearer normally that night.

| Output Items | Protection |
|---|---|
| 1 (undivided) | Full immunity — no roll required |
| 2 | DC 12 Constitution save each night |
| 3 | DC 13 |
| 4 | DC 14 |
| 5 | DC 15 |
| 6+ | Too diffuse to bind reliably — not feasible |

The save is silent to the character on failure. They simply wake at their reset point with no memory of the night.

---

## Crafting Time

One "day" is one full loop iteration. Work must be stored in a **dead zone** before midnight each night or it resets. Loop-aware crafters (Aliss's husband) handle this naturally.

The bulk of the labor is the initial extraction and setup — binding additional vessels is incremental once underway.

- **Protection conversions** (binary effects): **1 day**, regardless of how many items are produced
- **Quantitative conversions** (divided effects): **2 days**, regardless of how many items are produced

---

## Who Can Perform This

### Aliss's Husband (Misty Forest)
Skilled smith and enchanter working out of the ground floor of Aliss's house. Loop-aware through Aliss (she tells him each morning after reading the dead box). Access to the dead box means in-progress work persists across resets. Motivated to help if the party has earned Aliss's trust; may work at or near material cost.

### Mazikeen (Mazikeen's Magicka, Duskwall)
Enchantment transfer is an established service at Mazikeen's Magicka; these conversions extend it. Mazikeen is not loop-aware and won't understand why the party wants this, but won't refuse a paying commission. Multi-day work is the party's problem — they should arrange dead zone storage for in-progress items. Standard markup is 30%; at best, Mazikeen will reduce this by 20 points (to ~10% above cost).

---

## The Three Conversions

### The Loadstone → Protection from Teleportation

See: [misc_items.md]({{PLUGIN_ROOT}}/items/chapter_1/misc_items.md) — *The Loadstone*

**What's lost:** All active properties — the six daily item-teleportation charges, line-of-sight cargo movement. The Loadstone is destroyed.

**What's gained:** N items (amulet, brooch, ring, or any small item) whose wearers cannot be teleported against their will — including by the cycle's **3:00 AM Teleport step**. Apply the splitting mechanic above.

**Item name suggestion:** *Shard of the Loadstone*

**Attunement:** Required.

**Note:** The Loadstone is currently held by Delmuir Goodfeet. The party must acquire it before this conversion is possible.

---

### Pendant of Waking Hours → Protection from Sleep

See: [pendant_of_waking_hours.md]({{PLUGIN_ROOT}}/items/chapter_1/pendant_of_waking_hours.md)

**Removing the PoWH first:** The pendant's irremovable property is suppressed inside a dead zone. Thagnog can take it off while standing within one — no special procedure or additional cost.

**What's lost:** The pendant itself (destroyed). The irremovable property does **not** transfer — that was Lisandre's deliberate modification, not the core enchantment.

**What's gained:** N items whose wearers cannot be magically put to sleep — including by the cycle's **12:00 AM Sleep step**. Apply the splitting mechanic above.

**Item name suggestion:** *Band of Waking Hours*

**Attunement:** Required.

---

### Akadi's Abarkas → Distributed Speed

See: [akadis_abarkas.md]({{PLUGIN_ROOT}}/items/chapter_1/akadis_abarkas.md)

**What's lost:** The Abarkas themselves (destroyed). Theren loses the 8× speed bonus.

**What's gained:** N items (must be **footwear** — boots, sandals, greaves), each carrying an equal share of the 8× multiplier. The splitting mechanic above does not apply here — speed is already a quantitative effect, so distributing it is the natural weakening.

**Item name suggestion:** *Sandals of Akadi's Step* / *Akadi's Fragment*

**Attunement:** Required per item.

**Stopping Save:** The original Abarkas required a DC 13 Dexterity save to stop cleanly because of the extreme speed involved. This save only applies when a split item's speed bonus exceeds **+40 ft over the wearer's base movement**. At or below that threshold, no save is required.

| Split | Per-Item Multiplier | Extra Speed (base 30 ft) | Stop Save |
|---|---|---|---|
| 2-way | 4× | +90 ft | DC 11 |
| 3-way | ~2.67× | +50 ft | DC 9 |
| 4-way | 2× | +30 ft | None |
| 5-way | 1.6× | +18 ft | None |

---

## Pricing

Base costs reflect fair-market material and labor — what Aliss's husband would charge at cost.

### Protection Conversions (Loadstone or PoWH)

| Output Items | Base Cost | Mazikeen (at best, +10%) |
|---|---|---|
| 1 (undivided) | 600 gp | 660 gp |
| 2 | 800 gp | 880 gp |
| 3 | 1,000 gp | 1,100 gp |
| 4 | 1,200 gp | 1,320 gp |
| 5 | 1,400 gp | 1,540 gp |

Cost increases with N because each additional binding is its own enchantment step, even if the extraction is shared.

### Abarkas Speed Distribution

| Split | Base Cost | Mazikeen (at best, +10%) |
|---|---|---|
| 2-way | 900 gp | 990 gp |
| 3-way | 1,200 gp | 1,320 gp |
| 4-way | 1,500 gp | 1,650 gp |
| 5-way | 1,800 gp | 1,980 gp |

---

## DM Notes

- **Nightly save timing:** Constitution save fires at the moment the cycle step triggers. Characters are not aware they failed — they simply wake at their reset point.
- **Non-attuned wearers:** Not protected. The essence is bound to the attuned wearer.
- **DC calibration:** If DC 12 feels too easy for 2-way splits at the table, shift all DCs up by 2. If too punishing, shift down by 2.
