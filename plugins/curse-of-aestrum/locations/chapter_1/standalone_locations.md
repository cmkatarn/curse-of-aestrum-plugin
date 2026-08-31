---
id: standalone_locations
name: Standalone Locations
type: collection
---

## Charnelhold

*Promoted to its own file:* see [charnelhold.md]({{PLUGIN_ROOT}}/locations/chapter_1/charnelhold.md).

---

## Deckard Estate

**id:** loc_deckard_estate  
**region:** Aestrum (near Misty Forest)  
**curse_affected:** false (dead zone)  
**npcs_present:** [npc_rowan_deckard]

**Rowan is here at night only** — he returns inside the dead zone each night to preserve his memory across the reset. A farm property owned by Shar cultist Rowan Deckard. The entire estate is a magical dead zone where spells and magical items are rendered inert. The small house contains a bedroom whose ceiling is covered with thousands of symbols of Shar. A locked larder on the property serves as a mass grave containing hundreds of corpses of Miri Amblecrown.

The dead zone means anything left here persists across the reset, which makes the estate uniquely valuable to anyone who finds it — and costs Rowan his anchor if they stay.

---

## Dunleaven Deadery

**id:** loc_dunleaven_deadery  
**region:** Aestrum (southwest of Dunleaven)  
**curse_affected:** true  

A cave-born crypt system southwest of Dunleaven. Open access — the Deadery itself is not locked. Individual crypts within vary; the larger ones are often booby-trapped and sealed.

**The Trambeathen tomb:** Reached through a locked wooden door (conventional lockpicking DC). Behind it: a large stone door immune to magic — the loop does not operate on it, spells cannot open or affect it. Operated by a wheel crank set into the rock wall beside the door.

**Current interior state of the Trambeathen tomb:** The Runic Skeleton (carrying the Eyeball Staff) patrols continuously. A gargoyle serves as secondary defense, positioned to protect against discovery of Elsinoor Trambeathen's remains. The lesser skeletons are buried in shallow graves throughout the tomb floor — unseen unless summoned by the Runic Skeleton. Elsinoor's corpse is interred with the Pendant of Waking Hours (the cursed version Lisandre crafted to kill her) still on her body. No one outside the tomb knows any of this.

The hauntings that historically sustained Dunleaven's exorcism trade stopped when the Trambeathen tomb was sealed. Locals attribute the silence to unknown causes.

A living connection to the tomb exists in Duskwall: Lisandre Trambeathen, who scries for the Eyeball Staff each morning and finds it not where he left it.

---

## Misty Forest

**id:** loc_misty_forest  
**region:** Aestrum  
**curse_affected:** true  
**dead_zones_within:** [loc_misty_forest_dead_zone]  
**npcs_present:** [npc_aliss_perisdottir, npc_rowan_deckard, npc_mieke]

The large forest within Aestrum. Contains Aliss Perisdottir's three-story stone house at its center, a Shar shrine at the edge of the forest dead zone (Rowan Deckard's base), the hunting trail where Mieke and his mercenary group reset each morning, and the giant tree where Akadi's Abarkas and the Caliconia flower were found.

**The Misty Forest Shar Shrine (loop anchor):** A ruined structure of dark stone with only one wall still standing. Contains two stained glass windows, both stained deep magenta. Rowan built a personal effigy here (a replacement for the Shar statue Hati relocated to the Duskwall shrine). This shrine is the second prayer anchor point Shar uses to sustain the cycle — Rowan prays here each morning for one more day/chance to convince Miri.

**The forest dead zone:** Third significant dead zone in Aestrum. Rowan returns inside it each night to preserve his memory.

---

## Mirot

**id:** loc_mirot  
**region:** Aestrum (edge of Nahamkate Desert)

