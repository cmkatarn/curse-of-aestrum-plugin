---
id: loc_routes
name: Routes & Travel Times
type: reference
mode: on_foot
---

## Conventions

**Baseline pace:** Normal overland walking — approximately 3 mph / 24 miles per day (8 hours travel). Times assume a typical adult traveler on a maintained road carrying moderate gear. Rough terrain or unmaintained paths slow travel by roughly one-third.

**What times include:** Active travel only. Does not include meal stops, camp setup, or time spent within a destination. "1 day" means roughly 8 hours of walking, typically a single long day with a break for lunch.

**What `~` means:** Approximate — within roughly 20% of the stated figure. Precise measurement was not the source's concern.

**What `[proposed]` means:** The distance or time is my best inference from geographic context, not a number stated in a campaign file. Treat these as working defaults until confirmed or corrected.

**Curse / boundary barrier:** The Aestrum boundary barrier (`locations/duskwall/as_the_crow_flies.md:50`) prevents snapshot recipients from leaving Aestrum once they have crossed in — see [rules/time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md). The inter-duchy routes below describe the underlying geography. Whether the active party can currently use them is tracked in [the saved overlay](saved/routes.md) and updates when the curse breaks.

**Every figure in this file is a walking figure, and that is not an omission.** Aestrum has no riding tack and no saddle horses — farm animals pull, the Duke's carriage horses are under guard in Duskwall Castle, and nobody rides anywhere. Mounted times are therefore not listed, for the party or for NPCs. See [rules/travel.md]({{PLUGIN_ROOT}}/rules/travel.md), *On Foot Is the Only Sustainable Mode*, for why, and for what happens if a party acquires an animal anyway.

**Intra-city walks excluded:** Sub-locations within the same settlement (Duskwall market → Duskwall harbor, etc.) are too short to matter and are not listed here.

---

## Road Network — Aestrum

Aestrum's maintained roads and paths form the following topology. Rough track and footpath are roughly one-third slower than maintained road.

```
              Nahamkate Desert
                    |
                  Mirot (N)
                    |
  Setland (W) ── [four-way crossroads (4WI)] ───── [three-way junction (3WI)] ─── Duskwall (NE)
                    |                            /         \
                Rockwood (S)    walking path → Perisdottir   south →
                    |          (south spur, 3 mi W of Tine) (Deckard Estate gate, ~1 hr from Duskwall)
              Temple of Kossuth                                  ↔
              (mountain path)                              dilapidated bridge
                                                                 ↔
                                                             Dunleaven
```

**Quarterways** — the four-way crossroads (4WI). The farmland crossroads connecting Mirot (north), Rockwood (south), the Setland road (west), and the road east toward Tine Cross (on to Duskwall and Dunleaven). A weathered four-armed **signpost** stands at the corner:
- **West — Setland**
- **North — Mirot**
- **South — Rockwood**
- **East — Duskwall & Dunleaven** (the east road runs to Tine Cross, where the two part)

**Tine Cross** — the three-way junction (3WI), ~20 minutes northeast of Duskwall. Three roads: northeast to Duskwall, south toward Dunleaven (passing the Deckard Estate gate and the dilapidated bridge), and west to Quarterways (and the Setland road beyond). A three-armed **signpost** stands at the fork:
- **Northeast — Duskwall**
- **South — Dunleaven**
- **West — Setland, Mirot & Rockwood** (via Quarterways)

**Maintained walking path (to Perisdottir house)** — a spur off the 4WI–3WI road leading south into the Misty Forest, terminating at Aliss Perisdottir's house. The path branches from the road **~3 miles west of Tine Cross** — nearer the Tine Cross end than the middle, with ~5 miles of road still running west to Quarterways beyond it. The path is navigable without woodcraft. Leaving it inside the forest is where navigation becomes difficult.

**Deckard Estate gate** — the estate's gate opens directly onto the Duskwall–Dunleaven road, approximately 1 hour south of Duskwall (~40 min south of the three-way junction). Not a junction — the road passes the gate and continues to the bridge. Most travelers are heading to Dunleaven; the estate is a waypoint, not a destination.

**Dilapidated bridge** — on the Duskwall–Dunleaven road, between the Deckard Estate gate and Dunleaven. Condition unknown; treat as a potential chokepoint.

Locations **not on the road network** (rough track or footpath only): Misty Forest sub-locations off the walking path (dead zone, Shar shrine, great tree, spider territory), Temple of Kossuth, Dunleaven Deadery, Moonmaiden Falls, Runnaheim pass approach.

> **Map note:** An earlier version of the LEGO campaign map showed two separate 3-way intersections; these have since been merged into the single four-way crossroads above. The photo retained in memory reflects the pre-merge layout.

---

## Aestrum — Internal Routes

### Duskwall ↔ Three-Way Junction
- **distance:** ~1 mile
- **on foot:** ~20 minutes
- **terrain:** maintained road
- **hazards:** none
- **notes:** the junction is the branching point for all routes out of Duskwall on foot; close enough that most travelers treat it as the start of the journey rather than a waypoint
- **canon source:** ~20 min confirmed by DM

---

### Quarterways (4WI) ↔ Tine Cross (3WI)
- **distance:** ~8 miles
- **on foot:** ~2.5–3 hours
- **terrain:** maintained road, running east
- **landmarks — declare these every time (see [rules/travel.md]({{PLUGIN_ROOT}}/rules/travel.md)):** the **Misty Forest** lies to the **south** along this whole leg, its treeline closing the southern horizon; **~3 miles west of Tine Cross** (i.e. ~5 miles east of Quarterways — noticeably nearer the Tine Cross end than the middle) a maintained **walking-path spur branches south** off the road, leading to **Aliss Perisdottir's house** inside the forest (see the *Maintained walking path* entry above and the Perisdottir route below)
- **hazards:** none on the road itself; leaving it south into the Misty Forest is where navigation becomes difficult
- **notes:** the road between the two named junctions — Quarterways at the west end, Tine Cross at the east (~20 min short of Duskwall). A party travelling from Quarterways to Duskwall passes Tine Cross before the city
- **canon source:** back-solved from three DM-confirmed figures — Duskwall ↔ Perisdottir (~6 mi) minus Duskwall ↔ Tine Cross (~1 mi) minus the Perisdottir spur (~2 mi) fixes the spur junction at ~3 mi west of Tine Cross; Duskwall ↔ Mirot (~12 mi) minus that ~1 mi and the ~3 mi Quarterways ↔ Mirot leg fixes the full leg at ~8 mi. Misty Forest to the south — *Maintained walking path* entry above
- **supersedes:** an earlier *[proposed]* ~5 miles / ~1.5–2 hours, and the description of the Perisdottir spur as branching at the leg's midpoint. Both were inferences; the spur's true position follows from the DM-confirmed distances above

