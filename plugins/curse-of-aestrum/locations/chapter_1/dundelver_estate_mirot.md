---
id: loc_dundelver_estate_mirot
name: The Dundelver Estate
region: mirot
curse_affected: true
connected_locations: [loc_mirot, loc_rockwood]
npcs_present: [npc_darwinnith_dundelver_1, npc_darwinnith_dundelver_2, npc_corran_vye, npc_milo_tarrow, npc_kip_malbry]
npcs_present_notes: "Darwinnith the Second is here ~10 AM to ~7 PM. Vye, Tarrow and Kip arrive together ~4:45 PM; the guards stay until the midnight reset takes them, Kip until she goes home for her supper. Darwinnith the First arrives later in the evening, after his son has gone. The ~4:45-7 PM overlap is the only time DD2 and the guards are both present."
related_quest: quest_murder_of_rezibund_highbottom
---

## Overview

A modest rural estate on the edge of Mirot, the kind of property that suggests old money gradually becoming less of both. The grounds are maintained but not immaculate — the hedgerow is trimmed, the path is clear, the paint on the door is only a few years past fresh. The house belongs to Darwinnith Dundelver the First, who is currently in Duskwall seeking medical treatment for a worsening illness. His son, Darwinnith the Second, manages the estate in his absence and arrives each late morning to keep things in order.

The physical layout is provided by the LEGO build (overhead map). Five distinct areas: an entrance room, the dining room, the kitchen, the office, and the bedroom. The servant's quarters (Rezibund's) are a separate outbuilding accessed from the exterior.

## Daily Reset State

Each morning, the estate resets to the following state:

