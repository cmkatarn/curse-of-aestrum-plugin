---
id: loc_lions_den
name: The Lion's Den
parent: loc_charnelhold
region: setland
curse_affected: false
connected_locations: [loc_charnelhold]
npcs_present: [npc_malak_du_leon, npc_quellenna_ilphekiir]
---

## Campaign Opening — The Pitch

**This is step 3 of the opening sequence.** The PC(s) and any user-authored party NPCs arrive at eleventh bell alongside a handful of other locals who answered the criers' call. They are admitted into the Lion's Den, take positions in the audience space below the dais, and witness Quellenna deliver the back-taxes framing on Malak's behalf.

The author-declared party members may or may not have crossed paths before entering the chamber — that is per-campaign state. If they have not, the pitch is the moment they discover one another as the people who, independently, made the same choice to stay. See [setland_city.md § Who Actually Takes the Expedition]({{PLUGIN_ROOT}}/locations/chapter_1/setland_city.md) for the canonical convention: by the close of the pitch, every non-author-declared applicant has withdrawn, leaving exactly the PC(s) and author-declared NPCs in the room. Quellenna's formal acceptance at the pitch's close is the in-fiction **join-point** for any author-declared NPCs whose `traveling_with_party` state was `false` going in.

### Timed-event schema

Per [time_and_events.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/time_and_events.md):