---

### Duskwall ↔ Deckard Estate (gate)
- **distance:** ~3 miles
- **on foot:** ~1 hour
- **terrain:** maintained road; route: Duskwall → three-way junction → Deckard Estate gate
- **hazards:** none on the road; the estate itself is a dead zone (all magic ceases, loop does not reach it); the dead zone boundary is detectable before the gate
- **notes:** the estate gate opens directly onto the Duskwall–Dunleaven road; the road continues south past the gate toward the dilapidated bridge and Dunleaven
- **canon source:** gate on road ~1 hour from Duskwall — confirmed by DM; "south of Duskwall" — `locations/duskwall/salient_cartographer.md:28`

---

### Duskwall ↔ Aliss Perisdottir's House (Misty Forest)
- **distance:** ~6 miles
- **on foot:** ~2 hours (20 min to 3WI, then ~3 miles / ~1 hour west on the road to the spur junction, then ~2 miles / ~45 min south on the walking path into the forest)
- **terrain:** maintained road to 3WI, then maintained road west, then maintained walking path south into the Misty Forest
- **hazards:** leaving the walking path inside the forest is disorienting — mist is consistent, canopy closes off the sky; spider-infested corridor is to the east; stay on path unless you have a reference point
- **notes:** the walking path is a spur off the 4WI–3WI road; it leads directly to Perisdottir's house and is navigable without woodcraft; sub-locations off the path (dead zone, Shar shrine, great tree) require leaving it
- **canon source:** "Misty Forest to the northwest" — `locations/duskwall/salient_cartographer.md:28`; walking path confirmed by DM; distance confirmed by DM; 4WI is west of 3WI (travel west from 3WI to reach 4WI)

---

### Deckard Estate (gate) ↔ Dilapidated Bridge
- **distance:** ~2.25 miles
- **on foot:** 45 minutes
- **terrain:** maintained road south
- **hazards:** none on the road; the bridge itself is the hazard — see bridge entry below
- **notes:** —
- **canon source:** confirmed by DM

---

### Dilapidated Bridge
- **distance:** —
- **on foot:** the bridge is **completely out** — it cannot be crossed
- **terrain:** the road terminates at the riverbank; no crossing exists here
- **hazards:** **[UNKNOWN TO ALL]** — travelers do not know the bridge is gone until they arrive and find the gap; plan accordingly for party reactions; the failure mode is arriving here expecting to cross to Dunleaven and being stopped cold
- **notes:** two options to reach the far bank: (1) creative crossing at the bridge site; (2) travel upriver toward Dunleaven where the water becomes shallow and slow enough to ford — this ford is the intended workaround, and it adds time to the journey
- **canon source:** confirmed by DM

---

### Dilapidated Bridge ↔ Dunleaven
- **distance:** ~3.75 miles
- **on foot:** 75 minutes (assuming a crossing has been achieved)
- **terrain:** maintained road north into Dunleaven
- **hazards:** none on the road; see bridge entry above for the crossing problem
- **notes:** if the party fords upriver instead of crossing at the bridge, they rejoin this road closer to Dunleaven and save some of this time
- **canon source:** confirmed by DM

---

### Deckard Estate (gate) ↔ Dunleaven
- **distance:** ~6 miles
- **on foot:** 2 hours total (45 min to bridge + crossing + 75 min to Dunleaven); crossing time not included — variable
- **terrain:** maintained road; bridge crossing is the critical unknown
- **hazards:** bridge is completely out — see bridge entry; party will not know until they reach it
- **notes:** if the party fords upriver, add time for the detour; the ford is near Dunleaven so most of the delay is early in this leg
- **canon source:** confirmed by DM

---

### Deckard Estate ↔ Misty Forest (entry)
- **distance:** under 1 mile
- **on foot:** under 30 minutes
- **terrain:** open field to forest edge
- **hazards:** none on approach; see forest entry notes above once inside
- **notes:** estate is the closest permanent structure to the forest
- **canon source:** "within walking distance of the Misty Forest" — `locations/chapter_1/deckard_estate.md:15`; distance confirmed by DM

---

### Deckard Estate ↔ Misty Forest Shar Shrine (Rowan's morning route — hidden)
- **distance:** ~2–2.5 miles  *[proposed]* (under 1 mile estate → forest's east edge, then ~1.5 mi cross-forest interior, east-to-west, to the NW-quarter shrine)
- **on foot:** **~2 hours for Rowan**, and that is him at an accelerated pace on ground he has walked daily for ten years. A **following** party is slower still — call it 2.5–3 hours — and pays the forest's navigation penalty on top (consistent mist, closed canopy, no trail).
- **why so slow for the distance:** the middle leg is trackless forest interior, not road. Closed canopy, standing mist, no path to follow and no sightlines; effective pace through it is barely over a mile an hour even for someone who knows it. Do not rate this leg off its mileage.
- **supersedes:** an earlier *[proposed]* ~1–1.5 hours, which rated the leg as though the distance were walkable at road pace. Rowan's whole morning schedule is built on the two-hour figure — see [loop_anchors.md]({{PLUGIN_ROOT}}/rules/loop_anchors.md)
- **terrain:** open field to the forest's **east** edge, then **dense, trackless** interior — mist, closed canopy, no maintained path — bearing roughly **east-to-west** across the interior toward the forest's NW quarter, ending at the Shar shrine (~100 yds W of the dead zone)
- **hidden / secret:** **not a known, mapped, or local-knowledge route.** It is Rowan Deckard's habitual cross-country line from his estate to the forest shrine for his ~7:00 AM prayer — he sets out at ~5:00 and the leg takes him two hours — **he walks it by knowledge of the woods, not by following any path.** No maintained trail marks it, no local names it, it is on no map. It is discoverable **only by following Rowan** from the estate (as a tailing party does). Do **not** surface it via directions, a mapmaker, or a local; it is learned by the feet, behind the man who walks it.
- **landmark — declare it (per [rules/travel.md]({{PLUGIN_ROOT}}/rules/travel.md)):** roughly **two-thirds of the way across** (travelling **E→W**) — after the open fields and the eastern interior, and **before** reaching the dead zone and shrine — the cross-forest line **crosses a worn walking-path** running roughly **north–south**: the maintained **Perisdottir spur** (north to the 4WI–3WI road; south, at its terminus, to **Aliss Perisdottir's house** near the forest's center). Declare it as a minor but noticeable landmark: a kept track cutting across trackless wood.
  - **Naming discipline (retrieved-concrete — [epistemic_discipline_checklist.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline_checklist.md) Row 19):** name it to the party as **"the Perisdottir path"** (or attach its destination — Aliss's house) **only if that party has themselves already travelled it** (e.g. approached Aliss's from the road). A party that has **not** walked it sees only *a worn track cutting across their line* — no name, no known destination. The recognition — *this is the path to the seer's door; the murderer's morning route runs right past it* — is available **only** to a party that already holds that knowledge.
- **hazards (DM-facing labels — narration-gated, see below):** the western end lies in the forest's NW quarter — the **dead zone** (magic fails within; Rowan's fallback anchor), the **Shar shrine** (his territory and ~7:00 AM prayer site), and his hunting range: Rowan ranges here in **wolf form** later in the morning, and only on the trespass branch (the prayer window is the man on foot, not the wolf). See [misty_forest.md]({{PLUGIN_ROOT}}/locations/chapter_1/misty_forest.md) DM Notes.
  - **Narration discipline (same gate as the path-name above — retrieved-concrete):** the labels above are **DM-facing** and party-knowledge-gated; do not narrate them to players as free facts of the route.
    - **"Dead zone"** — narrate the *label* only to a party that has already learned the concept (from Aliss / Bari / the cartographer / firsthand). A party without it perceives only the raw phenomena **on-site:** magic failing, a dead stillness, a flame that burns without a flicker — un-named. The concept is not attached to this ground until the party attaches it.
    - **"Wolf's ground" / the werewolf** — this framing is **withheld canon.** Aliss warns of the NW quarter but **withholds the wolf.** No party has the wolf / werewolf connection until it is *earned in play,* and it must **never** surface in narration before then — not as a label, not as a POV thought, not as an aside. A party warned by Aliss knows only *dangerous NW ground she forbade, holding a shrine and a vigil-keeper* — **never** "the wolf's ground." The `wolf` / `wolf form` references above are for the DM's eyes only.
