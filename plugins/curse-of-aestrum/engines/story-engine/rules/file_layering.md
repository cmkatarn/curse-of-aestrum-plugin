---
id: rule_file_layering
name: File Layering — Base, Chapter, Current
type: meta_convention
---

# File Layering — Base, Chapter, Current

A layered file model so that location, character, and group state can evolve cleanly
across a work without rewriting base files.

## The Three Layers

| Layer | Purpose | Required |
|---|---|---|
| **Base** | The canonical start state. Authored once, edited rarely. The world as it exists when a new run begins. | yes |
| **Chapter** | A planned future state that applies once chapter N begins. Overlay on base. Authored deliberately as the work's chapter-level transitions are designed. | only if the work has chapters |
| **Current** | The live, accumulating state. Choices, observed events, changes the cast made. Overlay on whatever chapter is active. | yes |

A work must bind **base** and **current**. The **chapter** tier is optional: a work
whose parts are self-contained — no chapter progression to plan for — binds two tiers
and the load order below collapses to base → current.

## Layer Names vs. Directory Names

<!-- anchor: file-layering.tier-binding -->

The three names above are **layers**, not paths. Every rule in this engine, and every
rule in any layer above it, is written in terms of the layer — *"written to the
current overlay"*, *"never edited in base"*. Which **directory** holds each layer is
the consuming work's business, declared once in its override.

| Layer | Bound by the override to a path such as |
|---|---|
| **Base** | `[work]/[domain]/[file].md`, or a dedicated immutable tree |
| **Chapter** | `[work]/[domain]/chapter_N/[file].md` |
| **Current** | a per-run overlay tree under the work's own state directory |

Two works will spell these differently, and both are conformant — one may put current
state in a tree beside its authored canon, another in a per-run state tree kept
outside the authored content entirely. **This engine never names those directories**;
a shared-layer file that hardcodes one work's directory name silently excludes every
work that spells it differently.

`[domain]` is one of: `locations`, `characters`, `items`, `events`, `goals`,
`groups`, `lore`, etc. — again as the override names them.

## Load Order

The skill (scene, or any authoring/play skill) loads the layers in this order and merges them:

**During Chapter 1:**
1. Read **base** file
2. Read **current** overlay (if present)
3. Merge

**During Chapter 2 (or any later chapter):**
1. Read **base** file
2. Read **chapter_N** overlay (if present, for the active chapter)
3. Read **current** overlay (if present)
4. Merge in that order

The chapter overlay loads *between* base and current. Current always wins on conflicts because it represents what has actually happened in the run. Chapter overlays describe the world's planned state for that chapter — current overlays describe what the cast has done to it within that chapter.

## Examples

- **A village peaceful in Chapter 1 and burned in Chapter 2.** Base file describes the peaceful village. The chapter-2 overlay describes the burned state. If the cast further damaged a specific building, that's a current-layer entry on top.
- **A character alive in Chapter 1, dead by Chapter 2.** Base file is the living character. The chapter-2 overlay marks them deceased and notes the cause. If the cast witnessed or caused the death, the current layer records the circumstances.
- **A group whose disposition shifts at a chapter transition.** Base file is the start-state disposition. The chapter-2 overlay revises its reach and posture. The current layer tracks run-specific standing effects.

## When to Use Each Layer

- **Base** — anything that is true at the start and would be true regardless of the cast's choices. Geography, architecture, established characters, default faction relations.
- **Chapter** — anything that *will* be true at chapter N regardless of the cast's choices. Planned timeline events. Predetermined state changes. Off-screen developments that have unfolded between chapters. Authored ahead of time as part of the work's design.
- **Current** — anything that has *actually happened in play.* Choices, observed reveals, deaths, bonds, betrayals, lost items, gained allies. The literal play record.

## Authoring Rules

- **Do not duplicate base content in a chapter overlay.** Overlays describe *what changed*, not *what is*. If something is unchanged from base, the overlay says nothing about it.
- **Do not put a protagonist's run-state in any layer except the current one.** A protagonist's reactions, discoveries, and choices all go to the current overlay. Base and chapter files describe the world independent of any particular run.
- **Chapter overlays are authored, not accumulated.** When you finalize how the world has changed by chapter N, you write that chapter's overlay deliberately. Do not let current-layer overlays drift into describing chapter-state changes.
- **Play-triggered facet auto-fill writes to the current layer.** When a deferred facet on a stub/developing character is filled because play needed it (see [authoring_progressive.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_progressive.md), procedure (b)), the new fact is current-layer state — write it to the current overlay, not back into the base/chapter file.

## Migration Note

When existing current-layer files contain entries that describe **chapter-state changes rather than play events**, those entries should eventually be moved to chapter overlays once the chapter tier is fully wired up in the relevant skills. A work with no chapter tier has nothing to migrate.
