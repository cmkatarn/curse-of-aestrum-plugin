---
id: rule_campaign_lifecycle
name: Campaign Lifecycle — RPG Overlay
type: homebrew_rule
related_rules: [rule_scene_framing, rule_file_layering]
---

## Overview

The RPG-vocabulary overlay on Aria's neutral
[story_lifecycle.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/story_lifecycle.md), which owns the
lifecycle mechanics: it supplies the multi-scene **work** container and maps
Resume / Switch / Save-Close onto Calliope's generic scene-lifecycle operations
(`scene_lifecycle.md`). **Read Aria's file first.** This file does not
reimplement those mechanics — it renames the concepts into TTRPG terms, supplies
the RPG command synonyms, and adds the RPG-specific hidden-state caution.

**Vocabulary mapping** (RPG term ≡ Aria's neutral term):

- **campaign** ≡ work — the multi-scene container grouping a party, a saved-state
  set, and a running timeline.
- **party** ≡ cast roster.
- **PC / player character** ≡ protagonist / viewpoint character (the resume POV).
- **"Save campaign state?"** ≡ the close prompt's player-facing wording.

A consuming game's thin-shell `SKILL.md` loads Aria's `story_lifecycle.md`
alongside this overlay and the Calliope scene layers; the game's override
supplies the concrete bindings (the active-set indicator path, the party roster
location, the time-anchor system).

---

## Command Synonyms — RPG Vocabulary

The lifecycle operations are Aria's; these are the player-facing phrases that
trigger them in a campaign context.

- **Resume** (→ Aria's *Resume*): "resume campaign", "continue the campaign",
  "resume the game", "continue the game", "load my game", "pick the campaign back
  up", or simply "resume" in a campaign context.
- **Switch** (→ Aria's *Switch*): "switch to campaign `<id>`", "load the `<id>`
  campaign", "change to campaign `<id>`", "play the `<id>` campaign".
- **Save / Close** (→ Aria's *Save / Close*): the RPG layer adds nothing
  structural; the override re-supplies the wording so the close prompt reads
  "Save campaign state?" instead of the generic "Save scene state?".

---

## RPG Hidden-State Caution

The campaign refresher is the place **RPG hidden state** most easily leaks —
companion secrets, DM-only bounties, unrevealed identities, a claude-controlled
NPC's concealed agenda. Aria's gated-refresher rule already forbids surfacing
what the protagonist does not know; this is the TTRPG-specific reminder of *what*
that hidden state tends to be. The refresher carries only what the PC has
observed, plus the override's allowed OOC orientation (character level and
mechanics, the time anchor for bearings, the content rating). It never names
another character's hidden state, and never surfaces a fact the PC does not know
— not even by negation ("you don't know X").