A community of estates comprised primarily of retired individuals. Located at the edge of the Nahamkate Desert — to the north, vegetation abruptly stops, transitioning into a barren, orange-hued wasteland. Home to the Dundelver estate (with Rezibund Highbottom's skeleton in the dining room) and Rose Landon's apothecary.

---

## Moonmaiden Falls

**id:** loc_moonmaiden_falls  
**region:** Aestrum (near Dunleaven)

A waterfall near Dunleaven forming the pond from which the Moonmaiden River rises — fed by freshwater springs high on the slopes of Mount Mumandad, not Runnaheim snowmelt, despite older notes. Full detail in [moonmaiden_falls.md]({{PLUGIN_ROOT}}/locations/chapter_1/moonmaiden_falls.md); the river itself now has its own file, [moonmaiden_river.md]({{PLUGIN_ROOT}}/locations/chapter_1/moonmaiden_river.md). "Moonmaiden" is a poetic title of Selûne — the name predates the current divine conflict. The Selûne statue removed from the Duskwall shrine was dumped in this pond by Hati Heldrivver's arrangement.

---

## Nahamkate Desert Dead Zone

**id:** loc_nahamkate_dead_zone  
**region:** Aestrum (Nahamkate Desert)  
**dead_zone:** true

Approximately a quarter-mile off the main path into the Nahamkate Desert. Identifiable by magical charring — patches of discoloration on stone and compacted sand, fused grains, scorch patterns with no fire source. Functions as an antimagic field — magical items lose their properties and spells cannot be cast. See `{{PLUGIN_ROOT}}/locations/chapter_1/nahamkate_desert.md`.

---

## Nahamkate Temple

**id:** loc_nahamkate_temple  
**region:** Aestrum (Nahamkate Desert)  
**curse_affected:** true  
**npcs_present:** [npc_assaneela]

An ancient structure dedicated to the Yuan-Ti deity Sathraza, located in a box canyon deep in the Nahamkate Desert, marked by smoke from everlasting torches. The party located the temple, encountered a group of Yuan-Ti including the priestess Assaneela, solved a gemstone puzzle room using the Mounted Ruby, and discovered the large tangerine quartz flame relic in a hidden chamber. The party escaped through a rear tunnel.

---

## Nortmunde (Kingdom)

**id:** loc_nortmunde  
**type:** kingdom

The overarching kingdom of which Aestrum, Setland, Skaarsdaam, Mikaelvad, and Dalihad are all duchies. The capital — also called Nortmunde — is one very large land-locked city at the geographical center. The duchies radiate outward, each bordering two others. The king has died with no heir, triggering an open succession crisis.

**Succession mechanism:** The throne is claimed by ducal vote — each duchy casts one vote. A regent (Tarwick Grale) currently holds the capital.

**Current vote alignment:**
- **Setland** → Malak du Leon (self-vote)
- **Skaarsdaam** → Amblecrown (self-vote)
- **Aestrum** → conditional (Luca/Lucretius Tallwood holds the vote)
- **Mikaelvad** → undecided; Duke opted out of candidacy but vote is unaligned
- **Dalihad** → undecided; Duke knows he cannot win and will back whoever he believes will

**The diplomatic math:**
- If party assists Luca and keeps him alive through the Setland invasion: Aestrum votes Amblecrown. Party needs only ONE of the two swing votes.
- If party does not assist Luca: Setland's pressure forces Aestrum to vote Malak. Party needs BOTH swing votes.
- A 2-2 tie with Aestrum's vote uncastable results in civil war.

---

## Rockwood

**id:** loc_rockwood  
**region:** Aestrum

A town within Aestrum. The Dundelver estate is 3–4 hours from here. Darwinnith Dundelver the Second claims to have been in Rockwood the night of Rezibund's murder; a child neighbor contradicted his arrival time.

---

## Runnaheim Mountains

**id:** loc_runnaheim_mountains  
**region:** Aestrum northern / northwestern border

A mountain range forming Aestrum's northern and northwestern border. A single mountain pass through the Runnaheim range exits Aestrum to the north — **not** directly into another Nortmunde duchy, but into the neighboring **Kingdom of Vrynholt**. From Vrynholt, the southern roads connect southwest to Mikaelvad and Dalihad. (The Moonmaiden River does **not** originate here despite older surveyor notes — its source is Mount Mumandad in the south near Dunleaven; see [moonmaiden_river.md]({{PLUGIN_ROOT}}/locations/chapter_1/moonmaiden_river.md).)

**Status as an escape route:** last resort. The pass route is slow (10–14 days to Mikaelvad or Dalihad), requires transiting a foreign kingdom whose authorities have no obligation to grant passage, and exposes the party politically. The primary planned Chapter-1-endgame escape is by sea aboard [The Incorrigible]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/the_incorrigible.md); the Runnaheim pass is the fallback if both the Setland road and the ship are unavailable. To be introduced in an upcoming session.

---

## Temple of Kossuth

**id:** loc_temple_of_kossuth  
**region:** Aestrum (south of Rockwood)

