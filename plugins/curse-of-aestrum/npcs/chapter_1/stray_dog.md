---
id: npc_stray_dog
name: The Stray Dog
race: Beast (Dog)
location_status: roaming
loop_frozen: false
cycle_aware: false
alignment: unaligned
disposition_default: wary_then_warm
playable: false
control: claude
age: "4–5 years"
loop_memory_notes: "Outside the loop: never Recreated, never memory-wiped. Continuous memory across resets; remembers the party without an amulet. No intellectual grasp of the loop. Unremembered by looped residents, who re-meet it 'for the first time' each day."
governed_by: rules/companion_animals.md
---

## Overview

One of Aestrum's two adoptable animal companions. The behavior layer — no
voice/POV, manifestation, the danger-alert, judgment vs. loyalty, the undead
reaction, adoption-lock, death/persistence, separation/reunion at reset, and
the post-reveal realization beat — is authoritative in
[rules/companion_animals.md]({{PLUGIN_ROOT}}/rules/companion_animals.md). This sheet
carries the dog's **content**: how it looks, how it behaves, and what it can
do.

Before adoption it is a single dog-*presence* glimpsed in passing across
Aestrum, never the same breed twice. On adoption its appearance **locks**, it
becomes *the* dog for the rest of the campaign, and no further stray dogs
appear.

## Appearance (indeterminate until adopted)

Each encounter shows a different dog — a different breed, size, and coat —
until the player adopts one and fixes it. Draw from a spread when seeding a
glimpse; lock whatever was present at the adoption moment. Examples:

| Encounter feel | Manifestation |
|---|---|
| Working-town dog | Wiry shepherd mix, dust-grey, one ear that won't stand up |
| Dockside dog | Short-haired tan mongrel, ribs showing, fast on its feet |
| Hearth dog | Heavy-coated black-and-white, broad chest, calm eyes |
| Lean stray | Rangy brindle hound, long legs, a notch out of one ear |
| Small scrappy | Terrier-ish, rough white coat, far too much opinion for its size |

Whatever the body, the eyes read the same: attentive, weighing, present. It is
four to five years old — past puppyhood, not yet slowing.

## Behavioral Profile

- **No voice, no POV.** It is never spoken for and never the narration anchor.
  The player sees posture, ears, hackles, where it sits — and reads meaning
  from that, as from an Insight tell.
- **Accurate judge of character.** Eases toward people of genuine good will,
  holds wariness toward those who mean the party harm. This read is reliable;
  it is *not* the same as loyalty (see below).
- **Danger-alert.** Growls or barks when someone approaching the party carries
  present hostile intent toward them. The alert answers only *does this person
  intend us harm right now* — not identity, not secrets, not past deeds, and
  not mere dislike. See the bounding rules in `companion_animals.md`.
- **Loyalty by treatment, not morality.** Bonds to whoever treats it as part
  of the party — including a cruel or chaotic-evil master who still feeds and
  shelters it. Abuse or sustained neglect makes it leave **permanently**; no
  new stray will appear after.
- **Undead instinct.** Hackles, growl, and refusal toward undead as a
  category. Over a scene it can learn to accept a specific undead-natured ally
  (e.g., a dhampir) it reads as no true threat, settling toward that
  individual while keeping the instinct toward others.

## What It Can Do

*Ordinary beast — a dog, not a war-trained mastiff.* Its mechanical value is
the **danger-alert** above; otherwise treat it as a standard dog (a Mastiff or
smaller per the engine bestiary if a stat line is ever needed). It is not a
combatant and should not be built into encounters as one. If a player sends it
into danger, normal animal mortality applies — and animal death is permanent
(see [death_and_dying.md]({{PLUGIN_ROOT}}/rules/death_and_dying.md)).

## DM Notes

- **Seed in passing only.** A dog trotting along the far side of a market,
  gone before anyone calls. One beat, then move on. Never push adoption; let
  the player be the one to cross the distance.
- **Adoption** locks appearance and stops further dog-manifestations; record
  the adopted instance in the overlay at
  `{{PROJECT_ROOT}}/campaign_state/<C>/npcs/saved/stray_dog.md` per `companion_animals.md`. **The
  overlay slug stays `stray_dog`** (so the loader pairs it with this base
  sheet); the player's chosen name goes in frontmatter (`adopted_name:`) plus an
  adoption event, **not** in the filename. The animal's `home` field (where it
  goes when separated at a reset) is tracked in the same overlay — see
  `companion_animals.md`. Never write the adopted dog into canon.
- **The realization beat** (the dog as a creature left outside the reset,
  unremembered) is post-reveal, once, and belongs to an NPC's voice — see the
  rule file. Do not foreshadow it before the loop is laid bare.
