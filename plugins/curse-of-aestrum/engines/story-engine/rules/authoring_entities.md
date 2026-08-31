---
id: rule_entity_authoring
name: Entity Authoring — Places, Things, Goals, Groups
type: authoring_module
related_rules: [rule_file_layering, rule_progressive_authoring]
---

# Entity Authoring — Non-Character Entities

Authoring procedure for every entity that is **not** a character: locations, items,
goals, groups, and the connections between them.

[FRONTMATTER.md]({{PLUGIN_ROOT}}/engines/story-engine/FRONTMATTER.md) is the *data spec* — what fields a file carries
once it exists. This file is the *act of creating one*: where it goes, what its id
is, and what else has to change when it lands.

Character authoring has three modules ([authoring_progressive.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_progressive.md),
[authoring_connectable.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_connectable.md),
[authoring_random.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_random.md)) because a character is largely
self-contained — one can be authored without opening another file. A non-character
entity is not. It is defined mostly by **what it is attached to**: a location by its
neighbors and its residents, an item by its holder, a goal by its participants,
a group by its members. Authoring one is therefore always a **graph edit**, and its
failure modes are graph failures.

---

## The Four Failure Modes

<!-- anchor: entity-authoring.integrity -->

Every rule below exists to prevent one of these. They matter because none of them
fails a load — each silently produces a *different world* depending on which file the
loader entered from.

| Failure | Shape |
|---|---|
| **Dangling reference** | A file cites an id that no file defines. The loader finds a name with nothing behind it, and either improvises the entity or drops it. |
| **Alias drift** | One entity acquires a second id — a synonym, a reordering, a shortened slug. Half the graph points at a ghost; both halves look correct in isolation. |
| **One-way edge** | A names B as a neighbor; B does not name A. Enter from A and the connection exists; enter from B and it does not. |
| **Key drift** | The same relation spelled with two different field names in different files. The loader reads one and misses the other. |

A work that authors entities by hand accumulates all four. Preventing them is far
cheaper than repairing them: a repair has to decide which of two ids was the real
one, and by then that is often no longer recoverable from the files.

---

## Invariants and Bindings

<!-- anchor: entity-authoring.bindings -->

Two works will not spell their entity data the same way, and they do not have to. This
engine separates what it **requires** from what a work **names**.

| Required — the invariant | Named by the override — the binding |
|---|---|
| A reference resolves to exactly one entity. | How uniqueness is guaranteed: a type prefix in one shared namespace, or a bare slug scoped by its domain directory. |
| An id is minted once and never restated; other names for the same entity are registered as aliases. | — |
| Containment is declared on the child, with **one** key used for every kind. | What that key is called. |
| Peer relations are declared on both ends. | What each relation is called. |
| Every entity's kind is resolvable, and by one rule throughout the work. | Whether kind comes from an explicit `type` or from the domain directory — and, under the latter, what `type` carries instead. |
| Each write goes to the correct **layer**. | Which directory each layer lives in. |
| A goal carries a status drawn from a closed set. | What the statuses are called. |

Where a rule below names a field or a directory, read it as illustrative unless it
appears in the left column. **A shared-layer file that hardcodes one work's spelling
silently excludes every work that spells it differently** — which is the same defect as
the entity drift this file exists to prevent, committed one level up.

---

## STEP 1 — Does it already exist?

Before minting anything, search the entity tree **by display name and by every
plausible id spelling** — word order reversed, the article dropped, the container
prefixed or not (`loc_harbor_steps` / `loc_steps_harbor` / `loc_the_harbor_steps`).

Most alias drift is authored by someone who was confident the entity was new. An
entity mentioned in another file's prose, or cited in another file's frontmatter,
already exists as far as the graph is concerned — even if it has no file yet. In that
case you are **completing** it, not creating it: adopt the id already in use rather
than minting a better one.

If the id already in use is genuinely wrong, rename it in one pass across every file
that cites it. Never leave both spellings live.

**When the second name is real, register it as an alias.** Cast and prose often carry
more than one name for the same entity — a formal name and what everyone actually
calls it. That is one entity with an `aliases` list, not two entities. Registering the
alternates is also what makes this step work next time: a search by name finds the
entity under any of its names, and the alias-drift failure never gets its opening.

---

## STEP 2 — Mint the id

Mint per the work's own id binding. Where the work carries type-prefixed ids in one
shared namespace — the style this engine's examples use — that is `<type>_<slug>`:
`char_`, `loc_`, `item_`, `goal_`, `grp_`, `event_`, `conn_`. Where it scopes ids by
domain directory instead, the bare slug is the id.

- The slug derives from the display name: lowercase, underscores, articles dropped.
  *The Harbor Steps* → `loc_harbor_steps`, or `harbor_steps` filed under the locations
  domain.
- **Whichever binding applies, the id must resolve to exactly one entity.** An
  unprefixed id in a flat shared namespace does not — nothing can resolve it by kind,
  and two domains will eventually collide on the same slug.
- **An id is minted once and never restated.** The display name may change freely;
  the id does not follow it. If a rename is genuinely required, it is a tree-wide
  edit (STEP 1), not a new file.
- **A second name for one entity is an alias, not a second id** — see STEP 1.

---

## STEP 3 — Choose the layer before writing

Placement follows [file_layering.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/file_layering.md). The question is not where the
entity sits in the fiction — it is **who owns it**:

- **Authored canon** — part of the work as shipped, true at the start of every run →
  the work's **base** tree. A deliberate later-chapter state for it → a **chapter**
  overlay.
