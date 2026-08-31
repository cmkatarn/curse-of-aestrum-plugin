# Frontmatter & File Conventions

The data shapes a consuming work authors so that Calliope can load a scene. Every
entity a scene touches — **characters, locations, items, goals, groups,
events** — is a markdown file with a YAML frontmatter block and a body of named
sections. This file documents the genre-neutral conventions; the work's override
file supplies the concrete bindings (path tree, character-type table, time-anchor
format).

This file defines the **shape** of an entity file. The **procedure** for creating
one — id minting, layer placement, wiring its relations, and the integrity checks
that keep the entity graph consistent — is
[rules/authoring_entities.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_entities.md) for non-character
entities, and the `authoring_*` character modules for the cast.

This engine defines **no mechanics**. None of the fields below carry stats, dice,
or a resolution system. A work that wants a system layers it on top in its own
files and override — it is invisible to this engine.

These conventions are the file shape that Calliope's
`scene/references/character_memory_template.md` and `location_memory_template.md`
read at scene start. Author to them and a scene loads without improvisation.

---

## Common fields

Every entity file carries at minimum:

| Field | Meaning |
|---|---|
| `id` | Identifier, minted once and never restated. It must resolve to exactly one entity; how a work guarantees that is its own binding (see below). |
| `name` | Display name. Free to change; the `id` does not follow it. |
| `type` | Under the **explicit-kind** binding, the entity kind from the controlled set: `character`, `location`, `item`, `goal`, `group`, `event`, `connection`. Under the **directory-kind** binding, free for the work's own finer classification. |
| `aliases` | Optional. Other names the same entity is known by, in prose or by the cast. |
| `subtype` | Optional. Finer classification within the kind (`tavern`, `heirloom`, `household`), where `type` is carrying the kind. |

**Every entity's kind must be resolvable; how is a binding.** The kind is what the
loader and the gate branch on, so it can never be a guess — but a work has two
conformant ways to supply it:

| Binding | The kind comes from | Then `type` is |
|---|---|---|
| **Explicit kind** | the `type` field, from the controlled set | the kind; finer classification goes in `subtype` |
| **Directory kind** | the domain directory the file sits in (`locations/`, `groups/`) | free — the work's own classifier |

**A work declares which binding it uses, in its override, and uses it consistently.**
The two must not be mixed within one work: a reader that resolves kind by directory
will misread a `type` it was not expecting, and a reader that trusts `type` will
misread a file that never carried one. Mixed is the only non-conformant option. The
examples throughout this file use the explicit-kind binding.

Under the directory-kind binding, keep `type` a short classifier rather than a
sentence — anything that groups or filters by it needs the values to be comparable.
Descriptive prose about the entity belongs in the body's Overview either way.

**`aliases` is how alternate names stay attached to one entity.** A place the cast
calls three things is one entity with three aliases — never three ids. Registering the
names is what makes a search-before-authoring pass (see
[rules/authoring_entities.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_entities.md), STEP 1) actually find it.