- **notes:** the route's very existence is the lead — a party that learns *where the estate's keeper goes at dawn* has found the forest Shar shrine (a loop anchor) and, via the path-crossing, its proximity to Aliss's house. Pairs with the *Misty Forest Dead Zone ↔ Shar Shrine* and *Deckard Estate ↔ Misty Forest (entry)* entries.
- **canon source:** route, the path-crossing, the hidden status, and the naming discipline — confirmed by DM (this session)

---

### Walking Path (4WI–3WI road) ↔ Aliss Perisdottir's House
- **distance:** ~2 miles
- **on foot:** ~45 minutes (maintained walking path — no navigation required)
- **terrain:** maintained walking path south from the 4WI–3WI road into the Misty Forest
- **hazards:** none on the path itself; leaving the path is where forest navigation becomes difficult
- **notes:** the path terminates at Aliss's house; it does not continue further into the forest as a maintained route
- **canon source:** distance confirmed by DM

---

### Misty Forest (entry) ↔ Misty Forest Dead Zone
- **distance:** ~2–3 miles  *[proposed]*
- **on foot:** ~2–3 hours (navigation factor applies)
- **terrain:** dense forest interior, northwest quadrant
- **hazards:** same as above; the dead zone boundary is detectable (magic items stop functioning) but unmarked on the ground
- **notes:** dead zone is north and west of Aliss's house (just west of the Perisdottir path), east of the shrine; antimagic field within
- **canon source:** Geography spine — `{{PLUGIN_ROOT}}/locations/chapter_1/misty_forest.md` (W→E: road · hunting trail · shrine · dead zone · Perisdottir path)

---

### Misty Forest Dead Zone ↔ Shar Shrine
- **distance:** ~100 yards
- **on foot:** ~2 minutes
- **terrain:** forest floor
- **hazards:** shrine is outside the dead zone intentionally — Shar cannot hear prayers from within an antimagic field
- **notes:** distance is deliberate by design; the shrine must be outside the dead zone to function as a prayer anchor
- **canon source:** "West of the dead zone (~100 yards): The Shar shrine" — `locations/chapter_1/misty_forest.md:21`

---

### 4WI ↔ Misty Forest Hunting Trail (spur)
- **distance:** spur begins ~3 miles south of 4WI along the Rockwood road; spur runs ~1 mile east into the forest before reaching the camp clearing
- **on foot:** ~1 hour to reach the spur entry from 4WI, then ~20 minutes along the spur to the camp
- **terrain:** maintained road south to the spur entry; spur is a narrow hunting trail, less maintained, canopy closes overhead within minutes of leaving the road
- **hazards:** Mieke's mercenary camp on the trail (see below); Rowan's hunting range overlaps the trail's western half; the dead zone lies east of the camp, past the shrine (~quarter-mile-plus)
- **notes:** the hunting trail is a SPUR off the 4WI ↔ Rockwood road, not the maintained corridor — travelers moving between 4WI and Rockwood pass the spur entry without taking it; the spur terminates at the camp clearing and does not continue further as a maintained path
- **canon source:** spur topology confirmed by DM; supersedes the older "hunting trail between Rockwood and the road to Setland" framing in `{{PLUGIN_ROOT}}/npcs/chapter_1/remaining_npcs.md`

---

### Hunting Trail Spur ↔ Mieke's Mercenary Camp
- **distance:** ~1 mile from spur entry; the camp is at the spur's effective terminus
- **on foot:** ~20 minutes along the spur
- **terrain:** narrow trail through forest; canopy closes overhead; mist softens visibility past ~20 ft
- **hazards:** band's patrol rotates around the camp perimeter; the dead-zone-side (east) approach is the least watched
- **notes:** see [mieke_mercenary_camp.md]({{PLUGIN_ROOT}}/locations/chapter_1/mieke_mercenary_camp.md) for full layout, sightlines, and approach analysis
- **canon source:** [mieke_mercenary_camp.md]({{PLUGIN_ROOT}}/locations/chapter_1/mieke_mercenary_camp.md); spur topology confirmed by DM

---

