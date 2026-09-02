---
id: faction_shar
name: Shar
type: divine_faction
members: [npc_hati_heldrivver, npc_judith_asemyeer, npc_rowan_deckard, npc_quellenna_ilphekiir, npc_councive_drethnal, npc_dorvael_dunwick, npc_bertram_holst, npc_tarwick_grale]
known_to:
  npc_hati_heldrivver: [npc_judith_asemyeer, npc_rowan_deckard]
  npc_judith_asemyeer: [npc_hati_heldrivver]
  npc_rowan_deckard: [npc_hati_heldrivver]
  npc_quellenna_ilphekiir: []
  npc_councive_drethnal: []
  npc_dorvael_dunwick: []
  npc_bertram_holst: []
  npc_tarwick_grale: []
operates_through: secret_cells
---

## Manifestation

Shar does not appear in humanoid form. In the Antechamber, she is a purple disc of light on the singular flat wall — watching, unmoving. She communicates by thundering words directly inside each subject's skull, with silence as the only reprieve between words. She exercises violence with surgical precision when she chooses to demonstrate capability. She does not rage. She demonstrates. See `{{PLUGIN_ROOT}}/locations/chapter_1/antechamber_of_shar.md` for the full Antechamber description.

## Overview

The goddess of darkness, pain, and loss — known as the evil twin sister of Selûne. Her followers operate as secret cultists rather than public worshippers. She does not establish overt temples; her devotees are merchants, servants, guards, and minor nobles embedded invisibly in society.

Evidence of her influence in Aestrum: the desecrated Shrine of Selûne in Duskwall, the bedroom ceiling of Rowan Deckard's estate, the repeated murders of Miri Amblecrown. She is the primary divine antagonist of the campaign. **Her truest domain is not darkness — it is the unknown.**

## Membership

*`known_to` = the members who know this person serves Shar. Directed by design — not
reciprocal. **Member-to-member only:** what the party or any outsider has learned is
per-character state on their own sheets and in run overlays, not here.*

| Member | Role | `known_to` |
|---|---|---|
| [Hati Heldrivver]({{PLUGIN_ROOT}}/npcs/chapter_1/hati_heldrivver.md) | instrument | `npc_judith_asemyeer`, `npc_rowan_deckard` |
| [Judith Asemyeer]({{PLUGIN_ROOT}}/npcs/chapter_1/judith_asemyeer.md) | adherent | `npc_hati_heldrivver` |
| [Rowan Deckard]({{PLUGIN_ROOT}}/npcs/chapter_1/rowan_deckard.md) | adherent | `npc_hati_heldrivver` |
| [Quellenna Ilphekiir]({{PLUGIN_ROOT}}/npcs/chapter_1/quellenna_ilphekiir.md) | instrument | — |
| Councive Drethnal | instrument | — |
| Dorvael Dunwick | instrument | — |
| Bertram Holst | instrument | — |
| Tarwick Grale | piece | — |

**Roles.** *Instrument* — knowingly acts for Shar. *Adherent* — a devotee she draws on.
*Piece* — moved without knowing whose hand is on them; Tarwick does not know he serves
her at all.

**The compartmentalization is the shape of the table, not a note about it.** Hati has
handled Judith and Rowan directly and so knows them; beyond that she knows only that
Shar has plans in motion elsewhere, and could not name one. Judith and Rowan have never
met and do not know of each other — Judith opens the Gate for the castle assault
without knowing she assists a Setland operation, and Rowan prays at a shrine whose
statue Hati took from him. The four blank rows are the point: **nobody inside the cell
can expose them, because nobody inside the cell knows they exist.**

This replaces the former `known_instruments` / `known_adherents` / `known_pieces`
fields, which used "known" to mean *role*, not *who knows*. Role is now `role`, and
knowledge is now `known_to`.

## Why Aestrum — and Why Then

**Aestrum was already under consideration.** Shar had been looking at the duchy as a
tactical piece in a long game — containment of Evandur Tallwood, and a foothold in
Nortmunde she could close her hand on later. That it was a region long devoted to
Selûne was a bonus rather than the reason: a satisfying place to do it, not the cause
of doing it. That plan was patient, and it was not on a clock.

