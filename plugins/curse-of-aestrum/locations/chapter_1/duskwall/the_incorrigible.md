---
id: loc_the_incorrigible
name: The Incorrigible
type: ship
parent: loc_duskwall
curse_affected: conditional
loop_trapped: conditional
npcs_present: [npc_rylin_tsarran, npc_rick_hastley, npc_baldric, npc_emmo_durast, npc_wren_calvert]
---

## Description

A Calimshan brigantine — two-masted, square-rigged on the foremast, fore-and-aft on the main, built for speed over cargo volume. Typically crewed by a captain and 7–8 hands; currently running lean. Key crew: Drow first mate Rylin T'Sarran (de facto captain; Erethezra operative), Baldric (Able Seaman), Rick Hastley (Ordinary Seaman), Emmo Durast (Topman), and Wren Calvert (Helmsman).

## Arrival Sequence

The Incorrigible arrives on **Day 9**. Its arrival is not deliberate — maritime protocol requires check-in at the nearest available port when a captain dies at sea. Aestrum was the nearest port.

**Timeline:**
- The captain died before the ship crossed into Aestrum's boundary. He was committed to the sea shortly after death — maritime custom when a captain is lost days from port, and a decision Rylin made promptly (see [`rylin_tsarran.md`]({{PLUGIN_ROOT}}/npcs/chapter_1/rylin_tsarran.md)). No body entered Aestrum. He was never snapshotted and is permanently gone.
- The ship anchors just off the Duskwall docks around **10:00 PM**.
- **Midnight:** The curse snaps a snapshot of the crew — but only if the cycle is still active. If the cycle has already been broken, no snapshot is taken and the crew never becomes loop-trapped.
- **Day 10 morning:** Rylin and Baldric offload the cargo onto the waterfront.

Everything from the offload forward depends on campaign state at the time of arrival.

## Loop Entrapment

*Only applies if the cycle is active on Day 9.*

Each evening around 11:00 PM, the ship attempts to depart Duskwall's harbor. It strikes an invisible physical barrier on open water, the hull fails, and the ship sinks with all hands. The crew resets at midnight to their snapshot position — anchored just off the docks — with no memory of the sinking. This repeats each night until the cycle is broken.

*If the cycle was already broken before Day 9:* The ship arrives, anchors, concludes its business, and departs normally. The crew is never snapshotted. There is no loop.

## Cargo

The hold contains approximately **256 vials of alchemist's fire** (1d4 damage each). Rylin arranged a buyer prior to arrival. Baldric assists with the offload on Day 10 morning.

**Buyer — conditional:**

- **If Luca is alive and Evandur is still Duke:** Luca will learn of the alchemist's fire and move quickly to acquire it. He approaches the waterfront transaction disguised as an elderly man via the Mirror of Illusion, preventing the deal from being traced back to The Shrikes. The crates pass to Luca's men and are moved toward the castle.
- **If no buyer is found** (Luca is dead, deposed, or otherwise unavailable): the cargo is treated as unsold. Rylin re-loads it onto *The Incorrigible* and departs with it.

**If the cargo is re-loaded while the cycle is still active:**

The ship departs in the evening, strikes the barrier at sea, and sinks. The alchemist's fire detonates on impact — a catastrophic explosion, far larger than any castle maze detonation, visible across the entire harbor. The crew resets at midnight as normal. The explosion does not persist.

## Waterfront Market Effect

*Conditional on the cycle being active and a buyer having been found.*

While the cycle is running after The Incorrigible's arrival, alchemist's fire becomes available as a purchasable item at the Waterfront District. The daily reset recreates market conditions; secondary stock cycles through waterfront vendors each morning. A character who knows to look for it can acquire it there.

*If the cycle was already broken before Day 9:* The cargo sells once and is absorbed by whoever buys it. No market availability results.

## Crew Details

**Emmo Durast and Wren Calvert:** Both joined within the last three months in Calimshan — Emmo as topman replacing two hands who withdrew before the contraband run, Wren as helmsman after her previous vessel was held by port authorities. Neither has strong loyalties or visible grievances. They consider Rylin a capable officer: precise, fair, does not give an order twice. Rylin has made no intelligence use of either. Full entries: [`emmo_durast.md`]({{PLUGIN_ROOT}}/npcs/chapter_1/emmo_durast.md), [`wren_calvert.md`]({{PLUGIN_ROOT}}/npcs/chapter_1/wren_calvert.md).

**Baldric and Rick rank dispute:** Rick holds Ordinary Seaman; Baldric holds Able Seaman. Rick argued for Ordinary Seaman believing it sounded more distinguished. Able Seaman outranks Ordinary Seaman. Rick has spent years lording the title over Baldric. Neither Baldric nor Rylin has ever corrected Rick.

**Baldric's name origin:** His given first name is also Rick. The crew began calling them "Rick" and "Bald Rick" — a reference to Baldric's hairlessness. Baldric heard "Bald Rick" as "Baldric," adopted it as a proper name, and has never connected the nickname to his bald head.

## DM Notes

**Escape route — conditional on the cycle being broken:**

The Incorrigible is the primary planned escape route from Aestrum at the Chapter 1 endgame. This is only viable if the cycle has been broken before or during Day 9 — a loop-trapped ship sinks each night and cannot fulfill passage. Passage terms once the cycle is clear: 5 gold per person, flat rate, non-negotiable. Rylin does not haggle.

**Voyage intelligence goals:** See [`rylin_tsarran.md`]({{PLUGIN_ROOT}}/npcs/chapter_1/rylin_tsarran.md) for Rylin's full handling — what he wants from the party during the voyage and how he extracts it.
