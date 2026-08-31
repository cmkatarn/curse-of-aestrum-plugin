---
id: rule_item_persistence
name: Item Persistence
type: homebrew_rule
related_rules: [rule_searches_and_loot]
---

## Overview

How taken items behave across time in the game.

**Default 5e:** items the party takes are permanently theirs. Containers and bodies that have been looted stay looted. Generated loot rolled once is the contents from then on; the desk does not become a random-number generator each time it's opened.

Settings with reset / loop / time-rewind / memory-wipe mechanics need to specify what happens to items at each reset event. The default is silent unless the override addresses it.

---

## Generic Defaults

- **Mundane items stay where they're put.** If the party takes the coin, the coin is gone from the location until someone puts coin back.
- **Generated loot is fixed once rolled.** The first time the party searches a container and produces a result (e.g., an Investigation roll yields 20 gp and a chipped silver locket), that result becomes the permanent contents of the container for every future visit. Record it in working memory and in the conversation save; do not re-roll on revisit.
- **Unique objects are unique.** A signet ring, a named relic, a one-of-a-kind document does not respawn or duplicate. If the party takes it, the original location no longer has it.
- **Magical items are tracked individually.** Their location, attunement state, and any charges are part of the conversation save.

---

## Reset-Aware Settings

If the consuming game has a periodic reset mechanic, the override specifies the persistence rules. The questions the override must answer:

1. **What does a reset restore?** All taken items, only some categories, none?
2. **What prevents restoration?** Are there shelter zones, persistence anchors, runed objects, attuned wielders, or other mechanisms that exempt items from the reset? If so, what is the exact rule that determines whether a given item is exempt?
3. **What happens to recreated copies?** When the reset puts an item back at its origin while the party still holds the original, does the new copy carry the same enchantments, become inert, or behave some third way?
4. **What's the test moment?** At what point in the reset cycle is the exemption evaluated — based on the item's physical location, the carrier's location, both? What if the item and the carrier are in different states?
5. **How does generated loot behave across resets?** Does the "fixed once rolled" rule above still hold across cycles, or does each cycle roll fresh?

The override should write a setting-specific item-persistence file answering these questions concretely. The engine version of this file is the default behavior absent any such override: items stay where they're put.

---

## Stacking and Bookkeeping

If the party exploits a persistence loophole or a generated-loot lock to accumulate wealth, track the accumulation. Exploits are features when they're earned by playing the mechanics correctly — only flag them when they've begun to deform the campaign's economic assumptions, and surface in conversation save notes rather than nerfing the cache silently.
