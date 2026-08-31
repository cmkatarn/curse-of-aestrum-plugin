---
name: create-party
description: >
  Use this skill when the user wants to assemble a full party (up to 5 PCs) for
  a new Curse of Aestrum campaign instance. Triggers on "create a party",
  "build a party", "start a new campaign", "set up the party", "make a group of
  characters", or any request to author multiple PCs at once coordinated by a
  single player. The skill orchestrates per-slot character creation (player
  builds, fully random, or guided random with sex/race/class/archetype hints),
  enforces party diversity, finalizes the roster, and opens the campaign with
  an introduction to Setland. Do NOT use for solo PC creation (use
  create-character) or for NPC creation.
allowed-tools: [Read, Grep, Glob, Write, Edit, PowerShell, Skill]
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


# Create Party — Curse of Aestrum

Thin shell. Loads the rpg-5e engine's create-party orchestration and the
Curse of Aestrum setting overrides. Calls the create-character skill
internally for each slot.

**Path resolution.** Every path below is written `{{PLUGIN_ROOT}}/...` and
resolves against this plugin's bundled root — **not** this skill's own base
directory, and **not** the working directory. The engines are vendored inside
the plugin: Canterbury is at `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/...`. There
is no sibling engine repo to reach for, and no path leaves the plugin. If a read
404s, re-resolve the placeholder against the plugin root before assuming the file
is missing.

## Load order

1. **Engine orchestration.** `Read` `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/create-party/core.md`.
2. **CoA override (party-level).** `Read` `{{PLUGIN_ROOT}}/overrides/create-party.md`.
3. **CoA override (character-level — inherited).** `Read` `{{PLUGIN_ROOT}}/overrides/create-character.md`.

The engine's `core.md` will invoke the `create-character` skill for
each player-built slot (which itself loads the engine PC walkthrough +
CoA character override). For random / guided-random slots, the engine
routes the per-slot roll through
`{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/random_character_generation.md` (the shared
randomization module); follow it silently with the CoA override applied,
adding the engine's multi-slot layer (cross-slot diversity, role
coverage).

## Workflow

After loading the layers above, follow the workflow in
`{{PLUGIN_ROOT}}/engines/rpg-5e-engine/create-party/core.md` (STEPs 1–6), with both CoA
overrides applied at draft time. The party-level override supplies:

- State-directory and instance scaffold (`{{PROJECT_ROOT}}/campaign_state/<slug>/`).
- Anti-conflict additions (Shar acolyte, Shrikes membership, Aestrum
  origin, etc.).
- Outsider rule.
- Opening location list (Lion's Den, Charnelhold streets / lower
  districts, Setland docks, Setland temple, trade road).
- Case B Beat 2 specifics (Quellenna + Duke Malak deliver the
  expedition pitch).
- Pre-read location files for the opening scene.
- Hand-off region name ("The party is in Setland").

The character-level override (inherited) carries the spoiler
discipline, blood-relation list, and hook tables that apply to every
slot.
