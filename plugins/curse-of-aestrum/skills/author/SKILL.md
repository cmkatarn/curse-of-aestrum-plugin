---
name: author
description: >
  Use this skill when the user wants to author a piece of the Curse of Aestrum
  world that is not a character — a location, an item, a quest, a faction, or a
  connection between two places. Triggers on "author a location", "create a
  location", "write up the X", "make a faction file", "add an item", "new quest
  file", "give X its own file", "we need a file for X", or any request to create
  or formalize a world object. Also triggers when a dangling reference needs
  closing ("close loc_aidra_house", "that place needs a file"). Do NOT use for
  characters — NPCs go to create-npc, player characters to create-character,
  parties to create-party. Do NOT use for writing prose, or for live play
  (scene).
allowed-tools: [Read, Grep, Glob, Write, Edit, PowerShell]
version: 1.1.0
---

> **Plugin path resolution — read this first.** You are running inside an installed plugin. Two
> placeholders appear in this skill and in every file it leads you to read:
> `{{PLUGIN_ROOT}}` = `${CLAUDE_PLUGIN_ROOT}` (this plugin's bundled files — engines, rules,
> overrides, and campaign content) and `{{PROJECT_ROOT}}` = `${CLAUDE_PROJECT_DIR}` (the player's
> own working directory, where every `campaign_state/…` play-state file is read and written).
> Whenever any file you read contains a `{{PLUGIN_ROOT}}/…` or `{{PROJECT_ROOT}}/…` path, replace
> the placeholder with the absolute path shown above and read/write that. **Never** resolve these
> against the working directory or a file's own folder, and never write into `{{PLUGIN_ROOT}}`.


# Author — Curse of Aestrum

Thin shell over Aria's non-character authoring procedure, bound to this
campaign's spellings.

**Path resolution.** Every path below is written `{{PLUGIN_ROOT}}/...` and
resolves against this plugin's bundled root — **not** this skill's own base
directory, and **not** the working directory. The engines are vendored inside
the plugin: Aria is at `{{PLUGIN_ROOT}}/engines/story-engine/...`. There is no
sibling engine repo to reach for, and no path leaves the plugin. If a read 404s,
re-resolve the placeholder against the plugin root before assuming the file is
missing.

## Subject types

| Subject | Domain | Prefix |
|---|---|---|
| **location** | `locations/` | `loc_` |
| **item** | `items/` | `item_` |
| **quest** | `quests/` | `quest_` |
| **faction** | `factions/` | `faction_` |
| **connection** | `locations/` | `conn_` |

Characters are **not** this skill's subject. Send NPCs to `create-npc`, PCs to
`create-character`, parties to `create-party`.

## Load order

1. **Engine procedure.** `Read` `{{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_entities.md` —
   the six-step procedure, the four failure modes, and the invariant/binding
   split. This is the *how*.
2. **CoA bindings.** `Read` `{{PLUGIN_ROOT}}/overrides/frontmatter.md` — this campaign's
   spellings: id prefixes, the peer-relation pairs table, containment, placement
   (`location` vs `location_status`), `groups:` vs `deity:`, the layer paths, and
   the current Known Gaps. This is the *what*.

Read on demand:

- `{{PLUGIN_ROOT}}/engines/story-engine/FRONTMATTER.md` — the neutral field/body shape per kind.
- `{{PLUGIN_ROOT}}/rules/aestrum_location_curation.md` — **always, for `location`.** See below.
- `{{PLUGIN_ROOT}}/rules/file_layering.md` — if the canon/overlay call is not obvious.

## The curation rule is not suspended here

`{{PLUGIN_ROOT}}/rules/aestrum_location_curation.md` forbids *Claude* introducing new Aestrum
locations **during play**. This skill is the sanctioned path around that: it is
**DM-directed authoring**, invoked deliberately, outside a scene.

That permission is narrow. It licenses writing the file the DM asked for. It does
**not** license inventing neighbouring places, settlements, or landmarks to fill
the file out. If the work needs a second location, stop and ask.

## Placement

| What it is | Where it goes |
|---|---|
| **Authored canon** — true at the start of every run | `<domain>/chapter_N/<file>.md` |
| **Run-created** — exists because *this* playthrough produced it | `{{PROJECT_ROOT}}/campaign_state/<C>/<domain>/saved/<file>.md` |

`<C>` is the active campaign slug from `{{PROJECT_ROOT}}/campaign_state/.active`. **A run never
writes into the canon tree**, and canon never records what one playthrough did.
When in doubt, ask which it is — the answer is rarely ambiguous once stated.

## Workflow

Follow the six steps in `authoring_entities.md`, with these CoA specifics:

**STEP 1 — Does it already exist?** `Grep` the tree for the display name *and*
plausible id spellings before minting anything. If a file already cites the
entity, **adopt the id already in use** rather than a tidier one. Check the
rosters too — `{{PLUGIN_ROOT}}/npcs/chapter_1/remaining_npcs.md` and
`{{PLUGIN_ROOT}}/locations/chapter_1/standalone_locations.md` each hold many entities in one file.

