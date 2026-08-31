---
id: rule_death_and_dying
name: Death and Dying
type: core_mechanic
related_rules: [rule_time_loop, rule_snapshot, rule_revert, rule_dead_zones, rule_rest_and_recovery]
---

## Overview

Standard 5e death-save and stabilization rules apply. The loop modifies what happens *after* a creature dies: a subject with a [snapshot]({{PLUGIN_ROOT}}/rules/snapshot.md) who dies outside a [dead zone]({{PLUGIN_ROOT}}/rules/dead_zones.md) is restored by the loop's **Recreate** step at 1:30 AM and wakes at their reset point at 6 AM. A subject who dies inside a dead zone, or who has no snapshot, stays dead until the body's situation changes.

---

## Death Saves and Stabilization (RAW)

- A PC at 0 HP makes a death save each turn: 10+ succeeds, under 10 fails. Three failures = death. Three successes = stabilized at 0 HP. A nat 1 counts as two failures; a nat 20 restores 1 HP.
- Damage taken at 0 HP causes one failure (two on a crit).
- **Massive damage instant death** (RAW): a single hit that deals damage equal to or exceeding the PC's HP maximum *while they are at 0* kills them outright.
- **Massive damage from a hit that takes them to 0** (RAW): if a single hit's remaining damage after reducing the PC to 0 is equal to or exceeds their HP maximum, they die instantly without death saves.
- Stabilization via Medicine (DC 10), Spare the Dying, or any HP recovery.
- The player rolls their own death saves visibly in text. No secret death saves by default.

---

## PC Death Outside a Dead Zone

- **A PC with a snapshot who dies outside a dead zone is restored by the Recreate step at 1:30 AM.** The body is fully restored ("creatures are fully restored, even if parts were missing" per [time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md)), teleported to the reset point at 3 AM, and wakes at 6 AM with snapshot state per [rest_and_recovery.md]({{PLUGIN_ROOT}}/rules/rest_and_recovery.md).
- **The party continues without that PC for the remainder of the in-fiction day.** They are dead from death until 6 AM the following morning. A PC who falls at 9 PM is out for the rest of the evening; a PC who falls at 2 AM is out from death until 6 AM. Mid-combat death is mechanically recoverable but tactically costly.
- **Newcomers without a snapshot stay dead permanently** (existing rule from [time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md)). Practically, every player PC has a snapshot by the time of play, so this is a concern only for new arrivals in their first day.

---

## PC Death Inside a Dead Zone

- **Recreate cannot reach a body inside a dead zone.** A PC who dies inside a dead zone (the Deckard estate, the Misty Forest shrine, the Nahamkate dead-zone pocket, or any other) is not restored at the next reset. The body stays where it fell.
- **The body can be extracted.** Once the body is carried out of the dead zone and is on loop-susceptible ground at midnight, the next Recreate step at 1:30 AM restores them normally. The PC then wakes at 6 AM at their reset point with snapshot state.
- **Practical implication:** the Deckard estate — the party's home base — is the most dangerous place in Aestrum to fall. Any combat death there requires the surviving party to drag the body across the boundary before midnight to trigger recovery. Failing that, the body must be carried out before resurrection magic can be cast on it (see below).
- A body left in the dead zone indefinitely simply remains dead. There is no time limit on extraction — the loop's Recreate does not care about decay state, only that the body is in range when the step fires.

---

## Moon Amulet and the Memory of Death

A Moon Amulet wearer who dies and is restored by Recreate **remembers dying.** The amulet blocks Modify Memory; the death-memory is not exempt.

- The PC retains every moment up to the killing blow. They wake at 6 AM at the reset point knowing exactly how they died, who killed them, and what the last things they saw and felt were.
- Between the moment of death and the moment of waking, there is no experience to record — not because memory is suppressed but because there was no consciousness during that interval. The amulet preserves what the wearer experienced, and they did not experience the Recreate.
- This is a significant psychological weight on a party that wears amulets. Repeated deaths to the same threat (Rowan, for example, if a PC interposes against him) accumulate as remembered trauma.