**Id uniqueness is the invariant; the spelling is a binding.** A work may guarantee it
with a type prefix in a shared namespace (`char_mara_vale`, `loc_harbor_steps` — the
style this file's examples use), or with bare slugs scoped by a per-domain directory
(`home`, `network`, filed under `locations/` and `groups/`). Both are conformant. What
is *not* conformant is a namespace where a reference cannot be resolved to exactly one
entity.

State for any entity layers across files per [rules/file_layering.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/file_layering.md):
a **base** file (canonical start state), optional **chapter** overlays (planned later
state), and a **current** overlay (what actually happened). The loader merges them;
current wins on conflict. The directory each layer lives in is named by the work's
override, never by this engine.

### Relation fields

Entities reference each other by `id`, never by display name. Two field shapes cover
every relation, and which one applies is not a matter of taste:

| Shape | Field (example spelling) | Rule |
|---|---|---|
| **Containment** — a sub-area inside a place, an entry inside a collection | `parent` | Declared on the **child only**, and with **one key across every entity kind**. A `parent_<kind>` variant alongside `parent` splits the graph in half. |
| **Peer connection** — neighbouring places, a member and their group, an item and its holder | `connections`, `members`, `owner` | Declared on **both ends**. A peer relation present on one side only is a bug, not a shorthand. |

**The shapes are the invariant; the field names are a binding.** A work that spells its
peer link `connects_to` rather than `connections` is conformant — what it may not do is
spell containment two ways, or author a peer link on one end. The override declares the
work's chosen spellings once; this engine cares that a relation has the right shape,
not what it is called.

Every id written into a relation field must resolve to exactly one entity, or be a soft
pointer the work has explicitly documented as intentionally unresolved. An empty
relation is authored as an empty list (`characters_present: []`) — that asserts *nobody
is normally here*, which is information. Omitting the field asserts nothing and forces
the loader to guess.

The full procedure and its failure modes are in
[rules/authoring_entities.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_entities.md).

---

## Characters

A character file is the source of who the character is, how they speak, and — most
importantly for the gate — **what they know and what they must not know**.

### Frontmatter

```yaml
---
id: char_mara_vale
name: Mara Vale
type: character              # or a work-defined subtype per its character-type table
memory_continuous: true      # true = linear memory; false/omit = time-filtered (reset, wipe, loop)
status: complete             # stub | developing | complete (see authoring_progressive.md)
home_location: harbor_steps  # optional; for the override's resident auto-injection
---
```

The override's **character-type table** maps each `type` to where its base and
overlay files live and whether its memory is time-filtered or continuous. The
`memory_continuous` flag is the per-file way to declare the policy when the type
table doesn't fully determine it.

#### Optional gate-activation fields

Calliope's epistemic gate keeps several detectors **dormant** until a work opts in
by supplying the named field. Include these only when the work uses them:

| Field | Activates | Use when |
|---|---|---|
| `join_points` | group-roster references | the protagonist joined a group at a known point; bounds what "the group" can imply about them. |
| `foresight` | future-state claims | the character has a defined, bounded source of foreknowledge (prophecy, vision). |
| `recognition_state` | identity-through-disguise | a character is disguised/unrecognized and narration must not name them through it. |
| `known_languages` / `literacy` | language comprehension | the work has multiple languages/scripts; sets the character's spoken-comprehension and reading boundary. Content outside the set is marks, not meaning. |

A work with terms that must never surface in narration (system vocabulary, OOC
labels) points the override at a `mechanical_vocabulary_file`; the gate's
meta-vocabulary detector reads it. This engine ships no such file — it has no
vocabulary to hide.

### Body sections

```markdown
## Overview
Who they are in 2–4 sentences.

## Appearance
What they look like, to the depth the work wants on the page.

## Voice
Speech pattern, diction, verbal tics, rhythm — what makes their lines theirs.

## Personality
Trait / ideal / bond / flaw, or whatever shape the work uses.

## Character Memory
The epistemic boundary the gate enforces. Calliope rebuilds this into a working
block at every scene load. Carry:
- What they know — each with a source (own experience, told by X, a document, rumor).
- What they explicitly do NOT know — the knowledge flags.
- Relationships / disposition — their standing toward others, and their *read* of
  others, bounded to what they have observed.
- Agenda / goals — active intentions and hidden plans. This is boundary state:
  other characters must not act on it without in-fiction access.
- Known languages / literacy, if the work uses them.

## Private Knowledge
Narrative facts this character holds that the rest of the cast does not — secrets,
private conversations, single-character revelations. See
[rules/private_information.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/private_information.md).

## Open Slots — To Develop in Play
Deferred facets, for stub/developing characters only. See
[rules/authoring_progressive.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_progressive.md).
```

A character whose data predates these headings still loads — the override supplies
the header conventions that map free-form prose onto the memory block's slots, and
Calliope rebuilds the block from source each load. No rewrite is forced.

---

## Locations

The authoritative source for layout, fixtures, ambient conditions, and fixed
residents. **Calliope never improvises a location's geometry or contents when a
file exists** — author it here or accept improvisation.

```yaml
---
id: loc_harbor_steps
name: The Harbor Steps
type: location
parent: loc_dockside              # optional; the containing place, on the child only
connections: [loc_fishmarket]     # optional; peer places, declared on both ends
characters_present: []            # who is normally here; `[]` means nobody
---
```

Body sections describe **layout** (rooms, exits, fixtures, dimensions — no invented
geometry at scene time), **fixed residents** (who is plausibly present; anyone else
needs a reason), **ambient conditions** (light, sound, weather, smell), and **what's
in the rooms** (items, marks, hidden details). Note the **language or script** of
any in-location text (signage, inscriptions, letters) so the comprehension boundary
can gate a character "reading" a script they lack.

Locations may be flat files or organized into subdirectories (districts, chapters,
regions) as the override documents; sub-areas may have their own files. Directory
nesting is presentation — `parent` is the containment of record, and a sub-area
filed in a subdirectory still declares it. Persistent changes the cast makes go to
the current overlay, not the base.

Where the passage *between* two places carries content of its own — duration,
terrain, what comes into view when — that content belongs in a `connection` entity
rather than in either endpoint; see
[rules/authoring_entities.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_entities.md).

---

## Items

```yaml
---
id: item_brass_key
name: The Brass Key
type: item
owner: char_mara_vale    # optional; current holder
---
```

The body records what the item is, its salient properties, and any **persistent
state** that should carry across scenes (broken, lost, altered, consumed). Ownership
and state changes during play go to the current overlay. There is no mechanical
layer here — no charges, no binding rules — only continuity of who has what and what
condition it is in.

---

## Goals

Something a character or the cast is pursuing, avoiding, or entangled in — a
through-line with a state worth carrying between scenes. The span is the work's
business: a goal may live inside a single scene (*find the right moment to tell him*)
or run the length of the story. A work with a system layer on top may call these by
its own name (a job, a contract, a case); the engine knows only that they are
through-lines with a holder and a status.

```yaml
---
id: goal_the_missing_ledger
name: The Missing Ledger
type: goal
owner: char_mara_vale          # whose goal it is; omit for one the whole cast holds
scope: story                   # the work's own span vocabulary — e.g. scene | story
status: open                   # the work's own status vocabulary
characters_involved: [char_mara_vale]
locations_involved: [loc_harbor_steps]
---
```

`scope` and `status` carry **work-bound vocabularies** — one work's `open / resolved /
abandoned` is another's `active / complete`. The override declares the set; the engine
requires only that a goal have a status and that the set be closed.

The body records **what it is**, **what resolution looks like**, **how the cast comes
to know of it**, and its **state so far**. State changes during play go to the current
overlay; the base file describes the goal as it stands before any run touches it.

### Optional disclosure fields

A goal is often known to the cast under one description before a reveal reframes it —
the disappearance that turns out to be a killing, the errand that turns out to be a
theft. When a work tracks that, it carries the cast-facing title separately from the
true one:

| Field | Meaning |
|---|---|
| `known_as` | What the cast currently calls this, before the reveal. This is what surfaces in anything the cast reads. |
| `known_as_after` | What it is called once the reveal lands. |
| `reveal_trigger` | The in-fiction event that switches the two. |

These are **disclosure state**, not decoration: `known_as_after` is author-only until
its trigger fires, and naming it early is a leak of the same class
[rules/private_information.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/private_information.md) governs.

---

## Groups

Any standing collective the fiction treats as an actor: an order, a household, a
company, a faction. A work may file these under whatever domain name it prefers —
`groups`, `factions`, `organizations` — since the directory is a binding and `type:
group` is what identifies the kind.

```yaml
---
id: grp_customs_authority
name: The Customs Authority
type: group
members: [char_mara_vale]        # peer relation — the character's file names it too
---
```

The body records **what the group wants**, **how far its reach extends** (where it can
act, and where it merely has ears), **who speaks for it**, and its **standing toward
other groups**. Reach is the field scenes lean on hardest: it is what decides whether
the group can plausibly show up in a given place, and improvising it at scene time is
how a local outfit silently becomes a continental power.

Membership is a peer relation — a character listed in a group's `members` names the
group in their own file. A group whose disposition shifts at a chapter transition is
a chapter overlay; standing earned during a run is current-layer state.

---

## Events / Timeline

Events ground time-dependent claims and feed Calliope's time-anchor at scene start.

```yaml
---
id: event_storm_night
name: The Storm Night
type: event
time_tag: "day 12, evening"   # in the work's own time-anchor format
---
```

The body records **what happened** and, where relevant, who witnessed it. The
`time_tag` uses whatever time-anchor format the override defines (day index,
calendar date, scene counter, episode marker). Time-filtered characters include an
overlay or event entry only if its `time_tag` is at or before the scene's anchor;
continuous-memory characters accumulate linearly. The override points the loader at
the canonical event log and the active overlay set's event log.