Located south of Rockwood, this temple to Kossuth was razed approximately 200 years ago during the Acolypyrrhic Battles. Some stained-glass windows remain. A note left by a priest describes the resting place of a relic of Akadi. At noon, sunlight through the sun-shaped stained-glass window, focused through the Flame-Shaped Quartz, creates a beam of light pointing toward the Nahamkate Temple, where the Akadi relic is hidden.

---

## The Antechamber of Shar

**type:** extradimensional

An extradimensional space serving as an antechamber to Shar's realm, reached when the Shar statue in the Duskwall Shrine of Selûne is destroyed. Full arrival, presence, physical-effect, exit, and DM-note mechanics live in its dedicated file — see [antechamber_of_shar.md]({{PLUGIN_ROOT}}/locations/chapter_1/antechamber_of_shar.md) (`loc_antechamber_of_shar`).

---

## Dalihad

**id:** loc_dalihad  
**type:** duchy  
**duke:** npc_dorvael_dunwick

A duchy within Nortmunde, renowned throughout the kingdom for its stonework. Dalihad quarries produce the pale grey stone found in Nortmunde's most significant structures. Dalihad guild masons are known for tight-fitted, mortar-free construction. The duchy's stone trade has made it wealthy and politically difficult to antagonize. Sage passed through briefly en route to Aestrum. The party has not yet visited.

*DM convention: Any elegant, well-constructed, or notably durable building described going forward should reference Dalihad stone or craftsmanship as the source.*

**The labor pipeline:** Dunwick runs forced labor across quarry operations. When a worker is no longer productive, they are transferred to a "secondary work camp" in Mikaelvad — where they are fed upon by vampires. The Blooddigger clan is imprisoned in these quarries. Some have already been transferred.

---

## Mikaelvad

**id:** loc_mikaelvad  
**type:** duchy  
**duke:** npc_bertram_holst

A duchy within Nortmunde, occupying an entire valley. Almost permanently covered in dense fog. Known for significant vampiric activity. Despite the ever-present threat, its population appears content. Sage was extremely cautious during her passage — careful about lodgings, company, and timing. She never encountered a vampire directly.

The Duke has declined to stand as a succession candidate — his vote is unaligned and both sides will court it.

**Capital:** Mireval — see below.

**DM only:** The Duke is a vampire. The "secondary work camp" from Dalihad is a sustained vampire feeding operation. See `npcs/bertram_holst.md`.

---

## Mireval

**id:** loc_mireval
**type:** city (capital of Mikaelvad)
**parent:** loc_mikaelvad

The capital city of Mikaelvad, set in the lower valley where the fog is heaviest. Built of pale Dalihad stone and dark slate; tall narrow buildings, steep tiled roofs, broad boulevards in the central districts and twisting lanes in the older quarters. A river runs through it. Lanterns are kept lit along the main streets from dusk to dawn — the city's quiet, ungoverned acknowledgment that something other than weather walks here at night.

By day Mireval looks like any prosperous Nortmunde capital: markets, magistrates, guild halls, the Duke's keep on the rise above the river. By night the population thins, the wealthy retreat indoors, and the city assumes its other character. The residents do not discuss this directly. The arrangement is understood and not examined.

**Notable establishments:**
- **The Vesper Hall** — a private society in the central district. See [`locations/mireval/vesper_hall.md`]({{PLUGIN_ROOT}}/locations/chapter_2/mireval/vesper_hall.md).
- **Vasik's Practice** — a respected private physician's clinic in the professional quarter. See [`npcs/chapter_1/andrei_vasik.md`]({{PLUGIN_ROOT}}/npcs/chapter_2/andrei_vasik.md).

**DM only:** Mireval is where the civilized vampire-mortal coexistence of Mikaelvad is most visible. Holst's keep is here; many of his lieutenants reside in townhouses in the upper districts. The Vesper Hall is the cleanest social-register access point to that circle the party will encounter.

---

## Skaarsdaam

**id:** loc_skaarsdaam  
**type:** duchy  
**duke:** npc_amblecrown

A duchy within Nortmunde, located west of Setland. Ruled by Duke Amblecrown, described as a benevolent and just ruler, well-loved by his subjects. Militarily capable but outmatched by Setland if the two duchies go to war alone. The Duke is visibly saddened — his daughter Miri went missing approximately ten years ago. His treasury has been essentially emptied funding covert expeditions to find her.
