---
id: quest_the_assassination_of_duke_tallwood
codex_name: "The Heist"
codex_name_updated: "The Murder of Evandur Tallwood"
codex_name_update_trigger: party_learns_shrikes_true_objective
type: main
related_npcs: [npc_luca_lucretius_tallwood, npc_evandur_tallwood, npc_haladon]
related_locations: [loc_castle_vault]
---

## Overview

The true objective behind The Shrikes' castle infiltration, masked as a vault heist. The Shrike team bypassed the vault and headed toward the Duke's quarters. This creates a moral dilemma for the party: risk their safety to save a man destined to die and reset with the time loop, or focus on their own escape and preservation of resources.

## DM Notes

Evandur dies each night in the castle ambush by the Setland advance expedition — he resets each morning with no memory of it. The Shrike team's assassination attempt, if it had succeeded, would simply have been another death he reset from.

### Timed-event schema

Per [time_and_events.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/time_and_events.md), the nightly castle ambush is a **world-state moment** the party may witness, prevent, or arrive after:

- **`time:`** 11:30 PM exactly (Aestrum-local). The advance expedition's strike is timed to the duke's nightly transit between his study and his quarters; the ambush opens the instant he reaches the corridor.
- **`duration:`** ~3 minutes from the first blade drawn to Evandur dead on the floor. The fight is one-sided — he is not equipped to survive a coordinated professional team — and the Shrikes' contingency window is similarly tight.
- **`catchup: none`** — the ambush is the moment. A party that arrives at 11:33 PM finds the corridor as it was left: the duke dead, the strike team gone, the household just beginning to react. They may investigate, but they cannot re-enter the ambush itself. Arriving at 11:30 sharp puts them in the corridor with the strike team; arriving at 11:29 gives them the slim window to warn or shield Evandur before it begins.
- **The 12:00 AM Sleep step fires regardless.** Even if the party prevents the ambush, Evandur's snapshot reverts him at the next reset — and the strike team's snapshot puts them back in position for the following night. Both are loop-bound.

Luca's actual motivation is revenge for The Survivor explosion and a desire to reclaim his duchy. His Chapter 2 arc involves Setland leverage and the question of legitimate succession. The vote mechanics and "the new obstacle" pattern are documented in [luca_lucretius_tallwood.md]({{PLUGIN_ROOT}}/npcs/chapter_1/luca_lucretius_tallwood.md).