- **Run-created** — brought into being because *this* run needed it (a place the cast
  built, a thing they made, a goal they took on, a group they founded) → that run's
  **current** overlay, as a self-contained file, in whichever directory the override
  binds that layer to.

**A run never writes into the shipped canon tree.** This is the boundary
[authoring_progressive.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_progressive.md) draws for a canon character's
flesh-out, applied to whole entities: shared canon stays pristine and reusable, and
two runs may hold different versions of the world without colliding.

Promotion from run-created to canon is an authoring decision made deliberately
between runs — never a side effect of play.

---

## STEP 4 — Write the file

Fields and body sections come from [FRONTMATTER.md]({{PLUGIN_ROOT}}/engines/story-engine/FRONTMATTER.md). Two things
carry over from character authoring:

**The completeness axis applies.** `status: stub | developing | complete` and the
`## Open Slots — To Develop in Play` section work identically for non-character
entities — see [authoring_progressive.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_progressive.md). A stub location
with three named fixtures and a deferred `[layout]` slot is a legitimate, runnable
file, and strictly better than no file: the alternative is improvisation at scene
time with no record of what was improvised.

**Each kind has its own runnable floor** — the minimum at which a scene can use the
file without inventing:

| Kind | Runnable floor |
|---|---|
| **Location** | A name; what a character registers on arrival; its exits and its container; who is normally present — even if that is *no one*. |
| **Item** | A name; what it is and what it looks like; who holds it now, or where it rests. |
| **Goal** | A name; what completion means; who is involved; how it becomes known. |
| **Group** | A name; what it wants; how far its reach extends; who speaks for it. |

An empty relation is a **statement**, not an omission. A location with
`characters_present: []` asserts that nobody is normally there. Leaving the field off
entirely asserts nothing, and the loader must then guess. Author the empty list.

---

## STEP 5 — Wire the graph, both directions

<!-- anchor: entity-authoring.relations -->

Relations come in two shapes, governed by different rules. Confusing them is the
source of most one-way edges.

### Containment — declared on the child only

A sub-area within a place, an entry within a collection: the child names its
container with **`parent`**, and the container names nothing.

```yaml
id: loc_harbor_steps_undercroft
parent: loc_harbor_steps
```

One key, one direction, one source of truth. A container's children are derivable by
scanning for the containment key, so listing them on the container would be a second
copy that can go stale.

The key's *name* is the work's binding — `parent` here, something else elsewhere. What
is invariant is that there is exactly **one** of it, used for every entity kind.
**Never introduce a second containment key**: a `parent_<kind>` variant alongside
`parent` is key drift, and it splits the graph in half — half the tree declares
containment in a way the other half's reader does not look for.

### Peer connection — declared on both ends

A road between two places, a membership between a character and a group, a holder for
an item: there is no natural owner, so **both files carry the relation**.

```yaml
# in loc_harbor_steps
connections: [loc_fishmarket, loc_customs_house]

# in loc_fishmarket
connections: [loc_harbor_steps, ...]
```

`connections` is this engine's example spelling; a work may call its peer link
whatever it likes, and the reciprocity requirement is unchanged by the name.

A peer relation authored on one end only is a bug, not a shorthand. When you add a
neighbor, open the neighbor's file in the same edit — not later. This is the one
rule here with no partial credit: a half-authored edge is worse than no edge, because
it reads as authored fact from one side and as absence from the other.

### Every cited id must resolve

An id in frontmatter is a promise that some file defines it. Before finishing an
entity edit, confirm each id you wrote is either defined somewhere in the tree or is a
**declared soft pointer** — a target the work has documented as intentionally
unresolved (a run-scoped overlay path, a region-scale name the work never files
individually). Soft pointers are legitimate; *undeclared* soft pointers are
indistinguishable from dangling references.

---

## STEP 6 — Verify before you stop

An entity edit is complete when:

1. The id is prefixed, unique, and collides with nothing already in the tree.
2. The layer matches ownership — canon to base, run-created to the current layer.
3. Every peer relation is present on both ends.
4. Every containment is declared with `parent`, on the child, and nowhere else.
5. Every id cited resolves, or is a declared soft pointer.
6. Relations that are genuinely empty are written as empty, not omitted.

---

## Connections as entities

Usually a connection is nothing more than reciprocal fields. Promote it to a file of
its own — `type: connection`, id `conn_<a>_<b>` — when **the edge itself carries
content** that neither endpoint can hold: how long the passage takes, what the terrain
is, what is visible from where along it, what is met on the way.

```yaml
---
id: conn_harbor_steps_fishmarket
name: The Fishmarket Stair
type: connection
endpoints: [loc_harbor_steps, loc_fishmarket]
---
```

The endpoints still list each other in `connections` — a connection file *supplements*
the edge, it does not replace it.

The reason to promote is that traversal content is otherwise homeless. Written into
one endpoint it is invisible from the other; improvised at scene time it contradicts
the authored geography while looking correct on the surface, because the destination
name is right and only the journey is wrong. A journey is implicit world-building
about the place it arrives at, and it is authored content like any other.

---

## When a cited entity has no file

If a scene or an authoring pass reaches an entity that other files reference but
nothing defines, that entity is **underspecified, not absent**. Do not silently invent
it, and do not quietly drop the reference — either move alters the work's world
without leaving a record.

Surface it instead: name the entity, name the files that cite it, and let the
consuming work decide whether to author it, alias it onto an existing entity, or
declare it a soft pointer. A work may hold a curation rule that makes this mandatory —
its set of places closed, its set of groups fixed. This engine does not know which, so
it asks rather than assumes.
