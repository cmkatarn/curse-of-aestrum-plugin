---
id: rule_progressive_authoring
name: Progressive Authoring — Stubs and Deferred Facets
type: authoring_module
related_rules: [rule_file_layering, rule_random_character_generation, rule_connectable_companions]
---

# Progressive Authoring — Stubs and Deferred Facets

A character does not have to be fully authored to be playable. The **common path**
is: produce a runnable character fast (a concept plus a thin personality seed), mark
the rest as deferred, and flesh facets out later — on demand, or automatically when
play first needs them.

This is the **completeness axis** of the builder (the other axis is authoring
source — see [authoring_random.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_random.md)). Completeness has two values:

- **Complete** — everything filled now. Default for a protagonist.
- **Stub** — runnable concept + thin seed + explicit deferred-facet markers. Default
  for incidental and supporting characters, especially those spun up quickly.

The two axes compose: *random + stub* is the fast supporting-character path; *guided
+ complete* is a deep hand-build; *guided + stub* and *random + complete* are both valid.

---

## The `status` Field

Every character file carries a `status:` frontmatter field with a controlled
vocabulary:

| Value | Meaning |
|---|---|
| `stub` | Runnable concept + at least one personality seed + deferred facets present. |
| `developing` | Some deferred facets fleshed; others still open. |
| `complete` | No open deferred facets remain. |

A reader that encounters a legacy or free-form value treats any non-`complete` value
as **not complete** — do not force a rewrite of existing files; normalize
opportunistically.

A `complete` character may omit the field entirely (absence = complete).

---

## The Runnable Floor

A **stub is only valid if it is runnable** — i.e., it can be dropped into a scene and
played without further authoring. The floor is narrative readiness, not a data block:

- A **name**.
- A one-paragraph **concept** (the Overview) — who they are and what they want.
- At least one **personality or voice seed** — a trait, a manner, a one-line note on
  how they speak.
- Enough **appearance and role** that the narrator can put them on the page and the
  cast can react — what they look like at a glance, and what they're doing in the
  scene. Fine detail may be deferred via an `[appearance]` slot, but the
  at-a-glance impression must be addressed or explicitly deferred with a reason.

Everything else may be deferred: full backstory, the complete trait/ideal/bond/flaw
set, relationships, names of relations, any secret-state contents.

---

## The Deferred-Facet Section

A stub or developing character carries a trailing section with this exact heading:

```
## Open Slots — To Develop in Play
```

Each entry is a bullet with a light **category prefix** so the builder and play-time
skills can locate a facet by kind without heavy syntax:

```
## Open Slots — To Develop in Play

- **[relation]** <name/role> — <what is reserved>
- **[reveal]** <facet> — reserved for <trigger>
- **[bond]** <facet> — emergent; formed in play
- **[backstory]** <facet> — open until the story benefits
- **[appearance]** <facet> — author on demand
- **[name]** <facet> — reserved as a reveal
```

Controlled vocabulary: `relation`, `reveal`, `bond`, `backstory`, `appearance`,
`name`. The prefix is a convenience, not a schema requirement — a prefix-less bullet
is still valid prose.

---

## Where a Flesh-Out Writes — Base vs. Overlay

**Decide the write target before writing the facet.** Routing follows
[file_layering.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/file_layering.md):

- **Run-owned character, initial authoring → run base.** A character created for
  *this* run whose base sheet already lives in the run's own tree (the protagonist, a
  supporting character authored for this story), while `status` is still `stub` /
  `developing` and the facet is foundational definition (backstory, base appearance) —
  write to that character's own base file. Completing a not-yet-finished sheet is
  authoring, not play state.

- **Canonical character that ships with the work → overlay, never the base.** A canon
  character whose base lives in the shared content roster (the authored
  `[work]/characters/...` tree) **must not** have its base file edited by a flesh-out.
  Write the fleshed facet to *this run's* current overlay for that character. The
  shipped base stays pristine and reusable across runs — one run's development must
  never mutate shared canon. Different runs may resolve the same Open Slot differently
  in their own overlays.

- **Anything surfaced or created during play → overlay, any character.** A reveal in a
  scene, a fact the play established (procedure (b)'s rule governs here too).

**When in doubt, prefer the overlay.** Editing a base file is only for deliberate
initial authoring of a run-owned, not-yet-complete character.

For a canon character fleshed to the overlay: do **not** edit the base to strike the
Open Slot bullet or bump `status` — leave the base's authored stub record intact and
record the resolution in the overlay (the merged base+overlay view treats the slot as
filled for this run).

---

## Procedure (a) — On-Demand Flesh-Out

When the user asks to develop a specific facet ("develop her bond", "name the
handler", "give him a backstory"):

1. `Read` the file, including its `## Open Slots` section.
2. Locate the matching `[category]` bullet.
3. Author the facet **consistent with everything already established** — never
   contradict locked frontmatter, the resolved concept, established backstory, or any
   already-resolved facet.
4. **Determine the write target** (see *Where a Flesh-Out Writes* above), then write
   the facet into its proper body section in that file — the run base for a run-owned
   character still in initial authoring; otherwise the current overlay.
5. Update the Open Slots tracking **in the same file you wrote to.** If you wrote to a
   base you own (run-owned, initial authoring), remove the resolved bullet there. If
   you wrote to an overlay (canon character, or a play-surfaced fact), record the
   resolution in the overlay and leave the base's bullet untouched.
6. Nudge `status` on the file you own: a run base with no Open Slots left becomes
   `complete`, otherwise `developing`. Never bump a shipped canon base's `status` from
   a run — track that run's progress in its overlay.

---

## Procedure (b) — Play-Triggered Auto-Fill

When a scene needs a deferred facet that has not been authored (the protagonist asks
a character their mother's name and a `[name]` slot reserves exactly that):

1. The play-time skill (scene) detects the gap by matching the need against the
   `## Open Slots` categories.
2. Auto-fill the minimum needed, consistent with established canon.
3. **Write the new fact to the current overlay, not the base file** — a
   play-surfaced fact is current-layer state per [file_layering.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/file_layering.md).
   The base/chapter sheet is not edited by play.
4. Append a one-line note that the facet was filled in play (date / scene).
5. Update the `## Open Slots` section and nudge `status`.

This keeps auto-fill obedient to the three-layer model rather than inventing a new
write path.
