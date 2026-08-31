---
id: rule_private_information
name: Private Information & Knowledge Silos — 5e Layer
type: homebrew_rule
related_rules: [rule_information_disclosure, rule_social_checks]
---

## Overview

The D&D 5e mechanical layer over Aria's neutral
[private_information.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/private_information.md), which
owns the genre-agnostic core: in-line **[Private — X]** delivery, opacity-by-
default sharing between characters, per-character private-knowledge tracking,
in-fiction private channels, the metagame guardrail, and player absence.

**Read Aria's file first.** This file adds only the 5e dice mechanics — how
secret rolls are conducted and surfaced — and the dice-opacity hard limit.

---

## Secret Rolls — Tied to Player Mode

How rolls are displayed depends on the affected player's mode (see
[information_disclosure.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/information_disclosure.md#scene-density--novel-vs-game-modes)
and the game's party-preferences file). The Novel/Game modes are a player-level
disposition consulted by every rule that has to choose between mechanical
transparency and narrative opacity.

### DM-Side Rolls (NPC Stealth, Deception, traps, hidden DCs)

For rolls that resolve behind the screen — an NPC sneaking, lying, hiding a trap
— the DM rolls in secret regardless of mode. What changes is how the result is
delivered to each affected PC:

| Mode | What the player sees |
|------|----------------------|
| **Novel** | Narrated outcome only. "He meets your gaze evenly and says…" No indication a roll occurred, no indication of success/failure beyond the in-fiction signal. |
| **Game** | Narrated outcome plus a brief mechanical line. "He meets your gaze evenly and says… *(opposed Deception 18 vs. your passive Insight 14 — he reads as honest)*." Player sees the dice math. |

### Player-Rolled Checks (PC attacks, saves, skill checks)

Players always roll their own dice. Mode controls whether the DC and modifier
interpretation are shown:

| Mode | What the player sees |
|------|----------------------|
| **Novel** | Player rolls and reports the d20 + modifier. DM narrates the outcome without naming the DC. Whether they cleared by 1 or by 10 is felt through narration, not stated. |
| **Game** | Player rolls; DM names the DC and confirms result. Standard table feel. |

### Mixed-Mode Resolution

When a check involves players on different modes (Doran on Game tries to Stealth
past Lior on Novel), each player is shown the result according to **their own
mode** — not the roller's, not the observer's. Doran sees the dice; Lior sees
only what her PC observes.

---

## Hard Limits — 5e Additions

These extend Aria's Hard Limits (the marker convention assumes good faith;
delivery doesn't override knowledge boundaries; opacity hides what the *character*
doesn't know, not what the *player* missed):

- **Mode preferences opacify the dice, not the world.** Novel mode hides the
  *math* — DCs, modifiers, roll results, mechanical breakdowns. It does not hide
  things the PC objectively knows. On request, a player in any mode can be told:
  their current HP and conditions, distance to a visible foe, what their PC has
  already successfully observed this scene, what gear is in their hand. If a
  player is about to make a tactical declaration based on a misread of the prose
  ("I charge the orc" — but the orc is 60ft away, not 20ft), the DM clarifies the
  world state *before* resolving the action. Failed Perception on a hidden trap
  killing the PC is fair; the same death because the player misread the room
  geometry is not.
