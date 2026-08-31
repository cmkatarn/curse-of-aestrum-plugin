---
id: loc_castle_vault
name: The Castle Vault / The Maze
type: dungeon
parent: loc_duskwall
connected_locations: [loc_duskwall]
curse_affected: true
dead_zone: false
designed_by: miklas_of_thundertree
npcs_present: []
infinite_wealth_exploit: true
---

**Luca is never personally here.** The Shrikes reach the vault through Haladon's
infiltration team; Luca directs the operation and does not walk it. (An
`npc_luca_via_agents` placeholder previously sat in this roster — it named no one and
has been removed.)

**Haladon and the Shrike team are not here during the day.** They arrive in the
**evening** for the maze run; their anchor is [the waterfront warehouse]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/waterfront_warehouse.md),
which is where they are found the rest of the time. `npcs_present` reflects the anchor,
not the raid.

## Overview

A vault and escape route complex carved into the cliffs beneath Duskwall Castle. Designed by Miklas of Thundertree, the former vizier to Duke Lognan Tallwood. Lognan commissioned the maze as a secret escape route; Miklas built it so labyrinthine it defeats its own purpose twice over — the doors grow increasingly difficult to open the closer you are to the castle exit, and a fleeing Duke would still have to solve a procedurally shifting puzzle under duress. Lognan had Miklas's role stripped and imprisoned him for decades. Evandur freed Miklas after Lognan's death; Miklas wandered Duskwall broken until Luca recruited him. The map he provided was useless. Luca killed him in Shrike fashion. Miklas's death and the failed map prompted Evandur to post two guards with an alarm pyre at the exterior cliff face entrance — the Entrance Hall at row 0.

The vault itself is a separate door at the far end of the barracks corridor, distinct from the maze entrance. It has a minor lock. The vault's cut-stone corridors and door frames are Dalihad work — precise, interlocking, fitted to exacting tolerances.

Evandur keeps three maze keys and three maze tokens hidden in his private quarters as escape supplies. Galadiil procured one of each.

## Maze Structure

**Grid:** 7 rows (0–6) × 5 columns. Each tile may contain 1–3 exit doors, one per wall maximum. Doors are the only exits; walls without doors are solid stone.

- **Row 0 (Entrance Hall):** Exterior cliff face entrance. The Entrance Hall tile has one entrance from outside (no mechanism) and three exit doors — one advancing forward into row 1, two advancing sideways into adjacent row 0 tiles. Not locked from outside. Two Setland agents are posted here disguised as Duskwall guards — the real guards Evandur posted here after Miklas's map surfaced in hostile hands. The agents kill and replace them each morning.
- **Row 6 (Exit room):** Center tile. A handle-only door on the castle-facing wall — no mechanism, opens freely from either side into the barracks corridor. The corridor beyond is unguarded and empty under normal conditions.

**Direction of travel for the heist:** Enter at row 0 (exterior Entrance Hall), navigate toward row 6 (corridor connection, vault access).

## Door Mechanics

Each internal door has a three-tumbler mechanism: a handle, a keyhole, and a token slot.

**Sequence when approaching a door:**
1. Turn the handle → the mechanism rolls for locked state
   - Row 0: 0% locked. Each row increases by ~10%. Row 6: 60% locked.
2. **If locked:** Nothing happens. The door suggests itself as stuck. Insert a key → key unlocks the door and fuses permanently into the mechanism (single use, irreversible). Proceed to step 3.
3. **If not locked (or now unlocked):** The three tumblers cycle through available rooms and stop after one second, displaying the selection pool.
4. **Optional — insert a token:** Re-rolls the three available rooms (token consumed, slot closes). Can only be done before committing.
5. Push the desired tumbler → mechanism deactivates, door opens to the selected room.

**Items:**
- **Key:** Unlocks one locked door. Fuses into the mechanism on use — single use, cannot be retrieved.
- **Token:** Re-rolls the room selection pool. Consumed on use.
- **Maul:** Opens chests. Can shatter Schist rock (see The Cave-in).
- **Spade:** Required to open holes.

## Room Archetypes

- **Red:** Potentially dangerous effect.
- **Green:** Always unlocked. Roll 1d6 for contents: 1 Nothing, 2–3 Chest, 4 Hole, 5 Maul, 6 Spade. Chests require Maul; Holes require Spade. Both yield on d12: 1–4 Nothing, 5–11 Key, 12 Token.
- **Orange:** Straight corridor. Small chance of key or token.
- **Yellow:** Single exit (90-degree corridor). Roll 1d6: 1–2 Nothing, 3–4 Key, 5–6 Token.
- **Blue:** Cold. Exits are frozen shut — must be melted; forcing breaks the mechanism. High potential for key or token.