### Shar Shrine ↔ Mieke's Mercenary Camp (game trail)
- **distance:** ~quarter-mile
- **on foot:** ~5–10 minutes
- **terrain:** game trail through forest
- **hazards:** Mieke's mercenaries present; Jiasha is held captive at this camp
- **notes:** camp resets each morning with the loop; see [the_abduction_of_jiasha.md]({{PLUGIN_ROOT}}/quests/chapter_1/the_abduction_of_jiasha.md) for the rescue mechanism (Aliss's three-signal vision) and [mieke_mercenary_camp.md]({{PLUGIN_ROOT}}/locations/chapter_1/mieke_mercenary_camp.md) for camp layout
- **canon source:** "mercenaries... camp on the game trail approximately a quarter mile from the Shar shrine" — earlier timeline reference; confirmed by DM

---

### Misty Forest (path) ↔ Misty Forest Great Tree
- **distance:** ~2–3 miles  *[proposed]*
- **on foot:** ~2 hours (off the walking path — navigation required)
- **terrain:** off the maintained walking path; dense forest, lower-center of the forest
- **hazards:** forest navigation; eastern spider corridor runs adjacent; Stripe hunts this area
- **notes:** marked by an orange flower growth at its base; an Akadi's Abarkas and a Caliconia flower can be found at the base; depart the walking path and head south
- **canon source:** "South (center): The great tree" — `locations/chapter_1/misty_forest.md:22`

---

### Duskwall ↔ Dunleaven
- **distance:** ~9 miles
- **on foot:** ~3 hours under normal conditions (20 min to 3WI + ~40 min to Deckard gate + 45 min to bridge + 75 min to Dunleaven); crossing time at the bridge not included — variable
- **terrain:** maintained road throughout; route: Duskwall → 3WI → Deckard Estate gate → dilapidated bridge → Dunleaven
- **hazards:** **bridge is completely out** — party will not discover this until they arrive at the ~1h45m mark; Deckard Estate dead zone is adjacent to the road at the gate (~1 hr mark)
- **notes:** the Deckard Estate gate is the visible landmark at the 1-hour point; Moonmaiden River runs parallel on the southern leg; Moonmaiden Falls are just outside Dunleaven; a ford upriver near Dunleaven is the fallback crossing
- **canon source:** "South to Dunleaven" — `timelines/saved/aestrum_events.md:76`; directional cues — `locations/duskwall/salient_cartographer.md:30`; leg times confirmed by DM

---

### Dunleaven ↔ Moonmaiden Falls
- **distance:** ~1 mile
- **on foot:** ~20–30 minutes
- **terrain:** river path, well-worn
- **hazards:** none
- **notes:** falls form a pond; the Selûne statue from the Duskwall shrine was dumped in this pond
- **canon source:** "Moonmaiden Falls near Dunleaven" — `locations/duskwall/salient_cartographer.md:30`; confirmed by DM

---

### Dunleaven ↔ Dunleaven Deadery (Trambeathen tomb)
- **distance:** ~2 miles
- **on foot:** ~45 minutes
- **terrain:** rough track (not on the road network); footpath southwest of town, into cave-born crypt entrance
- **hazards:** undead within; Runic Skeleton, gargoyle, lesser skeletons active in Trambeathen tomb
- **notes:** Deadery entrance is open; Trambeathen tomb requires lockpick + stone door crank
- **canon source:** "cave-born crypt system southwest of Dunleaven" — `locations/chapter_1/standalone_locations.md:39`; confirmed by DM

---

### Quarterways (4WI) ↔ Mirot
- **distance:** ~3 miles
- **on foot:** ~1 hour
- **terrain:** maintained road, running north from the crossroads; farmland gives way to the estate road
- **hazards:** none routine
- **notes:** the shortest of the four arms off Quarterways, and the reason Mirot feels close to the crossroads and far from everywhere else. The Nahamkate Desert begins ~1 mile north of the village.
- **canon source:** confirmed by DM — "about an hour north of Quarterways"

---

### Quarterways (4WI) ↔ Rockwood
- **distance:** ~9 miles
- **on foot:** ~3 hours
- **terrain:** maintained road, running south; elevation rises approaching Rockwood
- **hazards:** none routine on the road; the Misty Forest hunting-trail spur leaves this road ~3 miles south of Quarterways (see that entry)
- **notes:** the long southern arm off Quarterways. Rockwood is three times as far from the crossroads as Mirot is, which is what makes the Dundelver estate a half-day round trip from Darwinnith the Second's house rather than a short errand.
- **canon source:** the DM-confirmed 12-mile Rockwood ↔ Mirot run, less the ~3-mile Quarterways ↔ Mirot leg above

---

### Duskwall ↔ Rockwood
- **distance:** ~18 miles
- **on foot:** ~6 hours — a long day's walk, but a single day; no overnight needed
- **terrain:** maintained road; route: Duskwall → Tine Cross (3WI) → Quarterways (4WI) → Rockwood
- **hazards:** none routine on the road; southern highlands have ruins including the razed Temple of Kossuth
- **notes:** no settlement at either junction. This is the longest of Aestrum's internal settlement-to-settlement runs and the one most likely to be attempted in a single push. Rockwood is *not* symmetrical with Mirot: Mirot sits ~3 miles north of Quarterways and Rockwood ~9 miles south, so Rockwood is markedly the more remote of the two from Duskwall.
- **canon source:** location and direction — `locations/duskwall/salient_cartographer.md:40`. Distance summed from this file's own legs: Duskwall ↔ Tine Cross (~1 mi, DM-confirmed) + Tine Cross ↔ Quarterways (~8 mi) + Quarterways ↔ Rockwood (~9 mi).
- **supersedes:** ~35 miles / 1.5 days (not derived from the legs at all), and then ~12 miles (which assumed Quarterways sat at the midpoint of the Rockwood ↔ Mirot run — superseded by the DM-confirmed ~1-hour Quarterways ↔ Mirot leg).

---

### Rockwood ↔ Temple of Kossuth
- **distance:** 3 miles
- **on foot:** ~1.5–2 hours (zig-zagging ascent slows pace beyond raw distance)
- **terrain:** rough mountain path departing Rockwood; zig-zags up into the mountains, terminating at the temple site
- **hazards:** mountain path — footing uneven, route not intuitive without prior knowledge or a map; structure was razed ~200 years ago, structural instability possible at the site
- **notes:** Rockwood is the trailhead; the path does not connect onward to any other named location
- **canon source:** "ruins in the highlands including a structure labeled 'razed temple — Kossuth worshippers, approx. 200 years'" — `locations/duskwall/salient_cartographer.md:40`; distance and mountain path confirmed by DM

---

### Rockwood ↔ Mirot (Dundelver Estate)
- **distance:** ~12 miles
- **on foot:** 3–4 hours
- **terrain:** maintained road; route: Rockwood → four-way crossroads → Mirot
- **hazards:** none routine
- **notes:** Darwinnith Dundelver II claims to have been in Rockwood the night of Rezibund's murder — this is a traveled and attested route. Quarterways is **not** the midpoint: it sits ~9 miles from the Rockwood end and ~3 from the Mirot end, so the great majority of this run is the southern leg
- **canon source:** "Dundelver estate is 3–4 hours from here [Rockwood]" — `locations/chapter_1/standalone_locations.md:137`; "approximately three hours south of the Dundelver estate in Mirot" — `npcs/chapter_1/remaining_npcs.md:397`

---

### Duskwall ↔ Mirot
- **distance:** ~12 miles
- **on foot:** ~4 hours
- **terrain:** maintained road throughout; route: Duskwall → Tine Cross (3WI) → Quarterways (4WI) → Mirot
- **hazards:** none routine; Nahamkate Desert is immediately north of Mirot
- **notes:** Mirot is a community of retired estates at the desert's edge; Dundelver Estate is here. Four hours at a normal walk, three at a brisk one — which is what lets the daily Duskwall guard detail reach the Dundelver estate in the late afternoon and still leaves the walk back as an unappealing prospect. See [the quest]({{PLUGIN_ROOT}}/quests/chapter_1/the_murder_of_rezibund_highbottom.md).
- **canon source:** summed from this file's own legs — Duskwall ↔ Tine Cross (~1 mi, DM-confirmed) + Tine Cross ↔ Quarterways (~8 mi) + Quarterways ↔ Mirot (~3 mi, DM-confirmed)
- **supersedes:** an earlier *[proposed]* figure of ~50 miles / 2 days on this route, which was derived from the also-proposed Duskwall ↔ Rockwood distance and contradicted the leg distances above. The ~12-mile total here has since survived two revisions of how it is composed and is the figure the Dundelver guard timeline depends on — see [the quest]({{PLUGIN_ROOT}}/quests/chapter_1/the_murder_of_rezibund_highbottom.md).

---

### Mirot ↔ Nahamkate Desert (entry / fence-post line)
- **distance:** ~1 mile  *[proposed]*
- **on foot:** ~20–30 minutes
- **terrain:** estate road becomes irregular cobblestone, then sand; fence posts mark the original road into the desert
- **hazards:** vegetation stops abruptly; standard navigation aids fail past the fence-post line
- **notes:** the road "does not end so much as surrender"; fence posts extend further than cobblestones and are the best navigation aid into the desert
- **canon source:** `locations/chapter_1/nahamkate_desert.md:13`

---

### Nahamkate Desert (entry) ↔ Nahamkate Dead Zone
- **distance:** ~quarter-mile off the main path
- **on foot:** ~10 minutes
- **terrain:** open desert, departure from main path; no trail markers
- **hazards:** magic ceases at dead zone boundary; snakes and scorpions of species found nowhere else in Aestrum
- **notes:** identifiable by magical charring on ground — discolored stone, fused grains, scorch patterns without a fire source; a character who has encountered the Deckard Estate or Misty Forest dead zones recognizes the pattern immediately
- **canon source:** "roughly a quarter-mile off the main desert path" — `locations/chapter_1/nahamkate_desert.md:23`

---

### Nahamkate Desert (entry) ↔ Nahamkate Temple
- **distance:** ~15 miles  *[proposed]*
- **on foot:** ~6–8 hours into the desert (most of a day)
- **terrain:** open desert, canyon formations; main path navigable, departure from it is dangerous
- **hazards:** Yuan-Ti presence near the temple; snakes and scorpions; shifting sands can obscure landmarks; interior desert detail on maps not reliable past a few miles out
- **notes:** temple sits in a box canyon, marked by smoke from everlasting torches when within visual range; dead zone is a separate quarter-mile detour off this route, not on the path to the temple
- **canon source:** "box canyon... further in" / "its magical features function normally" — `locations/chapter_1/nahamkate_desert.md:23`; canyon navigation — `locations/duskwall/salient_cartographer.md:32`

---

### Duskwall ↔ Runnaheim Mountains (pass entrance)
- **distance:** ~80 miles  *[proposed]*
- **on foot:** 3–4 days
- **terrain:** rough track for part (not fully on the road network); road northwest from Duskwall through the Aestrum interior, then rough mountain approach to the pass entrance along Aestrum's north/northwest border
- **hazards:** mountain terrain near the pass; the pass exits Aestrum into the Kingdom of Vrynholt to the north — not into another Nortmunde duchy directly
- **notes:** Runnaheim Mountains form Aestrum's northern and northwestern border. (The Moonmaiden River does *not* originate here — its source is Mount Mumandad's springs in the south near Dunleaven; see [moonmaiden_falls.md]({{PLUGIN_ROOT}}/locations/chapter_1/moonmaiden_falls.md). Older surveyor notes that attribute the river to Runnaheim snowmelt are superseded.)
- **canon source:** "Runnaheim Mountains forming Aestrum's north/northwest border... mountain pass connects to Vrynholt (and onward to Mikaelvad and Dalihad)" — `locations/duskwall/salient_cartographer.md:30`; `locations/chapter_1/standalone_locations.md:132`

