---
id: faction_mieke_band
name: Mieke's Band
type: mercenary_company
base: loc_mieke_mercenary_camp
members: [npc_mieke, npc_hollis_tarn, npc_danic_ordwell, npc_reyn_cobbet]
cycle_aware: false
---

## Overview

A mercenary band out of Setland under [Mieke]({{PLUGIN_ROOT}}/npcs/chapter_1/mieke.md), captain,
sent into Aestrum on contract to claim the Galadiil bounty. They camp on the hunting
trail in the Misty Forest, roughly a quarter-mile west of the Shar shrine, and they are
holding [Jiasha]({{PLUGIN_ROOT}}/npcs/chapter_1/jiasha.md) captive there.

**They have no formal name**, and that is not an oversight — it is what they are. The
Shrikes and the Black Arrows are *identities*; this is a working crew that takes
contracts under its captain's name. To anyone in Setland they are Mieke's lot, and when
the contract ends they will be something else.

## Membership

*`known_to` = the members who know this person belongs. Directed; member-to-member only.*

| Member | Role | `known_to` |
|---|---|---|
| [Mieke]({{PLUGIN_ROOT}}/npcs/chapter_1/mieke.md) | captain | **all** |
| [Hollis Tarn]({{PLUGIN_ROOT}}/npcs/chapter_1/remaining_npcs.md#hollis-tarn) | lieutenant — Mieke's second | **all** |
| [Danic Ordwell]({{PLUGIN_ROOT}}/npcs/chapter_1/remaining_npcs.md#danic-ordwell) | operative — scout, perimeter watch | **all** |
| [Reyn Cobbet]({{PLUGIN_ROOT}}/npcs/chapter_1/remaining_npcs.md#reyn-cobbet) | operative — scout, captive detail | **all** |

A contract crew in a shared camp: nothing is hidden among them, and the `known_to`
column is **all** down the line because there is nothing to hide.

**Four is the whole band** — Mieke, his lieutenant, and two operatives. Not a baseline
to scale off: this is the crew that crossed the boundary, it is the crew the snapshot
caught, and it is the crew that reconstitutes at the camp every morning. Mieke picked
small on purpose. A four-person crew moves quietly, crosses a border without a column's
worth of attention, and splits a bounty four ways. Anyone at the camp who is not one of
these four and not [Jiasha]({{PLUGIN_ROOT}}/npcs/chapter_1/jiasha.md) is not in the band and needs
a reason to be standing there.

## Contracted, Not Affiliated

**This band is contracted by [the Black Arrows]({{PLUGIN_ROOT}}/factions/chapter_1/black_arrow.md); it is not part of
them.** The Arrows' briefing was a briefing — target, location, proof, payment — and
the band took the work because the money was good.

**Mieke himself came up through the Arrows** in his twenties and made captain over
fifteen years of contract work: escort, assassination, recovery. That is his history and
his professional network, not his current membership. He belongs to the crew he runs.

The distinction matters at the table because the party can pull on either thread and
get somewhere different: **the contract** leads to Quellenna, the Charnelhold writ and
the eye-and-hand-with-ring proof; **Mieke's past** leads into the Arrows themselves.

## The Band in a Fight

The camp is a workable fight and the party is meant to be able to take it — see
[mieke_mercenary_camp.md]({{PLUGIN_ROOT}}/locations/chapter_1/mieke_mercenary_camp.md) for the
ground and [combat.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/combat.md) for presentation. Mieke's
own block is on [his sheet]({{PLUGIN_ROOT}}/npcs/chapter_1/mieke.md#combat-profile); the other
three are below.

**Encounter weight.** Four bodies — Mieke (~CR 4), Hollis (CR 3), two operatives (CR 1/2
each) — is 2,000 XP raw, ×2 for a four-creature group = **4,000 adjusted**. Against a
party of four at level 6 that is a **hard** fight (hard 3,600 / deadly 5,600); against
five at level 6 it sits between medium and hard. It is not a pushover and it is not a
boss fight.

### Hollis Tarn — lieutenant

*Veteran (MM, CR 3), re-kitted to the band's documented gear — **chain mail** rather
than the stat block's splint, and a **shortbow** rather than the heavy crossbow. AC drops
to 16 accordingly; everything else is the block as written.*

**AC:** 16 (chain mail) | **HP:** 58 (9d8+18) | **Speed:** 30 ft | **Initiative:** +1 | **Proficiency Bonus:** +2

**Stats:** STR 16 (+3) | DEX 13 (+1) | CON 14 (+2) | INT 10 (+0) | WIS 11 (+0) | CHA 10 (+0)
**Skills:** Athletics +5, Perception +2 | **Passive Perception:** 12
**Languages:** Common, Thieves' Cant

**Actions:**
- **Multiattack:** two longsword attacks; she may replace one with a shortsword attack
- **Longsword:** +5 to hit, 1d8+3 slashing (1d10+3 two-handed)
- **Shortsword:** +5 to hit, 1d6+3 piercing
- **Shortbow:** +3 to hit, 1d6+1 piercing, range 80/320

**Combat behavior:** Hollis fights to keep the band intact, not to win. She holds the
line beside Mieke while he has it, and the moment he goes down she is the one who calls
the disengage — see her stub for why. She will not chase, she will not split off to
finish a fleeing PC, and she will take a trade that gets her two operatives out of the
clearing alive. A party that focuses Mieke is fighting a shorter battle than a party
that works inward from the edges.

### Danic Ordwell and Reyn Cobbet — operatives

*Scout (MM, CR 1/2), as written — the band's kit already matches the block: longbow,
shortsword, leather armor. Add a Black Arrows pin to each.*

**AC:** 13 (leather armor) | **HP:** 16 (3d8+3) | **Speed:** 30 ft | **Initiative:** +2 | **Proficiency Bonus:** +2

**Stats:** STR 11 (+0) | DEX 14 (+2) | CON 12 (+1) | INT 11 (+0) | WIS 13 (+1) | CHA 11 (+0)
**Skills:** Nature +4, Perception +5, Stealth +6, Survival +5 | **Passive Perception:** 15
**Languages:** Common, Thieves' Cant

**Keen Hearing and Sight:** advantage on Perception checks relying on hearing or sight.
This is what makes the camp's watch rotation real — a passive 15 with advantage is a
genuine obstacle to a sloppy approach, and it is the number to roll Stealth against.

**Actions:**
- **Multiattack:** two melee attacks or two ranged attacks
- **Shortsword:** +4 to hit, 1d6+2 piercing
- **Longbow:** +4 to hit, 1d8+2 piercing, range 150/600

**Combat behavior:** skirmishers. They open at range from opposite sides of the fire
ring, fall back rather than trade blows with anything armored, and use the twenty-foot
mist limit to break line of sight and reposition. Danic is the better shot and the one
already on the perimeter when a fight starts, so he is usually the first to act and
often shooting from outside the clearing. Reyn is at the picket line with Jiasha; his
first instinct is to put himself between her and the party, which reads as guarding the
captive and is at least half that.

### Tuning

The roster is fixed, so **the difficulty dial is not headcount** — adding nameless
operatives contradicts both the membership above and the reset that restores exactly
these four every morning. Turn the fight up or down on:

- **Approach.** A party that walks up the trail fights all four at once with a scout
  already behind them. A party that stages from the shrine and takes the perimeter watch
  quietly starts the fight two-on-four. This is the largest single swing available.
- **Mieke's Action Surge and Commander's Strike timing.** Held until the third round
  against a party that is winning, spent early against a party that is not.
- **Hollis's disengage.** She ends a losing fight rather than grinding it out. Let her.
- **If a genuinely harder fight is wanted,** raise Hollis a tier or give Mieke a full
  superiority-dice refresh mid-fight — do not add bodies.

## DM Notes

**The band is loop-bound.** They crossed into Aestrum and were snapshotted; the camp
resets each midnight, and Mieke wakes each morning at the same camp with Jiasha already
taken and no idea why the mission never advances. He does not know the loop exists —
**nobody in Setland told him, because nobody in Setland knows.**

**They are living on borrowed ground.** The camp sits inside Rowan Deckard's range, and
he has tolerated them so far. If a party displaces him from the Deckard Estate, the
band is the nearest thing to trespassers he has — see the "Rowan displaced → camp
slaughtered" branch in
[the_abduction_of_jiasha.md]({{PLUGIN_ROOT}}/quests/chapter_1/the_abduction_of_jiasha.md).
