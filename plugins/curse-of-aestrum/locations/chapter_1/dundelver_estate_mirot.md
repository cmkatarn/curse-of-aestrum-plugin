---
id: loc_dundelver_estate_mirot
name: The Dundelver Estate
region: mirot
curse_affected: true
connected_locations: [loc_mirot, loc_rockwood]
npcs_present: [npc_darwinnith_dundelver_1, npc_darwinnith_dundelver_2]
related_quest: quest_murder_of_rezibund_highbottom
---

## Overview

A modest rural estate on the edge of Mirot, the kind of property that suggests old money gradually becoming less of both. The grounds are maintained but not immaculate — the hedgerow is trimmed, the path is clear, the paint on the door is only a few years past fresh. The house belongs to Darwinnith Dundelver the First, who is currently in Duskwall seeking medical treatment for a worsening illness. His son, Darwinnith the Second, manages the estate in his absence and arrives each late morning to keep things in order.

The physical layout is provided by the LEGO build (overhead map). Five distinct areas: an entrance room, the dining room, the kitchen, the office, and the bedroom. The servant's quarters (Rezibund's) are a separate outbuilding accessed from the exterior.

## Daily Reset State

Each morning, the estate resets to the following state:

- The skeleton of Rezibund Highbottom is lying face down on the dining room floor, clothes in tatters. The wood around and beneath the body is stained; additional staining near the facial area (vomiting).
- Darwinnith the Second arrives in the late morning, discovers the skeleton, and immediately claims sorcery or necromancy — the victim was fine just the day before and is now an aged skeleton.
- Darwinnith the First is expected at the estate later that evening (arriving from Duskwall). He resets in Duskwall, not here.

---

## Rooms

### Entrance Room

A small receiving area. Plants. Functional, unremarkable. Provides access to the rest of the house. No investigation value.

---

### Dining Room

The crime scene.

**On the table:** One bottle, one goblet, one plate. The plate holds half a cheese-pie and some salted pork.

**On the floor:** The skeleton lies face down. The wood is stained in a wide radius around the body; additional staining near the skull (vomiting).

**The china hutch:**
- PER 8: One goblet is missing from the set — it is the one on the table.
- INV 11: One goblet in the hutch is slightly out of alignment with the others, as though recently replaced after washing.

**The plates:**
- PER 8: One plate is missing from the set — it is the one on the table.
- INV 12: A second plate has been haphazardly washed. High investigation may notice the same pie crust residue as the one on the table — suggesting a second portion was served and the plate cleaned after.

**The bottle:** Examination reveals no powdery residue.

**The skeleton:**
- PER 9: No wounds to the bones — no weapon marks, no signs of strangulation.
- INV 11: The clothes are intact but aged far beyond what the victim's death would explain. This rules out blunt trauma and strangulation.
- INV 12: Poisoning is a highly likely cause of death.

**The goblet:**
- PER 11: Trace amounts of a powdery substance in the goblet on the table.

---

### Kitchen

Adjacent to the dining room. The smell of old dishwater.

**The counter:** Food preparation area. Fruit, vegetables, a cauldron, a stove with chimney. A cleaver. The kitchen sees regular use.

**The dishwater:** Leftover from the previous evening. Contains remnants of cheese-pie.
- PER 14: No poison in the dishwater.
- PER 14: Two portions of salted pork appear to have been removed from the larder.

**The window:** A latticed window on the exterior wall.
- INV 16: The window is positioned such that someone inside the kitchen could reach through and access whatever is stored against the exterior of the building — including any rat poison kept near the foundation.

---

### Office

DD1's working space. Everything here is in plain view — nothing is hidden.

**On the desk:**
- A hand-drawn partial map to a forgotten temple in the Nahamkate desert. **Quest item** — the party may attempt to follow it independently. See `{{PLUGIN_ROOT}}/locations/chapter_1/nahamkate_temple.md` for what they find.
- Darwinnith the First's personal journal.
- A scrap of paper with a nonsensical sentence scrawled across it.