---

## Inter-Duchy Routes

> All routes below are outbound from Aestrum. The boundary barrier prevents snapshot recipients from leaving — see the callout in [Conventions](#conventions). Distances and times reflect the underlying geography, usable for any non-snapshot traveler and for the party once the curse is broken. Active block state for the party is in [saved/routes.md](saved/routes.md).
>
> **Escape from Aestrum — priority order (Chapter 1 endgame):**
> 1. **The Setland road, west** — fastest, most direct, the route the party already knows. Use this first unless Setland has become politically or militarily impassable for them.
> 2. **The Incorrigible, east by sea** — primary alternate. A Calimshan merchant vessel docked at Duskwall's harbor; see the [sea route entry](#aestrum-duskwall--external-ports-via-the-incorrigible) below and [the_incorrigible.md]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/the_incorrigible.md). The party should be guided toward this when overland west is closed.
> 3. **The Runnaheim pass, north into Vrynholt** — last resort. Slow (10–14 days), foreign-kingdom transit, politically exposed. Use only if both of the above are denied.
>
> Aestrum's east is the Cathar Sea — no land route east exists. Skaarsdaam and the capital are reachable only via one of the routes above plus onward travel.

---

### Aestrum (Duskwall) ↔ Setland (Charnelhold)
- **distance:** ~48 miles  *[revised]* — Duskwall ↔ 4WI (~9 mi / ~3 hrs) + 4WI ↔ Setland City (~39 mi / ~13 hrs via the Setland East Road corridor); Charnelhold shares a wall with Setland City
- **on foot:** ~2 days (~16 hours of walking; overnight at Jiasha's hut is the intended split, and a second overnight is likely depending on departure timing)
- **terrain:** maintained road; route: Duskwall → three-way junction → four-way crossroads → west through Aestrum approach → boundary → Jiasha's hut → forested foothills → farmland → Setland City → Lion's Gate into Charnelhold
- **hazards:** Setland's military installations are not along this corridor at campaign start (Malak's deliberate concealment); outbound from Aestrum is blocked for snapshot recipients (see callout)
- **notes:** the Setland road exits Aestrum from the four-way crossroads heading west (see the Setland East Road corridor entries earlier in this file); the older cardinal-direction canon ("northeast of Aestrum") is superseded by user-confirmed geography
- **canon source:** summed from the corridor segments above; supersedes prior ~120 miles / 5 days, and then ~30 miles
- **supersedes:** the ~30-mile figure, whose stated derivation was wrong in both terms — it called Duskwall ↔ 4WI "~1 day" when the internal legs make it ~3 hours, and then summed to less than the Setland-side leg alone

---

### Aestrum (Duskwall) ↔ External Ports (via The Incorrigible)
- **distance:** n/a — sea route across the Cathar Sea
- **on foot:** n/a — passage only; ~5 gold per person, flat rate, non-negotiable (Rylin does not haggle)
- **terrain:** sea voyage from Duskwall harbor east across the Cathar Sea to whichever coastal port the captain agrees to make for; duration depends on destination and weather
- **hazards:** while the curse is active, the ship strikes the invisible boundary on open water and sinks each night around 11pm with all hands (resets in the morning) — the party can only use this route once the curse is broken; once unsealed, standard maritime hazards apply
- **notes:** **primary planned Chapter-1-endgame escape.** A Calimshan merchant vessel, captained de facto by drow first mate Rylin T'Sarran (Erethezra operative). See [the_incorrigible.md]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/the_incorrigible.md) for crew, cargo, and intelligence-collection terms attached to the passage. Duskwall is on the **western** shore of the Cathar Sea (the sea forms Aestrum's eastern border, with no land route east).
- **canon source:** `locations/duskwall/the_incorrigible.md`; Cathar Sea geography — `lore/abridged_history_of_aestrum.md:106`; Cathar Sea Coastal Chart — `locations/duskwall/salient_cartographer.md:52`

