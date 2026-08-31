---
id: quest_ducats_for_the_party
name: Ducats for the Party
type: side
related_npcs: [npc_luca_lucretius_tallwood, npc_malak_du_leon, npc_aidra_calemthor, npc_galadiil_ilphekiir]
related_locations: [loc_castle_vault]
---

## Overview

The third path through the Duskwall vault: the party keeps the gold for
themselves. This quest exists as the implicit alternative to handing the vault
contents to Luca ([Ducats for the Flock]({{PLUGIN_ROOT}}/quests/chapter_1/ducats_for_the_flock.md)) or to a
Setland representative ([Ducats for the Duchy]({{PLUGIN_ROOT}}/quests/chapter_1/ducats_for_the_duchy.md)).

The vault resets each morning and any wealth carried into a dead zone stays
there permanently, so "keeping it" is mechanically trivial — what's at stake is
the *refusal* of the other two claims.

## Lifecycle

- **Trigger:** The moment the party enters the vault chamber proper (not the
  maze approach).
- **Complete:** Either of the other two Ducats quests fails (the party explicitly
  declines both Luca and Setland), OR the other two complete in a way that still
  leaves vault wealth in party hands.
- **Fail:** The party fully discharges their gold to Luca or to Setland, closing
  out one of the other two Ducats quests at the party's expense.

## The Ducats Trilemma

Only one of the three Ducats quests can resolve as `completed` per campaign
instance. The same gold cannot be in two places. The matrix:

| Outcome | Flock | Duchy | Party |
|---|---|---|---|
| Party gives vault contents to Luca | completed | failed | failed |
| Party gives vault contents to Setland (Aidra/Malak) | failed | completed | failed |
| Party declines both | failed | failed | completed |

All three resolutions unlock the shared badge **Ducat or Leave It** (see
[badges/side_quests.md]({{PLUGIN_ROOT}}/badges/side_quests.md)).

## DM Notes

This quest is largely bookkeeping — it doesn't need its own narrative beats. Its
purpose is to make the "keep it" branch a tracked outcome rather than a default,
so the achievement fires cleanly and the campaign codex reflects what actually
happened.
