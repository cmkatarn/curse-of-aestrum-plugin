---
id: rule_item_persistence
name: Item Persistence Across Resets
type: homebrew_rule
related_rules: [rule_time_loop, rule_dead_zones, rule_revert, rule_snapshot, rule_magic_immune_runes]
---

## Overview

This campaign has a built-in farming risk. Players can — and will — return to the same location across multiple loop resets and reasonably expect the treasure to be there again. The rules below codify how the loop actually behaves around items the party finds, takes, and tries to keep. Hold them consistently and let the players exploit what is genuinely exploitable.

The general principle: the loop preserves the start-of-day snapshot for every container, body, and location. Items removed during the day are restored at the [Recreate step (1:30 AM)]({{PLUGIN_ROOT}}/rules/time_loop.md#recreate-mechanics) unless something interferes. Dead zones — and items that are themselves dead zones — are the only interference that works.

---

## Mundane Wealth Resets Every Loop

Coin, gems, sellable goods, and ordinary gear are snapshot contents. A purse looted on Day 6 is back on Day 7. This is intentional, part of the cycle's texture, and a legitimate source of party funding. Do not invent reasons for these caches to be empty just because the players are smart.

---

## Generated Loot Is Fixed Once Rolled

The first time the party searches a given container or area and produces a generated result — e.g., an Investigation roll yields 20 gp and a chipped silver locket in a tavern desk — **that result becomes the permanent contents of that container for every future visit, every future cycle.**

- Record it in working memory and in the conversation save.
- The next day's snapshot of that desk is the snapshot that existed the moment of the first search: 20 gp and a locket.
- Do not re-roll it. The desk does not become a random-number generator just because the party keeps opening it.

---

## Magical Items

The loop fights for the snapshot. The item's physical location at 1:30 AM is what decides the outcome.

### The Determining Rule

**Where is the item at the moment Recreate fires?**

- **Inside a dead zone (or inside a runed container, which is itself a dead zone):** the item is invisible to Recreate. It stays where it is. The party retains it.
- **Outside any dead zone:** Recreate restores the item to its original location and removes it from wherever it currently is — including from a player's inventory.

The carrier's status is irrelevant to the item. A player can stash an item inside a dead zone and themselves sleep outside; the item still persists in the zone. A player who carries an item with them must keep *the item* in a dead zone at 1:30 AM. The common case — player shelters in a dead zone with the item on their person — is just the most convenient way to satisfy the rule, not a separate mechanic.

### Practical Consequence — The "Carrier-Reset" Case

If a player has been preserving a magical item across multiple days by carrying it with them into a dead zone each night, and one night they sleep outside a dead zone while still carrying the item, **the item is outside any dead zone at Recreate and snaps back to its original location.** The party must re-acquire it the same way they did the first time.

This is not a separate clawback mechanism — it is the determining rule applied to the typical carry-with-me preservation pattern. A single missed night cancels every preceding night of protection, because protection has always been per-night and per-location.

### Inert Copies

When a magical item is preserved (in a dead zone or otherwise kept outside the loop's reach), Recreate still acts on the original location: the snapshot regenerates **an inert copy** of the item there. This is the same Recreate behavior described in [time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md#recreate-mechanics): the physical object is recreated; the enchantment is not.

- Inert copies are visually and physically identical but drained of magical energy. They cannot be activated, attuned, or sold as magical. A merchant who can tell will say so; a merchant who cannot will pay for it as a curio at best.
- Inert copies behave like generated loot from this point forward: the copy is now permanent snapshot contents for that location, present on every revisit.
- If the party loots an inert copy and protects it like a magical item, no further copy is generated — there is no magic in the copy for the loop to perpetuate.

---

## Magic-Immune (Runed) Items

A magic-immune runed item is itself a localized dead zone the size of the object (see [magic_immune_runes.md]({{PLUGIN_ROOT}}/rules/magic_immune_runes.md)). The cycle cannot act on it directly. This is a separate persistence path from the dead-zone-shelter path described above, and it behaves differently in three ways:

1. **The runed item never moves at reset.** It does not recreate at its original location. It stays exactly where it physically is at midnight. If a player is carrying a runed sword and sleeps outside a dead zone, the player teleports to their reset point at 3:00 AM; the sword stays where the player was sleeping. (The player wakes up at the reset point with no memory of the sword; the sword is wherever they left it.)
2. **The runes do not protect the carrier.** A runed item is a dead zone *for itself only.* It does not project a field. A character carrying a runed sword is still subject to Sleep, Recreate, Teleport, and Memory Revert normally — they just keep the sword.
3. **A runed container protects what is inside it.** A non-runed magical item placed inside a runed box (like Aliss's dead box) is physically inside a dead zone for purposes of the determining rule above. This is the cleanest way to preserve a captured magical item without dragging the carrier's behavior into it.

No inert copy is generated for a runed item, because the item was never pulled from its location in the first place — Recreate had nothing to restore.

---

## Unique Non-Magical Objects

Named documents, signet rings, relics keyed to a story role, and other unique non-magical items follow the same item-location rule as magical items — they reappear at the original location after a reset unless they are physically inside a dead zone (or are themselves runed) at 1:30 AM.

These items do **not** generate inert copies. They simply reappear, fully themselves.

---

## Stacking and Bookkeeping

If the party hits the same merchant's strongbox twelve cycles in a row for 50 gp each time, that is 600 gp in their pocket. Track it.

If the party's funding is starting to outpace what the campaign assumes, that is information for the DM — surface it in conversation save notes rather than nerfing the cache silently. The exploit is a feature; only flag it when it has begun to deform the campaign's economic assumptions.
