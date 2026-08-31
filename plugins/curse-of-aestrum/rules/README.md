---
id: rules_index
name: Aestrum Mechanics Index
---

# Mechanics Index

Each file codifies one game mechanic. Lore, motivation, and political context live in [key_lore_summary.md]({{PLUGIN_ROOT}}/lore/key_lore_summary.md); this directory is the table-facing rules layer.

## The Loop

- [time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md) — Timed midnight reset sequence (Sleep → Recreate → Teleport → Modify Memory → Wake) and recreate rules.
- [snapshot.md]({{PLUGIN_ROOT}}/rules/snapshot.md) — Memory snapshot taken on first entry. Open rulings flagged.
- [revert.md]({{PLUGIN_ROOT}}/rules/revert.md) — Midnight memory rollback to the snapshot.
- [fuzzball.md]({{PLUGIN_ROOT}}/rules/fuzzball.md) — Pattern-correcting sub-process planted after revert. Escalation by exposure level.
- [loop_anchors.md]({{PLUGIN_ROOT}}/rules/loop_anchors.md) — Anchor shrines, qualifying prayer rule, breaking the loop.

## Antimagic

- [dead_zones.md]({{PLUGIN_ROOT}}/rules/dead_zones.md) — How dead zones interact with each reset step and with the fuzzball.
- [magic_immune_runes.md]({{PLUGIN_ROOT}}/rules/magic_immune_runes.md) — Runed items as portable dead zones; the script convention.

## Homebrew Rules

- [optional_rules.md]({{PLUGIN_ROOT}}/rules/optional_rules.md) — Catalog of toggleable override rules a single campaign may opt into (e.g. `ignore_material_components`). Campaigns flip toggles in `{{PROJECT_ROOT}}/campaign_state/<C>/rules/rule_overrides.md`; behavior is defined here.
- [magical_item_conversion.md]({{PLUGIN_ROOT}}/rules/magical_item_conversion.md) — Essence-extraction conversions; per-step protection items (Sleep, Teleport) and distributed speed.
- [item_persistence.md]({{PLUGIN_ROOT}}/rules/item_persistence.md) — How looted items behave across resets; item-location determines retention, inert copies, runed items as a separate persistence path.
- [rest_and_recovery.md]({{PLUGIN_ROOT}}/rules/rest_and_recovery.md) — Short/long rest mechanics under the loop; dead zones grant RAW long rests, sleeping outside dead zones reverts HP/slots/exhaustion to snapshot (no recovery), hit dice always refresh at midnight, daytime long rests outside dead zones grant temporary benefits until reset.
- [death_and_dying.md]({{PLUGIN_ROOT}}/rules/death_and_dying.md) — Death saves and stabilization (RAW); Recreate restores snapshotted subjects who die outside dead zones; dead-zone deaths require body extraction or in-fiction resurrection; Moon Amulet wearers remember dying; resurrection magic works only outside dead zones with component refund at reset; animals/familiars stay dead.
- [travel.md]({{PLUGIN_ROOT}}/rules/travel.md) — Encounter defaults inside and outside Aestrum; pace and loop-edge behavior.
- [consequences.md]({{PLUGIN_ROOT}}/rules/consequences.md) — How the world reacts to off-rail play. Three-tier model: proportional consequences for unexpected exploration, escalating danger for drifting from the story, wildcard danger for actively threatening canon.
- [companion_animals.md]({{PLUGIN_ROOT}}/rules/companion_animals.md) — The two adoptable animals (dog, cat); no voice/POV, appearance indeterminate until adoption locks it, danger-alert (dog), judgment vs. treatment-based loyalty, undead instinct with per-scene acclimation, continuous memory, and the post-reveal realization beat. Content sheets: `{{PLUGIN_ROOT}}/npcs/chapter_1/stray_dog.md`, `stray_cat.md`.

## Engine-Layer Mechanics (Canterbury)

Generic D&D 5e mechanics — combat presentation, turn order & pacing, active-effects tracking, scene framing, information disclosure, private information, social checks, searches & loot, race anatomy — live in the shared engine at `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules` and are loaded per the `scene` skill's mechanics table. This index covers only Curse of Aestrum homebrew: the loop, antimagic, and the setting's overrides/extensions of engine rules (`item_persistence`, `travel`, `rest_and_recovery`, `death_and_dying`, `consequences`).
