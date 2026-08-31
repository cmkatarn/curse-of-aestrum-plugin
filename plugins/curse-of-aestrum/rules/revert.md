---
id: rule_revert
name: The Revert
type: core_mechanic
related_rules: [rule_snapshot, rule_fuzzball, rule_time_loop, rule_dead_zones]
---

## Overview

At **4:30 AM** (the Modify Memory step of the [reset sequence]({{PLUGIN_ROOT}}/rules/time_loop.md)), each affected subject's memory is reverted to their [snapshot]({{PLUGIN_ROOT}}/rules/snapshot.md). Everything experienced since the snapshot — conversations, discoveries, trauma, relationships — is erased. The subject wakes believing it is the morning they first arrived in Aestrum.

Modify Memory deliberately runs **after** Recreate (1:30 AM) so resurrected subjects do not wake carrying memories of having died.

The revert is paired with the [fuzzball]({{PLUGIN_ROOT}}/rules/fuzzball.md), a pattern-correcting sub-process planted immediately after.

---

## Who Is Affected

- **Affected:** Any subject inside Aestrum at 4:30 AM who is not in a dead zone and is not wearing a Moon Amulet.
- **Not affected:** Subjects inside a dead zone at the moment the step fires. Their snapshot remains on file; the revert fires the next midnight they sleep outside a dead zone.
- **Not targeted at all:** Moon Amulet bearers. Selûne's gift blocks the Modify Memory targeting entirely.

See [dead_zones.md]({{PLUGIN_ROOT}}/rules/dead_zones.md) for dead-zone interactions in detail.

---

## What Is Reverted

- Memory of the day's events, conversations, discoveries.
- Emotional state tied to those memories.
- Relationships formed since the snapshot.

What is **not** reverted by this step (other reset steps handle these):
- Physical objects → handled by the Recreate step at 1:30 AM.
- Creature bodies and missing parts → also Recreate at 1:30 AM.
- Spatial position → handled by Teleport at 3:00 AM.

---

## Edge Cases

- **Newcomers in their first 24 hours.** Their snapshot was just taken; the revert returns them to a state essentially identical to the present, with at most a day of erasure.
- **Long-term residents.** Their snapshot is years out of date. The revert erases years of subjective experience every night.
- **Subjects mid-conversation with a memory-retaining party member.** Mid-conversation, the NPC simply ceases responding as Sleep fires first at midnight; revert fires while unconscious. They wake with no memory of the encounter.
