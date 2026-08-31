# Create Character — Curse of Aestrum Override

Setting overrides for the rpg-5e-engine `create-character/core.md`.

---

## Spoiler Discipline

A new PC arrives in this region as an outsider, the same way real
players do.

**Never reveal in conversation, sheet content, or backstory hooks:**

- That Aestrum is trapped in a time loop, or anything about resets,
  Modify Memory, Recreate, dead zones, the Moon Amulet system, or loop
  anchors.
- That Shar is operating in the region, or any reference to her shrine,
  her Antechamber, Shar's Debt, or Rowan Deckard's true allegiance.
- Anything about Selûne's suppression in Aestrum, Miri Amblecrown,
  Jiasha's disconnection, the Amber Crown Prophecy.
- The internal politics of Nortmunde beyond what a literate citizen would
  read on a public posting **at campaign start (Day −14, before the King's
  death)**: the King is **alive but ailing**, the duchies are in quiet
  tension, and Setland (Duke Malak) is openly hiring contractors for the
  Aestrum back-taxes expedition. **The King's death, the succession crisis,
  and any Setland march on Aestrum are post-Day-0 events that have not
  happened yet — never present them as current or public** (see
  `{{PLUGIN_ROOT}}/lore/key_lore_summary.md` → Political Situation). Specific operations
  (Quellenna's vision, Luca's identity, the Galadiil bounty, Erethezra's
  recall, etc.) are off-limits.
- Any current state from Chapter 1 or Chapter 2 of the existing
  campaign (party actions, NPC outcomes, castle destruction, etc.).
- Any internal arc, secret, item, or trauma belonging to the canon PCs
  (Thagnog, Belmita, Theren, Sage, Zephyra).

**Recommend, don't leak.** If the user picks a background that's near a
sensitive plot thread, recommend it without explaining why.

**Aestrum is opaque.** No new PC has any prior knowledge of what is
actually happening inside Aestrum. The region's mystique — "people who
go too far in don't come back" — is all an outsider knows. Therefore:

- **Do not offer hooks** that originate inside Aestrum (no Misty Forest
  origin, no Nahamkate Desert origin, no Duskwall residency, no
  awareness of dead zones, no connection to *The Incorrigible* or Rylin
  T'Sarran, no Aestrum-internal factions).
- If the user volunteers an Aestrum-internal connection unprompted, ask
  once what they want from it and then find an outsider-compatible
  reframe (e.g. "ancestor came from there generations ago and never
  spoke of it").

---

## Blood-Relation List (Canon-Load-Bearing NPCs)

**Never assign or suggest blood relation to:**

- Quellenna Ilphekiir
- Galadiil Ilphekiir
- Duke Evandur Tallwood
- Duke Malak du Leon
- Rowan Deckard

These are load-bearing canon figures and direct blood ties break their
arcs.

**Single exception — Amblecrown lineage.** If the user *explicitly and
without your prompting* declares Amblecrown lineage (Duke Amblecrown of
Skaarsdaam, Miri's house), allow it. It can produce a strong campaign.
Do not suggest it, do not list it as an option, and do not steer toward
it. Only honor it if the user brings it up first.

---

## Restricted Race / Class Features

Per the engine's "Reject features that would short-circuit the campaign
premise" rule, reject:

- **At-will plane-shifting** (would let the PC leave Aestrum trivially).
- **Innate time manipulation / chronomancy** (would short-circuit the
  loop premise).
- **Party-wide memory protection** (would short-circuit the Modify
  Memory mechanic).
- **"Always knows what happens tomorrow" abilities** (would short-circuit
  prophecy / loop tension).

For each, find a reskin if the player wants the flavor.

Warn the player (without explanation) if their race carries divine
signatures that may "read loudly" to NPCs in the region — particularly
aasimar, genasi, or other lineage-visible races near factions sensitive
to divine alignment.

---

## Output Path

```
{{PROJECT_ROOT}}/campaign_state/<C>/party/saved/<instance>/<character_slug>.md
```

- **`<C>`** — active campaign slug from `{{PROJECT_ROOT}}/campaign_state/.active`.
- **`<instance>`** — save-snapshot identifier passed in by the caller
  (create-party skill), or asked from the user if invoked standalone.
  Default: `instance_<YYYYMMDD>`.
- **`<character_slug>`** — lowercase `firstname_lastname` (or single
  name) with underscores.

**Never** write a PC into `party/` root or `party/chapter_1/` — those
are reserved for the canonical roster and the canonical PC companions.
All player-created PCs live in `{{PROJECT_ROOT}}/campaign_state/<C>/party/`.

---

## Campaign Time Anchor (frontmatter — load-bearing)

Every CoA PC sheet carries the campaign's primary time anchor in
frontmatter:

```yaml
joined_expedition_nortmunde_day: -14
```

This is the **Nortmunde Day the PC signed on** for the Aestrum expedition
— the field every later scene reads to place the world Before vs. after
the King's death (see [scene.md]({{PLUGIN_ROOT}}/overrides/scene.md) → Roster-at-T parameters and
`{{PLUGIN_ROOT}}/lore/key_lore_summary.md` → Political Situation). **Default `-14`** (the
expedition-dispatch / sign-on day); a PC who joins in-fiction after
departure takes the Day they joined. When `create-party` invokes this
skill, use the party's sign-on Day; invoked standalone to add a PC to an
existing campaign, use that campaign's sign-on Day (default `-14`). **A PC
sheet written without this field is a defect** — add it before finishing.

---

## NPC Output Paths

For NPCs built via the `create-npc` skill (engine subject type = NPC):

- **Every campaign NPC is pure overlay** — companion and incidental alike are
  written as a single self-contained sheet at
  `{{PROJECT_ROOT}}/campaign_state/<C>/npcs/saved/<character_slug>.md`. The sheet holds the full
  character and accumulates play state below it; there is **no** separate
  campaign-level base file. (This is where the companions Drasha and Kaeline and
  any incidental face of the playthrough all live — one file each, in `saved/`.)
- The **companion vs. incidental** distinction governs authoring richness only
  (a companion gets the connectable-personality treatment and a fuller sheet);
  it does **not** change the output path.

`<C>` is the active campaign slug from `{{PROJECT_ROOT}}/campaign_state/.active`. **Never** write
an NPC into the canonical project-root `npcs/chapter_N/` roster — that tree is
reserved for authored canon, and a campaign-created NPC (companion included) is
**not** canon. The only base/canon tier is that project-root roster; everything
under `{{PROJECT_ROOT}}/campaign_state/<C>/npcs/` is non-canon overlay.

---

## Connectable Companions — Worked Example

The engine's `authoring_connectable.md` requires companion NPCs to be
authored so a player can bond with them at minimal effort, with flaws that
complicate bonds rather than prevent them. A concrete CoA illustration,
from Kaeline Vos (`{{PROJECT_ROOT}}/campaign_state/hessian/npcs/saved/kaeline_vos.md`):

**Isolating draft (rejected).** An early flaw set pointed her armor at the
party: distrusts all closeness, keeps everyone abstract, withdraws as a
reflex, reads kindness as a maneuver. The result would have been a
companion a player could travel with for a whole campaign and never get a
foothold on — present for her stats and nothing else.

**Warm-direction set (shipped).** The corrected flaws keep her armor
pointed at her *targets and her past*, not the party:

- *Camaraderie comes free; vulnerability stays barred* — instant foxhole
  bond, but she deflects sincerity. Closeness is cheap; depth is earned.
- *Adopts the party as a crew, needs it to have a shape* — she connects
  through structure and frets when it's absent.
- *Mistakes intensity for intimacy* — quick to bond, prone to misreading
  what the bond is.

Each gives the player a fast way in and reserves the difficulty for the
relationship's interior. That is the target shape for any CoA companion.

---

## Writ-Seeding for Single Companion NPCs

When `create-npc` builds a **questionable-background, Claude-controlled**
companion (a Black Arrows operative, an Erethezra contact, a bounty
hunter), the Galadiil-writ secret-state pattern may apply — the same
mechanic `create-party` seeds for random party NPCs.

- The authoritative seeding rules, betrayal/spread behavior, and
  reset / dead-zone interactions live in `{{PLUGIN_ROOT}}/overrides/create-party.md`
  (Random-Slot Seeding of the Galadiil Bounty). Do not duplicate them;
  read that section when seeding a single NPC.
- The gate still holds: secret state is only coherent for a
  `control: claude` NPC. Never seed it onto a player-directed NPC.
- Sheet pattern: `carries_galadiil_writ: true` + `secret_state: true`
  frontmatter, hidden material in a clearly DM-only section. See
  `{{PROJECT_ROOT}}/campaign_state/hessian/npcs/saved/kaeline_vos.md` ("The Writ — DM-Only") as
  the reference implementation.

---

## Hook Tables (Nortmunde-Side Only)

All hooks below are **Nortmunde-side only**, per the Aestrum-opacity
rule. Aestrum-internal hooks are forbidden.

### Background → Faction Hooks

| Background | Suggest |
|---|---|
| **Urchin / Criminal** | **Erethezra** (Setland-based criminal organization, name means "ghost" in Elven; vanish after every job, hard to identify while living, continental reach). **The Black Arrows** (Setland family-style gang, wrist arrowhead tattoo, communicates in Thieves' Cant, patriarch Roland Elakian openly allied with Duke Malak). **Never offer The Shrikes** — even the historical Setland branch is too entangled with current plot threads. |
| **Soldier** | Served under one of the Nortmunde duchies. Default options: **Setland** (Duke Malak du Leon — rising aggressor, lion crest; the duchy hiring the Aestrum tax-collection expedition). **Skaarsdaam** (Duke Amblecrown — old-line house, quiet demeanor). **Mikaelvad** (cold northern duchy, austere reputation — warn the player it has a sinister cultural reputation but do not elaborate). **Dalihad** (Duke Dorvael Dunwick — quarry-heavy economy, hard labor culture). |
| **Sailor** | Worked the Sword Coast or Calimshan trade routes out of Setland's port. Possible exposure to gang signal language hidden in shanties — performers across the Setland-Calimshan run sometimes carry coded messages between criminal cells. |
| **Noble** | Minor house in one of the duchies. Beluir's halfling **Goodfeet** clan (third-born son Delmuir is known by name) is a viable invention point. Other minor houses are open. Never tie to a sitting Duke or to the Ilphekiir sisters (Galadiil, Quellenna) by blood. |
| **Acolyte** | Any standard god other than Shar. **Selûne** devotee is a strong story choice — recommend it as "interesting" without explaining why. Lathander, Tymora, Tempus, Helm, Sune, Mystra, etc. are all open. If the player picks Shar, ask once if intentional and warn (without specifics) that it positions them against the party — let them choose. Leira-line warlocks are fair game per the canon-arc rule. |
| **Folk Hero / Outlander** | Tie to a specific Nortmunde village or wilderness *outside Aestrum*. Skaarsdaam moors, Setland farmland, Dalihad quarries' outskirts, Mikaelvad highlands. **Do not place them in any Aestrum-internal location.** |
| **Sage / Hermit** | Researcher of pre-loop Nortmunde history, the Acolypyrrhic Battles (~1280 DR — multi-deity warfare era, public historical record), divine theology generally. Do not let them claim research into dead zones or loop mechanics. |
| **Entertainer** | Performer working the Setland-Calimshan circuit. Possibility of being an unwitting signal carrier for a gang's coded shanties — same hook as Sailor. |
| **Guild Artisan / Merchant** | Setland trade guild ties. Lion's Den connections plausible (the Duke's general assembly chamber is the city's commercial-political hub). |
| **Charlatan** | Setland or general Nortmunde confidence games. Identity-theft schemes against minor noble names (including Goodfeet) are open per the canon-arc rule. |

### Race → Hooks

| Race | Suggest |
|---|---|
| **Dwarf (any subrace)** | The **Blooddigger clan** — a Mountain Dwarf bounty-hunting clan that operates across the Nortmunde duchies, particularly Dalihad. Player can be a member, estranged cousin, in-law, or have an old debt to the clan. Do not describe any current state of the clan beyond "they take contracts across the region" — anything more is spoiler. |
| **Halfling** | The **Goodfeet** clan in Beluir is a known halfling house — Delmuir Goodfeet is the third-born son. Player can claim the name legitimately, by marriage, by adoption, or as a forgery, per the canon-arc rule. |
| **Elf / Half-Elf** | Generic Nortmunde elven communities or migrant from the Sword Coast / Evermeet. No blood ties to the Ilphekiir sisters. |
| **Human** | Most flexible — tie to any duchy. |
| **Gnome / Tiefling / Dragonborn / Half-Orc** | No specific canonical hook; let the player invent within Nortmunde or the Sword Coast. |
| **Drow** | Rare in Nortmunde. Surface drow with a credible non-Aestrum origin is allowed. Do not connect them to any criminal organization the player has not chosen themselves. |

### Class → Hooks

| Class | Suggest |
|---|---|
| **Cleric / Paladin** | Patron deity matters more in this region than the player will initially understand. Recommend Selûne, Lathander, Tymora, Tempus, Helm, Sune, or Mystra as "strong story choices" without explaining why. Shar is allowed only with the warning above. |
| **Warlock** | Patron matters. Archfey, Fiend, Hexblade, Great Old One, Celestial, and the various trickster-god patron lines are all open. Recommend the player give thought to what the patron wants from the pact — these stories tend to surface in play. |
| **Druid / Ranger** | Nortmunde-side wilderness origins. Skaarsdaam moors, Dalihad foothills, Setland coastal forests. **Not** Misty Forest, **not** Nahamkate. |
| **Wizard / Sorcerer / Bard** | Academy or guild ties — Setland's collegium, Skaarsdaam's older arcane traditions, free-roaming bard circuits. Do not let the player claim pre-knowledge of dead zones or anti-magic phenomena in Aestrum. |
| **Fighter / Barbarian / Monk / Rogue** | Faction / duchy hooks via background carry the weight here. |

---

## Anatomy Pass

The engine's anatomy pass is innate-knowledge-first (recall the race's
features from canon; consult `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/race_anatomy.md` only
for departures, depth conventions, and pinned entries). **Standard races
need no pre-documentation** — build them from recall.

This setting does not currently introduce non-standard lineages with
anatomy that departs from canon. If one ever does (a custom lineage, a
setting-specific physical departure, or a feature this campaign wants
documented at unusual depth), pin a section in the engine
`race_anatomy.md` per its "Races Not Listed Above" guidance rather than
here. A character's own specific choices are pinned on their sheet
regardless — that sheet is the per-character consistency anchor.

---

## Content Rating Context

The session default outside in-game sessions is **M**. If the user
writes backstory with mature themes, confirm the rating context but do
not require an explicit choice unless they ask. See the full rating
system in [scene.md]({{PLUGIN_ROOT}}/overrides/scene.md#content-rating-system).
