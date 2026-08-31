---
id: loc_setland_city
name: Setland City
region: Setland (duchy capital)
curse_affected: false
connected_locations: [loc_charnelhold, loc_setland_east_road, loc_aidra_house]
npcs_present: [npc_emanthur_wallerbridge, npc_roland_elakian]
---

## Campaign Opening — Guidance, Not a Leash

**This location is the campaign's starting point.** The opening's job is to make the *next step obvious* without ever forcing it. The party should never wonder where the campaign expects them to go until they have actually crossed into Aestrum. They should also be free to wander the city, explore the farmland and forested foothills east of it, ignore the call entirely, or actively try to bypass the campaign. **If they break free, let them.** A clear guide, not a leash.

**The intended sequence:**

1. **Party arrives in Setland City** (hook provided per the table at character creation).
2. **Party hears about the expedition** — criers in the squares, postings on public boards, casual mention from any city NPC asked about work, news, or the day. The line is consistent across every source: *"Duke requests those of sound mind and body for expedition. Eleventh bell, at The Lion's Den."*
3. **Party presents themselves at the Lion's Den** within Charnelhold — see [the_lions_den.md]({{PLUGIN_ROOT}}/locations/chapter_1/the_lions_den.md). Quellenna delivers the back-taxes pitch on Malak's behalf.
4. **Party departs Setland City via the east road** — through farmland, into forested foothills.
5. **Party encounters Jiasha** at her hut at the edge of the forested foothills, essentially at the Aestrum boundary (see [routes.md]({{PLUGIN_ROOT}}/locations/chapter_1/routes.md) for corridor mechanics and [npcs/chapter_1/jiasha.md]({{PLUGIN_ROOT}}/npcs/chapter_1/jiasha.md) for the overnight stop and moon amulet exchange).
6. **Party crosses into Aestrum.**

**How to apply this without railroading:**

- Surface the expedition pitch through several channels in the first scene or two. Never just once — the party should hear it three or four times from independent sources within their first hour in the city.
- If the party asks an NPC for work, news, gossip, or rumors, the expedition is in the answer.
- If the party explores the docks, the markets, an enchantment shop, the temple district — they may hear about the expedition there too. The city is talking about it.
- If the party leaves the city by the east road *without* visiting the Lion's Den, do not stop them. They will reach the forested foothills and Jiasha regardless. The Lion's Den pitch is the cleanest entry into the campaign's middle, but it is not the only one.
- If the party leaves by any other road (south to Skaarsdaam, by ship from the port, etc.), let them. Some of those exits are dead-ends for the campaign and that's fine — the campaign has not started yet, and a party that wants to fundamentally bypass Aestrum has earned the conversation that follows.

## Overview