---

## Resurrection Magic

Standard 5e resurrection magic (Revivify, Raise Dead, Resurrection, True Resurrection, Reincarnate) **works only outside dead zones.**

- Inside a dead zone, all resurrection magic fails, the same way other spellcasting fails inside antimagic. The body must be extracted from the dead zone before any resurrection spell can be cast on it.
- Outside a dead zone, resurrection magic functions per RAW — spell slots, material components (the diamond for Revivify, the diamond for Raise Dead, etc.), and timing windows all apply as written.
- **The loop will refund the components.** Inventory reverts to snapshot at the next reset, so consumed diamonds and other material components return. In practice this makes resurrection magic effectively free if cast late enough in the day that the caster will not need that inventory again before midnight. A diamond used at 10 PM is back in the component pouch at 6 AM.
- Resurrection magic is mainly relevant for: (a) saving a PC who fell inside a dead zone and was successfully extracted, where the party wants them back same-day rather than waiting for the reset; (b) avoiding a several-hour partial-day downtime with the party shorthanded; (c) NPC resurrection, where the loop will not necessarily restore the NPC in a useful state.

---

## Animals, Familiars, and Summons

[time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md) establishes that **animals are excluded from the Recreate phase entirely.** This rule extends to anything occupying the "animal" slot in play:

- **Beast Master companions, Find Steed mounts, Find Familiar familiars** — if killed, they stay dead. The Ranger/Paladin/Wizard must use the appropriate ritual/spell to re-bond a new one.
- **Conjure Animals / Summon Beast / Conjure Woodland Beings and similar summons** — these are bounded by their own spell duration and disappear when the spell ends; the Recreate question does not apply.
- **Pack animals, horses, livestock** — if killed during the day, dead. This is part of why hired animal transport is rare inside Aestrum: nobody risks the asset.

NPCs and PCs are not animals for the purpose of this rule, even if polymorphed. A polymorphed PC who dies in animal form drops out of the form at 0 HP per RAW Polymorph, then proceeds as a normal PC death.

---

## NPC Death

Loop NPCs follow the same rules as PCs:

- An NPC with a snapshot who dies outside a dead zone is restored by Recreate. They wake at 6 AM with no memory of having died (Modify Memory wipes it; they have no amulet).
- An NPC who dies inside a dead zone stays dead until the body is extracted or resurrection magic is cast outside the dead zone.
- Non-loop NPCs (anyone outside Aestrum, anyone without a snapshot) follow plain RAW — dead is dead unless magically resurrected.

The Miri / Rowan cycle is the canonical example: Miri dies to Rowan's blade each night and is restored by the loop's Recreate. Whether she remembers depends on her amulet status (see her character file).

---

## Permadeath Conditions — Quick Reference

A PC stays dead, with no automatic recovery, if **any** of the following hold:

1. They have no snapshot (newcomer killed before their first midnight).
2. Their body is inside a dead zone at the next Recreate step *and* the party never extracts it.
3. They were resurrected by magic that subsequently failed (i.e., the spell never completed successfully, e.g. interrupted casting).

In all other cases, the loop will restore them at the next reset.

---

## Quick Reference Table

| Situation | Outcome |
|---|---|
| PC with snapshot dies outside dead zone | Recreated at 1:30 AM, wakes 6 AM at reset point with snapshot state |
| PC with snapshot dies inside dead zone, body NOT extracted | Stays dead |
| PC with snapshot dies inside dead zone, body extracted before next midnight | Recreated at next 1:30 AM, wakes at reset point |
| PC with snapshot dies inside dead zone, party casts Revivify after extraction | Resurrected per RAW |
| Newcomer without snapshot dies anywhere | Stays dead permanently |
| Moon Amulet wearer dies and is recreated | Wakes remembering their death |
| Familiar / mount / Beast Master companion dies | Stays dead (animals excluded from Recreate) |
| Resurrection magic cast inside a dead zone | Fails |
| Resurrection magic cast outside a dead zone | Works RAW; components refund at next reset |
