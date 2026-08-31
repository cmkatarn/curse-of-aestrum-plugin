---
id: rule_searches_and_loot
name: Searches and Loot Generation
type: homebrew_rule
related_rules: [rule_item_persistence]
---

## Overview

Rules for resolving a search of a location, body, container, or area for valuables. Covers what to do with declared loot, how to generate loot on the fly when nothing is declared, the d20 band for search rolls, and constraints on seeding magical items.

If the consuming game has reset / loop / persistence mechanics that affect taken items, those interactions live in the game's override or in [item_persistence.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/item_persistence.md).

---

## The Honest-Resolution Principle

Resolve a search honestly — generate a result or return nothing based on whether the place could plausibly hold anything worth finding. A player who searches the side of a country road for treasure finds dirt. A player who searches a noble's bedchamber finds at least *something*. Don't reflexively reward looking; reward looking *where it makes sense*.

---

## Declared Loot

If the location file (or a linked container file) declares specific loot — a `treasure:` set, a named cache, a particular item — use it as written.

A declared cache may be flagged as **obvious** or **hidden**:

- **Obvious declared loot** is handed over on a successful search regardless of roll quality. The fact that the coin pouch is on the body is not in doubt.
- **Hidden declared loot** still requires a roll into the right band. A location whose *only* declared treasure is a false-bottom strongbox under the floorboards is not a guaranteed find — a low roll yields the surface-level scraps from the generation rules below and nothing more. The hidden item remains in place until someone rolls well enough to find it (or pries the floor up explicitly, which bypasses the roll).

When in doubt about whether a declared item is obvious or hidden, ask what an unaided sweep would reveal. Coin on a corpse: obvious. The signet ring hidden in the corpse's boot heel: hidden.

---

## Generating Loot On the Fly

For any reasonable search target without a declared set, build the result from three inputs:

1. **Location appropriateness.** What would plausibly be here? A merchant's desk: ledgers, coin, correspondence, a sealed letter. A guard barracks: weapons, rations, dice, a flask, a half-finished letter home. A noble bedroom: jewelry, a hidden compartment, perfumed garments. A monster's lair: bones, half-eaten gear from prior victims, the occasional unusual find dragged in.
2. **Thematic fit.** Match the campaign feel of the location. A dark-god shrine yields nothing of cheer — dark fabric, obsidian, a torn page of liturgy. A moon-goddess shrine carries silver, moonstones, prayer beads. A serpent-cult temple has scale-and-snake motifs through every piece. Faction-aligned spaces drop faction-marked items. The loot should *tell* the player where they are.
3. **The player's search check.** Use the appropriate 5e skill for what they're actually doing — **Investigation** for deliberate sifting through contents (drawers, papers, a body's pockets), **Perception** for noticing what's out of place at a glance (a loose flagstone, a seam in the wainscoting).

---

## The Roll

When the player has a known modifier, roll `d20 + skill modifier` once for the search and read the band:

| d20 + modifier | Quality outcome |
|----------------|-----------------|
| ≤ 5 | Scraps. A few coppers, a broken tool, a stained rag. Just enough to confirm someone lived here. |
| 6–10 | Mundane utility. Modest coin, a usable tool, ordinary gear in serviceable condition, an unremarkable document. |
| 11–15 | Notable. A meaningful sum, a quality item, a clue or readable correspondence, a small piece of jewelry, a single dose of a useful consumable. |
| 16–19 | Exceptional. A substantial cache, a fine item, a piece of intelligence with leverage, possibly a low-tier magical item if location-appropriate. |
| 20+ | Remarkable. A real find — significant wealth, a notable magical item, or a story-relevant secret. |

- On a **natural 1**, the search disturbs something — a trap triggers, an occupant notices, an item breaks in their hands.
- On a **natural 20**, push to the top of the band and consider revealing a *second*, hidden item the player did not specifically ask for.

---

## No Modifier, No Roll

If the player has not provided a modifier for the relevant skill, **do not roll.** Pick a result from the 11–15 band and present it as fact. Do not ask for a modifier mid-attempt; if the player wants rolls, they'll provide the number.

**Hidden declared loot still requires a roll** — a player who hasn't rolled hasn't found the false-bottom strongbox, even if generation defaults handed them the surface scraps.

---

## Don't Gate on Dice for the Obvious

A player searching a kitchen finds kitchen things without a roll. The d20 governs *how much*, *how notable*, and *whether anything hidden surfaces* — not whether the obvious is visible. State plain findings as fact; reserve the roll for the loose floorboard, the false bottom, the sealed letter under the mattress.

---

## Magical Items

Magical items are acceptable when they fit the location (a wizard's tower, a temple vault, a powerful enemy's body, an ancient cache). They must:

- Match the place's flavor and the cultural source of the loot.
- Sit at or below the party's current power level. Never seed an item that breaks an upcoming encounter — no boss-killing weapons, no save-or-die effects, no mass-clear AoE for a low-level party, no consumable that trivializes a planned set-piece. When unsure, prefer flavor items, consumables, or items with strong narrative use and modest mechanical effect.
- Be hand-named and described, not pulled from a generic table. Even a +1 dagger deserves a sentence about whose initials are scratched into the pommel.

For what happens to a recovered magical item in games with reset / loop mechanics, see the game's override or [item_persistence.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/item_persistence.md).