Capital of the duchy of Setland. A walled city of perhaps thirty thousand, built in tiers along the south slope of the rise crowned by Charnelhold. The two share a wall — the castle and the city are not separated by open ground; Charnelhold's south face *is* part of the city's northern wall. The shared wall has a single internal gate (the Lion's Gate) that the duchy controls; presenting yourself for court business means passing through it.

Setland's color palette is everywhere: deep crimson, black, dull gold. Lion-headed motifs adorn doorways, fountains, the brass buckles of guardsmen's belts. The city reads as a confident, prosperous duchy capital, not as a war camp.

At campaign start the city is **deliberately not on a war footing.** The King of Nortmunde is still alive. Any visible military build-up would raise eyebrows among neighboring duchies, and Malak — guided by Quellenna — has been careful not to give them anything to look at. The garrison is at normal strength. The parade grounds are quiet. The gates are open and patrolled at their usual cadence. The duchy is, by every public indicator, going about its ordinary business.

The expedition pitch fits inside that posture: it is framed as a *diplomatic financial recovery action* — collecting ten years of unpaid Aestrum back-taxes on behalf of Nortmunde — and is therefore exactly the kind of routine ducal affair that warrants a small contracted party, not a regiment. That this same pitch later becomes the predicate for an actual military operation (once the King dies and the framing flips from financial recovery to succession-era assertion) is not something any street-level resident is in a position to read.

Setland City is **outside Aestrum's loop entirely.** Time runs forward here. Magic functions normally. Nothing resets at dawn.

## What's Here

- **The Lion's Gate (north)** — internal gate in the shared wall between Setland City and Charnelhold. The only public approach to the castle. Guards check names against a small daily list of expected court business; otherwise petitioners are routed to a holding hall.
- **Charnelhold** — the ducal seat. Sits directly atop the north rise, sharing its south wall with the city. See [charnelhold.md]({{PLUGIN_ROOT}}/locations/chapter_1/charnelhold.md).
- **The Lion Square** — the central plaza below the Lion's Gate. Public notices, messaging boards, a permanent crier's stand. The square is where most residents first hear the day's news.
- **The Merchant Quarter** — south and east of Lion Square. Markets, money-changers, several inns (the Crimson Hart and the Two Banners are the largest; a number of smaller establishments serve traders and travelers).
- **The Docks** — a respectable port on Setland's coastline, accessed via the city's west-southwest gate and a short ride down to the water. Coastal traffic to other Nortmunde ports, a modest fishing fleet, a customs house. The docks are not bustling at campaign start — Setland's commerce moves mostly overland — but they are functional, well-kept, and quietly expected to grow. (DM-only: a campaign-active timer; the port grows visibly between chapters as Setland's posture shifts.)
- **Manny's Mysterium** — an enchantment shop in the merchant quarter, run by Emanthur "Manny" Wallerbridge. The city's primary destination for magical goods and minor enchantment work. See his future file for personality; he is a useful early-campaign NPC because he sells things the party wants, talks while he works, and has heard most of what passes through the merchant quarter.
- **The Barracks District** — northeast quadrant. The garrison at normal strength. Quiet at campaign start.
- **The Parade Ground** — north of the barracks, against the castle wall. Empty at campaign start. (Later in the campaign, after the King's death, this fills.)
- **The Temple District** — three modest temples to state-observed gods. None notable. Religion in Setland is correct, attended, and weightless.

## Pressure Mechanisms — Surfacing the Expedition

*These are not "ways to force the party toward Charnelhold." They are the channels through which the expedition is in the air.*

- **Criers in Lion Square and the Merchant Quarter.** Per [time_and_events.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/time_and_events.md): `time:` on each hour from sixth bell (6:00 AM) through tenth bell (10:00 AM) inclusive — the call goes up five times, on the hour, exact; `duration:` ~30 seconds per call, then the criers move to their next station; `catchup: full` — every call is identical, so missing one means catching the next. The final call goes out at tenth bell; **no call is made at eleventh bell** (the call is *for* eleventh bell, not at it). The call: *"Duke requests those of sound mind and body for expedition! Eleventh bell, at The Lion's Den!"* — terse, public, identical across criers.
- **Postings on public messaging boards.** Every district has one. Each carries an identical printed notice giving the same line, the time, the location, and a small lion-headed seal. The notices are fresh — papered up this morning.
- **Organic mention from any city NPC.** Innkeepers, shopkeepers (including Manny), dockhands, the magistrate's clerk, the recruiting sergeant — if the party engages any of them on work, news, the day, what's happening — the expedition is in their answer. They don't know much about it (because it has not been briefed publicly) beyond what the criers say.
- **The Crimson Hart and Two Banners.** Both inns have a small clutch of would-be expedition applicants nursing drinks and trying to look qualified. Useful color for a party that wants to feel out the competition. **See "Who Actually Takes the Expedition" below for how this resolves at the Lion's Den.**
- **Manny at the Mysterium.** If asked about the expedition, he says he's heard it called a "diplomatic detail." He does not endorse going. He does not warn against it either. He is a merchant, and merchants don't choose sides in things they don't have to.

## Who Actually Takes the Expedition

The criers and postings cast a wide net. The expedition itself is, by design, a small contracted party. The campaign needs to keep the party from being bundled with a handful of NPCs the player didn't author. The convention is:

- **A handful of locals show up** for the eleventh-bell call at the Lion's Den. Not a mob — three or four, plus the PC(s) and any user-authored party NPCs declared at campaign init. Atmosphere, not staffing.
- **The non-author-declared applicants bow out during or right after Quellenna's pitch.** The framing (an *Aestrum* expedition) lands on people who have heard the rumors their whole lives, and the rumors do their work. A would-be applicant nods through the introduction, hears the destination named, and quietly excuses themselves. Another lasts until the back-taxes brief and then leaves. One or two thank Lady Ilphekiir for her time on the way out. By the close of the pitch, every applicant who was not declared at campaign init has withdrawn.
- **The party is what's left in the room.** Exactly the PC(s) and any user-authored party NPCs. Quellenna does not press the withdrawers; she lets them go. The contrast is the point — *these are the people who heard the same thing you did and chose otherwise.*
- **Quellenna formally accepts the remaining applicants as the contracted party** at the close of the pitch. That moment is the in-fiction **join-point** for any author-declared party NPCs who were not already with the PC: from the pitch's acceptance onward, they are party. The campaign-state field `traveling_with_party` flips from `false` to `true` for those NPCs at this beat. (Their per-NPC frontmatter may carry a `traveling_with_party_join_point` note describing the moment in their own terms.)
- **A non-author-declared NPC who somehow remains in the room past the bow-out beat is still sent away** with the duchy brushoff — *"thank you for your interest, please leave your name with the magistrate's office for future consideration."* The pitch is not a recruiting wall for the campaign; only author-declared NPCs walk out as party. This is firm.

**Why this works.** User-authored NPCs are pre-authorized party members the player has chosen for this campaign. The pitch surfaces the in-fiction reason the three (or four, or five) of them end up bound together as a contracted party — they each independently saw the postings, walked into the Lion's Den, stayed when others bowed out, and were accepted by the duchy as the recovery team. The acceptance is the moment "party" becomes the right noun. Before the acceptance, they are strangers who happened to all stay; after it, they are colleagues with a sealed letter of introduction and the same east road to take.

**Per-NPC join-point fidelity.** An author-declared NPC's `traveling_with_party_join_point` note should describe the join in *their* terms — what made them stay, what they read off the other remaining applicants, whether they greet the others or hold back. The pitch is the common in-fiction event; the *experience* of joining is per-NPC.

---

## What People Say When Asked About Aestrum

*Useful color for any scene where the party is trying to learn what they're being sent into.*

- **Nobody in Setland City has actually spoken to a current resident of Aestrum.** This is consistent and worth noticing. Ask ten city residents about Aestrum and you will get ten answers; ask any of them whether they have *spoken* to someone who lives there now, and the answer is always second-hand or third-hand. *"My cousin's friend used to trade out there, years ago. He said —"* *"There was a man at the docks last winter who'd been —"*
- **The stories are uniformly about forgetting.** Aestrum residents don't remember previous visitors. A merchant you spent an afternoon with last spring greets you the next time as a stranger. A traveler who lodged at an inn returns a year later and the innkeeper does not recognize them — yet the room is somehow ready, the prices the same, the staff working the same patterns as before. No one in the city can explain it; most chalk it up to rural eccentricity or exaggerated traveler tales.
- **Avoid surfacing time oddities or repeated-conversation patterns.** The forgetting tell is fine to plant — it is what Setlanders genuinely observe. The deeper structure of the loop (the day resetting, conversations replaying, fixed daily timings) is not visible from outside Aestrum and must not appear in city rumor. A second conversation with the same Aestrum resident does not replay — minor variables shift it — so a traveler who visited twice would not be able to report "the same conversation." Hold this line.
- **Border traders who do go in come back fine.** A handful of merchants near the border occasionally cross into Aestrum to trade — and return without difficulty. They report the same kinds of strange interactions (Aestrum residents who have forgotten the previous visit), but it doesn't trouble them. They go in, do their business, leave before nightfall, come back the next month. The pattern works.
- **No one in Setland City frames Aestrum as dangerous.** Strange, yes. Backward, yes. Worth a long expedition? Apparently — that's what the criers are saying. But not *dangerous.* The expedition recruits in the inns are not afraid; they are curious and looking for coin.

**DM-only — why the traders get out:** Aestrum's loop bubble acts only on those who have received a Modify Memory snapshot. A subject who enters Aestrum after the morning Wake step and leaves before that night's Sleep step never receives a snapshot and is therefore not subject to the bubble's containment or the next morning's reset. Codified in [time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md#snapshot-receipt-and-the-boundary-bubble).

## Faction Reach

- **House du Leon (ducal authority):** total but quiet. Garrison at normal strength; the Lion's Hand patrols at normal cadence; the duchy's writ runs without question but does not flex its arm in public.
- **The Black Arrows:** quiet but pervasive. The Elakian clan's long-standing contract with Charnelhold gives them operational latitude in the city. They do not display colors. They handle the off-the-books work the duchy commissions through Quellenna's contact channels.
- **Setland court (Quellenna):** invisible to street-level residents. Even at court she is *only an advisor.* See DM Notes below.
- **Foreign factions:** Skaarsdaam and Mikaelvad maintain quiet observers. Aestrum has no presence — and a current Aestrum resident in Setland City at campaign start would be conspicuous (none should appear).

## Seed Secrets

*Vessel-agnostic. Any elevated character can be assigned one of these at upgrade time.*

- A Lion's Hand quartermaster is skimming the requisition books — modest amounts, well below what would trigger an audit. Quellenna knows. She tolerates it as a control lever: the quartermaster owes her his silence and, when she needs something the books should not record, owes her his cooperation. The arrangement has never been articulated between them. He understands. *(One instance of Quellenna's standard operating method — see DM Notes.)*
- A magistrate's clerk who has run private debts at the city's quieter card-house. Quellenna learned of the debts through a different thread entirely and has never raised them with him. She does not need to. He behaves as a man who knows. *(Second instance — same SOP.)*
- A respected merchant in the wine quarter who once retained a Black Arrows discretion service for a personal matter that would not survive his wife knowing about it. The transaction left a paper trail Quellenna has copies of. He has been a quietly reliable channel for off-the-books duchy procurement ever since. *(Third instance — same SOP.)*
- A specific contact-house in the merchant quarter (a wine-importer's shop with a closed upstairs room) is the routing point for Black Arrows commissions that originate in Charnelhold. The shop's proprietor does not know what they actually traffic in.
- A border trader operating out of the Crimson Hart has crossed into Aestrum more than a dozen times over the past several years and never once been remembered by the same resident twice. He has not connected the pattern to anything beyond rural strangeness; he has stopped trying.

## Callback Slots

- "A Charnelhold contact who routed the Galadiil bounty to the Black Arrows" → referenced in [quellenna_ilphekiir.md]({{PLUGIN_ROOT}}/npcs/chapter_1/quellenna_ilphekiir.md) and [standalone_locations.md]({{PLUGIN_ROOT}}/locations/chapter_1/standalone_locations.md). Likely sits in Setland City rather than inside the castle itself.
- "The skimming quartermaster Quellenna keeps as a quiet asset" → unnamed, callback slot for an elevated Lion's Hand character.
- "A junior magistrate's clerk who notices things the duchy would prefer not noticed" → potential ally for a party that returns to Setland later.
- "A border trader who has crossed into Aestrum repeatedly without realizing what he was observing" → useful for a returning party investigating the loop from the Setland side.

## Named Characters

**Emanthur "Manny" Wallerbridge** — Proprietor of Manny's Mysterium. Enchanter. Talks while he works, knows everyone who passes through the merchant quarter. *(See his future file for full personality and stock.)*

*Other named NPCs at campaign start live in [the_lions_den.md]({{PLUGIN_ROOT}}/locations/chapter_1/the_lions_den.md) and [charnelhold.md]({{PLUGIN_ROOT}}/locations/chapter_1/charnelhold.md). Setland City itself is mostly a stage at the opening; characters get elevated here as the campaign returns.*

## DM Notes

- **The opening is a guide, not a leash.** Reiterating because it matters: the party can wander. They can spend a day in the merchant quarter. They can take the east road without visiting the Lion's Den. They can sail out of the port. Let them. The expedition pitch is loud and frequent enough that any party engaging the city for more than a few minutes will know where the campaign expects them — and a party that *chooses* to ignore that is having a more interesting opening, not a broken one.
- **The campaign has teeth.** See [rules/consequences.md]({{PLUGIN_ROOT}}/rules/consequences.md) for the three-tier model. In Setland City specifically: Tier 1 actions (petty trespass, low-stakes nosing around) get proportional in-fiction responses; Tier 2 actions (deliberately stepping off the expected flow) shift the city's posture from welcoming to indifferent or hostile; Tier 3 actions (attempting to remove canon NPCs or destroy canon locations — Quellenna, Malak, Charnelhold itself) trigger the wildcard-danger response, including DM honesty out-of-character about what the action would cost the campaign.
- **Quellenna's profile in the city is invisible and at court is "merely advisor."** Even within the Lion's Den she works to never *appear* to be the actual decision-maker. The mechanics:
  - On banal matters (a tax adjustment, a guild dispute, a magistrate's docket question), Quellenna defers to Malak openly and immediately. He answers. The answer is fine because the question was small. The court sees His Grace ruling on routine business and the advisor staying out of his way.
  - On matters of weight, Quellenna does not propose answers — she **guides Malak to them.** A small reframing question. A reference to "what His Grace did last spring on the matter from Beluir." A half-finished observation she lets Malak complete. The court hears Malak ruling and Quellenna listening attentively. Malak hears himself thinking clearly.
  - The mask is total. Petitioners with decades of court experience may suspect, but cannot point to a single moment where she overstepped. Newer party arrivals will get no signal at all unless they specifically watch for the pattern across multiple audiences. This is by Quellenna's design.
- **Leverage and secrets as currency — Quellenna's standard operating method.** Shar-inspired and held with discipline across the campaign. The principle: *find the secret, hold it until you need it.* She prefers controllable assets over clean ones, and she does not spend the leverage casually — most of the people she has documented compromises on have never been asked for anything, and may never be. The mere knowledge that she *could* ask is sufficient to keep them in alignment. The quartermaster, the magistrate's clerk, and the wine merchant (above) are three instances of the same pattern; she has many more. If the party surfaces this pattern across multiple data points, they have glimpsed Quellenna's method without quite seeing her — and they may begin to understand why Charnelhold runs the way it does.
- **The expedition pitch language is deliberately civilian.** *"Sound mind and body for expedition."* No mention of taxes, of Aestrum specifically, of military duty, of the duchy's interests. This is by Quellenna's design — the pitch reads as adventurer-grade work, not as a state operation. The actual framing (back-taxes, diplomatic recovery action) is delivered only in the Lion's Den itself, in private, to the assembled candidates.
- **The east road is the way to Aestrum.** Due east through farmland (~7 hours), then forested foothills (~1 hour), then Jiasha's hut at the eastern edge of the foothills, then ~200 feet to the Aestrum boundary, then ~2 hours to 4WI inside Aestrum. Route mechanics and corridor register live in [routes.md]({{PLUGIN_ROOT}}/locations/chapter_1/routes.md#the-setland-east-road-setland-city--jiashas-hut--4wi); campaign-running content for the overnight at the hut and moon amulets lives in [npcs/chapter_1/jiasha.md]({{PLUGIN_ROOT}}/npcs/chapter_1/jiasha.md); Chapter 2 devastation lives in [chapter_2/setland_east_corridor.md]({{PLUGIN_ROOT}}/locations/chapter_2/setland_east_corridor.md).
- **The escape tunnel is now canonized at ~100 yards** beneath the shared wall (reconciled from the prior "quarter-mile" framing). See [charnelhold_escape_tunnel.md]({{PLUGIN_ROOT}}/locations/chapter_1/charnelhold_escape_tunnel.md).
- **Aidra as background introduction on castle grounds.** Aidra Calemthor is Malak's General and a fixture at Charnelhold — introduce her as such while the party is on castle grounds. She does not need to be a scene. She can be glimpsed crossing the courtyard with two officers in tow, briefly named when she enters the Lion's Den to pass a message to Malak, or referenced by a servant ("the General is at the parade ground today, Lady Ilphekiir said to advise you"). The goal is *recognition* — when the party encounters her later in Aestrum, they should know who she is by name and face. Her house in the city is not on the campaign's surface at this point, and the campaign does not lead the party to it — the introduction is professional and public, not domestic.
- **If players try to find her house anyway, let them.** If a PC explicitly investigates her residence — asks around in the city, follows her after court, scouts the wall — let them do it. The information is discoverable. The campaign does not pretend otherwise. **But the campaign has teeth.** Snooping on castle grounds, scaling the shared wall, breaking into a Setland general's home — all of these are actions Charnelhold's security responds to, and the response is a cadre of guards, jail in the Lower Levels, and (if the action is egregious or repeated) death. See the general principle in DM Notes below.
- **The port is a quiet timer.** A modest, functional port at campaign start; expected to grow visibly as the campaign progresses and Setland's commerce/military posture shifts. Use it as ambient background early and as a deliberate change-of-state marker later.
- **The Aestrum rumor texture is the early hint at the loop.** Players who pay attention to what city NPCs say about Aestrum will pick up something is *strange* there before they ever cross the border. Don't overplay this — the strangeness should feel like folk-tale exaggeration, not like a posted warning. The fact that *nobody has actually spoken to an Aestrum resident* is the key tell, and it should be discoverable only by a player who asks the right follow-up.
