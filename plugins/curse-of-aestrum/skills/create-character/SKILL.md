---
name: create-character
description: >
  Use this skill when the user wants to create a single new player character (PC)
  for the Curse of Aestrum campaign. Triggers on "create a character",
  "make a new PC", "build a character", "roll up a character", "I want to play
  a [race/class]", or any request to author a single PC sheet. Supports two
  modes: the user provides a complete sheet (stats / inventory / spells), or
  the skill walks them through D&D 5e character creation with campaign-tied
  background hooks. Do NOT use for assembling a multi-PC party (use
  create-party) or for NPC creation (use create-npc).
allowed-tools: [Read, Grep, Glob, Write, Edit, PowerShell]
version: 2.0.0
---

> **Plugin path resolution — read this first.** You are running inside an installed plugin. Two
> placeholders appear in this skill and in every file it leads you to read:
> `{{PLUGIN_ROOT}}` = `${CLAUDE_PLUGIN_ROOT}` (this plugin's bundled files — engines, rules,
> overrides, and campaign content) and `{{PROJECT_ROOT}}` = `${CLAUDE_PROJECT_DIR}` (the player's
> own working directory, where every `campaign_state/…` play-state file is read and written).
> Whenever any file you read contains a `{{PLUGIN_ROOT}}/…` or `{{PROJECT_ROOT}}/…` path, replace
> the placeholder with the absolute path shown above and read/write that. **Never** resolve these
> against the working directory or a file's own folder, and never write into `{{PLUGIN_ROOT}}`.


# Create Character — Curse of Aestrum

Thin shell. Loads the rpg-5e engine's create-character walkthrough and
the Curse of Aestrum setting overrides.

**Path resolution.** Every path below is written `{{PLUGIN_ROOT}}/...` and
resolves against this plugin's bundled root — **not** this skill's own base
directory, and **not** the working directory. The engines are vendored inside
the plugin: Canterbury is at `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/...`. There
is no sibling engine repo to reach for, and no path leaves the plugin. If a read
404s, re-resolve the placeholder against the plugin root before assuming the file
is missing.

## Load order

1. **Engine walkthrough.** `Read` `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/create-character/core.md`.
2. **CoA override.** `Read` `{{PLUGIN_ROOT}}/overrides/create-character.md`.

The engine's `core.md` will direct on-demand reads of:

- `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/race_anatomy.md` (STEP 3.5 anatomy pass).
- `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/random_character_generation.md` (if the PC is
  rolled — Random source).
- `{{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_progressive.md` (if built as a stub).

## Workflow

After loading the layers above, follow the workflow in
`{{PLUGIN_ROOT}}/engines/rpg-5e-engine/create-character/core.md` (STEPs 1–4), with the CoA
override applied at draft time. The override supplies:

- Spoiler discipline (the Aestrum-opacity rule and what canon must not
  leak).
- Blood-relation list (Quellenna, Galadiil, Evandur, Malak, Rowan;
  Amblecrown exception only on user volunteer).
- Restricted race / class features.
- Output path convention (`{{PROJECT_ROOT}}/campaign_state/<C>/party/saved/<instance>/`).
- The three hook tables (Background → Faction, Race → Hooks, Class →
  Hooks) — Nortmunde-side only.
- Content-rating session context (M default outside in-game sessions).