## Seeded Rooms

### Red
**The Cross / The Double-Cross:** A four-door room — one ingress, three exits — forming a cross shape. The mechanism displays the name *The Cross* before entry. All exit doors are locked. The trap springs as soon as any member advances substantially into the room — the ingress door closes and locks behind them, potentially separating the party. The mechanism updates to display *The Double-Cross*.

**The Cave-in:** Dead end. A crack in the far wall offers a view of the exit on the other side. The rock is Schist — a character with relevant knowledge (Thag) recognizes it as brittle under blunt force. The crack can be expanded enough to pass through using the Maul.

**The Void:** Complete darkness — no non-magical light functions. The tumblers cycle but the party cannot see which room they are selecting. *DM only: this room is not a simulacrum of Shar's realm — it IS a pocket of Shar's actual domain. Any character who enters has physically set foot in Shar's realm.*

**The Dead-end:** A vertical coffin stands at the far wall. A skeleton spawns every minute. Defeated skeletons re-animate when the next one spawns.

**The Furnace:** Opening this door deals 1d10 fire damage to all characters in the adjoining room. If this room is built adjacent to any room with frozen doors, all ice in that room melts.

### Blue
**The Drain:** A damp, moldy room with a large floor grate (spacing ~one foot). Characters with Darksight who examine the grate see a skeleton and a shield below. After one minute, a Gelatinous Cube oozes up through the grate. *The cube contains a lion shield belonging to a Setland expeditionary soldier — permanently dead, the only physical trace of their passage.*

**The Ice Box:** All exits are frozen shut. Attempting to free them with the Maul breaks the tumbler mechanism. If The Furnace is built adjacent, all doors thaw and unlock.

**Frigida Dura Veritas:** *[ARCHIVED — not seeded in text-based campaigns. Retain for in-person use.]* The first character to enter is mirrored as a simulacrum and may no longer speak as themselves — only as the simulacrum. One other player may speak at a time. The simulacrum answers every question honestly and completely. The player channeling the simulacrum may omit but may not lie.

### Green (Seeded)
**The Rotunda:** A vertically-mounted wheel controls the direction of the room's single exit. Always unlocked. Apply standard green contents roll.

**The Tool Shed:** Contains both a Maul and a Spade. The first of the two items to be removed from the room causes the other to vanish permanently.

## Gameplay Rules

**Be fair:** The locked door percentages are guidelines, not mandates. If a player has been running cold — repeated bad luck, locked doors stacking up, dwindling resources — fudge the rolls to keep the maze engaging. This puzzle should feel challenging, not unwinnable. This principle applies broadly: any time a player seems to have had a recent run of bad luck, adjust quietly to keep the game fun.

**Rule of Cool:** If a player attempts something creative that isn't explicitly covered by the mechanics, let it work. The doors are solid stone — Shatter cast on one would likely destroy both the door and its mechanism, making that passage permanently unusable. A spell used to duplicate a key is valid. A player who finds an unexpected angle deserves to see it pay off.

## Infinite Wealth Exploit

Valuables removed from the vault and secured in a dead zone persist across resets, while the vault's contents restore to base state each morning. The maze may be occupied by Shrikes on any given run.

## DM Notes

- **The Setland advance expedition — 15 members total, none loop-aware:** Sent by Setland nearly ten years ago to assassinate Evandur. They believe time is passing normally and they are simply down a few men.
  - **Entry timeline:** Entered Aestrum shortly after midnight — the cycle had just reset without them; they witnessed nothing unusual. Spent the following day moving stealthily into position before entering the maze that night, still before their first midnight in Aestrum.
  - **3 died inside the maze** before that first midnight. They never received a snapshot — permanently dead. The lion shield in The Drain's Gelatinous Cube is the only physical trace.
  - **The remaining 12** survived to their first midnight in Aestrum and received snapshots. The fuzzball prevents them from questioning their missing comrades — they reset each morning with no awareness of the loss.
  - **2 are at the exterior maze entrance (row 0 Entrance Hall)** disguised as Duskwall guards — whom they kill each morning, then replace. The real guards reset at midnight; this repeats daily. Current attack vector: main castle gate, held open at 11:30 PM by Judith Asemyeer. → Full detail in [duskwall_castle.md]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/duskwall_castle.md).
  - **10 remain camped in the nearest woods**, awaiting a success signal. They reset each morning believing they are still waiting on their first genuine attempt.
- **The vault:** Minor lock, immense ducal wealth behind it. The infinite wealth exploit is viable as long as a dead zone is accessible for storage.