---

### Aestrum (Duskwall) ↔ Mikaelvad (via Runnaheim pass — last-resort overland)
- **distance:** ~220 miles  *[proposed]*
- **on foot:** 10–12 days (3–4 days to pass entrance + 1–2 days through the pass + ~3 days across Vrynholt + ~3 days southwest into Mikaelvad)
- **terrain:** road northwest to Runnaheim pass, then mountain pass crossing into Vrynholt, then Vrynholt's southern roads, then southwest descent into Mikaelvad's fog valley
- **hazards:** mountain pass conditions; transiting a foreign kingdom (Vrynholt) requires fresh provisioning and may attract attention from local authorities — see Vrynholt note below; Mikaelvad valley sits under near-permanent dense fog, reducing visibility; limited surveyor data on the interior
- **notes:** **last-resort overland route** — reserved for when both the Setland road and The Incorrigible are unusable. The pass requires crossing the Kingdom of Vrynholt, which is not part of Nortmunde and has no obligation to grant transit to Nortmunde nationals; viable, but slow and politically exposed. Mikaelvad is currently undecided in the succession vote.
- **canon source:** pass-and-transit topology confirmed by DM; supersedes the prior "pass connects directly to Mikaelvad" framing in `locations/duskwall/salient_cartographer.md:30` and `locations/chapter_1/standalone_locations.md:132`

---

### Aestrum (Duskwall) ↔ Dalihad (via Runnaheim pass — last-resort overland)
- **distance:** ~260 miles  *[proposed]*
- **on foot:** 12–14 days (pass + Vrynholt transit + Dalihad interior roads)
- **terrain:** same as Mikaelvad route to the pass and through Vrynholt, then continuing southwest into Dalihad's quarry road network
- **hazards:** mountain pass; Vrynholt transit (see Mikaelvad entry above); Dalihad's road network is built for quarry transport — reliable but optimized for heavy wagons, not foot travel
- **notes:** **last-resort overland route** — same reasoning as the Mikaelvad-via-pass entry. Dalihad is known for stonework and quarrying; Duke will back whoever he believes will win the succession; road reliability is good once past the mountains and out of Vrynholt.
- **canon source:** pass-and-transit topology confirmed by DM; Dalihad road network — `locations/duskwall/salient_cartographer.md:46`

---

### Aestrum (Duskwall) ↔ Skaarsdaam
- **distance:** ~150 miles  *[proposed]*
- **on foot:** 6–7 days
- **terrain:** road west-northwest out of Aestrum; Skaarsdaam borders both Setland and Mikaelvad
- **hazards:** no specific road hazards known; Skaarsdaam is politically isolated — "not much reason to go that direction unless you're already from there"
- **notes:** Duke Amblecrown's seat; Skaarsdaam is currently voting for itself in the succession; sees less traffic than the eastern routes
- **canon source:** "Skaarsdaam and its borders with Setland and Mikaelvad" — `locations/duskwall/salient_cartographer.md:48`

---

### Aestrum (Duskwall) ↔ Nortmunde (capital)
- **distance:** ~250 miles  *[proposed]*
- **on foot:** 10–12 days
- **terrain:** long route toward the geographic center of the kingdom; road quality likely decreases past active duchy borders
- **hazards:** extended journey requires provisioning stops; political sensitivity — Regent Tarwick Grale currently holds the capital
- **notes:** the capital sits at the kingdom's geographic center; this is the longest journey among the inter-duchy routes; any diplomatic mission to the capital requires planning for a multi-week round trip
- **canon source:** "capital at the kingdom's geographic center" — `locations/chapter_1/standalone_locations.md:114`

---

### Setland (Charnelhold) ↔ Skaarsdaam
- **distance:** ~120 miles  *[proposed]*
- **on foot:** 5 days
- **terrain:** Setland's western road connecting to Skaarsdaam's eastern border
- **hazards:** Setland military presence near the border
- **notes:** relevant if the party is already in Setland and needs to reach Skaarsdaam without returning through Aestrum; not currently blocked by the Aestrum curse (applies only to Aestrum outbound travel)
- **canon source:** duchy adjacency — `locations/chapter_1/standalone_locations.md:114` ("each bordering two others")

---

## The Setland East Road (Setland City ↔ Jiasha's Hut ↔ 4WI)

The east road out of Setland City carries the campaign opening from Charnelhold to the Aestrum boundary. Distances are confirmed by DM. Chapter 2 state lives at [chapter_2/setland_east_corridor.md]({{PLUGIN_ROOT}}/locations/chapter_2/setland_east_corridor.md). The campaign-running content for the overnight stop and moon amulets at Jiasha's hut lives in [npcs/chapter_1/jiasha.md]({{PLUGIN_ROOT}}/npcs/chapter_1/jiasha.md).

### Setland City ↔ Jiasha's Hut
- **distance:** ~24 miles  *[derived from 8 hours at standard pace]*
- **on foot:** ~8 hours (7 hours farmland belt + 1 hour forested foothills) — a single long day with morning departure
- **terrain:** maintained road east; cobbled near Setland City, packed earth and gravel through the foothills
- **hazards:** none routine at campaign start; the mercenary encounter may fire in the forested foothills if the bounty thread has not been carried into Aestrum (see [setland_east_road.md]({{PLUGIN_ROOT}}/locations/chapter_1/setland_east_road.md))
- **notes:** farmland south of the road, forest north; foothills are short (~1 hour) and rise to where Jiasha's hut sits at their eastern edge; hut is the intended overnight stop before crossing into Aestrum; the campaign uses rain in the afternoon to motivate the stop
- **canon source:** distances confirmed by DM

