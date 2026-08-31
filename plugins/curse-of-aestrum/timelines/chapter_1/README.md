# `timelines/chapter_1/` — Canonical Timelines

This directory holds canonical, campaign-instance-independent timelines.

- **`{{PLUGIN_ROOT}}/timelines/chapter_1/nortmunde_regional.md`** — Canonical Nortmunde regional events for Chapter 1. World political, divine, and historical events that occur in every playthrough. Conditional events (e.g., Aidra's army moving on Aestrum) are tagged `*[conditional]*` and may be preempted by party action.

## No `aestrum_events.md` here — by design

The in-loop session log is entirely playthrough-specific (which NPCs the party met when, what they discovered, which encounters they survived). Each new campaign that enters Aestrum produces its own `saved/aestrum_events.md`; no canonical Chapter 1 version makes sense.

A future canonical artifact for Aestrum *may* be authored at this level — a **daily NPC schedule** describing where each loop-trapped NPC goes on a typical loop day (Rowan's routine, the Trambeathen funeral procession, market hours, etc.). That is intentionally **not** included in the current refactor; if/when it lands, it should live here as something like `aestrum_daily_schedule.md` rather than as an events timeline.
