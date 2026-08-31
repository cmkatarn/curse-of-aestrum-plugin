---
id: rule_active_effects_tracking
name: Active Effects Tracking
type: homebrew_rule
related_rules: [rule_combat, rule_information_disclosure]
---

## Overview

How ongoing mechanical state — concentration spells, conditions, buffs, ongoing damage, temp HP — is tracked and surfaced in a text medium. In person, a token on the mat reminds everyone. In chat, effects silently rot: the Bless from round one is still up at round six but nobody remembers; the poisoned condition that should have prompted a save at the start of the turn gets skipped; concentration drops without a Con save ever being called.

This rule closes those failure modes by putting the DM in the loop as authoritative tracker, with explicit surfacing cadences for the cases where forgetting hurts the most.

---

## DM Is Authoritative

The DM holds the canonical record of every active effect on every PC and every NPC: source, duration, save DC, ongoing damage, and any rider conditions. Players may volunteer reminders ("I'm still concentrating on Bless") and should, but on conflict the DM's record wins.

The tracker lives in working memory during a session. If combat or a long-lived effect spans across sessions, the DM captures the active-effects state in the session save so it can be reloaded cleanly. Single-encounter effects (Bless, the bandit's Haste, a 1-round poisoned condition) do not need persistence.

For state with longer reach — multi-day buffs, attunement, persistent injury — see [item_persistence.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/item_persistence.md). For settings with reset / loop mechanics that affect effects, see the game's override.

---

## Surfacing Cadence

The DM surfaces active effects at four moments. The cadence is calibrated so forgetting an effect rarely costs the player something they couldn't have avoided.

### 1. Top of Each Turn in Combat

Before handing the turn to the active PC, append a single line of their currently-active effects to the turn callout (see [combat.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/combat.md#layer-c--active-pc-callout-on-that-pcs-turn)):

> *Sera, from the wagon: the sword bandit is 25ft (one move), the axe bandit 30ft, the archer 45ft behind cover, the caster 65ft. Bren is 5ft to your left.*
> ***Active on you:** Bless (4 rds), poisoned (save end of next turn).*

If the active PC has no effects, the line is omitted. Don't print empty rosters.

### 2. Start of Each DM Narrative Response — Debuff Persistence Reminders

When a PC is carrying an effect that **actively hurts them** — ongoing damage, disadvantage, a condition that gates their next roll — the DM surfaces it at the **start of each DM narrative response that involves that PC**, not only on their turn.

- **Ongoing damage** (poisoned with end-of-turn damage, on fire, bleeding): remind every turn that the damage occurs, with the number, before continuing the beat.
- **Disadvantage** (frightened, prone, restrained): surface the disadvantage **before the player attempts anything** that would be affected, not after the roll.
- **Save-required conditions** (charmed, dominated, recurring saves): name the save and its DC at the moment it triggers.

Buffs do not get this loud cadence — forgetting a buff costs the player only what they didn't get to use, which is self-correcting. Debuffs get the loud cadence because forgetting them creates wrong decisions the player would have made differently.

### Player Mute — Granular, Auto-Unmute on Re-Acquisition

Players may **mute debuff reminders** at any time during a session. Muting is:

- **Granular by effect, by PC.** A player can mute a specific condition while keeping others live: *"stop reminding me about blinded"* mutes the blinded reminder but keeps the poisoned and frightened reminders surfacing as normal. The mute applies only to that PC; other PCs' reminders are unaffected.
- **Blanket also allowed.** *"I've got it, mute everything on me"* mutes all current and future debuff reminders on that PC for the session. This is a one-shot — re-acquisition doesn't unmute under a blanket mute.
- **Auto-unmute on re-acquisition (per-effect mutes only).** A per-effect mute applies to the *current instance* of the effect. If the muted condition ends and the same condition is later re-applied, it's a fresh mechanical event the player hasn't been juggling for the last several turns — the mute clears and reminders resume. The player can re-mute cheaply if they're still on top of it.
- **Session-scoped.** All mutes — granular and blanket — clear at session end. This prevents permanent opt-outs from compounding into silently-rotted state across sessions.

The DM tracks active mutes alongside the effects themselves.

### 3. On Trigger

Independent of the above: every save required, every damage dealt or healed, every effect expiring, every condition imposed gets surfaced in the moment. This is just the consequence side of the dice and is not subject to the opt-out above.

### 4. On Request

Players in any mode may ask "what's active on me?" or "what's on the bandit caster?" at any time. The DM answers from the tracker — for PCs, fully; for NPCs, only what the party could observe (see *Foe Effects* below).

---

## Concentration — DM Auto-Prompts the Con Save

When a concentration-holder takes damage, the DM names the save in the same beat as the damage, automatically:

> *The bandit's arrow catches Sera in the shoulder — 9 damage. **Con save DC 10 to maintain Bless.***

DC is the standard `max(10, half damage taken)`. If the spell drops, the DM names the drop and removes the effect from the tracker and from any PCs it was buffing. Concentration is the single most-forgotten rule in chat-medium combat; auto-prompting closes the gap.

Concentration also ends RAW on: casting another concentration spell (DM flags before the new cast resolves), incapacitation, death, and explicit player choice. The tracker reflects all four.

---

## Mode Interaction — Game vs. Novel Display

How active-effects lines are rendered depends on the affected player's mode (see [information_disclosure.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/information_disclosure.md#scene-density--novel-vs-game-modes)).

### Game Mode

Mechanical line, terse and explicit:

> ***Active on you:** Bless (+1d4 atk/save, 4 rds), poisoned (1d4 dmg & disadv on atk, save DC 12 end of next turn).*

### Novel Mode

Narrative reminder threaded into prose, mechanically equivalent but tonally embedded:

> *Your god's hand still rests warm on your shoulder. Your stomach still churns from the bandit's blade — and you can feel it isn't done with you yet.*

Both deliver the same information: Bless is active, poisoned is active with ongoing damage and a save coming. Game players see the numbers; Novel players feel the conditions. **Debuff reminders cadence does not change with mode** — only the rendering does. A Novel player still gets the persistent-debuff reminder at the start of each DM response involving their PC; it's just woven into the prose rather than tagged as a mechanical line.

---

## Foe Effects — Observable Only

Effects on NPCs and foes appear in the [combat.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/combat.md#layer-b--foe-roster-each-round-or-when-it-shifts) foe roster as a parenthetical — **only if the party could observe them**.

- ✅ The bandit is bleeding from a gut wound (visible damage over time).
- ✅ The caster is wreathed in shimmering haze (visible Haste).
- ✅ The orc is shaking and won't meet your eyes (visible frightened).
- ❌ The cultist has Bless on her (invisible buff, no outward sign).
- ❌ The bandit captain has 11 HP left (numeric state, not observable).

Hidden effects stay in the DM's tracker and influence rolls invisibly. When a hidden effect would *become* observable — the cultist visibly winces as a Bless die fires, the caster's concentration breaks and the Haste shimmer dissipates — that's the moment it surfaces.

This matches the *signal not stat* principle from [combat.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/combat.md) and the *reveal vs. withhold* line from [information_disclosure.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/information_disclosure.md#info.sensory-channels).

---

## Spell Slots, Resources, and Charges

Primary responsibility for tracking spell slots, ki points, sorcery points, rage charges, item charges, and similar **rests with the player**. The DM's tracker may shadow these for verification but does not auto-surface them.

Exception: when a resource is **down to one or zero** and the player is about to declare an action that would use one ("I cast Fireball" but they're out of 3rd-level slots), the DM flags it in the moment — "you're out of 3rd-level slots; do you want to upcast from 4th or pick something else?" — before resolving the action. This is the same principle as the [private_information.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/private_information.md#private.hard-limits) world-state-clarification rule: don't run a decision built on a wrong resource picture.

---

## Reset / Loop Interaction

If the consuming game has a reset / loop / memory-wipe mechanic that fires periodically, the override specifies what happens to active effects at the moment of reset. Common patterns the override should address:

- Magical effects with durations (Bless, Haste, spell-imposed conditions) — dissolved on reset? carried through?
- Non-magical conditions (mundane poison, exhaustion, fear from a mundane source) — same question.
- Persistent items granting effects (runed items, attuned artifacts) — typically governed by an item-persistence rule.
- Concentration — usually ends on a reset because the caster is unconscious / unmade / reset; the override confirms.

The DM clears the tracker as the override specifies and re-applies only what the persistence rules say carries through.

---

## Hard Limits

- **The tracker is for tracking, not for narration shortcuts.** Surfacing an active effect doesn't replace describing what it looks like in-fiction. A poisoned PC's ongoing damage gets narrated as a wave of nausea, not just announced as a number — especially in Novel mode.
- **Debuff reminders are a courtesy, not a rule against consequences.** The DM reminds the player they're at disadvantage before they roll; if the player still chooses a bad action, the bad action runs. The reminder closes the OOC-memory gap, not the IC-decision gap.
- **Mutes are per-session and per-effect-instance.** Granular mutes auto-clear on re-acquisition; all mutes clear at session end. See [Player Mute](#player-mute--granular-auto-unmute-on-re-acquisition) above. This prevents permanent opt-outs from compounding into silently-rotted state across sessions.
- **DM-authoritative does not mean DM-secretive.** When the DM's tracker says an effect is over and the player thinks it isn't, the DM names the discrepancy openly: "I have Bless ending last round when Bren dropped concentration after the Con save. Sound right?" Tracker corrections happen in conversation, not by fiat.
