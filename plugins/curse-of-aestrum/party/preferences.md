---
id: party_preferences
name: Campaign Display Preferences
type: config
related_rules: [rule_information_disclosure]
---

## Overview

Campaign-level display preferences, consulted by the DM at scene start (and at any point where the rules choose between mechanical transparency and narrative opacity). Governed by [rule_information_disclosure]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/information_disclosure.md) (scene density, the Novel/Game disposition, and the display-vs-resolution split) and [rule_private_information]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/private_information.md) (secret rolls, hidden DCs).

Curse of Aestrum uses the **campaign-level** form of these settings — one pair for the whole party, not per-player. This file holds the **canonical defaults**; a playthrough's live values overlay it at `{{PROJECT_ROOT}}/campaign_state/<C>/preferences.md` (Engine → Campaign → **Instance**; the instance value wins). See [overrides/scene.md]({{PLUGIN_ROOT}}/overrides/scene.md) for how the values are read and locked per scene.

---

## Settings (canonical defaults)

- **`narrationDisplay`**: `Novelization`
  The Novel/Game rendering disposition. `Novelization` = continuous prose; `Game` = an atmospheric line plus a `You notice:` bullet list and mechanical readouts. (See `information_disclosure.md`.)
- **`dice_display`**: `false`
  Whether the numeric mechanics-readout (`*[… check — d20 … vs DC … → …]*`) is shown. Default derives from `narrationDisplay != Novelization` (so `false` under the default Novelization), overridable independently. **Dice are always rolled regardless** — this toggles display only, never resolution.

Both default to the Novelization preset and are mutable at any time; a change applies on the **next scene** after the current one is closed and context cleared (locked within a scene).

---

## Other Preferences

Reserved for future expansion (e.g. content-rating preferences, combat-callout verbosity, recap frequency). Add new sections here as rules grow.
