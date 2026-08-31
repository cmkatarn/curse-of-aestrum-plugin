---
name: create-npc
description: >
  Use this skill when the user wants to create a single NPC for the Curse of
  Aestrum campaign — a companion who travels with the party, a recurring face,
  or an incidental contact. Triggers on "create an NPC", "make an NPC", "add a
  companion", "build a companion NPC", "spin up an NPC", "roll up an NPC", "give
  me a stub NPC", or any request to author one non-player character. Supports
  the same authoring axes as create-character: source (provided / guided /
  random) and completeness (complete / stub). The NPC default is random + stub —
  a fast, runnable character fleshed out in play. Do NOT use for player
  characters (use create-character) or for assembling a party (use create-party).
allowed-tools: [Read, Grep, Glob, Write, Edit, PowerShell]
version: 1.0.0
---

> **Plugin path resolution — read this first.** You are running inside an installed plugin. Two
> placeholders appear in this skill and in every file it leads you to read:
> `{{PLUGIN_ROOT}}` = `${CLAUDE_PLUGIN_ROOT}` (this plugin's bundled files — engines, rules,
> overrides, and campaign content) and `{{PROJECT_ROOT}}` = `${CLAUDE_PROJECT_DIR}` (the player's
> own working directory, where every `campaign_state/…` play-state file is read and written).
> Whenever any file you read contains a `{{PLUGIN_ROOT}}/…` or `{{PROJECT_ROOT}}/…` path, replace
> the placeholder with the absolute path shown above and read/write that. **Never** resolve these
> against the working directory or a file's own folder, and never write into `{{PLUGIN_ROOT}}`.


# Create NPC — Curse of Aestrum

Thin shell. Loads the rpg-5e engine's character walkthrough with the subject
type set to **NPC**, plus the Curse of Aestrum setting overrides.

**Path resolution.** Every relative path below resolves against the **CoA
project root** (`{{PLUGIN_ROOT}}`), **not** this
skill's own base directory. So `overrides/...` → `CurseOfAestrum\overrides\...`,
and `../rpg-5e-engine/...` reaches the sibling engine repo. If a read 404s,
retry from the project root before assuming the file is missing.

## Subject type

This skill always builds an **NPC**. At STEP 0, treat the subject as a
**companion NPC** by default (one built to travel with the party); use the
override's incidental-NPC framing if the user asks for a one-scene or minor
recurring figure. The engine's PC-only concerns (player ownership,
`identity_known_to_party`) do not apply; the NPC-only concerns (control flag,
secret state, connectability) do.

## Load order

1. **Engine walkthrough.** `Read` `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/create-character/core.md`.
2. **CoA override.** `Read` `{{PLUGIN_ROOT}}/overrides/create-character.md` — apply its spoiler
   discipline, blood-relation list, hook tables, **NPC Output Paths**,
   **Connectable Companions** example, and **writ-seeding cross-reference**.

The engine's `core.md` will direct on-demand reads of:

- `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/random_character_generation.md` (Random source).
- `{{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_progressive.md` (stub / completeness).
- `{{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_connectable.md` (companion personality).
- `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/race_anatomy.md` (STEP 3.5 anatomy pass — runs even
  for a stub).

## Defaults

- **Source / completeness:** NPC default is **random + stub**. State it in one
  line and proceed unless the user redirects ("build her in full", "I'll give
  you the sheet").
- **Control:** ask `control: player|claude` if not implied. Secret state
  (hidden agendas, the Galadiil writ) is only coherent for a `claude`-controlled
  NPC — see the override's writ-seeding cross-reference.

## Output paths

Per the override's **NPC Output Paths** section:

- **Every campaign NPC — companion and incidental alike — is pure overlay.**
  Write a single self-contained sheet to
  `{{PROJECT_ROOT}}/campaign_state/<C>/npcs/saved/<slug>.md`. There is no separate campaign-level
  base file; the self-contained sheet carries the full character and accumulates
  play state below it. (Companion vs. incidental affects authoring richness —
  connectable depth, stub vs. complete — **not** placement.)

`<C>` is the active campaign slug from `{{PROJECT_ROOT}}/campaign_state/.active`. Never write an
NPC into the canonical `npcs/chapter_N/` roster at the project root — that tree
is reserved for authored canon, and a campaign-created NPC (companion included)
is **not** canon.

## Workflow

Follow the engine workflow in `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/create-character/core.md`
(STEP 0 → STEP 4) with subject type = NPC and the CoA override applied. For a
companion, apply `authoring_connectable.md` at the personality stage so the NPC
is reachable. Stubs leave an `## Open Slots — To Develop in Play` section and
`status: stub`; flesh out later per `authoring_progressive.md`.
