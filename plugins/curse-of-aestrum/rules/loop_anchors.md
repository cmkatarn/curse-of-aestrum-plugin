---
id: rule_loop_anchors
name: Loop Anchors and Breaking the Loop
type: core_mechanic
related_rules: [rule_time_loop]
related_npcs: [npc_rowan_deckard, npc_judith_asemyeer, npc_hati_heldrivver]
related_locations: [loc_misty_forest_shrine, loc_shrine_of_selune]
---

## Overview

Shar sustains the [time loop]({{PLUGIN_ROOT}}/rules/time_loop.md) by drawing on prayers at **two physical anchor shrines**. The loop is broken on any day where no qualifying prayer reaches either shrine.

---

## Qualifying Prayer

Any prayer at either anchor location that can be interpreted as **"I wish I could re-live today"** is sufficient to sustain the loop for that cycle.

The bar is interpretive, not literal. A prayer for one more day, one more chance, more time with someone, another shot at something — all qualify.

---

## The Anchor Shrines

1. **The Shar statue in the Duskwall Selûne shrine.** Originally a Selûne shrine; desecrated and converted, currently run by Hati Heldrivver.
2. **The Misty Forest shrine.** Two valid Shar likenesses can be present here:
   - **Hati's donated idol** — a carved Shar likeness left by Hati when she took the original forest statue to Duskwall. Predates the loop, resets each midnight, and qualifies as an anchor on its own. This is Shar's redundancy at the forest shrine and is always present.
   - **Rowan's hand-carved effigy** — a *conditional* additional anchor, and **not present by default.** He must be driven from the Deckard Estate **and** have lost Miri to the party as a long-term protected asset. Until both are true he prays through Hati's idol, which he has always considered lesser — a substitute that has not earned its place in Shar's shrine — and tolerates out of habitual disdain rather than need.

     **What changes is not his theology, it is his temper.** Once his world has come apart, the disdain stops being tolerable: praying to something unworthy while he has lost everything is an insult he will no longer swallow, and he begins fashioning a likeness he considers deserving — out of frustration and the anger underneath it. The effigy is a grievance made solid, not a devotional upgrade. When present it postdates the snapshot and disappears at midnight; he re-carves it each cycle.

     **Rowan's own sheet formerly described the carving as unconditional daily routine. That is superseded — this file is authoritative.**

Both shrines reset each morning along with the rest of Aestrum. Destroying an anchor object removes Shar's ability to hear prayers through it until the next reset — so destruction is a **same-day window**, not a permanent fix.

**Breaking the forest shrine on a single day requires destroying every present likeness.** Hati's idol alone if the effigy isn't being carved; both if it is. Rowan will pray through whichever remains.

---

## Current Prayer Sources (DM only)

These are the known prayer-givers as of the current state. New sources may emerge.

Each prayer entry below follows the
[time_and_events.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/time_and_events.md)
schema. Prayer-givers are world-state participation events: the prayer
happens at the declared time within the declared duration, regardless
of whether the party is watching. Interrupting a prayer is a
participation play and is governed by the schema's mid-event arrival
rules; the prayer's `catchup` field describes what an arriving party
can do *to* it, not what they recover from missing it.

- **Rowan Deckard**
  - `location:` the **Misty Forest shrine** (anchor 2). He is the only known prayer-giver who reaches this anchor.
  - `time:` **~7:00 AM.** He leaves the Deckard Estate dead zone at around **5:00 AM** — he shelters until **Modify Memory has fired at 4:30**, the last step that can reach him, then goes — and the cross-country line to the shrine takes him a full two hours through trackless forest, fast as he moves. See [time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md) on why wakefulness alone would not have protected him.
  - `duration:` ~2–5 minutes at the Misty Forest shrine.
  - `catchup: partial` — once the prayer completes, the loop is sustained for the cycle; intercepting Rowan mid-prayer can still prevent qualification if every word is cut off before the petition resolves.
  - **Petition:** one more day / one more chance to convince Miri.
- **Judith Asemyeer**
  - `time:` 7:00 AM ± 10 min (her routine is consistent but not bell-precise).
  - `duration:` ~10 minutes at the Duskwall Selûne shrine.
  - `catchup: partial` — same as Rowan; once the petition resolves the loop is sustained for the cycle.
  - **Petition:** one more day to safely serve Shar. Her prayer reaches the Shar statue (anchor 1).
