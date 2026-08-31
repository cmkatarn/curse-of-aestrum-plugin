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
   - **Rowan's hand-carved effigy** — a *conditional* additional anchor. Rowan only carves it when his fixation on Miri has been disrupted to the point that Hati's idol no longer satisfies his need for a likeness of his own. Specifically: he must be driven from the Deckard Estate **and** have lost Miri to the party as a long-term protected asset. Without both, he has no drive to carve his own — he prays through Hati's idol as a matter of habitual disdain rather than displacement. When the effigy is present, it postdates the snapshot and disappears at midnight; Rowan re-carves it each cycle.

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
  - `time:` immediately after he rises from his dead-zone shelter at the Deckard Estate (no fixed clock time; trigger-driven). Typical: shortly after dawn.
  - `duration:` ~2–5 minutes at the Misty Forest shrine.
  - `catchup: partial` — once the prayer completes, the loop is sustained for the cycle; intercepting Rowan mid-prayer can still prevent qualification if every word is cut off before the petition resolves.
  - **Petition:** one more day / one more chance to convince Miri.
- **Judith Asemyeer**
  - `time:` 7:00 AM ± 10 min (her routine is consistent but not bell-precise).
  - `duration:` ~10 minutes at the Duskwall Selûne shrine.
  - `catchup: partial` — same as Rowan; once the petition resolves the loop is sustained for the cycle.
  - **Petition:** one more day to safely serve Shar. Her prayer reaches the Shar statue (anchor 1).
- **Delmuir Goodfeet**
  - `time:` ~9:30 PM ± 30 min (late evening, before he retires).
  - `duration:` ~5 minutes.
  - `catchup: partial` — same.
  - **Petition:** another day with the woman he's courting. *(Unencountered.)*

**Window-of-failure note.** Because qualifying prayers can fire at
multiple times of day across the prayer-giver roster, a party
attempting Approach B (intercept all prayer-givers) must hold the
window from Rowan's dawn prayer through Delmuir's late-evening
prayer — roughly fourteen waking hours, on a single cycle. Approach
A (destroy both anchor shrines before any prayer that day) avoids
the window problem but inherits its own timing: the earliest prayer
of the day fires shortly after dawn, so the shrines must be down
before Rowan rises.

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
