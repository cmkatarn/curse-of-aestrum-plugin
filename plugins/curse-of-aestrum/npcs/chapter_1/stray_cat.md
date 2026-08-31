---
id: npc_stray_cat
name: The Stray Cat
race: Beast (Cat)
location_status: roaming
loop_frozen: false
cycle_aware: false
alignment: unaligned
disposition_default: aloof_then_warm
playable: false
control: claude
age: "4–5 years"
loop_memory_notes: "Outside the loop: never Recreated, never memory-wiped. Continuous memory across resets; remembers the party without an amulet. No intellectual grasp of the loop. Unremembered by looped residents, who re-meet it 'for the first time' each day."
governed_by: rules/companion_animals.md
---

## Overview

One of Aestrum's two adoptable animal companions. The behavior layer — no
voice/POV, manifestation, judgment vs. loyalty, the undead reaction,
adoption-lock, death/persistence, and the post-reveal realization beat — is
authoritative in
[rules/companion_animals.md]({{PLUGIN_ROOT}}/rules/companion_animals.md) (no voice/POV,
manifestation, judgment vs. loyalty, the undead reaction, adoption-lock,
death/persistence, separation/reunion at reset, and the post-reveal realization
beat). This sheet carries the cat's **content**: how it looks, how it behaves,
and what it does (which, mechanically, is nothing).

Before adoption it is a single cat-*presence* glimpsed in passing across
Aestrum, never the same coat twice. On adoption its appearance **locks**, it
becomes *the* cat for the rest of the campaign, and no further stray cats
appear.

## Appearance (indeterminate until adopted)

Each encounter shows a different cat until the player adopts one and fixes it.
Draw from a spread when seeding a glimpse; lock whatever was present at the
adoption moment. Examples:

| Encounter feel | Manifestation |
|---|---|
| Alley cat | Lean grey tabby, torn ear, watchful from a height |
| Temple cat | Long-haired white, unhurried, sits where the light is |
| Hearth cat | Round black-and-orange tortoiseshell, slow blink |
| Dock cat | Short-haired ginger tom, scarred nose, fearless |
| Shadow cat | Sleek black, green eyes, there and then not |

Whatever the coat, the manner reads the same: self-possessed, assessing, in no
hurry to be liked. It is four to five years old.

## Behavioral Profile

- **No voice, no POV.** Never spoken for, never the narration anchor. The
  player reads it from posture, ears, tail, proximity, and where it chooses to
  settle — meaning inferred, never stated for it.
- **Accurate judge of character.** Warms slowly toward genuine good will,
  withholds from those who mean the party harm. The read is reliable but
  understated — a cat's verdict is whether it stays in the room.
- **Loyalty by treatment, not morality.** Bonds to whoever treats it as part
  of the party, including a cruel or chaotic-evil master who still feeds and
  shelters it. Abuse or sustained disinterest makes it leave **permanently**;
  no new stray will appear after.
- **Undead instinct.** Bottlebrush tail, flattened ears, and refusal toward
  undead as a category. Over a scene it can come to accept a specific
  undead-natured ally (e.g., a dhampir) it reads as no true threat — typically
  shown by *closing the distance* it first refused.

## What It Can Do

**Nothing, mechanically.** The cat has no utility function — no alert, no
combat role. Its entire value is companionship and its quiet, accurate read of
the people around it. Treat it as an ordinary cat (engine bestiary Cat if a
stat line is ever needed); it is not an encounter participant. Animal death is
permanent (see [death_and_dying.md]({{PLUGIN_ROOT}}/rules/death_and_dying.md)).

## DM Notes

- **Seed in passing only.** A cat watching from a windowsill, gone when looked
  at twice. One beat, then move on. Never push adoption; let the player choose
  to cross the distance.
- **Adoption** locks appearance and stops further cat-manifestations; record
  the adopted instance in the overlay at
  `{{PROJECT_ROOT}}/campaign_state/<C>/npcs/saved/stray_cat.md` per `companion_animals.md`. **The
  overlay slug stays `stray_cat`** (so the loader pairs it with this base
  sheet); the player's chosen name goes in frontmatter (`adopted_name:`) plus an
  adoption event, **not** in the filename. The animal's `home` field (where it
  goes when separated at a reset) is tracked in the same overlay — see
  `companion_animals.md`. Never write the adopted cat into canon.
- **The realization beat** (the cat as a creature left outside the reset,
  unremembered) is post-reveal, once, and belongs to an NPC's voice — see the
  rule file. Do not foreshadow it before the loop is laid bare.
