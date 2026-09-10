---
name: mechanics
description: >
  Use this skill when the user invokes /mechanics, or asks to "load mechanics",
  "reset mechanics context", or "load a fresh mechanics context". This skill
  loads the core Aestrum campaign mechanics — how the cycle works and how to
  break it — so they are authoritative in the current session. Designed to be
  run after /clear to eliminate stale context before making campaign changes.
allowed-tools: [Read]
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


# Mechanics Context Load — Curse of Aestrum

Disregard any prior conversational assumptions about Aestrum mechanics. The file
read below is authoritative. Answer only from what is loaded here.

**Path resolution.** The path below resolves against the **CoA project root**
(`{{PLUGIN_ROOT}}`), **not** this skill's own base
directory. If the read 404s, retry from the project root before assuming the
file is missing.

## Step 1 — Read the mechanics file

Read this file now:

- `{{PLUGIN_ROOT}}/lore/key_lore_summary.md`

## Step 2 — Confirm

Once the file is read, reply with a single line:

> Mechanics loaded — cycle rules and break conditions are in context. Ready.