- **Delmuir Goodfeet**
  - `location:` the **Duskwall Selûne shrine** — his prayer reaches the Shar statue (anchor 1), the same anchor Judith's does. He is not a forest-shrine prayer-giver.
  - `time:` ~9:30 PM ± 30 min (late evening, before he retires). He has spent the day with Maris Vell, walked her home, and comes to the shrine after.
  - `duration:` ~5 minutes.
  - `catchup: partial` — same.
  - **Petition:** another day with the woman he's courting. *(Unencountered.)*

**Window-of-failure note.** Because qualifying prayers can fire at
multiple times of day across the prayer-giver roster, a party
attempting Approach B (intercept all prayer-givers) must hold the
window from Rowan's dawn prayer through Delmuir's late-evening
prayer — roughly fourteen waking hours, on a single cycle.

**Anchor split, for Approach B planning.** Two of the three prayers
(Judith at ~7 AM, Delmuir at ~9:30 PM) reach **anchor 1**, the Shar
statue in the Duskwall shrine. Only Rowan's reaches **anchor 2**, the
Misty Forest shrine. A party that destroys the Duskwall statue and
stops Rowan has covered every known source; a party that stops only
the people has to hold a fifteen-hour window.

**The morning collision — the hard constraint on Approach B.**
**Rowan prays at ~7:00 AM at the forest shrine. Judith prays at ~7:00
AM at the Duskwall shrine.** The two earliest prayers of the day are
*simultaneous*, at anchors two and a half hours apart on foot — and
part of that leg is trackless forest that cannot be hurried.

This is not a tight window. **There is no window.** A single group
cannot be at both, cannot reach the second after the first, and cannot
arrive early enough at one without abandoning the other. Nothing about
the geography or the timings gives on this.

**So a pure Approach B is not available to one group.** The party must
either split across two sites with no way to coordinate once the morning
starts, or take one of the two prayers off the board by other means
before 7:00 that same morning:

- **Destroy the Duskwall statue before 7:00.** Note what this buys:
  anchor 1 takes *both* Judith's 7:00 prayer and Delmuir's 9:30 PM
  prayer, so felling one statue in the early morning collapses the
  roster to Rowan alone. **This is the cleanest line through the whole
  problem** and a party that finds it has genuinely solved the day.
- **Move a prayer-giver off their routine** — Rowan drawn into company,
  Judith kept from the shrine — before the hour arrives.

**Do it that same morning, not the night before.** Destroying an anchor
is a *same-day window*: both shrines are restored at the midnight reset,
so last night's work is undone before the party wakes. The statue has to
come down between the 6:00 AM Wake step and Judith's arrival at 7:00.

**This is deliberate and should not be softened by fudging either time.**
Rowan's ~5:00 AM departure is a hard behavioural rule (he shelters until
Modify Memory has fired at 4:30), the two-hour forest leg cannot be
hurried, and Judith's routine is consistent. The impossible morning is
the price of Approach B; Approach A exists precisely because it is
payable. Approach
A (destroy both anchor shrines before any prayer that day) avoids
the window problem but inherits its own timing: the earliest prayer
of the day fires at ~7:00 AM — two of them do, at once — so both
shrines must be down inside the single hour between the 6:00 AM Wake
step and 7:00.

---

## Breaking the Loop

All qualifying prayers must be prevented on the same day. Two viable approaches:

### Approach A — Destroy both anchor shrines before any prayer that day

Removes Shar's ability to hear any prayer made at those locations. Most reliable, since it cuts off all prayer-givers at once. The window closes at the next morning reset, when both shrines are restored.

### Approach B — Intercept every prayer-giver before they pray

Stop each person before they pray that day. Higher operational complexity, requires complete knowledge of every active prayer source. Risk: an unknown prayer-giver sustains the loop and the attempt is wasted.

**Either way, the window is narrow.** Shrines reset each morning; prayer-givers' memories reset each midnight. A successful break must complete within a single cycle.

---

## After the Loop Breaks

See [fuzzball.md]({{PLUGIN_ROOT}}/rules/fuzzball.md) → *Post-Loop Dissolution* for the aftermath. NPCs will gradually surface years of suppressed strangeness over a short period.
