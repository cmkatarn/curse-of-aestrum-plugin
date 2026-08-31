---
id: rule_information_disclosure
name: Information Disclosure — 5e Layer
type: homebrew_rule
related_rules: [rule_combat, rule_social_checks, rule_searches_and_loot]
---

## Overview

The D&D 5e mechanical layer over Aria's neutral
[information_disclosure.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/information_disclosure.md),
which owns the genre-agnostic core: what a scene volunteers on the character's
behalf, concealed detail, the load-bearing-clue failsafe, scene-density
*rendering*, sensory channels, character knowledge, social-cue scaffolding,
in-character recall, and tells.

**Read Aria's file first.** This file adds only the 5e mechanics: passive-check
resolution, the player **mode** disposition that the density preference maps onto
(and that other 5e rules consult), the display-vs-resolution rule, and how
numeric readouts surface.

---

## Passive Checks Auto-Apply

When a PC enters a new scene or a situation changes, the DM checks each PC's
**passive Perception** and **passive Insight** against the relevant DCs and
volunteers what those scores would catch — without being asked. Active rolls are
only called for when:

- A player declares a focused search ("I check the desk drawers"), or
- The detail is genuinely concealed and beyond passive reach (a hidden
  compartment, a long con).

This is the 5e resolution of Aria's *What the Scene Notices* — a competent
adventurer notices what their passives would catch; forcing players to chant
"can I roll Perception?" at every doorway is a text-medium failure mode.

---

## Plot-Critical Failsafe — 5e Resolution

Aria owns the neutral failsafe (a load-bearing clue is never gated by a single
missed moment; a second opportunity is engineered; in extremis an ally
volunteers it). In 5e terms, the automatic surface is concrete: **a load-bearing
clue clears on the highest passive Perception/Insight in the party.** The dice
gate the *dramatic* stuff — the bonus detail, the early warning, the edge — never
the load-bearing stuff.

---

## Scene Density — Novel vs. Game Modes

The neutral density *rendering* (continuous prose vs. a scannable **You notice:**
list) lives in Aria. In this stack the choice is carried by a named **player-level
mode** — the disposition multiple 5e rules consult, not just this one.

- **Novel mode** ≡ Aria's *Continuous Prose* rendering.
- **Game mode** ≡ Aria's *Scannable List* rendering.

The mode is the most visible in scene density, but the same disposition also
controls how secret rolls are surfaced (see
[private_information.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/private_information.md#secret-rolls--tied-to-player-mode))
and how mechanics are displayed (below). Picking a mode is a single choice that
shapes the whole texture of play for that player. When the active party has
players on different modes, render to the **party default** set in preferences; a
player on the non-default mode may request a re-render or supplement in their
preferred mode on demand, without penalty.

---

## Party Preferences

Display preferences live in the game's party-preferences file (path defined by
the override). The DM consults this file at the start of any scene-framing beat.
The fields:

- **`narrationDisplay`**: `Novelization` or `Game`. The Novel/Game mode above
  (Novelization ≡ Novel mode, Game ≡ Game mode). Governs scene-rendering density
  and how mechanics are surfaced.
- **`dice_display`**: boolean. Whether the numeric mechanics-readout is shown.
  **Defaults to `narrationDisplay != Novelization`** (i.e. `false` under
  Novelization, `true` under Game), and may be overridden independently
  thereafter.

A consuming game may set these **per-player** (party default + per-player
overrides, with the mixed-mode handling above) or as a single **campaign-level**
value. *Curse of Aestrum uses the campaign-level form* — one `narrationDisplay` /
`dice_display` pair for the whole party.

**Lifecycle.** Both are mutable at any time but **locked within a scene**: read at
scene start, held to scene end. A change takes effect on the next scene after the
current one is closed (and context cleared) — the same lifecycle as a
narration-mode change.

When in doubt about a setting, use the party/campaign default rather than the
most recent override.

### Display, not resolution

These settings govern how mechanics are **displayed** — never **whether** they
resolve. **Checks with real stakes are always rolled** (the character's sheet
modifier governs the outcome; see [social_checks.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/social_checks.md));
`dice_display` only toggles whether the numeric readout is shown. Hiding the dice
never means skipping them — a low-stat character still fails what a high-stat one
passes; you just read it as prose rather than as `d20 … vs DC …`. The dice bite
in both modes.

---

## Insight Tells — 5e Variant

Aria's *Tells* rule (describe the observable signal, not the conclusion) is the
neutral core. In 5e terms, the trigger is a **passive Insight** (or a successful
active Insight) revealing that an NPC is lying, nervous, or playing a part. This
matches the *signal not stat* principle in [combat.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/combat.md). If a player
explicitly asks "do I think he's lying?" after the tell, the DM may then confirm
or shade the read based on what the Insight result actually was.

---

## Hard Limits — 5e Additions

These extend Aria's Hard Limits (failsafe doesn't override knowledge boundaries;
free IC recall doesn't rewrite facts):

- **Auto-applied passives still respect cover, darkness, distraction, and
  setting-specific impairments** (the override may add categories such as
  antimagic zones, perception-suppressing weather, magical fog). Passive
  Perception drops in unfavorable conditions exactly as RAW; the rule is
  "auto-apply," not "auto-succeed."
