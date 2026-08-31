---
id: quest_the_missing_relics
name: The Missing Relics of Akadi and Kossuth
type: side
related_npcs: [npc_assaneela]
related_locations: [loc_nahamkate_temple, loc_temple_of_kossuth]
---

## Overview

During the Acolypyrrhic Battles, a stolen relic of Akadi was hidden by a Temple of Kossuth priest. When Akadi's followers arrived and couldn't find it, they stole a relic of Kossuth instead. The priest left a poem describing the relic's hiding place:

> *At noon, beneath the burning sky... A beam, like truth in solemn grace, Did pierce the air, did find its place through sacred stone, through Kossuth's gift... I hid the item none must miss — A relic forged of ancient rite... The light shall fade, the day shall fall, but only the chosen will hear the call.*

The intended solution path: place the Flame-Shaped Quartz Relic in the ruined Temple of Kossuth at noon; follow the resulting light beam to the hidden Akadi relic (a massive tangerine quartz) inside the Nahamkate Temple, behind a puzzle door keyed to the Mounted Ruby.

## Timed-Event Schema — The Noon Beam

Per [time_and_events.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/time_and_events.md), the noon beam is a **world-state moment** the party must align with:

- **`time:`** 12:00 PM (Aestrum-local noon, when the sun is directly above the ruined Temple of Kossuth) — exact.
- **`duration:`** ~2 minutes. The beam forms when the Flame-Shaped Quartz Relic is in place and the sun crosses true noon; it sharpens for roughly a minute, then fades as the sun moves off the alignment.
- **`catchup: none`** — the alignment is the moment. A party that arrives at the temple at 12:05 PM with the relic placed finds the beam already faded; they have to wait until the next day's noon to try again. A party that arrives at 11:55 PM with everything in place watches the alignment land and gets their two minutes to read the beam's direction. The relic itself does not generate the beam without the sun.
- **Loop interaction.** Every cycle restores the temple, the relic, and the sun's path. A party that misses today's noon catches tomorrow's at no permanent cost — but each missed alignment costs a full Aestrum day, and the relic must be retrieved and replaced each cycle if the Recreate step has reverted it.

## DM Notes — Relic Chain (Full Reconstruction)

1. Followers of Kossuth stole a relic of Akadi and hid it in Aestrum.
2. Akadi's followers swept into Aestrum in retaliation — sparking the Acolypyrrhic Battles.
3. They reached and ransacked the Temple of Kossuth but never found their stolen relic (hidden by a priest).
4. As consolation they took the Flame-Shaped Quartz (a non-magical relic of Kossuth) and departed north through Mirot.
5. Travelling north, they encountered the Nahamkate Temple of Ssath'razza and ransacked it.
6. They found the Yuan-Ti magical relic more valuable than the non-magical Kossuth flame relic, so they left the tangerine quartz in the Yuan-Ti temple and took the Yuan-Ti relic north.
7. The party later found the tangerine quartz in the Nahamkate Temple and used it in the ruined Temple of Kossuth to locate the hidden Akadi relic via a light beam.

**The Scale of Ssath'razza (DM-created relic):** A single massive iridescent scale, believed to be a divine cast-off of the World Serpent Ssath'razza. Radiates transmutation magic. Properties: immunity to poison, charm resistance, serpentine qualities once per day. Taken north by Akadi's followers after the Nahamkate Temple ransacking — current location unknown. Assaneela came to the temple to retrieve it for Zehir, and has been trapped in the loop ever since. The Scale is a potential Chapter 2 hook — in Zehir's hands it consolidates his power over serpent-kind; in an enemy's hands it can be used against him.
