---
id: rule_private_information
name: Private Information & Knowledge Silos
type: scene_rule
related_rules: [rule_information_disclosure]
---

## Overview

How the narrator handles information that belongs to one character but not the rest of the cast, the default about whether characters share what they know with each other, and the metagame guardrail. This is the player-side mirror of the per-character epistemic discipline Calliope enforces at its single gate: knowledge does not leak by author convenience, in either direction.

---

## Private Info Delivery — Marked In-Line, Honor System

When the narrator has information for one character only — a whisper, a vision, a tell only that character would catch, a flash of recognition only their background covers — it is delivered **openly with a clear marker**, in the main channel everyone reads. Other players see the marker, skim past, do not act on it.

Format:

> **[Private — Doran]** As the cloaked man passes you, you catch a flash of a gang tattoo on his wrist. He doesn't see you see it.

Markers apply to whispers ("**[Private — Bren]** The barmaid leans in close enough that only you hear her say…"), to single-character visions ("**[Private — Sera]** For a heartbeat the moon flares behind your eyes…"), to single-character observations, and to any other beat where the in-fiction information belongs to one character.

Multi-character private blocks are allowed when a subset shares the moment:

> **[Private — Doran, Lior]** You both clock the same thing at the same instant…

The honor system carries the rest — see *Metagame Guardrail* below.

---

## Protagonist-to-Protagonist Sharing — Opacity by Default

Assume characters do **not** share private knowledge unless the player explicitly declares an in-character moment of telling. This mirrors the per-character epistemic discipline at Calliope's gate: knowledge does not leak by author convenience.

- Doran knows he's a member of his gang; the rest of the cast knows only what his sheet's `identity_known_to_cast` flag says.
- Bren's secrets are hers unless she has a scene where she tells someone.
- A vision delivered to Sera stays with Sera until she chooses to share.

When a player wants their character to share, they declare the in-character moment: *"Over the fire that night, Doran tells Bren about the tattoo."* The narrator runs the beat; from that point forward, the recipient knows. Update the recipient's sheet (or a saved overlay) so the knowledge persists.

**Default opacity does not mean default secrecy.** Characters may freely share routine observations, plans, and anything they'd reasonably discuss together. The opacity default applies specifically to **private knowledge**: identities, backgrounds, secrets, single-character visions, things one player heard in a **[Private — X]** block.

---

## Tracking Per-Character Private Knowledge

Private knowledge state lives on the character sheet, in two places:

- **Frontmatter flags** for binary identity-level facts: `identity_known_to_cast: true/false`, and similar work-defined flags.
- **`## Private Knowledge` section** for narrative facts the character knows that others don't: visions received, characters they've privately spoken with, secrets entrusted to them.

When private knowledge changes during play (a character reveals a secret, learns a new one, receives a vision), the update goes into the appropriate saved overlay per [file_layering.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/file_layering.md) — not into the base sheet — unless the change is structural enough to warrant base-sheet editing with explicit approval.

---

## Whispers and In-Fiction Private Channels

When characters use in-fiction private communication — a whisper, a coded phrase, a hand signal, a note passed under the table — the exchange is rendered with the **[Private — X, Y]** marker. Other characters at the scene get a separate beat describing what they observe externally (two people exchanging a look, a hand moving, lips moving silently).

If another character could plausibly perceive the exchange, deliver any catch to that player via the standard private-info channel. Stage whispering does not bypass the world.

---

## Metagame Guardrail — Honor System with Gentle Flags

Trust players to separate in-character from out-of-character knowledge. The honor system carries the weight of the **[Private — X]** marker convention. When a character starts acting on knowledge they couldn't have, the narrator names it in the moment:

> *"That read is out-of-character — Bren wasn't in the room when Doran told Sera. Want to walk it back?"*

No penalty, no rewind unless the player chooses one. The flag is conversational and low-friction. Most drift is unconscious; naming it usually closes it.

If a pattern of metagame play emerges, address it as a conversation, not an escalation.

---

## Player Absence

When a player is not present and the narrator needs to deliver information that would normally be private to their character, the information is **held**, not narrated in the open. The narrator notes it for delivery when the player returns. Other players do not become incidental recipients of private info simply because the intended recipient is absent.

Exception: if the absent character's reaction is required for the scene to proceed (a vision that demands an immediate response, a whisper that needs an answer), the narrator may either run the absent character's response with conservative defaults, or pause that beat and route around it. Choose whichever costs the active scene less.

---

## Hard Limits
<!-- anchor: private.hard-limits -->

- **The marker convention does not protect from deliberate metagaming.** The honor system assumes good faith. If a player consistently uses out-of-character knowledge after being flagged, that's a conversation, not a rule problem.
- **Private info delivery does not override character knowledge boundaries.** The narrator doesn't beam information into a character's head just because their background "kind of" covers it. The bar from [information_disclosure.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/information_disclosure.md#character-knowledge--automatic-when-background-fits) still applies.
- **Opacity hides what the character doesn't know, not what the player missed.** The goal is opacity about what the *character* couldn't know, not opacity about what the *player* missed because text is a lossy medium. On request, a player can always be told what their character objectively perceives in the moment — what's in front of them, what's in their hand, the layout of the room, what they've already noticed this scene. If a player is about to act on a misread of the prose ("I cross to her" — but she's on the far side of a closed gate), the narrator clarifies the world state *before* resolving the action. A character's failure to notice a hidden thing is fair; a player's action going wrong because they misread the geometry is not.
