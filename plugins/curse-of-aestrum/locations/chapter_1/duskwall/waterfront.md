---
id: loc_duskwall_waterfront
name: The Waterfront District
type: district
parent: loc_duskwall
region: aestrum
curse_affected: true
connected_locations: [loc_duskwall, loc_waterfront_warehouse]
npcs_present: [npc_delmuir_goodfeet]
chapter: 1
---

## Overview

Duskwall's dockfront quarter — the quay, the harbour it faces, and the trades that
work them. It is one of the city's named districts and is **undeveloped**: four
establishments exist as names, and almost nothing below them.

## The Sealed Port — read this before rendering anything

**Duskwall is a sealed-in port.** Aestrum's boundary traps sea traffic exactly as it
traps everyone on land: a vessel that tries to cross it strikes it and founders.
External ships do **not** come and go, and cargo, news and fresh arrivals do not wash
in off the water.

**Do not render the harbour with "busy seaport" ambient defaults.** No incoming or
departing ships, no masts crowding the quay, no sailors fresh off a boat, no word
carried in by sea — unless a specific documented vessel grounds it. A character looking
at the harbour sees the **static port**: the dockfront and quay, the waterfront trades,
the water, the weather, the lamps. Not asserted traffic.

This is the location-level companion to the gate's fabricated-concrete check. A sealed
setting makes ambient world-filling *unsafe* where an ordinary port would make it
harmless.

## What Is Here

Named, and little more — each is a hook rather than a described place:

- **Holy Mackerel** — fishmonger and eatery
- **Harbormaster** — the port authority office at the docks
- **Sorrow's Gems and Antiquities** — gems and curio dealer
- **Rogue's Waste Salvage** — salvage operation

The [city lockup]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/city_lockup.md)'s street-level entrance is nearby, carved into the
cliffside toward the seaport.

## The Daily Cycle

Three separate routines cross this district every day, and all of them repeat:

| Who | When | What |
|---|---|---|
| **[Delmuir Goodfeet]({{PLUGIN_ROOT}}/npcs/chapter_1/delmuir_goodfeet.md)** | **morning** | **five practice throws** with the Loadstone, from cover — pebbles to specific cracks in the dock planking, his cap onto a seagull's head, a coin to a beggar across the wharf |
| **Delmuir** | around the district | present most of the day; the charges are spent, the loitering is not |
| **Delmuir** | **late afternoon** | leaves with the **sixth charge** unspent, to impress Maris Vell with it; she kisses him goodnight; he goes on to the shrine late that evening |
| **[Rick Hastley]({{PLUGIN_ROOT}}/npcs/chapter_1/rick_hastley.md)** | from Day 9 | busking within earshot on roughly **one in three** party visits to the docks |
| **Miri and Rowan** | afternoon | pass through the Waterfront District together as part of their day |

**The theft never recedes.** Delmuir took the Loadstone from these docks on **Day 2 —
subjectively, and every day.** It is not something he did once in the past: the snapshot
holds him permanently on the second day of a courtship, permanently a day after the
theft, and permanently certain he has owned the thing for **exactly one day** — which
is why he is still delighted by how much he has worked out already.

**He is one throw from disaster and does not know it.** His budget of *five practice
throws and one for her* is not a careful allowance — it is the **precise upper limit**
of the charges. Every single day he has been one charge away from arriving at Maris
empty-handed, and has never once found out.

## Where He Practises — a spot away from the wharf's eyes

**He cannot practise in the open.** He stole the Loadstone from these docks, from people
who work them daily, and a halfling visibly making objects leap across the wharf is a
halfling who gets recognised. So the throws happen from **an empty, disused structure at
the dockfront's edge** — out of sight, with a view of the quay.

**The Loadstone makes that work.** It carries a load *from here to there*; the effect
lands at the target, not at the thrower. Tucked out of the way, he can put a pebble in a
plank crack, a cap on a gull and a coin in a beggar's hand clear across the wharf, and
nobody watching any of those things sees a source. **His targets are public; he is not.**

**That building is [the Waterfront Warehouse]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/waterfront_warehouse.md)** — the same
disused structure Luca uses to corner and conscript outsiders. Delmuir does not know
that, and the Shrikes do not know about him.

## The Incorrigible — a dated arrival

**Before Day 9 there is no ship.** *[The Incorrigible]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/the_incorrigible.md)* anchors
offshore on **Day 9**, and on the **morning of Day 10** Rylin and Baldric offload the
cargo onto this waterfront. Rick's busking begins from the same arrival.

That is a one-way trigger on the Aestrum clock — check the day before putting any
vessel, any sailor, or any offloaded cargo on the quay.

## The Alchemist's Fire Market — conditional, not default

*Conditional on the cycle being active **and** a buyer having been found.*

Once the cargo has landed and the cycle is still running, **alchemist's fire becomes
purchasable here**: the daily reset recreates market conditions, and secondary stock
cycles through waterfront vendors each morning.

**If the cycle was already broken before Day 9**, this never happens — the cargo sells
once, is absorbed by whoever bought it, and no market availability results. Do not
render the market unless both conditions hold.

## Open Slots — To Develop in Play

- **[layout]** All four establishments are names only. Holy Mackerel, the Harbormaster's
  office, Sorrow's, and Rogue's Waste have no interiors, no staff, and no described
  frontage.
- **[relation]** **The Incorrigible's regular cargo buyer** — a Duskwall waterfront
  buyer for the ship's legitimate cargo, referenced on Rylin's sheet and deliberately
  left unnamed as a callback slot. Assign to an elevated waterfront character when one
  fits.
- **[layout]** The quay itself: where cargo lands, how the
  dockfront meets the street.

## DM Notes

**The district's undeveloped state is not an accident to paper over.** It is named,
placed, and populated by routine — that is enough to run a scene at the docks without
inventing a port. Reach for the routines and the static-harbour rule before reaching
for detail that is not here.
