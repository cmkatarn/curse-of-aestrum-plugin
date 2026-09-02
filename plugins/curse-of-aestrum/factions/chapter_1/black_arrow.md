---
id: faction_black_arrow
name: The Black Arrows
type: criminal_gang
base: Setland
leader: npc_roland_elakian
members: [npc_roland_elakian, pc_theren_elakian, pc_sage]
known_to:
  pc_theren_elakian: [npc_roland_elakian]
  pc_sage: [npc_roland_elakian]
allied_with: [npc_malak_du_leon]
rival: [faction_erethezra]
former_rival: [faction_the_shrikes]
---

## Overview

A criminal gang based in Setland, with past regional reach including Duskwall. Led by patriarch Roland Elakian, who is openly allied with Duke Malak du Leon. Members identify themselves with a tattoo of a black arrowhead, often located on the wrist, and communicate using Thieves' Cant.

Unlike some gangs that kill indiscriminately, the Black Arrows operate more like a family that looks out for its own, focusing on theft and illicit activities rather than wanton murder. They were formerly in a turf war with The Shrikes, which ended approximately ten years ago when The Shrikes collapsed in the Setland region. Erethezra has since emerged as their primary rival.

The Black Arrows and Erethezra have shared territory long enough that each side has learned to read the other's communications — Black-Arrow-trained operatives can recognize Erethezra signal language.

The Elakian family has a standing connection to Charnelhold: contracted use of the torture chambers, providing services to the duchy in exchange for political cover and operational latitude.

## Membership

*`known_to` = the members who know this person belongs. Directed; member-to-member only.*

| Member | Role | `known_to` |
|---|---|---|
| [Roland Elakian]({{PLUGIN_ROOT}}/npcs/chapter_1/remaining_npcs.md) | patriarch | **all** |
| **Roland's wife** — *no sheet yet* | — | **all** |
| [Theren Elakian]({{PLUGIN_ROOT}}/party/theren_elakian.md) | member; contracted hunter on the Galadiil bounty | Roland, Roland's wife |
| [Sage]({{PLUGIN_ROOT}}/party/sage.md) | **former** member — deserted | Roland, Roland's wife |

**The gang is a family that looks out for its own, and the roster is close to literal
about it:** three of the four members are one household.

Roland's wife is a **canon member with no sheet and no name**, which is why she is named
here but held out of `members:` — an id nothing defines would put a hole into the graph
rather than record one. She is not incidental: she is one of only three people who know
which of them carries the Galadiil bounty.

**Only Roland and his wife hold the whole roster.** They know every Black Arrow, past
and present; that is what running a family cartel means. Nobody else on this table sees
past their own row.

**Theren and Sage did not know each other as Black Arrows.** Sage left several years
before the campaign opens and their memberships never overlapped, so neither appears in
the other's `known_to`. This is the clearest case yet for the field being directed: two
members of one gang, in the same duchy, mutually invisible *as members* — and only the
patriarch and his wife can see both of them at once.

Should a former member place a current one from outside the roster — Sage recognizing
Theren by the wrist tattoo, say — that is **deduction from outside the roster**, not
membership knowledge, and it does not enter `known_to`. At campaign start neither knows
the other's Black Arrow history; any recognition a playthrough produces runs one way
(Theren has no idea what Sage was) and lives on that character's `saved/` sheet. This
table holds only what the gang itself knew.

**Sage's row is the one that bites.** She did not drift out; she **deserted**, and there
is a standing bounty on her in Setland she cannot go back to. Roland and his wife know
exactly who she is — which is precisely why the Black Arrow tattoo stays hidden beneath
the thorny vines on her neck. Former membership is still membership, as far as Roland is
concerned.

## DM Notes

- **Roland's posture:** publicly dismissive, privately protective of family. When the political situation pressures him, expect him to disavow members loudly in public while quietly lobbying Quellenna or Malak for softer outcomes — especially where Theren is concerned.
- Roland coordinates openly with Malak and Quellenna as the political situation evolves; his allegiance is visible, his protectiveness of family is not.
- **Family-style ethic:** operatives cover for one another and recognize each other's marks even when concealed.
- **Erethezra signal recognition** is a long-standing capability among Black-Arrow-trained operatives.
- **Galadiil writ distribution — party-NPC seeding.** When a campaign is assembled with two or more random NPC party slots, one of those NPCs is secretly seeded as a current Black Arrows / Erethezra subcontractor holding the Galadiil writ. Spread and betrayal mechanics for that NPC are documented in [overrides/create-party.md § Random-Slot Seeding of the Galadiil Bounty]({{PLUGIN_ROOT}}/overrides/create-party.md#random-slot-seeding-of-the-galadiil-bounty).

## Post-Loop Arc — Galadiil Bounty Cancellation

*Applies if the loop breaks, Aidra brings Galadiil to Charnelhold alive, and the sisters' conversation runs as designed (see [npcs/chapter_1/galadiil_ilphekiir.md], [npcs/chapter_1/quellenna_ilphekiir.md], [npcs/chapter_1/aidra_calemthor.md]).*

**The cancellation.** Quellenna routes a revocation of the Galadiil bounty back through her original Charnelhold contact. The Black Arrows treat the cancellation as a courtesy to the principal — Quellenna placed the contract, Quellenna can pull it. No fee dispute, no debate. The kill order goes cold.

**Downstream — Theren's contract.** The contract Theren is carrying ceases to be a valid kill order the moment the cancellation propagates through the chain (Charnelhold contact → Roland → Theren). The ring is no longer a working death warrant. Anyone still holding the bounty as live (e.g., a Theren who has not yet received word, or a downstream actor he subcontracted) is operating on a defunct contract and would not be paid out.

**Roland's posture on cancellation.** Quietly relieved. The bounty was always a complication — a contract he could not openly refuse and whose author he had privately identified but that put his son in unmanageable proximity to Aestrum's loop (which Roland does not know about, but he does know his son has not come home). Cancellation gives him the space to bring Theren back without losing face with Quellenna. If Theren is still alive and reachable at this point, Roland would move to retrieve him. He still does not know Theren has been trapped in the loop.

**Communication delays.** Cancellation propagation depends on whether the loop has broken (Roland → Theren message can finally cross the border) and whether Theren has been physically extracted. If Theren is alive but the message has not yet reached him, he may continue acting on a contract that no longer pays.

**Party knowledge:** The party can learn the bounty has gone cold by pulling on the existing Black Arrows thread (Belmita's overheard "Black Arrows / special assistance" reference, the Mieke mercenary-group source, or Theren himself if he learns). The cancellation itself is not advertised; it surfaces when someone goes looking.
