---
id: faction_erethezra
name: Erethezra
type: criminal_organization
base: Setland (regional) / continental reach
leader: npc_erethezra_commander
rival: [faction_black_arrow]
members: [npc_erethezra_commander, npc_rylin_tsarran]
known_to:
  npc_rylin_tsarran: [npc_erethezra_commander]
name_origin: Elven word for "ghost"
---

## Overview

A criminal organization based in Setland with continental reach, and the primary rival of the Black Arrows. Their name is derived from the Elven word for "ghost." Known for vanishing entirely after every operation — they leave no witnesses, no evidence, and no trail. Elusive to the point that members are difficult to identify while living; usually only confirmed after death.

Erethezra has largely supplanted the Black Arrows' former dominance in the Setland region since The Shrikes collapsed there approximately ten years ago.

## Membership

*`known_to` = the members who know this person belongs. Directed; member-to-member only.*

| Member | Role | `known_to` |
|---|---|---|
| [The Erethezra Commander]({{PLUGIN_ROOT}}/npcs/chapter_1/erethezra_commander.md) | commander | **all** |
| [Rylin T'Sarran]({{PLUGIN_ROOT}}/npcs/chapter_1/rylin_tsarran.md) | operative | `npc_erethezra_commander` |

**Both rows are load-bearing, in opposite directions.** Every operative knows a
commander exists and takes her orders — but `known_to: all` records only that her
*membership* is known; **who she is** is not, and that is `recognition_state:
unidentified` on her sheet. Rylin's row is the inverse: his allegiance is known to
exactly one person, which is what lets him sit openly in
[the Incorrigible's crew]({{PLUGIN_ROOT}}/factions/chapter_1/incorrigible_crew.md) as first mate with nobody aboard aware
of it.

Members are "difficult to identify while living; usually only confirmed after death" —
that is the *outside* view, and it is a consequence of tables like this one being this
short.

## Known Operatives

**The Erethezra Commander** — Operational head. Has run the organization against the Black Arrows for over a decade without being identified. She is not a field operative — she is a commander. Full sheet: [`{{PLUGIN_ROOT}}/npcs/chapter_1/erethezra_commander.md`]({{PLUGIN_ROOT}}/npcs/chapter_1/erethezra_commander.md); her name is an unspent reveal.

**Rylin T'Sarran** — Drow first mate of *The Incorrigible*. Long-term operative embedded within a gang-controlled Calimshan shipping operation. See [`{{PLUGIN_ROOT}}/npcs/chapter_1/rylin_tsarran.md`]({{PLUGIN_ROOT}}/npcs/chapter_1/rylin_tsarran.md) and [the crew roster]({{PLUGIN_ROOT}}/factions/chapter_1/incorrigible_crew.md) she sits in openly.

## Signal Language

Erethezra uses an embedded signal language in songs and shanties performed by unwitting carriers. Specific phrases, nautical metaphors, and references to timing or direction translate to anyone fluent in the cant. Black-Arrow-trained operatives can recognize it — advanced but not impossible knowledge at experienced levels.

## DM Notes

**The Commander — full handling:**

- Does not meet people by accident. Any encounter that feels like a coincidence was a choice she made.
- Responds to demonstrated competence. Impressed by results she can verify, not reputation or bravado.
- Will not align with any succession candidate on principle. Erethezra's alignment is to Erethezra's interests.
- Toward Black Arrow members (including ex-members): not a personal enemy. She is the competition. The Black Arrows built something; Erethezra has been systematically taking it apart. Business.
- Will not move against a party without cause. Cause means actively working against Erethezra's interests, not simply operating in the same space.
- Should feel like someone who has been playing a longer game than anyone else in the room, and who is genuinely curious about new entrants rather than threatened by them.
- Character to be developed in play.

**Behavior in a succession crisis:**

- Expect her to treat it as opportunity and move assets accordingly.
- Standard early move: a general recall to operatives ("ghosts go home" or equivalent), embedded in songs and shanties carried by unwitting performers, repositioning her people ahead of the political conflict.
- If she becomes aware (through her own channels) that an outsider has decoded an Erethezra signal, she files it silently and adjusts her assessment of them upward without acknowledging it.