- **`time:`** 11:00 (eleventh bell) — exact. The chamber doors close to new entrants when Malak opens the audience; the doors do not re-open for petitioners until the audience concludes.
- **`duration:`** ~5 minutes (Malak's brief opening + Quellenna's pitch + Malak's interjections + the formal acceptance). Closer to ten minutes if the petitioners ask substantive follow-up questions.
- **`catchup:`** `full` — a late arrival walks into the speech in progress. Quellenna is mid-sentence on the back-taxes framing; she does not restart, and Malak does not interject to reset her. The latecomer picks up the speech from wherever it actually is when they slip in. After the pitch ends, the missed framing is recoverable in fiction: a fellow applicant can give a one-line summary, the magistrate's clerk on the way out can confirm the terms, and Quellenna herself — if approached politely — gives a brush-off pointer (*"the brief is on the magistrate's desk"*), not a re-pitch. The latecomer is **visibly the latecomer** in Quellenna's read of them, and that fact is carried forward as state.

**Late arrival beyond ~5 minutes — the door closes.** A PC who arrives more than five minutes after eleventh bell finds the audience concluded and the chamber emptying. The pitch itself is no longer recoverable as a witnessed event; what they can learn is restricted to the aftermath channel (the magistrate's clerk, any departing applicant, Quellenna's brush-off). The expedition contract is still available — the duchy was paying for the work, not for the lecture — but the PC has missed the framing and surfaces as a problem applicant from the first minute.

**If any PC arrives before eleventh bell, see the next section — the Bounty Overhear branch is available to early arrivals.**

**The pitch (framing):** Setland is dispatching a small contracted party to Aestrum on a **diplomatic financial recovery action** — the collection of ten years of unpaid Aestrum back-taxes owed to Nortmunde. The framing is civilian, the duchy is paying handsomely, and the work is described as *"a matter of papers and conversations, not blades."* No mention is made of the strange rumors. No mention is made of what Setland actually wants in Aestrum. The pitch is delivered as if this were ordinary ducal business — because, as far as the public-facing operation is concerned, that is exactly what it is.

**Other applicants bow out** (see [setland_city.md]({{PLUGIN_ROOT}}/locations/chapter_1/setland_city.md), "Who Actually Takes the Expedition"). The PCs are what remains in the room. Quellenna does not press anyone who declines. She lets them go.

**The party leaves the Lion's Den with:** the assignment, a small advance in Setland coin, sealed letters of introduction stamped with the lion seal, and Quellenna's name as the person they report to upon return. They are advised to depart by the **east road** before nightfall.

---

## Early Arrival — The Bounty Overhear

**A PC who arrives at the Lion's Den before eleventh bell finds Malak's court already in session — open audience day, ordinary business.** A magistrate's docket is being read; a tax-adjustment petition is being heard; servants pass between the dais and the side doors. The chamber is moderately attended. **There is a lull in activity** — a routine matter has just been resolved and the next petitioner is being summoned from the holding room. Quellenna has stepped down from the dais to the audience floor to receive a brief from a royal confidant during the pause.

**The setup is built on the chamber's acoustics** (see "The Acoustics" below). Quellenna and her confidant are speaking in the muffled zone along the east wall. From the dais and the front-of-runner zone, their conversation reads as rhythm without content — anyone in those positions hears courtly murmuring and nothing more. **A PC positioned in the audience floor near the east wall (the same acoustic zone) hears the conversation clearly.**

The PC needs an in-fiction reason to be near the east wall. Multiple paths are available:

- **A PC in noble disguise or socially adept register.** They have been admitted as an observer (or have talked their way in). They drift toward the wall because that is where the better-dressed observers stand on audience days — Quellenna's confidant came down from the dais to one of them, and the disguised PC has positioned themselves nearby as a matter of social plausibility.
- **A PC with a plausible servant or messenger role.** They are carrying something, delivering something, returning something. Servants move along the walls, not the runner. A PC who has bluffed their way into a courier task ends up exactly where the acoustic zone wants them.
- **A PC simply curious about the room.** Audience members are allowed to drift toward the side walls between petitioners. A PC who wanders that way during the lull will, with no special check required, end up within earshot of the wall conversation.

**Guide the PC to the conversation.** The Lion's Den runs on these positional choices; if a PC has come in early and is engaging with the room, surface the wall conversation as a thing they can pick up on. Do not gate it behind a Perception roll the player did not ask for — the architecture *is* the perception. The acoustic zone exists; if the PC is standing in it, they hear what is being said.

### What Quellenna Says

The conversation is brief — perhaps a minute of real time — and Quellenna's affect carries **uncharacteristic excitement**, notable to anyone who has seen her at court before. The substance:

- She has commissioned a **bounty through the Black Arrows** — *"special assistance"* — targeting a specific person in Aestrum.
- The target is named in passing: **Galadiil**. *(She does not say "my sister." She says "Galadiil." A PC who knows the duchess of Aestrum's name connects the dots; a PC who does not is left with a target name to investigate.)*
- The **proof of death required**: the **right eye** and the **right hand**. The right hand must include **her heirloom ring** as identification.
- Quellenna **cannot bear to look upon Galadiil's face**, not even in death. That is why eye-and-hand rather than head.
- The confidant nods, asks no questions, takes the brief, and returns to the dais. Quellenna composes herself before following — the moment of excitement passes and the controlled advisor returns.

### What the PC Does With It

The PC may:

- **Act on it.** Quietly collect what they can — observe the confidant, ask discreet questions of other audience members afterward, pursue the Black Arrows thread back to the city contact-house (see [setland_city.md]({{PLUGIN_ROOT}}/locations/chapter_1/setland_city.md)). The bounty is real, executable, and substantial. A PC who wants the work can pursue it.
- **Warn Galadiil.** Less obvious — Galadiil is in Aestrum, the party is being sent to Aestrum, and the warning could be carried in person. A PC who chooses this route has set up a significant future encounter (Galadiil receives a stranger bearing news of her sister's intent).
- **Sit on it.** The information becomes a piece of context the PC carries forward. It will inform how they read events in Aestrum and how they react when other party members surface related threads.

**The information does not need to be shared with the party.** A PC who learns of the bounty may keep it to themselves. This is a player choice; do not force a reveal. The campaign accommodates either path.

---

## Alternative Channels — How Else the Bounty Surfaces

The Lion's Den overhear is the cleanest entry, but not the only one. Disreputable PCs and PCs with the right connections may learn of the bounty (or its existence in vaguer form) through other routes:

- **Black Arrows ties.** A PC with recognized standing in the Black Arrows network (a visible tattoo, prior contract work, a known referrer) may be approached by a fellow operative who mentions the open commission. The exact bounty conditions are not necessarily shared — the Black Arrows compartmentalize — but the existence of a high-value target in Aestrum is the kind of news that travels within the network.
- **The wine-importer's contact-house.** The Setland City contact-house that routes Black Arrows commissions from Charnelhold (see [setland_city.md]({{PLUGIN_ROOT}}/locations/chapter_1/setland_city.md) seed secrets) is a plausible second-hand source. A PC who establishes themselves as working professional and asks the right questions in the right shop may be sold a piece of the bounty's existence — *"there's a Charnelhold writ moving through the network, target is in Aestrum, eye and hand are the terms"* — without learning who Quellenna is or that Galadiil is the target.
- **The Crimson Hart or Two Banners.** A would-be expedition applicant nursing a drink may, in the right kind of conversation, mention having heard *"there's other work in Aestrum than just the taxes."* They don't know details; they heard it from someone who heard it from someone.

The DM should match the channel to the PC's profile. A PC who is openly noble and socially placed gets the Lion's Den overhear; a PC who is working the underside gets the Black Arrows side channel; a PC who is doing neither but is curious gets the inn-talk rumor.

---

## Pre-Jiasha Goal — At Least One PC Should Know

**Ideally, at least one party member has heard of the bounty before the party reaches Jiasha.** This is not a hard requirement — the campaign survives without it — but it sets the stage cleanly for the Aestrum thread. A party that already carries the bounty's existence into Aestrum has a piece of information that compounds with every subsequent revelation (Galadiil's situation, Quellenna's reach, the Shar architecture).

**If no PC has surfaced the bounty by the time the party reaches the forested foothills, fire the fallback encounter below.**

## Overview

The Lion's Den is Malak's court chamber and the room from which he is seen ruling. It sits off the main hall on the ground floor of Charnelhold, accessible to petitioners and the general castle population on audience days. It is the room where the duchy's public face is performed.

The chamber is **dark.** The only light is what filters through the stained glass and what the braziers throw — and the stained glass is **orange and red**, so what light reaches the floor is warm, the color of a banked fire. The walls are dark stone. The ceiling vanishes into shadow above the brazier-glow. The room feels like the inside of a furnace at low burn.

**A large orange stained-glass window dominates the wall directly behind the dais**, set high. When Malak is on the throne and the afternoon light comes through it, he is silhouetted against an orange glow — which is exactly the effect he wants. The window is the chamber's single piece of theatrical staging and it does most of the work the lighting design needs to do.

**Two more stained-glass windows** flank the dais on either side wall, smaller, also in oranges and reds. **Braziers** at the foot of the dais and along the side aisles throw flickering light up the walls; the flame is reflected and broken in the stained glass, so the impression on entering is of a room lit by stained fire from every direction at once.

The chamber is **outside Aestrum's loop entirely.** Time and magic behave normally.

## Layout

- **The dais.** A wide stepped platform at the far (north) end of the chamber. Three or four broad steps up. Wide enough to accommodate the throne, Quellenna's standing position, two guards, and any incidental staff a given audience requires. The dais is the room's center of gravity in every sense.
- **The secondary throne.** A high-backed chair, heavy and carved, set at the center of the dais against the back wall directly beneath the large orange window. It is not the duchy's ceremonial throne — that one lives in the Throne Room next door and is brought out only on formal occasions. The secondary throne is what Malak uses for daily court. He prefers it. The Throne Room makes him feel small.
- **Verus's position.** The hound sits or lies beside the throne at Malak's right hand. He is part of the room's standing composition; petitioners learn quickly not to startle him.
- **Quellenna's position.** She stands on the dais slightly off to one side and a step or two back from the throne, **interposed between Malak and any petitioner**. She remains standing for the entire duration of court. She does not sit. She does not rest. The choice is deliberate and reads as deference; it is in fact positioning — every petitioner's question passes through her field of attention before it reaches Malak.
- **The two guards.** Lion's Hand, in dull crimson and brass, halberd-armed. One at each end of the dais, at attention. They do not move during proceedings unless required.
- **The red runner.** A long crimson rug runs from the foot of the dais steps down the central aisle to the main door. Petitioners walk this runner to approach. The aisle is wide enough for a small group; the runner narrows the visual approach into a deliberate, ceremonial walk.
- **The main door.** South wall, large double doors of dark wood with brass lion-headed pulls. The room's only public entrance.
- **Side doors.** Two smaller doors flanking the dais on the east and west walls. The **east side door** connects to the Throne Room (closed during ordinary court); the **west side door** connects to a short corridor running to Malak's apartments and Quellenna's wing — used by the household, not by petitioners. **The party should not see anyone come through the west side door during their audience unless something exceptional is happening.**
- **The audience space.** The central floor below the dais, on either side of the runner, where petitioners and observers stand or sit on a few benches along the walls. This space is where the party will be positioned during the pitch.

*See referenced photo (Lego construction) for visual composition: dais centered against a large orange window, throne flanked by Quellenna (left of throne, in red) and Verus (right of throne), two guards at the dais corners, braziers at the base, audience figures in the foreground space below.*

## The Audience Convention

Malak's court is **open to observers, deliberately and by design.** He wants to be seen ruling. The audience space is rarely empty — there is almost always a scatter of minor courtiers, household members, off-duty officers, and city notables present in some capacity. Most of them have been **summoned or had their presence required**, not to be called upon or recognized, but simply to be present. The visible audience is part of the staging. Malak likes a room with people in it.

This has two consequences worth holding:

- **A petitioner is never alone with the Duke.** Even the most private-seeming matters are conducted in front of an audience of strangers. If something is to be said that should not be overheard, it must be said in a way the room cannot follow — which is where the acoustics of the chamber come into play (below).
- **Reading the audience is a useful skill.** Who is summoned today, who is not, who has been positioned where on the floor — these are all signals. A perceptive PC can learn things from the audience composition that no one in the room will say aloud.

## The Acoustics

The chamber has an unusual acoustic property, built into its proportions and the angle of the dais. **Sound carries cleanly between two points: the dais itself, and the audience space directly in front of it (within roughly the first ten feet of the runner).** Voices spoken in either of those positions are audible to the other clearly, even at conversational volume.

**Sound originating anywhere else in the room — the side walls, the back, the corners — arrives at the dais (and at the front of the audience space) as a kind of muffled hush.** The cadence carries; the content does not. A listener on the dais hears the *rhythm* of a conversation across the room but cannot make out the words.

The effect is well-known to the castle's regulars. **Schemers find the Lion's Den an ideal place to speak privately.** Two courtiers standing along the back wall can discuss a matter no one on the dais can overhear, while every word the Duke speaks reaches them as if he were three feet away. The chamber's open audience and its private acoustics are a structural pairing: people come to be seen, and then they say things to each other that cannot be heard.

**Quellenna knows this. So does Malak, in the limited way he knows anything about how the room works. He believes the acoustics flatter him. They do flatter him — but they also do considerably more.**

## How Court Actually Runs

This is canon-supporting texture; see [malak_du_leon.md]({{PLUGIN_ROOT}}/npcs/chapter_1/malak_du_leon.md) and [quellenna_ilphekiir.md]({{PLUGIN_ROOT}}/npcs/chapter_1/quellenna_ilphekiir.md) for the underlying behavior.

- **Banal matters.** Quellenna defers to Malak immediately and openly. A tax adjustment, a guild dispute, a magistrate's docket question — Malak answers. The answer is fine because the question was small. The court sees His Grace ruling on routine business and the advisor staying out of his way.
- **Matters of weight.** Quellenna does not propose answers. She **guides Malak to them** — a small reframing question, a reference to *"what His Grace did last spring on the matter from Beluir,"* a half-finished observation she lets Malak complete. The court hears Malak ruling and Quellenna listening attentively. Malak hears himself thinking clearly.
- **The interjection pattern.** When Quellenna delivers procedural framing or clarification, Malak frequently adds a brief sentence after — an elaboration, a flourish, a small additional ruling. The interjections are sometimes superfluous and sometimes slightly wrong. Quellenna smooths them in real time without ever appearing to correct.
- **The mask is total.** Petitioners with decades of court experience may suspect, but cannot point to a single moment where Quellenna overstepped. The party will not catch this in a single audience.

## Faction Reach

- **House du Leon:** total. This is Malak's room. The chamber is the public face of his rule.
- **The Lion's Hand:** two guards on the dais at all times during court; more in the corridors.
- **Quellenna (publicly):** royal advisor, deferring to His Grace. Invisible authority.
- **The audience as faction-adjacent presence:** at any given session there are likely to be representatives of several minor Setland houses, the city's wealthier merchants, and one or two off-duty officers from Aidra's command. None will speak unless addressed.

## Seed Secrets

- A specific minor courtier attends every audience and never says a word — but listens carefully from a position along the east wall (in the muffled zone) and writes letters afterward to a correspondent in another duchy. The correspondent pays well. The courtier has done this for years and has never been caught.
- The orange window behind the throne contains a small piece of repair-work — three panes near the upper-left corner replaced about a decade ago after a storm. The replacement glass is a slightly different orange than the rest. No one mentions it. Malak has never noticed.
- One of the two dais guards has, over the course of his career, picked up enough of Quellenna's pattern to suspect what is happening — has held the suspicion in absolute silence for several years — and will, if ever asked the right question by the right person, tell what he has seen. He will not volunteer it. He will not lie if asked directly.

## Callback Slots

- "A silent courtier who attends every audience and reports to a foreign correspondent" → unnamed; useful as a slow-burn intelligence thread.
- "A dais guard who has noticed what Quellenna does and held his silence" → unnamed; potential ally for a party investigating the duchy's structure.

## Named Characters

**Duke Malak du Leon** — on the throne. See [malak_du_leon.md]({{PLUGIN_ROOT}}/npcs/chapter_1/malak_du_leon.md).

**Lady Quellenna Ilphekiir** — standing on the dais. See [quellenna_ilphekiir.md]({{PLUGIN_ROOT}}/npcs/chapter_1/quellenna_ilphekiir.md).

**Verus** — at Malak's right hand. See [malak_du_leon.md]({{PLUGIN_ROOT}}/npcs/chapter_1/malak_du_leon.md) for stat block.

## The East-Road Mercenary Encounter — moved

The fallback mercenary encounter (fired if no PC has learned of the Galadiil bounty by
the forested foothills) now lives in its proper home, the corridor where it happens:
[setland_east_road.md]({{PLUGIN_ROOT}}/locations/chapter_1/setland_east_road.md), *The Mercenary Encounter*. It was
previously housed here only because no east-road file existed.

**What still belongs here:** whether a PC leaves the Lion's Den already carrying the
bounty thread — through the briefing, Quellenna's name, or an alternative channel — is
what decides whether that encounter fires at all. If the bounty is carried out of this
room, the road to Jiasha is uneventful.
---

## DM Notes

- **The pitch is the scene's payload.** The party hears the back-taxes framing in Quellenna's voice, with Malak occasionally interjecting per the interjection pattern. The pitch is civilian, the work sounds straightforward, and the duchy is paying well. The party should leave with the assignment and with no reason to suspect what they're actually being sent into. The strangeness of Aestrum has been kept out of the official framing.
- **Do not over-perform Quellenna's invisibility.** The party should perceive a competent advisor doing her job and a Duke holding court. Anything more visible than that is wrong at this stage. The party may pick up the deference-then-guidance pattern across many sessions of the campaign — they will not pick it up here.
- **The acoustics are a tool to deploy when it would be interesting.** If a PC moves to the side or back of the room and tries to talk quietly with another PC, let them — *the room's acoustics work for them too.* This is also a way to permit player-side scheming during court without breaking the audience's plausibility. Conversely, if the party wants to overhear something specific in the room, the answer depends on where they are standing — the dais and the front of the runner hear everything; the rest of the room hears only rhythm.
- **The west side door is a Quellenna-and-household door.** If a PC tries to slip through it during or after the audience, that is a Tier 1/2 event (the corridor leads toward private wings). See [rules/consequences.md]({{PLUGIN_ROOT}}/rules/consequences.md). At campaign start, no in-fiction reason exists for a petitioner to use it.
- **Aidra's brief Lion's Den intrusion** (see [charnelhold.md]({{PLUGIN_ROOT}}/locations/chapter_1/charnelhold.md)) — if you choose to run it, it happens through the west side door, she takes the short corridor to the dais without crossing the audience floor, speaks low at Malak's ear, and leaves the same way. This is one of the few moments the west door is opened during court.
- **Audience composition is a DM dial.** The room can be thinly attended (a few minor courtiers along the walls), moderately attended (the default — a scatter of perhaps twenty observers), or full (a special audience day). For the campaign opening, **moderate is the right register** — the room feels formal but not overwhelming; the party can be seen.
- **The brazier-and-stained-glass lighting is the chamber's voice.** Lean on it in narration. Faces in the audience are partially shadowed; movement on the dais is highlighted; Malak's silhouette against the orange window is the room's strongest visual. Combat in this room, if it ever occurs, would play out in firelight against red and orange glass — a register the rest of the castle does not have.
- **The pitch should be delivered in Quellenna's voice, not Malak's.** Malak opens the audience and welcomes the candidates — a brief Setland greeting, perhaps a stock phrase about *"matters of importance to the duchy."* He then defers to *"Lady Ilphekiir, who has the particulars."* Quellenna delivers the framing in full. Malak adds an interjection or two at natural pauses (per the pattern) that Quellenna smooths over. He closes the audience by formally accepting the candidates as the expedition party. The whole thing should run inside ten minutes of real time.
- **A reference photograph of the chamber exists** (Lego construction); use it as the authoritative visual reference for composition, color palette, and figure placement. See file location with user if needed.
- **Do not let the same PC learn the bounty twice through redundant channels.** Once a PC has the information through one path (early-arrival overhear, Black Arrows ties, contact-house, inn rumor, or mercenary writ), the other channels in their path go quiet on the subject.
- **Quellenna does not say "my sister."** In the wall conversation she uses Galadiil's name only. The connection to Quellenna's family is something a PC must reach for — by asking around afterward, by recognizing the name from the duchess of Aestrum's title, by surfacing the Ilphekiir surname later. Do not hand the connection over for free. The bounty's existence is the gift; the sister-relationship is a separate discovery.
- **A PC who learns the bounty may keep it private.** This is firm. Player choice. Do not surface it in front of the rest of the party through narration ("you notice [other PC] looking troubled"). If the player chooses to share, the share happens through their character's mouth on their terms.
- **The mercenary fallback exists to set up Jiasha.** Do not skip the injury beat unless the party has already taken meaningful damage from another source on the road. Jiasha's introduction is stronger when she has an immediate role to play. Match the encounter's lethality to what the party will tolerate without resentment — this is not a hard fight; it is a delivery vehicle for the writ and a setup for healing.
