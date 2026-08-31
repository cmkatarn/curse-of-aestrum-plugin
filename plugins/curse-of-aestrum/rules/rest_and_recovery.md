---
id: rule_rest_and_recovery
name: Rest and Recovery
type: core_mechanic
related_rules: [rule_time_loop, rule_snapshot, rule_revert, rule_dead_zones, rule_active_effects_tracking]
---

## Overview

Standard 5e rest rules apply, modified by the loop. The headline: **outside a dead zone, sleeping through the midnight reset does not heal a PC** — they wake at 6 AM with the HP, spell slots, and exhaustion they had at their [snapshot]({{PLUGIN_ROOT}}/rules/snapshot.md), not at end of day. The only place a true long rest can be taken is inside a [dead zone]({{PLUGIN_ROOT}}/rules/dead_zones.md).

---

## Short Rests

- **RAW timing.** A short rest is one hour of in-fiction light activity.
- **Player-declared.** The DM does not auto-offer short rests. The party calls for them; the DM resolves availability based on the scene (combat ongoing, pursuit, time pressure).
- **Hit dice spending and short-rest abilities** (Warlock slots, Action Surge, Channel Divinity uses, etc.) follow RAW.
- **Short rests do not interact with the snapshot-revert.** Anything spent or recovered during a short rest is part of the day's mechanical state and is subject to the long-rest rules below.

---

## Long Rests — Inside a Dead Zone

Dead zones are the only places a long rest functions normally. RAW applies:

- 8 hours, at least 6 of which must be sleep (or species-equivalent rest).
- Full HP restored. All expended spell slots restored. Half the PC's total hit dice (minimum one) restored. Exhaustion reduced by one.
- One long rest per 24-hour period.
- RAW interruption rules apply (1+ hour of strenuous activity breaks the rest).

A PC sleeping inside a dead zone at midnight is not touched by the reset sequence — see [dead_zones.md]({{PLUGIN_ROOT}}/rules/dead_zones.md) — so the long rest completes cleanly.

---

## Long Rests — Outside a Dead Zone (the loop-forced sleep)

At 12:00 AM the loop's **Sleep** step forces unconsciousness on every loop subject not sheltered in a dead zone. The PC wakes at 6:00 AM when the **Wake** step lifts (see [time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md)).

This is **not a long rest.** It is the reset sequence, with [Revert]({{PLUGIN_ROOT}}/rules/revert.md) running between Sleep and Wake. The PC wakes with:

- **HP equal to their snapshot HP** — not their end-of-day HP. Damage taken during the day is undone, but so is any healing applied beyond snapshot HP. In practice, for most PCs this means waking at full HP because the snapshot was taken at a healthy moment; for a PC whose snapshot caught them wounded, the wound returns.
- **Spell slots equal to their snapshot slot count** — slots spent during the day return; slots that were already spent at the moment of snapshot remain spent, every cycle.
- **Exhaustion equal to their snapshot exhaustion level.** If snapshotted clean, the PC wakes clean. If snapshotted fatigued (level 1+), they wake fatigued — every reset, forever, until they break the loop or take a true long rest in a dead zone to reduce it.
- **Inventory and prepared spells** revert per [revert.md]({{PLUGIN_ROOT}}/rules/revert.md) and [snapshot.md]({{PLUGIN_ROOT}}/rules/snapshot.md).

**Moon Amulet bearers get no exception here.** The amulet protects memory only. HP, slots, hit dice, and exhaustion still revert to snapshot. The party cannot avoid the snapshot-revert by wearing amulets.

**Sleep-immune species are forced unconscious anyway.** The Sleep step overrides elven trance, warforged sentry mode, and similar racial features. They drop, freeze rigid, teleport, and wake at 6 AM like everyone else.

---

## Daytime Long Rests Outside a Dead Zone

A PC *can* take a normal RAW long rest during the day outside a dead zone (e.g., 2 PM to 10 PM at an inn). The long rest completes per RAW and grants full benefits at the moment of completion — full HP, all slots, half hit dice back, one level of exhaustion reduced.

**Those benefits then evaporate at midnight** when the snapshot-revert hits. The PC wakes at 6 AM with snapshot HP, snapshot slots, snapshot exhaustion — as if the daytime long rest never happened.

This makes daytime long rests outside dead zones useful only for **one big evening push** between rest completion and midnight. The party trades distance from the Deckard estate for a few hours of recovered resources.

---

## Hit Dice — Exception

Hit dice **always revert to full at the midnight reset, regardless of dead-zone status.** This is the one mechanical resource that does not follow the snapshot model.

- A PC sleeping in a dead zone gets the RAW "half hit dice restored" on long rest, then at midnight (which they don't experience inside the dead zone) — they simply complete the next day with their long-rest restored pool.
- A PC sleeping outside a dead zone wakes at 6 AM with the full hit dice pool, every cycle. Hit dice spent during the day are gone for that day but back tomorrow.

Treat hit dice as a daily-refresh resource for the duration of the loop.

---

## Exhaustion

Exhaustion follows the snapshot-revert model identically to HP and slots, with one practical note:

- A PC whose snapshot was clean (0 exhaustion) can only acquire exhaustion *during a day* and will always shed it at the next midnight outside a dead zone — or reduce it normally via a dead-zone long rest.
- A PC whose snapshot caught them at exhaustion 1+ is permanently stuck at that level until they either (a) take a dead-zone long rest to reduce it by one — and the reduction holds only until the next time they sleep outside a dead zone, at which point exhaustion reverts to snapshot — or (b) break the loop.

In effect, snapshot exhaustion is a baked-in floor for any PC unlucky enough to have one. The party currently has none on record, but this matters if a future PC enters Aestrum already fatigued.

Exhaustion tracking otherwise follows [active_effects_tracking.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/active_effects_tracking.md).

---

## Quick Reference

| Situation | HP / Slots / Exhaustion at 6 AM | Hit Dice at 6 AM |
|---|---|---|
| Slept in dead zone (RAW long rest) | Restored per RAW (full HP, all slots, -1 exhaustion) | Half restored per RAW |
| Slept outside dead zone (loop reset) | Reverted to snapshot values | Fully restored |
| Daytime long rest outside dead zone, then loop reset | Reverted to snapshot values at midnight | Fully restored |
| Awake in a dead zone through midnight | Unchanged — no rest, no reset | Unchanged |
