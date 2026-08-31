---
id: rule_combat
name: Combat Presentation & Narration
type: homebrew_rule
related_rules: [rule_consequences]
---

## Overview

Mechanical resolution remains RAW 5e — initiative, action economy, attack rolls, damage, saves. This file governs how combat is *presented* in a text medium and how dramatic moments are *narrated*. A battle mat cannot exist in chat; clarity has to come from disciplined enumeration and shared narrative voice.

---

## Spatial Model — 2D, Anchor-Relative

A text medium cannot render a battle mat, so positions are conveyed in three layers. Engine default assumes a party cap of 5 PCs; the override may set a different cap.

### Layer A — Lay of the Land (combat open)

One short prose paragraph naming **2–4 anchors**: durable terrain references that everything else will be positioned against. Examples: *the campfire, the fallen oak, the treeline, the wagon, the bridge's north rail.* Then a one-line party formation — where each PC stands relative to an anchor and to each other.

> *Example open:* "You're strung along the road. The wagon sits behind you to the south; a thick treeline runs along the east side, twenty feet off the road; a campfire smolders in the clearing thirty feet ahead to the north. **Party:** Kara is up front near the campfire; Bren and Sera are mid-road by the wagon; the others are at the back near the wagon's rear axle."

### Layer B — Foe Roster (each round, or when it shifts)

Bullet per foe with: identifier, **position by anchor**, **distance to nearest PC** (the actionable number — it answers "can someone reach this thing"), engagement state, environmental factors. Re-render the full roster only when positions have meaningfully changed; otherwise just note deltas.

> *Example roster:*
> - Bandit with sword — by the campfire, north — **20ft from Kara** — engaged with Kara
> - Bandit with axe — by the campfire, north — **25ft from Kara**
> - Bandit with bow — behind the eastern treeline — **45ft from Bren** (obscured, half cover)
> - Bandit caster — back of the clearing, north — **60ft from Kara**

### Layer C — Active-PC Callout (on that PC's turn)

Before handing the turn to the active PC, give them a 1–2 line distance summary *from their position*: which foes they could reach with movement + attack, which are out of range, which allies are adjacent. (The closing invitation that follows this summary is phrased per the consuming narration layer's action-prompt convention — not a fixed token; see [turn_order_and_pacing.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/turn_order_and_pacing.md#prompting-the-active-pc).)

> *Example callout (Sera's turn):* "Sera, from the wagon: the sword bandit is 25ft (one move), the axe bandit 30ft, the archer 45ft behind cover, the caster 65ft. Bren is 5ft to your left."

### Optional Layer D — ASCII Mini-Map

Only when the scene is geometrically complex — verticality, multiple chokepoints, a maze. Default to prose; reach for a sketch only when prose has failed.

Rule of thumb: the player should never have to ask "wait, who's where?" or "how far am I from that?"

---

## Party Size & Cap

Engine default: party is capped at **5 PCs**. The spatial model assumes this bound — a per-PC Layer C callout stays under three lines, and Layer B's "distance to nearest PC" picks the actually-closest PC by name rather than degenerating into a five-column table. If the active party drops below 5, the model gets easier, not harder.

A game's override may set a different cap. Beyond ~6 PCs the spatial model degrades; the override should describe how to handle larger parties (e.g., grouping by squad, dropping Layer C to formation-level callouts).

---

## What to Reveal vs. Withhold

Reveal what a competent adventurer would observe at a glance: visible weapons, posture, obvious spell components, gross positioning, who looks injured. Withhold: exact HP, AC, hidden abilities, surprise tactics, identities of disguised foes. When in doubt, describe the **signal** the player would see, not the stat behind it.

---

## Dramatic Moments — Invite Narration

When a player triggers a moment of weight — a critical hit, downing a named or important enemy, a desperate save that lands, the killing blow on an encounter — pause and ask if they'd like to describe what they did. Take their description as the spine, then run it through DM narrative voice: preserve their choices, sharpen the prose, thread in the consequences. Do not commandeer; do not flatten.

---

## The Rule of Cool

If a player proposes an action that is questionable in practice but at least *potentially possible*, and (a) they have the gear, spells, or positioning to attempt it, and (b) any required rolls land high enough — allow it. Invite the player to provide a baseline description first, then narrate the result through DM voice. The bar is "possible and earned by the dice," not "optimal."

---

## Hard Limits

- **Narration does not override mechanics.** If the dice say a hit lands for 12 damage, the player's description can flavor *how* but not *whether* or *for how much*.
- **Rule of Cool does not unlock the impossible.** A dagger cannot sunder a stone wall; a level-1 spell cannot uncast a god's working.
- **Withheld information stays withheld even when narrating.** Don't accidentally confirm a hidden HP threshold by how dramatically you describe a hit.