**STEP 2 — Mint the id.** `<prefix>_<slug>`, lowercase, articles dropped. Minted
once, never restated.

**STEP 3 — Choose the layer.** Per the placement table above.

**STEP 4 — Write the file.** Fields per `{{PLUGIN_ROOT}}/overrides/frontmatter.md`. Prefer a
**stub with Open Slots** over invented detail: reserve `[layout]`, `[relation]`,
`[name]` and say so in the file. A stub that names what it does not know beats a
file that quietly makes it up.

**STEP 5 — Wire both ends.** Every peer relation in the pairs table is authored
on **both** sides in the same edit. A location gets `npcs_present` (`[]` if
genuinely nobody). A character pointing at it gets `location:`. Containment is
`parent`, on the child, and nowhere else.

**STEP 6 — Verify.** Run the checker from `fiction-host`:

```
py -m runtime entitycheck --config {{PLUGIN_ROOT}}/entitycheck.toml
py -m runtime refcheck --config {{PLUGIN_ROOT}}/refcheck.toml
```

**Acceptance: the issue count must not rise.** If the new file closed a dangling
reference, it should fall. Report the before/after count in the summary.

## Stop and ask — do not invent

Surface the question and wait. Do not guess at any of these:

- **A second location** the file seems to need (the curation rule).
- **A proper name** that canon has never given — a person, a town, a title.
  Reserve it as `[name]` instead.
- **A date or duration** not derivable from `timelines/chapter_1/` or
  `{{PLUGIN_ROOT}}/locations/chapter_1/routes.md`.
- **Which run a fact belongs to**, when it reads like playthrough history.
- **Whether a present-tense fact is start-state or later-state**, when the trigger is
  not obvious — see *Snapshots vs. transitions*.
- **A referenced entity with no file** — say what cites it and let the DM decide
  whether to author it, alias it, or declare it a soft pointer.

## Snapshots vs. transitions — check the clock on every present-tense fact

**The failure this prevents:** inheriting a true-but-dated fact from another file and
writing it into a new one as though it were always true.

Grounding discipline protects against *inventing*. It does nothing against
*inheriting* — a sentence like *"Aidra is commanding in Aestrum; her house is
unoccupied"* is correctly grounded, correctly sourced, and **wrong in a canon file**,
because it is only true from Nortmunde Day 0 onward.

**The check.** For every fact about **presence, occupancy, possession, office or
status**, ask:

> Is this true at campaign start, or true from some later trigger?

If it is anything but "always," **write the shape, not the snapshot.** There are three,
and they are not interchangeable:

**1. One-way transition** — a dated trigger fires and the state changes for good. Write
both states and the trigger between them.

| | before | after |
|---|---|---|
| Aidra's house | her anchor; occupied | empty from Day 0, when the invasion orders come |
| Aestrum Field Command | does not exist | forms Day 0, crosses the border ~Day +5 |

**2. Repeating cycle** — the same sequence every day, reset by the loop. Write the
sequence and say that it repeats, so nobody reads one row as the settled state. The
hour a scene starts decides which row is live.

*The Perisdottir house:* Aliss resets each midnight and is **functionally not
loop-aware** until her eye catches the dead box an hour or two into the morning. Arrive
in the morning and she is a fortune teller who does not know what year it is; arrive in
the afternoon and she is the woman who has been waiting years for you.

**3. Conditional branch** — a state that exists only if something happens, and may never
happen at all. Write it, mark the trigger, and say explicitly that it is **not the
default** and must not be rendered until it has fired.

*Examples:* Thalamin alone in the house if Aliss ever leaves with a party; Rowan
displaced from the Deckard Estate; the cellar encounter under Aidra's house, which
fires only when she is home.

**None of these is run state.** Run state is one playthrough's history and belongs in an
overlay. These three are **campaign-wide** — true in every run, just not now, not at
this hour, or not unless something happens. All four belong out of a plain canon
assertion, for four different reasons.

**Two clocks.** Aestrum days and Nortmunde days advance together, and a party deep in
the loop can be well past an outside event without knowing it happened. When a fact
turns on a date, name which clock it is on. `{{PLUGIN_ROOT}}/timelines/chapter_1/nortmunde_regional.md`
is the anchor (Day 0 = the King's death).

If you cannot tell whether a fact is start-state or later-state, **ask** — that one
belongs on the stop-and-ask list.

## Grounding discipline

Assemble from what the repo already says; do not embroider. Before writing, grep
for every existing mention of the subject — the material is usually scattered
across three or four files and the file's job is to *collect* it. When the sheet
says something specific (a distance, a rule, a habit), quote its shape rather
than paraphrasing it loosely.

If nothing in the repo grounds a section, leave it an Open Slot and say so in the
summary.

## Summary format

Close with:

1. The file path and id.
2. What it was assembled from — which existing files supplied the material.
3. What was reserved as an Open Slot, and why.
4. Both ends of every relation wired.
5. `entitycheck` / `refcheck` before → after.
6. Any question raised under *Stop and ask*, still open.