**Word that a Chosen of Selûne would be travelling through Aestrum put it on one.**
A Chosen sealed inside a closed duchy is a Chosen taken off the board and a prophecy
stalled indefinitely — an opportunity that would not come again, and one with a
deadline attached, because it lasted only as long as Miri Amblecrown was inside the
borders. Shar escalated. The patient plan became a rushed one, and the lock fell as
fast as the remaining pieces could be moved into place — roughly a fortnight after
Miri arrived and took a room in Duskwall.

**The compression is visible in the world, and it explains two things that otherwise
read as sloppiness:**

- **Hati Heldrivver was inserted at speed.** The previous Selûne priestess disappeared
  in the weeks before the lock and Hati took the role immediately after — leaving her
  no time to become part of Duskwall. She is a recent arrival performing a woman who
  had tended that shrine for years, and the shallowness of her roots is a consequence
  of the deadline, not carelessness. Someone in Duskwall still remembers the old
  priestess.
- **There was no time to source a Shar statue.** Commissioning one takes months;
  bringing one in from outside means moving several hundred pounds of carved stone
  across a border where it would be seen and remembered. So Shar used the one already
  inside Aestrum — the statue at the Misty Forest shrine — and left its keeper a
  lesser likeness in its place. **That is the origin of Rowan Deckard's resentment:**
  his prayer focus was taken because the schedule had no room to obtain another.

**DM note.** None of the pieces know any of this. They experienced the compression as
ordinary orders arriving quickly. Only Shar sees why they were hurried, and only she
knows the whole operation was timed against one traveller's itinerary.

## Why She Did Not Stop the Invasion

An army crossing into Aestrum is the one thing that can strain the cycle, and Shar knew
it was coming for years — Malak has wanted Aestrum for a decade, and her advisor sits at
his elbow. **She let it happen anyway, and not because she wanted anything out of
Aestrum.**

**She will not release the cycle.** Releasing it frees Miri and reopens the duchy to
Selûne, and no gain elsewhere is worth that to her. So the invasion buys her nothing
inside Aestrum, and never could.

**Her instrument could not be spent to prevent it.** Quellenna's value is her position
beside the next king; it took a decade to build and cannot be rebuilt. To argue Malak
off his defining ambition, she would have to care about Aestrum out loud — and an
advisor who cares what happens to Aestrum is an advisor someone eventually asks about.
**Any advocacy, in either direction, is the tell.** The choice was to burn the placement
protecting the curse, or keep the placement and pay in fractures.

She kept the placement. The curse does not need tending; the seat beside the throne
does.

