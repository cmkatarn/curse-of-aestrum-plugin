---
id: rule_file_layering
name: File Layering — Base, Chapter, Current
type: meta_convention
---

# File Layering — Base, Chapter, Current

The campaign uses a three-layer file model so that location, NPC, and faction state can evolve cleanly across the campaign without rewriting base files.

## The Three Layers

| Layer | Path Convention | Purpose |
|---|---|---|
| **Base** | `campaign/[domain]/[file].md` | The canonical campaign-start state. Chapter 1 default. Authored once, edited rarely. The world as it exists when a new playthrough begins. |
| **Chapter** | `campaign/[domain]/chapter_N/[file].md` | A planned future state that applies once chapter N begins. Overlay on base. Authored deliberately as the campaign's chapter-level transitions are designed. |
| **Current** | `campaign/[domain]/saved/[file].md` | The live, accumulating campaign state. Player actions, kills, decisions, observed events. Overlay on whatever chapter is active. |

`[domain]` is one of: `locations`, `npcs`, `party`, `factions`, `lore`, etc.

## Rules Layering (Separate from Content Layering)

Rules — game mechanics, race/class definitions, homebrew rulings — follow their own three-tier model that runs orthogonally to the base/chapter/current model above:

| Layer | Path Convention | Purpose |
|---|---|---|
| **Engine** | `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/[file].md` | Canterbury — generic D&D 5e mechanics. Setting-agnostic. Vendored inside the plugin. |
| **Campaign** | `{{PLUGIN_ROOT}}/rules/[file].md` | Curse of Aestrum — homebrew that applies to every playthrough of CoA (time loop, dead zones, revert, etc.). Overlays Canterbury. |
| **Instance** | `{{PROJECT_ROOT}}/campaign_state/<instance>/rules/[file].md` | This specific playthrough — table rulings, non-standard PC backgrounds, custom Oaths/lineages, one-off mechanics tied to a specific party. Overlays both Engine and Campaign. |

Load order is **Engine → Campaign → Instance**. Last loaded wins on conflict.

