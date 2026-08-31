---
id: quest_breaking_the_cycle
name: Breaking the Cycle
status: active
type: main
related_npcs: [npc_rowan_deckard, npc_hati_heldrivver, npc_judith_asemyeer, npc_delmuir_goodfeet]
related_locations: [loc_shrine_of_selune, loc_misty_forest_shrine]
---

## Overview

The party is trapped within Aestrum in a repeating daily cycle that resets at midnight.

**Known reset effects (timed sequence — canonical order per [time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md)):**
- **12:00 AM** — Sleep (forces unconsciousness)
- **1:30 AM** — Resurrect/Recreate (restores creatures and objects to start-of-day state)
- **3:00 AM** — Teleport (moves sleeping individuals to their reset point)
- **4:30 AM** — Modify Memory (wipes the day's memories — must run after Recreate)
- **6:00 AM** — Wake (removes Sleep effect)

Each step is a world-state moment with `time:` exact, `duration: instant`, `catchup: none` per [time_and_events.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/time_and_events.md) — the full schema lives in [time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md).

**Protections:**
- Moon Amulets protect against Modify Memory
- Pendant of the Waking Hours protects against Sleep

## DM Notes

**How the loop is broken:** All qualifying prayers must be prevented that day — every prayer giver must be stopped before they pray. Destroying both anchor shrines (the Shar statue in the Duskwall Selûne shrine AND the effigy Rowan built at the Misty Forest shrine) achieves this by removing Shar's ability to hear the prayers, but the shrines are not the only path — preventing the prayers directly works equally. Both shrines reset each morning.

**Why Shar can't simply stop the party:** Maintaining the loop is a monumental effort even for a god. Shar is resource-strained. Any direct action against the party risks losing her grip on the cycle entirely.

*Planned narrative hint: Rowan will be found deep in prayer when the party arrives at the forest dead zone — an organic moment to begin conveying the significance of prayer.*

**True origin:** Shar created the loop deliberately — a precision divine trap constructed around Miri Amblecrown's presence in Aestrum. See `{{PLUGIN_ROOT}}/lore/key_lore_summary.md` for the full strategic picture.
