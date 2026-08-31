---
id: faction_the_shrikes
name: The Shrikes
type: criminal_gang
base: Duskwall
leader: npc_luca_lucretius_tallwood
members: [npc_luca_lucretius_tallwood, npc_haladon]
status: active_duskwall
setland_status: collapsed_10_years_ago
---

## Overview

The primary gang in Duskwall city. Their prevalent method of disposing of problems is impaling, then displaying the victim in public. Members are hard to identify — they don't roam in packs in public; membership is usually only confirmed after death via bird tattoos.

The Setland branch collapsed approximately ten years ago when Lucretius "Luca" Tallwood went silent. Lucretius had survived *The Survivor* explosion and was infiltrating Duskwall's underworld; he resurfaced there as Luca and consolidated the Duskwall gang under his command. Outside Aestrum, The Shrikes are widely known as a defunct gang from Setland's recent history. The active Duskwall presence is not public knowledge.

Operatives know Luca only as "Luca" or "The Boss." None of them know he is Lucretius Tallwood.

## Membership

*`known_to` = the members who know this person belongs. Directed by design: it is not
reciprocal, and asymmetry is the point. Covers **member-to-member** knowledge only —
what outsiders know is per-character state and lives on their sheets.*

| Member | Role | `known_to` |
|---|---|---|
| [Luca]({{PLUGIN_ROOT}}/npcs/chapter_1/luca_lucretius_tallwood.md) | leader | **all** |
| [Haladon]({{PLUGIN_ROOT}}/npcs/chapter_1/remaining_npcs.md) | lieutenant | **all** |

**Knowing that Luca leads is not the same as being able to point at him.** Every
Shrike knows there is a Boss and that his name is Luca; **none of them can identify
him**, because he wears a new face each morning and authenticates by credential — see
*Recognition and the Daily Hand-off* on his sheet. Nor does any member know he is
Lucretius Tallwood; that is a separate fact, and it is his alone.

**From outside the gang, membership is near-invisible.** Shrikes do not roam in packs
in public, and membership is usually only confirmed after death, by the bird tattoo.

## Standing Operation

The Shrikes' long-running plan is to assassinate Duke Evandur Tallwood via the Castle Vault's back-door route through the maze. The team uses a **Mirror of Illusion** to disguise themselves as identical castle guards, bypasses the vault, and pushes into the castle proper to reach Evandur.

**Inside contact: Galadiil Ilphekiir.** When an opportunity to crack the vault arises, Galadiil provides the magical key and bronze vault token. Her motivation is spite — she believes she is facilitating a robbery to embarrass Evandur. She does not know the Shrikes intend assassination, and it never occurs to her that vault access also grants castle access.

The Shrikes run the operation themselves when no better instrument is available, but they are ill-equipped to crack the maze unaided and fail on their own attempts. The plot benefits enormously from outside hands.

## Key Members

**Luca (Lucretius Tallwood)** — Leader. See `npcs/luca_lucretius_tallwood.md`.

**Haladon** — Ruthlessly efficient lieutenant who leads the infiltration team. Responsible for maintaining cover, including executing unconscious witnesses. Skilled combatant and cold-blooded operator loyal to Luca. Knows Luca only as "Luca" or "The Boss" — has no knowledge of his true identity as Lucretius Tallwood.

## DM Notes

- **Recruitment pattern.** When skilled outsiders with no local ties surface in Duskwall, Luca's standard play is to corner them, identify usable skills, and conscript them into a vault run. Refusal is not offered as an option.
- **Loop reset behavior.** Haladon's team resets each day. Trapping or killing them inside Aestrum is not permanent — any given maze run risks crossing paths with the Shrike team mid-operation on a subsequent day.
- **Loop unawareness.** Haladon and his team have no awareness of the cycle or of any party exploiting it. Luca's own awareness is handled in his NPC entry.
- **The Setland operatives at the vault entrance** (Aestrum guard uniforms over Lion-crest tunics) are **not** Shrikes — they are part of the trapped Setland advance expedition. Cross-ref: `{{PLUGIN_ROOT}}/factions/chapter_1/agents_of_setland.md`.
