---
id: loc_mieke_mercenary_camp
name: Mieke's Mercenary Camp
parent: loc_misty_forest
region: aestrum
curse_affected: true
connected_locations: [loc_misty_forest, loc_misty_forest_dead_zone, loc_misty_forest_shrine]
npcs_present: [npc_mieke, npc_hollis_tarn, npc_danic_ordwell, npc_reyn_cobbet, npc_jiasha]
chapter: 1
---

## Overview

A mercenary camp on the hunting trail in the Misty Forest, roughly a quarter-mile **west** of the Shar shrine; the Misty Forest dead zone lies beyond the shrine, another ~100 yards **east** of it — so the shrine sits between the camp and the dead zone. The camp is the Black Arrows-contracted band led by [Mieke]({{PLUGIN_ROOT}}/npcs/chapter_1/mieke.md), pursuing the Galadiil bounty placed by Quellenna (see [the_lions_den.md]({{PLUGIN_ROOT}}/locations/chapter_1/the_lions_den.md)). [Jiasha]({{PLUGIN_ROOT}}/npcs/chapter_1/jiasha.md) is held captive here.

The camp resets each midnight via the loop — see [Mieke's NPC file]({{PLUGIN_ROOT}}/npcs/chapter_1/mieke.md) and [misty_forest.md]({{PLUGIN_ROOT}}/locations/chapter_1/misty_forest.md). The band re-experiences the same day of failing-to-process their situation, perpetually, unless permanently removed via the dead-zone mechanic.

## Approach

The hunting trail leaves the 4WI ↔ Rockwood maintained road as a spur heading east into the Misty Forest. The trail is narrower than the road, less maintained, and the canopy closes over it within a few minutes of leaving the main route. About twenty minutes in it reaches the camp — a small clearing the band cleared themselves — packed earth, tree-stumps cut at sitting height, a fire ring in the center. The shrine and, beyond it, the dead zone lie further **east** past the camp.

The Shar shrine is a quarter-mile **east** of the camp, on the far side of a shallow ridge. The Misty Forest dead zone is **further east still** — about 100 yards beyond the shrine — detectable at its boundary by the standard antimagic signature (torches that burn without flicker, the slight pressure-change in the air; see [dead_zones.md]({{PLUGIN_ROOT}}/rules/dead_zones.md)). The shrine sits between the camp and the dead zone.

## Layout

- **The fire ring** — center of the camp. Stones piled into a low rim; a cookpot suspended on an iron tripod when meals are being prepared. The fire is lit most of the day; the band has nothing pressing them to conserve fuel and the forest is wet enough that they need the dry warmth.
- **Mieke's tent** — the largest, on the north side of the fire. Plain canvas, no insignia. A camp table inside with the bounty writ, a small map of Aestrum (woefully out of date — pre-loop, when borders meant something different), a sealed letter of credit on Charnelhold, and Mieke's secondary blade. He sleeps here.
- **The band's tents** — two smaller tents in a loose arc on the south and east sides. Hollis Tarn has one to herself; Danic Ordwell and Reyn Cobbet share the other. Three tents in the clearing all told, counting Mieke's — a party that scouts the camp and counts canvas gets the crew size right.
- **The picket line** — a low rope strung between two trees on the west side of the camp, used to tether captives. Jiasha is restrained here when she is not under direct watch — wrists bound, the rope long enough to reach the fire but not the trail. The band feeds her, gives her water, does not abuse her. She is operational equipment; they treat her accordingly.
- **The weapons cache** — a wooden chest near Mieke's tent containing spare bows, quivers, a few healing potions, the band's contract paperwork (in a sealed oilcloth), and a pouch of Setland coin for incidental expenses inside Setland (now useless, but Mieke does not yet realize this).
- **The latrine** — a slit-trench about thirty feet east of the camp through low brush. Standard military discipline.
- **The horses** — *absent.* The band left their horses at the boundary inn on the Setland side before crossing on foot. The horses do not come up; the band has not yet realized they cannot leave to retrieve them.

## Sightlines and Approach Cover

The camp is in a clearing about forty feet across. Mist persists in the canopy and softens visibility past about twenty feet — a Stealth approach is possible. Through the waking day the band keeps one on patrol and one awake at the fire; from evening to midnight that becomes two awake and two asleep (see Daily Pattern). On a four-person crew that rotation never degrades, because it never has to — the loop reverts them to snapshot every midnight ([rest_and_recovery.md]({{PLUGIN_ROOT}}/rules/rest_and_recovery.md)), so nobody at this camp is ever short of sleep. The same watch, the same argument and the same fatigue run again from 6 AM. Roll Stealth against the watcher: an operative is passive Perception **15** with advantage on any check relying on hearing or sight (Keen Hearing and Sight); Mieke is passive Perception **14** without the advantage.

- **Between midnight and 6 AM — there is no watch at all.** The loop's **Sleep** step
  fires at 12:00:00 AM and drops all four where they stand; **Wake** does not lift until
  6:00:00 AM (see [time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md)). In those six hours the camp
  is not lightly guarded — it is four unconscious bodies in a clearing. The only way to
  be awake for it is to have been **inside a dead zone when Sleep fired**; a Moon Amulet
  does not help, it explicitly does not block Sleep
  ([moon_amulets.md]({{PLUGIN_ROOT}}/items/chapter_1/moon_amulets.md)). The Misty Forest dead zone
  is a quarter-mile east past the shrine, which puts the one shelter that keeps a party
  conscious five minutes' walk from the one camp that is defenceless while they are.
  Note the clock inside the window: **Teleport fires at 3:00 AM** and returns sleeping
  individuals to their reset point, Jiasha included.
- **From the west (the trail / road approach):** the patrol's standard route covers the approach trail back toward the road. A stealthy party can flank by leaving the trail thirty feet out and circling through the brush.
- **From the east (the shrine and dead-zone side):** less watched. The shrine — a quarter-mile east — is a soft cover spot to stage from; beyond it the band has noticed the dead zone but does not understand it, treats that ground as "haunted," and avoids it. A party approaching from the east has a cleaner line, and the patrol crosses the shrine-side only intermittently.
- **From the flanks (north or south, through brush):** off-trail on either side; passable with a stealthy approach but slower going through the undergrowth.
- **From above:** the canopy is dense but Rowan (in wolf form, daytime hours) has been known to perch on a fallen tree at the camp's edge unnoticed. If the party brings a flier or a climbing approach, the camp does not look up.

## Jiasha's Position

Tethered at the picket line by default — wrists bound, the rope long enough to let her sit or move within a small radius. She is fed and watered; the band treats her with the rough impatience of a resource that has not paid out. She is silent in the camp by choice. The band has long since stopped trying to extract information from her — they tried for the first day or two, got nothing useful, and now keep her present without active interrogation.

She is exhausted but unharmed. The exhaustion is from sleeping outside a dead zone every night since her capture — she catches what sleep she can in the tethered position and wakes each morning with the same fatigue she woke with the previous morning, the loop holding her at her snapshot baseline of "captured woman tied to a tree." She has not been allowed to pray openly; the band notices and stops her when she tries.

## What Jiasha Knows (and Does Not)

- **She knows she was taken from her hut, that the hut was burned, that her captors are mercenaries from Setland.** She heard them speak about the contract on the road before she was gagged.
- **She knows the name Galadiil from their conversation.** She does not know who Galadiil is in any specific sense, only that she is the contract target and that the contract is paying.
- **She does not know about the loop yet.** She has been inside Aestrum for less than a week; she has noticed the days are repeating themselves in unsettling ways but she has not connected this to a cycle. Her connection to Selûne is suppressed inside Aestrum (see [key_lore_summary.md]({{PLUGIN_ROOT}}/lore/key_lore_summary.md)) and she is grappling with the silence as much as the captivity.
- **She does not know the party is coming.** She prays for help in vague terms. She does not know it will arrive as the people she handed amulets to several nights ago.

## Daily Pattern

The camp runs the same day every day:

- **6 AM (Wake):** the band rises with the loop. Breakfast around the fire. Patrol rotation begins. Mieke reads the bounty writ and the map; the routine never changes.
- **Morning:** Mieke sends one or two operatives down the hunting trail toward the 4WI to "make inquiries" — scouting for the target, looking for word in town, checking the road for travelers. They return midday with nothing. They never make it as far as Duskwall before something turns them back (loop-friction, the road's unfamiliarity, fuzzball drift, a sense of having forgotten something important; see [fuzzball.md]({{PLUGIN_ROOT}}/rules/fuzzball.md)).
- **Midday:** the band eats a hot meal. Mieke holds a brief council with his lieutenant about progress. The conclusion is always the same: the target has not surfaced, the guide is useless, the contract requires more time. He always agrees with himself.
- **Afternoon:** patrols continue. Mieke attempts to question Jiasha for the third or fourth time of the day (depending on her stamina); she does not answer. He notes her usefulness as declining.
- **Evening:** dinner. The band sits around the fire. The mood is sour but not desperate — they have done long contracts before. They do not realize this one will not end.
- **Night:** rotation rest. Two awake, the rest asleep.
- **Midnight (Sleep):** the loop catches them. They drop unconscious where they are. Recreate restores the camp's physical state. They wake at 6 AM with the same morning ahead of them.

## Faction Reach

- **Black Arrows (contracted):** Mieke's band is the only Black Arrows presence inside Aestrum. They do not coordinate with anyone — the contract is theirs alone and Roland's organization in Setland has no live communication with them across the boundary.
- **Shar (via the shrine):** the shrine is a quarter-mile east and is one of the loop's anchors (see [loop_anchors.md]({{PLUGIN_ROOT}}/rules/loop_anchors.md)). The band is unaware of the shrine's function. They have noticed the building exists and dismissed it as a forest ruin. They do not pray there.
- **Selûne (via Jiasha):** Jiasha is the only Selûne presence inside Aestrum currently, and her connection is suppressed. The band's proximity to the Shar shrine is doing additional damage to her connection on top of the regional suppression.

## Hazards

- **Rowan, in wolf form.** Rowan hunts the dead-zone perimeter during certain hours (see [misty_forest.md]({{PLUGIN_ROOT}}/locations/chapter_1/misty_forest.md)). The camp is inside his hunting territory but he has not attacked it — partly because four armed professionals keeping a standing watch are a bad hunt for a lone predator who has to go on living in this forest (they would notice him, they would hunt back, and they would cost him the quiet his whole routine depends on), and partly because his obsession is Miri, not Jiasha. **Note what the deterrent is not: danger.** Rowan is immune to nonmagical weapons that are not silvered ([combat profile]({{PLUGIN_ROOT}}/npcs/chapter_1/rowan_deckard.md#combat-profile)), and the band carries plain steel and plain arrows — nothing in this camp can put a scratch on him. He leaves them alone because killing them buys him nothing and costs him peace, not because they could stop him. **If Rowan is displaced from his normal cycle** (the party kills him on a prior day, moves his body, otherwise disrupts the murder cycle with Miri), he may turn on the camp. When he does it is not a battle, it is an execution: the camp gets slaughtered, Jiasha included, on the night Rowan's pattern breaks, and he has to do it in the evening window before midnight, because after 12:00 AM he is asleep in his own dead zone and the camp is unconscious anyway. Two awake and two in their tents is not a defence against something they cannot wound. The party racing to rescue Jiasha after disrupting Rowan needs to move quickly. See [misty_forest.md]({{PLUGIN_ROOT}}/locations/chapter_1/misty_forest.md) and [rowan_deckard.md]({{PLUGIN_ROOT}}/npcs/chapter_1/rowan_deckard.md).
- **The Misty Forest dead zone.** Useful — the dead-zone permanent-kill mechanic applies to Mieke and the band the same way it applies to Rowan (see his file). The party that figures it out for one threat figures it out for the other.
- **Spider territory** is east of the forest's center, well away from the camp. Not a hazard at this location.

## Seed Secrets

- **A folded letter in Mieke's tent**, addressed to himself, drafted but unsent. *"If I am gone longer than expected, the band is owed three months' wages forward from the Charnelhold writ payout. The Arrows are to honor this without dispute. If the writ does not pay, the wages are mine to settle personally. Distribute the contents of the chest at the boundary inn as severance."* The letter is dated to the morning the band crossed into Aestrum. Mieke wrote it as a precaution. He never sent it because he never accepted that the contract was not closing — and because he resets to the morning he wrote it, every day. The letter is a quiet portrait of who he is.
- **A small wooden carving** in one of the operative's packs — a child's toy, half-finished. He has been working on it during evening downtime. He will not see the child again until the loop breaks; he does not know this, and he does not let the others see him carving it.
- **A scrap of parchment** in the weapons cache, with three names crossed out and a fourth circled. The crossed names are recent Black Arrows operatives who have died on contracts; the circled name is "Theren." Mieke noted it because the patriarch's son was reported in Aestrum on a different expedition and Mieke wanted to know if their paths might cross. They have not.

## DM Notes

- **The camp's emotional register is "professionals in slow degradation."** Lean into the routine, the impatience, the unspoken fact that none of them are sure why this isn't working. Do not let the band perform menace; their dangerousness comes from being competent and trapped, not from theatrical cruelty.
- **Jiasha's quiet matters.** When the party arrives, she will not cry out for them. She will not perform distress. She is exhausted, suppressed, and watching the situation carefully. She recognizes the party — they have the amulets she made — and her reaction to seeing them is small, internal, and devastating. Hold the moment. Don't narrate her relief; let it land in what she does not say.
- **The camp is a workable infiltration scenario.** A stealthy or socially clever party can resolve the rescue without a full pitched battle. The dead-zone-side approach from the east is available, the Shar shrine (a quarter-mile east) is a staging point, Mieke is open to a conversation that gives him operational information. Reward creative approaches.
- **The camp is also a workable fight.** A party that wants combat gets a competent skirmish — Mieke is a Battle Master, Hollis Tarn is a Veteran, Danic and Reyn are Scouts. Stat blocks, encounter weight (**4,000 adjusted XP** — hard for four PCs at level 6) and the tuning levers are all on [the band's file]({{PLUGIN_ROOT}}/factions/chapter_1/mieke_band.md#the-band-in-a-fight). **The roster is fixed at four — do not scale by adding bodies**; the camp's population is canon and the reset restores exactly these four every morning. Scale on approach instead, which is the largest swing available. Use [combat.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/combat.md) and [turn_order_and_pacing.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/turn_order_and_pacing.md).
- **After the rescue, the camp resets.** Unless the party moves bodies into the dead zone before midnight, the next morning the camp is back to baseline — Mieke and the band and their tents and the writ on the table, identical to yesterday. Jiasha, once removed, does not return to the camp (she is now wherever the party put her), but the camp itself is permanent in the loop. The party that wants the camp gone has to use the dead-zone treatment on Mieke or destroy the loop itself.
- **Tier discipline:** the camp is Tier 1 for the party once Jiasha's abduction is established. Killing the band is sanctioned by the situation. Looting the camp is fine; the Charnelhold writ is the most valuable retrievable item. Burning the camp is fine; it resets anyway.

## Quick Reference

| Element | State |
|---|---|
| Mieke's location | Center of camp, near the fire ring or in his tent |
| Band present | All four, fixed — Mieke, Hollis Tarn, Danic Ordwell, Reyn Cobbet |
| Jiasha's position | Picket line, west side of camp |
| Distance to dead zone | ~quarter-mile-plus east (past the shrine) |
| Distance to Shar shrine | ~quarter-mile east |
| Distance to hunting trail spur from 4WI | ~20 minutes east of the 4WI–Rockwood road |
| Reset behavior | Full reset at midnight unless dead-zone treatment applied |