**The journal:** Contains an entry expressing longing for a woman named Anwe from Neverwinter — described as a meeting nearly twenty years ago. She was, in his words, likely his soul-mate. He has not seen her since.

**The bookshelf:** Various books, ledgers, and journals. The ledgers document repeated attempts to pressure Halimon the Apprentice into selling his land — formal correspondence, solicitor fees, failed offers.

---

### Bedroom

DD1's bedroom. Sparse and personal in equal measure.

**The bed:** A single bed, well-made.

**The painting:** A tropical coastline — colorful, warm. Out of place for Aestrum. Hung above the bed.

**The nightstand:** The Dundelver Safe rests here. A combination-locked device featuring slides numbered 1–16 and a rod. Incorrect combinations trigger an electric discharge (5-foot radius, 1d12 damage, CON DC 16; failed save renders affected appendage(s) unusable for 4 hours). See `{{PLUGIN_ROOT}}/items/chapter_1/misc_items.md`.

**The table:** Several glass jars containing insects.
- PER 12: One jar is open.
- INV 15: The missing insect is a non-poisonous scavenger-type bug. Its absence is consistent with it having been attracted to organic matter elsewhere in the house — the body in the dining room being the obvious candidate.

---

### Servant's Quarters (Exterior)

Rezibund's outbuilding. A short distance from the main house, accessed from outside.

**Exterior:** Rat poison is distributed around the perimeter — consistent with the pest problem the estate shares with the Tahen property next door.

**Interior:**
- The room contains almost nothing: a sleeping mat.
- INV 12: A letter, tucked away. From a woman named Anwe — addressed to Rezibund, claiming that Darwinnith Dundelver the First is his father. The letter is in good condition.
- INV 15: The letter is too new. The paper shows no travel wear, no aging consistent with the distance it would have needed to travel. It could not have arrived through normal means recently.

---

## DM Notes

**The bug:** The open jar and the missing scavenger insect are a subtle environmental detail available to attentive players — confirming the body has been there long enough to attract insects consistent with decomposition, which supports a death that predates the current morning. Not a critical clue, but rewards investigation.

**DD2's arrival window:** He arrives in the late morning each day. Players who arrive before him find the estate unattended. Players who arrive with him get his performance of genuine confusion. He does not know the party is investigating and will not behave suspiciously unless directly confronted with both the broken alibi and the letter simultaneously.

**DD1's expected arrival:** Later the same evening, from Duskwall. If the party is at the estate in the evening, DD1 is present. He is forgetful and lethargic from his illness — kind but difficult to keep on topic. He does not know Rezibund is dead or that his son is a murderer. If told the letter is a forgery, he gifts the party the safe.

**The second plate:** The haphazardly washed plate is DD2's — he washed it after the murder to remove any trace of his presence at the meal, then replaced it. He could not remove Rezibund's plate without making the absence conspicuous. The result: one plate on the table (the victim's, with food remaining), one plate haphazardly washed and returned to the hutch (the killer's). Combined with the goblet trace, the misaligned hutch goblet, and the kitchen window's poison access, it reconstructs a two-person meal in which one party poisoned the other and then cleaned only their own traces.

**The skeleton does not reset.** Rezibund died the day before the loop began — before Shar took a snapshot of Aestrum. He never entered the cycle. His remains are genuine: a decade of real decay, slowly reducing from a body to what the party finds now. The rest of the estate resets around him each midnight — the table setting is restored, the dishwater refreshes, the open jar reseals — but the skeleton stays, aging authentically while everything else pretends the day is new.

**DD2's sorcery claim is coherent.** His memory resets each morning. To him, Rezibund was alive and well yesterday — he has no recollection of the murder, the dinner, or any prior discovery. He arrives to find a skeleton that looks a decade old. The claim of necromancy or devilry is not hysteria. From his perspective, it is the only explanation that fits: a living man, reduced overnight to ancient bones. He is wrong about the cause and right about the impossibility.