---

### Jiasha's Hut ↔ Aestrum Boundary
- **distance:** ~200 feet
- **on foot:** under a minute
- **terrain:** maintained road through forest immediately east of the hut clearing
- **hazards:** the boundary itself is invisible to non-snapshot travelers; a first-time crossing produces no in-fiction signal
- **notes:** the hut sits essentially at the threshold of Aestrum; this proximity is the campaign-design point — Jiasha is the last waystation before the loop. The overnight at the hut is the campaign's built-in snapshot-positioning lever for the party — see [Corridor DM Notes](#corridor-dm-notes) for the framing guidance and [rules/snapshot.md]({{PLUGIN_ROOT}}/rules/snapshot.md) (Reset point) for the mechanic.
- **canon source:** [rules/time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md) on snapshot-receipt mechanics; distances confirmed by DM

---

### Aestrum Boundary ↔ Four-Way Crossroads (4WI)
- **distance:** ~15 miles
- **on foot:** ~5 hours
- **terrain:** maintained road, fair quality but less consistently kept than the Setland side
- **hazards:** Aestrum residents do not remember previous visits (loop effects); behavior of NPCs along this stretch follows the standard loop pattern (see [rules/time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md))
- **notes:** 4WI connects to Mirot (north), Rockwood (south), the three-way junction toward Duskwall (east), and back west toward Setland (the way the party came). **This is the longest single leg inside Aestrum, and deliberately so** — it is the stretch that carries the [Duskwall ↔ Jiasha's Hut](#duskwall--jiashas-hut-the-locked-leg) design constraint. Nothing lives along it; it is empty approach road, and it is supposed to feel like a commitment to walk.
- **canon source:** back-solved from the locked Duskwall ↔ Jiasha's Hut figure (~24 mi) less Duskwall ↔ Tine Cross (~1 mi, DM-confirmed), Tine Cross ↔ Quarterways (~8 mi), and the Boundary ↔ Hut gap (~200 ft, DM-confirmed)
- **supersedes:** an earlier ~6 miles / ~2 hours. That figure made a dawn-to-midnight round trip from the hut to Duskwall comfortable, which inverts the design intent of the corridor

---

### Duskwall ↔ Jiasha's Hut (the locked leg)
- **distance:** ~24 miles  **[LOCKED — design constraint, do not derive around it]**
- **on foot:** ~8 hours each way
- **terrain:** maintained road throughout; route: Duskwall → Tine Cross (3WI) → Quarterways (4WI) → west across the Aestrum approach → boundary → hut (200 ft beyond)
- **hazards:** none routine — and that is the point (see below)
- **composition:** Duskwall ↔ Tine Cross (~1 mi) + Tine Cross ↔ Quarterways (~8 mi) + Quarterways ↔ Boundary (~15 mi) + Boundary ↔ Hut (~200 ft)

**Why this value is locked.** Jiasha's hut sits ~200 feet *outside* the Aestrum boundary, which makes it the nearest ground on which midnight cannot take you. A party camped there has not yet been snapshotted. The journey this leg is built to frustrate is therefore a specific one: **leave the hut at dawn, reach Duskwall, make contact with someone in authority, and get back out past the boundary before the midnight Sleep step fires.**

That window is 18 hours (dawn ~6 AM → 12:00:00 AM). At the 3 mph baseline, 24 miles each way consumes 16 of them, leaving **two hours** to cover arrival at Duskwall's gate around 2 PM, finding a representative, waiting to be seen, and being heard — in a city whose officials keep daylight hours. The hard turnaround is 4 PM.

**It is meant to be highly unlikely, not impossible.** A party that force-marches (5e forced march, CON saves, exhaustion), finds its representative immediately, and wastes nothing gets back with minutes to spare. Everyone else is still inside the boundary at midnight and is snapshotted — which is the trap the corridor exists to set. Do not soften this by improvising a shortcut, a convenient courier, or an official who happens to be waiting at the gate.

**The deadline is midnight, not dark.** Night travel on this road is not dangerous: [rules/travel.md]({{PLUGIN_ROOT}}/rules/travel.md) establishes no random encounters inside Aestrum or on the approach, and the corridor register holds the road as peaceful and well-kept. Nothing punishes a party for walking after sundown except the cycle itself.

**Mounted travel would defeat this entirely** (~3 hours each way, ~12 hours of slack) — which is why Aestrum has no saddle horses and no riding tack at all, and why the party is outfitted on foot in Setland before they ever reach the hut. See [rules/travel.md]({{PLUGIN_ROOT}}/rules/travel.md). If a party does somehow turn up mounted, that is a real change to the corridor's difficulty and must be priced deliberately rather than waved through.

- **canon source:** locked by DM as a design constraint; the component legs are derived to satisfy it

---

### Setland City ↔ Four-Way Crossroads (4WI) (full corridor)
- **distance:** ~39 miles  *[derived]*
- **on foot:** ~13 hours of foot travel (Setland City → 7 hrs farmland → 1 hr foothills → Jiasha's hut → 200 ft to boundary → 5 hrs to 4WI); the campaign expects an overnight at the hut, splitting the journey across two calendar days
- **terrain:** maintained road throughout; farmland, forested foothills, descent into Aestrum interior
- **hazards:** see segments above; the corridor is peaceful and productive at campaign start, devastated in Chapter 2 (see [chapter_2/setland_east_corridor.md]({{PLUGIN_ROOT}}/locations/chapter_2/setland_east_corridor.md))
- **notes:** **this corridor is materially shorter than the original Aestrum ↔ Setland (Charnelhold) inter-duchy entry indicated.** That entry once read 120 miles / 5 days; it now reads ~48 miles and is derived from these segments rather than estimated independently
- **canon source:** the Setland-side segments are DM-confirmed and unchanged; the Aestrum-side segment grew with the locked Duskwall ↔ Jiasha's Hut constraint above
- **supersedes:** an earlier ~30 miles / ~10 hours, which assumed a ~6-mile Boundary ↔ 4WI leg

---

### Corridor Register & Regional Notes (Chapter 1)

*Brief regional content that doesn't fit in the per-segment entries above. Chapter 2 overrides live at [chapter_2/setland_east_corridor.md]({{PLUGIN_ROOT}}/locations/chapter_2/setland_east_corridor.md).*

- **Hold the peaceful-and-productive register.** The road, the farms, and the forest are healthy at campaign start. Crops in the fields, smoke from chimneys, kept fences, productive forest, fair-priced inns, road-warden posts in good repair. The duchy is on a quiet footing (Malak's deliberate concealment of war preparations — see [setland_city.md]({{PLUGIN_ROOT}}/locations/chapter_1/setland_city.md)). Lean into this; the Chapter 2 contrast lands only if Chapter 1 sells the peace.
- **Farmsteads.** Independent smallholdings paying Setland's standard agricultural tithe. Farmers are accustomed to travelers and treat them with friendly indifference — sell food and water at fair prices, permit short rests, pass along news without much filtering.
- **Foothill forest.** Healthy and productive. Setland charcoal-burners and timber crews work the lower slopes on a sustainable rotation; deeper forest is left largely alone. Game plentiful. Not the Misty Forest — no antimagic strangeness — but dense.
- **Faction reach (Chapter 1):** Setland's writ runs along the corridor (light presence — road-warden, occasional patrol). Black Arrows are opportunistic transients, not garrisoned. Aestrum has no Setland-side presence. On the Aestrum-side approach, residents behave per loop conventions.

### Corridor Seed Secrets (Chapter 1)

*Vessel-agnostic. Any elevated character can be assigned one at upgrade time. Chapter 2 may elevate these threads — see chapter overlay.*

- A particular farmhouse on the south side of the road, roughly mid-belt, is a Setland court intelligence drop. The farmer (paid quietly) holds messages for couriers passing in either direction. Quellenna has used the drop several times. The farmer believes he serves the duchy at large; he does not know he serves the advisor specifically.
- A charcoal-burner working the lower slopes has noticed the volume of timber crews has begun to tick up over the past several months. He has not connected the pattern to anything. He should. He will not.
- A road-warden post midway through the farmland belt is staffed by a sergeant who maintains a private ledger of wagons passing east toward Aestrum and back. He keeps it from idle interest. Nobody has asked to see it.

### Corridor DM Notes

- **The mercenary encounter is the only pre-authored event** on the corridor in Chapter 1. It lives in [setland_east_road.md]({{PLUGIN_ROOT}}/locations/chapter_1/setland_east_road.md), *The Mercenary Encounter* — fires in the forested foothills shortly before Jiasha's hut.
- **The boundary crossing is silent, and stays silent.** A first-time party crosses into Aestrum with no in-fiction signal — no shift in the air, no threshold-feeling. What the first snapshot resident gives them is **geographic confirmation only** (*yes, this is Aestrum; the Duskwall road is that way*) — **not** a reveal of the loop or that anything is wrong. Do not read "they discover they are in Aestrum from the first interaction" as "the first NPC tips the curse." It does not.
- **Keep Aestrum normal on the way in — early NPCs do NOT reveal the wrongness (load-bearing design).** The entry sequence exists to get the party *comfortable, incurious, and committed* — deep enough that a midnight snapshot quietly fixes their reset point and traps them — **before** anything reads as wrong. An early "something is wrong here" is the one failure that can turn a party back across the line before they are caught, which collapses the Chapter 1 premise. Therefore:
  - Land, road, farms, and residents all present as an ordinary, prosperous duchy. Nothing in the environment rings false — the loop is externally imperceptible (see [{{PLUGIN_ROOT}}/lore/key_lore_summary.md]({{PLUGIN_ROOT}}/lore/key_lore_summary.md), *External imperceptibility*).
  - Snapshot residents behave as normal people living an ordinary day: warm or indifferent per their nature, free with directions and mundane local color, and **puzzled by pointed questions.** A stranger asking "what's wrong here?" or "what year is it?" gets the odd look anyone would give.
  - The decade-stale frame (residents live 1480; it is really 1490) is real but **never volunteered.** The loop resets a Kythorn day, so season and month match — only the *year* is off, and no countryman states the year unprompted. It surfaces **only if the player drives it** (asks the date outright, presses stale news). Asked directly, the resident answers **honestly** — it is 1480 by their lights — and finds the asker strange. The reveal is then the *player's* to make, not the narrator's.
  - The narrator neither flags the wrongness nor reassures against it — both leak hidden state (Calliope's hidden-state-surfacing check: denial **and** its emphatic-affirmation twin). Render plain perception and stop.

  The first "that doesn't add up" should come from the party's own probing, or from accumulation on a later pass (the forgetting) — never handed to them at the door.
- **The overnight at Jiasha's hut is the snapshot-positioning lever.** This is the actionable point — by the time the party is on the boundary stretch, the decision is already made. A party that overnights at the hut spends the night on Setland soil (no snapshot fires) and crosses into Aestrum the following morning, giving them a full Aestrum-day of travel before their first midnight catches them and fixes their permanent reset point. A party that declines the overnight and pushes across the boundary the same evening will likely be snapshotted at Duskwall or near the boundary, locking their reset point near the western edge of the duchy for the rest of the campaign. The campaign's built-in motivators for the overnight stop (afternoon rain, Jiasha's warm offer, the late hour by the time they reach the foothills) exist to make declining feel like the unusual choice. Use them — and if the party still pushes through, let them; the worse reset point is theirs to live with. Do not surface this rationale out-of-character; Jiasha may suggest the overnight plainly (and does, per her standard offer) but will not explain mechanics. See [jiasha_hut.md]({{PLUGIN_ROOT}}/locations/chapter_1/jiasha_hut.md) DM Notes and [rules/snapshot.md]({{PLUGIN_ROOT}}/rules/snapshot.md) (Reset point).
- **Tier discipline:** Tier 1 along the corridor at campaign start. Turning on Jiasha is Tier 2, not Tier 3 (see [npcs/chapter_1/jiasha.md]({{PLUGIN_ROOT}}/npcs/chapter_1/jiasha.md) and [rules/consequences.md]({{PLUGIN_ROOT}}/rules/consequences.md)). The corridor does not protect any specific NPC with plot armor.

---

## Special / Conditional Routes

### Charnelhold — Escape Tunnel (Quellenna's quarters → Aidra's house)
- **distance:** ~100 yards (beneath the shared wall between Charnelhold and Setland City)
- **on foot:** ~1–2 minutes (underground passage, no navigation required)
- **terrain:** underground tunnel; well-maintained; no light source
- **hazards:** entering from Aidra's end surfaces in her cellar — if Aidra is present, she will react with immediate hostility (see NPC notes); tunnel is not on any official Charnelhold floor plan
- **notes:** concealed entrance in Quellenna's quarters (behind furniture never moved by staff); exit in Aidra's cellar; Aidra is currently absent from her house (commanding Setland forces in Aestrum); party can enter from cellar end without a key; this route bypasses all castle gates and guards
- **canon source:** `{{PLUGIN_ROOT}}/locations/chapter_1/charnelhold_escape_tunnel.md`; `{{PLUGIN_ROOT}}/npcs/chapter_1/quellenna_ilphekiir.md`

---

### Runnaheim Pass — Why It's a Distinct Entry

The Runnaheim pass route is recorded as a distinct entry from the direct Aestrum ↔ Setland road so the option remains visible when it becomes relevant — e.g., if the party cannot or will not travel through Setland.