- The skeleton of Rezibund Highbottom is lying face down on the dining room floor, clothes in tatters. The wood around and beneath the body is stained; additional staining near the facial area (vomiting).
- Darwinnith the Second arrives in the late morning, discovers the skeleton, and immediately claims sorcery or necromancy — the victim was fine just the day before and is now an aged skeleton.
- Darwinnith the Second gives the guards his statement, stays as long as he can stand to, and takes the cart home at roughly **the seventh hour past midday (~7 PM)** — twelve miles, about three and a half hours, lanterns lit, home around half past ten. He goes with visible reluctance, promising to return at first light. He does not. He arrives the next morning having forgotten he ever said it.
- Darwinnith the First arrives at roughly **8 PM**, an hour after his son has gone, by hired coach from Duskwall — the standing booking he keeps at [À la Cart]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/a_la_cart.md) because he is too ill to walk twelve miles. The driver turns straight around and is back in the city by about half past ten. DD1 resets in Duskwall, not here.
- Word goes out for the Duskwall guard within the quarter-hour. [Kip Malbry]({{PLUGIN_ROOT}}/npcs/chapter_1/remaining_npcs.md#kip-malbry), Mirot's thirteen-year-old runner, is sent down the road on foot and covers the twelve miles in a little under three hours.
- Two guards — [Corran Vye]({{PLUGIN_ROOT}}/npcs/chapter_1/remaining_npcs.md#corran-vye) and [Milo Tarrow]({{PLUGIN_ROOT}}/npcs/chapter_1/remaining_npcs.md#milo-tarrow) — set out from Duskwall on foot in the early afternoon and reach the estate at roughly the fifth hour past midday, with Kip walking the twelve miles back alongside them. They never leave it. Vye will not walk away from an unsecured body, so the two of them hold the scene through the evening and into the night, intending to resume at first light — and the midnight Sleep step drops them where they stand. The 3:00 AM Teleport step returns them to Duskwall, because Duskwall is their reset point. First light never arrives for them. Kip resets in Mirot.

---

## The Post Outside the House

From roughly the fifth hour past midday until midnight takes them, two Duskwall guards are standing outside the front of the house. They are not inside it — Vye put his head in once, looked at the body, and came back out, and neither of them has been in since.

Within the first hour they have done everything they are going to do: looked at the skeleton, taken Darwinnith the Second’s statement before he drives home, and stopped. What stops them is not laziness. The body is plainly a decade gone; their only witness says sorcery and cannot be disproved; they have no authority to search or hold anyone in Mirot; and — the part they do not know — they have never once had a second day to work with. Every cycle is hour one.

Kip sits on the wall with her legs out, wrecked from the run, watching them accomplish nothing, until someone sends her home for her supper.

**They do not walk back.** Vye’s position is that you do not leave a body in an empty house overnight, and you do not walk twelve miles to fetch a magistrate in the dark either. So the detail holds the scene until morning and means to work it properly at first light. Night comes on; one of them gets a lantern going; they talk about nothing in the way men do on a long post. At 12:00:00 AM the Sleep step drops both of them where they stand, and the 3:00 AM Teleport step puts them back in Duskwall, which is where they began the day and therefore where they begin every day. See [rules/time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md).

Vye has now kept this vigil roughly three thousand six hundred times, every one of them in order to be ready for a morning he has never once seen.

**This is the party's accusation window.** Full mechanics, the arrival timeline and the guards' pushback ladder: [Step 2 of the quest]({{PLUGIN_ROOT}}/quests/chapter_1/the_murder_of_rezibund_highbottom.md).

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

**DD2's window:** He is at the estate from the late morning (~10 AM) until roughly **7 PM**, when he takes the cart home to Rockwood. Players who arrive before him find the estate unattended. Players who arrive with him get his performance of genuine confusion. He does not know the party is investigating and will not behave suspiciously unless directly confronted with both the broken alibi and the letter simultaneously.

**Why he leaves, and what it costs to stop him.** The drive is three and a half hours and he has a wife at the other end of it. He is not racing the dark — the cart carries lanterns and he is used to finishing the run in them — he simply has no reason to sleep in a house with a skeleton in it when he has a bed twelve miles away.

> **Do not tie this to the alibi.** Maret's claim that he came home *"shortly after dark"* describes **the night of the murder only** — a single historical night before the cycle began, when he left the estate late because he had a body to arrange and a plate to wash, and Tovy saw him arrive near midnight. That night is fixed and is not replayed. His post-cycle daily departure is a separate fact, set for play rather than for the evidence, and changing it does not touch the alibi or Tovy's testimony in any way.

He can be held later. He will stay as long as someone is actively engaging him, growing steadily more anxious about the hour and the road. **A party that keeps him past about 8:30 PM has cost him the trip** — he cannot reach Rockwood before midnight and will bed down at the estate instead. The consequence is not his; it is the horse's. Animals do not reset ([rules/travel.md]({{PLUGIN_ROOT}}/rules/travel.md)): the cart and horse stay in Mirot, DD2 wakes in Rockwood without them, and he arrives the next day **on foot in the mid-afternoon** instead of by cart in the late morning — visibly put out, and with no idea why his cart is twelve miles away. A loop-aware party has just learned it can leave a fingerprint on tomorrow.

**DD1's expected arrival:** Around 8 PM, by hired coach from Duskwall — two hours at coach pace over the twelve miles, on the standing booking he keeps at [À la Cart]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/a_la_cart.md). His son leaves at 7; they do not meet, and neither of them remarks on it. If the party is at the estate in the evening, DD1 is present. He is forgetful and lethargic from his illness — kind but difficult to keep on topic. He does not know Rezibund is dead or that his son is a murderer. If told the letter is a forgery, he gifts the party the safe.

**The second plate:** The haphazardly washed plate is DD2's — he washed it after the murder to remove any trace of his presence at the meal, then replaced it. He could not remove Rezibund's plate without making the absence conspicuous. The result: one plate on the table (the victim's, with food remaining), one plate haphazardly washed and returned to the hutch (the killer's). Combined with the goblet trace, the misaligned hutch goblet, and the kitchen window's poison access, it reconstructs a two-person meal in which one party poisoned the other and then cleaned only their own traces.

**The skeleton does not reset.** Rezibund died the day before the loop began — before Shar took a snapshot of Aestrum. He never entered the cycle. His remains are genuine: a decade of real decay, slowly reducing from a body to what the party finds now. The rest of the estate resets around him each midnight — the table setting is restored, the dishwater refreshes, the open jar reseals — but the skeleton stays, aging authentically while everything else pretends the day is new.

**DD2's sorcery claim is coherent.** His memory resets each morning. To him, Rezibund was alive and well yesterday — he has no recollection of the murder, the dinner, or any prior discovery. He arrives to find a skeleton that looks a decade old. The claim of necromancy or devilry is not hysteria. From his perspective, it is the only explanation that fits: a living man, reduced overnight to ancient bones. He is wrong about the cause and right about the impossibility.