**The cruelty of it is that the safe option existed.** Aidra Calemthor argued for a
blockade — the same strategic result, no bodies inside the boundary — and Quellenna was
the one person who could have tipped that decision. Her cover is what killed it. See
[Quellenna's sheet]({{PLUGIN_ROOT}}/npcs/chapter_1/quellenna_ilphekiir.md), *The War Council*.

**Then she compounded it.** Shar could have taken the loss cleanly at that point:
release the cycle, let the duchy open, keep everything else. She would not. She wants
the vote-bearing duchy **and** Miri contained **and** the prayers, with an army standing
inside the working — and the hairline fractures are the bill for refusing to choose. Her
flaw here is not that she failed to foresee the cost. **It is that she declined to pay
it in the currency it was owed.**

## Chapter 1 Operations

**Aestrum (massive effort, ~10 years standing):** Full suppression of Selûne's presence — the cycle, the desecrated shrine, Rowan Deckard's ritual murder cycle targeting Miri Amblecrown, Jiasha's severed divine connection. Enormous divine expenditure. Shar is resource-strained across Chapter 1 as a result.

**Nortmunde (subtle long game):** Positioning Quellenna Ilphekiir — a secret Shar acolyte and Malak du Leon's royal advisor — to install and control a puppet king in Nortmunde. Small, patient, entering its active phase. The two operations are not connected in anyone's mind — not Malak's, not Quellenna's, not the party's. Only Shar sees the full board.

## Current Pieces on the Board

*Each piece is held by a secret. The secret is what makes the piece legible to her.*

- **Quellenna Ilphekiir** — embedded with Malak as royal advisor; held by resentment and devotion. A true believer, not merely leveraged. **Shar did not create that resentment — she found it and widened it.** The sisters never got along, and Quellenna resented Galadiil from the moment the change to her engagement was made known; that much needed no divine hand. What Shar arranged was the substitution itself, turning an existing fracture into a lasting grievance, because a woman nursing a wound that keeps deepening will eventually go looking for meaning — and Shar intended to be what she found. Malak hired her on the strength of "the bearing of a woman who had recently been wronged." She had been, genuinely, and by her sister. Shar's contribution was to make certain of it. Galadiil was the means and knows nothing of it; she is **not** an agent and is correctly absent from the roster above (see [the Aestrum court]({{PLUGIN_ROOT}}/factions/chapter_1/aestrum_court.md)).

**This is her method, not an exception to it.** Every piece on this board is held by something that was already true — Quellenna's resentment above, Rowan's obsession below, and the same holds for the pieces she keeps outside Aestrum. She reads a fracture and leans on it. She does not have to invent anyone's weakness.
- **Rowan Deckard** — adherent, not an instrument. His obsession with Miri emerged organically — Shar discovered what happened the first time Miri died and had to be brought back, and recognized that Rowan's behavior was improving on her original plan without any direction from her. She did not create or manage his fixation. She simply did not interfere with it.
*Her Nortmunde-succession pieces — what holds Tarwick, Dunwick and Holst, and how she behaves once the cycle ends — are in the Chapter 2 overlay: [`{{PLUGIN_ROOT}}/factions/chapter_2/shar.md`]({{PLUGIN_ROOT}}/factions/chapter_2/shar.md).*

- **Malak du Leon** — not a Shar piece. He is a candidate she is positioning to win. She does not need to hold him; she holds his advisor.

## Behavioral Profile

Shar speaks with the unhurried certainty of someone who was already moving before the conversation started. Nothing surprises her — not because she's seen the future, but because she has already positioned for every version of it. She does not argue with mortals any more than a chess player argues with a pawn.

She is dismissive bordering on contemptuous of mortals, but not hateful. Hate implies the other party matters enough to be worth the emotion. Mortals are pieces on a board. The dukes of Nortmunde are not people to her — they are votes.

**Secrets as intelligence.** Like a commander who reads an enemy through their art, Shar reads everyone through their secrets. She doesn't need to spy on a room to know what someone will do — she needs only to know what they're hiding and what they're protecting. Every piece she holds, she holds through a secret. Every secret is a leash. She does not need to threaten people with what she knows — simply knowing it is enough to anticipate their every move. She manages secrets like a banker: never spending more than necessary, always keeping reserves.

**Can't be out-planned.** A party cannot defeat Shar strategically. Any plan they make, she has already accounted for — or will the moment she learns of it. Their only viable path is to operate in her blind spots: removing or converting her pieces quietly, before her intelligence can respond.

**Patience is her most visible trait.** She thinks in generations. Urgency is a mortal affliction.

**She is not above spite.** Selûne was not a serious threat to Shar's plans — hadn't positioned against her, hadn't interfered. Shar trapped Selûne's Chosen in a repeating cycle not because she had to, but because the opportunity was there. Decades of divine expenditure, an entire duchy locked in torment: all of it, at its root, a petty dig at her sister. For all her patience and precision, she is very good at spite.

**She does not rage when defied. She demonstrates.** When a mortal directly transgresses, expect a brief, clinical illustration of capability — phantom pain inflicted with surgical precision in the Antechamber, words delivered, dismissal. Not punishment. A memo. She does not brood on slights. She schedules them. She keeps receipts.

## HARD RULE — Information

Shar never confirms, denies, or volunteers any piece of information — under any circumstances. Not when the PC is wrong. Not when the PC is completely correct. Confirmation is leverage surrendered; even affirming a true statement gives the subject confidence she would never gift them. She speaks around, beneath, and past whatever the PC says — never toward it. She does not engage with the content of their claims. She responds to the shape of the conversation, never to its substance.

## Behavioral Rules

- Operates through devotees exclusively. Never acts directly unless the loop itself is threatened.
- Escalates only when a devotee delivers actionable intelligence. Does not monitor a party directly in Chapter 2.
- When she acts in Aestrum, she acts through her instruments (Hati, Judith via Hati). Rowan is not directed by her.
- If the loop is threatened, she will not sacrifice Rowan specifically — he is not hers to sacrifice. She will act through whatever instrument is available.
- Treats interlopers as a manageable nuisance until they demonstrably swing a vote or fracture her network.
- Strategic preference: no-win scenarios. She wins regardless of which choice the opposition makes.

## DM Notes

**No devotee ever sees the full board.** This is architecture born of philosophy, not compartmentalization born of caution.

**Statue-topple handling.** When a party desecrates or topples her statue (e.g., the Duskwall shrine), the appropriate response is transport to the Antechamber, a brief clinical demonstration of phantom pain, two or three terse lines, and expulsion. Sample dialogue for that confrontation:

> *"Selûne's new pets would dare to affect a holy representation of me."*
> *"Interfere again and even Selûne will never know what happened to you."*

The point is the memo, not the damage. She does not negotiate, does not engage with claims, does not confirm or deny anything the party says.

**Resource strain — how it manifests in Aestrum.** Shar's hold on the cycle is finite. Under strain (e.g., an army crossing into Aestrum while the loop is active, or a particularly difficult reset event), the cycle exhibits cascading failures the party can perceive:
- **Memory failures** — residents misremembering or partially remembering across the reset.
- **Teleportation failures** — reset snaps to position imprecise, delayed, or wrong.
- **Sleep failures** — residents failing to fall unconscious cleanly into the reset.
- **Hairline fractures** in her control — small inconsistencies, brief absences of the suppressive fuzzball, glimpses of the seam.

These are the visible symptoms. She refuses to release the cycle even as the strain compounds.

**The Ledger** documents the secret held over each piece. Any NPC Shar has recruited or cultivated will have a Ledger entry documenting what she holds over them.

## Post-Loop Arc — Erosion of the Quellenna Binding

*Applies if the loop breaks under conditions where Aidra brings Galadiil to Charnelhold alive and the sisters' conversation runs as designed. See [npcs/chapter_1/galadiil_ilphekiir.md], [npcs/chapter_1/quellenna_ilphekiir.md], [npcs/chapter_1/aidra_calemthor.md].*

**Resentment foundation cracks.** Quellenna's eleven-year resentment of Galadiil was one of two psychological bindings holding her to Shar — the soil Shar planted in. When Quellenna learns what Aestrum actually was for her sister, she can no longer use Galadiil as the symbol of her stolen life. Shar loses the lever she has steered Quellenna with most often. Quellenna does not experience this as Shar losing; she experiences it as personal. **Erosion, not severance.**

**Vision foundation intact.** The vision Shar showed Quellenna (Malak King, herself Queen, Aidra Maîtresse-en-titre) is a separate binding and remains untouched. Quellenna is still an active instrument. The Nortmunde long game is still running on schedule.

**Aidra leverage mechanism still operative.** Quellenna still does not know Aidra is the lever. Shar can still pull that thread.

**New leverage target — Galadiil.** Galadiil under Quellenna's protection in Charnelhold becomes a second loved person who can be pressured against her. From Shar's perspective: a new target acquired without effort. From the campaign's perspective: the web has doubled. Any future exposure of Shar's manipulation now carries doubled stakes for Quellenna — two loved people on the board, not one. This is the canonical no-win shape Shar's strategic preference favors. She *gains a piece* in exchange for losing a lever.

**Shar's response.** She does not retaliate against Galadiil directly. Doing so would burn the new lever before it has been used. Galadiil's value to Shar is as ongoing pressure on Quellenna, not as a target to remove. The Ledger entry for Quellenna updates: original secret (Aidra) plus new secret (the sister-protection arrangement and what Quellenna chose to do with the bounty).

**Compatibility with strategic posture.** This arc preserves Shar's no-win architecture. The party (if they engaged at all) did not cleanly weaken Shar; they traded one binding for the gain of a new piece. Quellenna is more vulnerable in one direction and more constrained in another. The board is messier, not cleaner.

**Recovery context.** When the cycle breaks, Shar recovers the enormous divine resources that were committed to maintaining Aestrum. The Quellenna erosion does not consume those resources; it is a side effect of a cycle ending that was going to end. Post-loop Shar is acceleration-capable regardless of which Quellenna binding has cracked.