The Instance tier exists so a single playthrough can carry mechanical homebrew (a player's non-standard background, a custom subclass, a one-off ruling) without polluting the shared CoA `rules/` directory or the Canterbury engine. If the same homebrew appears across multiple campaigns, promote it upward to `rules/`.

## Load Order

The skill (scene, author, etc.) loads the layers in this order and merges them:

**During Chapter 1:**
1. Read **base** file
2. Read **current** overlay (if present)
3. Merge

**During Chapter 2 (or any later chapter):**
1. Read **base** file
2. Read **chapter_N** overlay (if present, for the active chapter)
3. Read **current** overlay (if present)
4. Merge in that order

The chapter overlay loads *between* base and current. Current always wins on conflicts because it represents what has actually happened at the table. Chapter overlays describe the world's planned state for that chapter — current overlays describe what the party has done to it within that chapter.

## Examples

- **A village peaceful in Chapter 1 and burned in Chapter 2.** Base file describes the peaceful village. `chapter_2/` overlay describes the burned state. If the party further damaged a specific building, that's a `saved/` entry on top.
- **An NPC who is alive in Chapter 1, dead by Chapter 2.** Base file is the live NPC. `chapter_2/` overlay marks them deceased and notes the cause. If the party witnessed or caused the death, `saved/` records the circumstances.
- **A faction whose disposition shifts at chapter transition.** Base file is the campaign-start disposition. `chapter_2/` overlay revises faction-reach and posture. `saved/` tracks party-specific reputation effects.

## When to Use Each Layer

- **Base** — anything that is true at campaign start and would be true regardless of party choices. Geography, architecture, established characters, default faction relations.
- **Chapter** — anything that *will* be true at chapter N regardless of party choices. Planned timeline events. Predetermined state changes. Off-screen NPC actions that have unfolded between chapters. Authored ahead of time as part of campaign design.
- **Current** — anything that has *actually happened at the table.* Party actions, observed reveals, kills, romances, betrayals, lost items, gained allies. The literal play record.

### The p0 test (diagnostic)

Base/canon files describe **p0 — the campaign-start moment.** For any reference to a
PC or the party, ask: *is this true at p0, or did it happen after?*

- **True at p0 → base.** Pre-campaign backstory that holds the instant play begins: a
  PC's history, deserted allegiances, standing bounties, a berth on a ship, an item
  obtained before setting out. This stays in canon even though it names a PC.
- **Happened after p0 → `saved/` overlay.** Events, discoveries, acquired knowledge,
  visit counts, an item picked up in a dungeon, a monster killed. This leaves canon
  even when it is phrased through a PC's name ("Belmita grabbed…", "Theren decoded…")
  rather than "the party."

The trap is the second case wearing a name instead of "the party." A grep for *"the
party has"* will not catch *"Sage tracked…"* — both are post-p0 play record and both
belong in `saved/`. Item canon has the same tell: an item acquired in play should be
described as it sits in the world at p0 (unheld, unattuned), not as the PC who later
carries it experiences it.

## Authoring Rules

- **Do not duplicate base content in a chapter overlay.** Overlays describe *what changed*, not *what is*. If something is unchanged from base, the overlay says nothing about it.
- **Do not put PC data in any of these layers except via `saved/`.** PC reactions, PC kills, PC discoveries — all go in `saved/`. Base and chapter files describe the world independent of any specific party. (See user feedback from session: "PC data should only ever go into the 'saved' overlays.")
- **Chapter overlays are authored, not accumulated.** When you finalize how the world has changed by chapter N, you write a chapter_N overlay deliberately. Do not let `saved/` overlays drift into describing chapter-state changes.

## Write Scope — Campaign Data Never Goes Into Canon (HARD)

The base/chapter content trees in this repo (`locations/`, `npcs/`, `party/`,
`factions/`, `lore/`, including their `chapter_N/` overlays) are **canon**: the
world as it exists independent of any single playthrough. Canon is authored
deliberately — the storyteller fleshes out entries and creates NPCs as the
campaign is developed and verified. That authoring is expected and fine.

What is **never** written into a canon/init file is **play-generated campaign
data** — the events of a specific playthrough, the player's characters, and
items gained, lost, or altered in play (kills, romances, betrayals, decisions,
the live play record). All of it belongs in the per-playthrough trees under
`{{PROJECT_ROOT}}/campaign_state/<instance>/` (via the `saved/` overlays). The flow is
one-directional: play data accumulates in `{{PROJECT_ROOT}}/campaign_state/`, never back into
canon.

Concretely:

- A `{{PROJECT_ROOT}}/campaign_state/` file **may** reference canon (a custom PC sheet pointing
  at a canon location or NPC).
- A canon file **must never** carry play-generated campaign data — not in body
  text, and **not in frontmatter or cross-references** (`related_npcs`,
  `note:`, links, etc.). A canon file that records a specific playthrough's
  event, or names a character that exists only in a specific playthrough, has
  had campaign data written into it.

**When a playthrough character or event ties to a canon place or NPC:** write
the world-level, playthrough-independent fact in the canon file (reusable by
any playthrough), and keep the playthrough-specific tie **only** on the
`{{PROJECT_ROOT}}/campaign_state/` sheet, pointing *up* at canon. Canon stays silent about who,
in any specific playthrough, is connected to it.

**Verify before saving any canon edit:** the change records no playthrough
event, character, or item. If a canon edit can only be expressed by naming
play-generated data, that fact belongs in `{{PROJECT_ROOT}}/campaign_state/` instead — not in
canon. (This is the authoring-side companion to the play-time write-scope rule
that already forbids *saves* from editing canon without explicit approval.)

## Location NPC Manifest (`npcs_present`)

A documented location's frontmatter `npcs_present` (list of NPC ids) is a
**conditional load manifest**: when the party is at that location, the scene
loader resolves each listed NPC to **base + campaign overlay** before first
contact — the same two-tier resolution participants get. The inverse also
holds: a campaign-created NPC sheet may declare `location` / `home_location`,
and the loader injects it at the matching place.

The manifest is what keeps a documented resident from being improvised over in
play. A documented, inhabited location with a missing or empty `npcs_present`
offers the loader nothing and falls back to on-the-fly invention — a latent
recurrence of authoring an NPC over canonical content. Populating
`npcs_present` on every such location is required backfill.

*(NPCs only for now; extending the manifest to items and quest threads present
at a location is planned — see the system-wide TODO.)*

## Status

- **Base + current (`saved/`) layering: in active use** across `npcs/`, `party/`, `locations/`, and `factions/`.
- **Chapter overlay tier: defined here, not yet wired into the skills** (scene, author, etc.). Skills do not auto-load `chapter_N/` overlays. Chapter overlay files can be authored, but the DM must load them manually when running scenes in the relevant chapter, until skill support lands.

## Migration Notes

- Existing `saved/` files that describe **chapter-state changes rather than party actions** should eventually be moved to `chapter_N/` overlays once the chapter tier is fully wired up. Examples to review: `locations/saved/charnelhold.md` (records Aidra-absent state, which is a campaign-timeline state not a party action — though it is currently the only `saved/` entry for that file).
- This is a future cleanup, not an immediate task.
