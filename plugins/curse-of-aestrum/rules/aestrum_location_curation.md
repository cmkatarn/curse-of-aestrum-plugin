---
id: rule_aestrum_location_curation
name: Aestrum Location Curation
type: meta_convention
---

# Aestrum Location Curation

Aestrum's geography is **author-curated** at the location layer. Existing questlines, factions, and lore depend on the established set of in-Aestrum places. Claude does not introduce new ones during play.

## What this rule covers

- **Settlements** (towns, villages, hamlets) inside the Aestrum territorial line.
- **Named structures** (inns, temples, shops, manors, the seat, specific houses, shrines) inside Aestrum.
- **Named landmarks** (hills, forests, springs, bridges, gates) inside Aestrum.

The rule binds Aestrum specifically. Outside Aestrum (Setland, the other duchies, the wider Nortmunde region), Claude has greater latitude to introduce locations as play requires, subject to standard scene discipline.

## What this rule does NOT cover

- **Characters.** Generated NPCs (hostlers, hostlers' boys, gate guards, market figures, chapel attendants, road travelers) are **necessary** for fleshing out the region's inhabited texture. Author them as play requires; they fall under standard scene discipline (knowledge boundaries, voice, etc.) and may be promoted into canon files when the DM judges they should persist. This rule does not constrain character generation.
- **Architectural detail within an established location.** An inn's under-stair sleeping nook, a castle's ledger-study, a chapel's bell-loft — these are detail-rendering of a canon location, not new locations.
- **Junctions** (road forks named for navigation, with no settled population). A junction names a fork; treating it as a destination is the leak. Already-canonized junctions (e.g., Quarterways at 4WI; Tine Cross at 3WI) may be rendered as the road-fork landmarks they are. New junctions may not be introduced.

## Why

Aestrum's questlines and authored content are tightly bound to the established location set. A fabricated settlement absorbs play attention the questlines did not budget for, creates a place the DM must then decide whether to canonize or retcon, and risks displacing or contradicting curated content. The cost is asymmetric: the in-fiction beat gains a small piece of texture; the campaign's authoring integrity takes a real hit.

Outside-Aestrum latitude exists because there is no equivalent curated set for Setland or the other duchies (yet); Claude may render a wayhouse or a hill chapel on Setland soil as the road requires, without the same risk.

## What to do when reaching for a location

When the next beat wants the party to be *somewhere* inside Aestrum, the only destinations available are those:

- **Already on a signpost the party has read** (current known set: **Mirot, Rockwood, Duskwall, Dunleaven, the Perisdottir residence**).
- **Already established in `locations/chapter_1/`** or surfaced through DM-authored in-fiction discovery in this campaign.
- **Named in a saved overlay** the party has been to.

If the beat wants a location not on these lists, the correct move is to **stop and ask the DM** rather than render it. The in-fiction shape of the beat (the test of the duchy, the next stop on the road) can almost always be redirected onto an existing destination once the menu is named honestly.

The leak shape to watch for: a candidate destination *named in passing* — *"a hamlet on the road," "a chapel up the hill," "the next village over"* — that is not on the curated list. Catch it before the narration commits to it as a place the party can walk to.

## Before rendering the approach to a canonical destination

Picking a destination correctly off the curated list is **not sufficient** — the *route to it* and the *first-sight rendering of it* are themselves canonical details, not Claude's to invent.

Before drafting any journey beat toward a curated destination, check the relevant source files for:

- **Distance and travel time** (see [`{{PLUGIN_ROOT}}/locations/chapter_1/routes.md`]({{PLUGIN_ROOT}}/locations/chapter_1/routes.md) for the road network's distances, foot-times, terrain, and hazards per segment).
- **Terrain and corridor character** (open road, forest, mountain pass, walking-path, etc.).
- **Visibility profile** — what is visible from where, at what point along the approach the destination first comes into view, what intervening landscape conceals it.
- **Known residents and other named entities** at or along the route.

The leak shape this prevents: a canonical destination rendered with an **improvised approach** — wrong terrain, wrong distance, wrong first-sight profile — that silently contradicts canon while looking compliant on the surface, because the destination *name* is right and only the *route* is wrong. The narration of a route is *implicit world-building* about the canonical location; it must trace to canon the same way the destination itself does.

When the route or approach is *not* canonized in the source files, the correct move is the same as for unlisted destinations: **stop and ask the DM** before improvising it. The DM may then supply the detail, codify it for future runs, or redirect the beat.

## Loading

This rule is loaded as a scene-time drafting constraint via the CoA override (`{{PLUGIN_ROOT}}/overrides/scene.md`).
