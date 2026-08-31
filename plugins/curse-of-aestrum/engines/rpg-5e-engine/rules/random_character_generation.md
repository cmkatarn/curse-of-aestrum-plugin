---
id: rule_random_character_generation
name: Random Character Generation — 5e Layer
type: authoring_module
related_rules: [rule_party_aligned_npcs]
---

# Random Character Generation — 5e Layer

The D&D 5e overlay on Aria's neutral
[authoring_random.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_random.md), which owns
the genre-agnostic procedure: the two sub-modes (guided / fully random), the
diversity bias, the anti-conflict contract, and the output-surface shape.

**Read Aria's file first.** This file adds only the 5e specifics: concrete party
role coverage, the duplicate-build rejections, and the 5e build line. Used by:

- `create-character/core.md` — a single character (PC or NPC), Random source.
- `create-party/core.md` — each random slot, with the multi-slot layer on top.

---

## Party Form — 5e Role Coverage

Extends Aria's *Cast form* cross-slot comparison with concrete 5e build axes.
When comparing across party slots (the create-party caller):

- Reject a **race** already present unless the user requested duplicates.
- Reject a **class** already present.
- Aim for at least one of each role across the party: **frontline melee**,
  **ranged / skirmisher**, **arcane caster**, **divine caster or support**,
  **skill / utility**. Weight uncovered roles higher on each pick.
- Backgrounds: avoid duplicates. Prefer backgrounds with strong hooks per the
  override's table for at least 2/5 of randomized slots.

A single-character caller with no party context skips the comparison clauses
(Aria's single-character bias still applies).

---

## Output — 5e Build Line

A Random build feeds back into the standard 5e builder stages (ability scores
through backstory) and the standard output template. The completeness axis
(complete vs. stub, see
[authoring_progressive.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_progressive.md))
decides how much gets filled now.

Surface a rolled character briefly as plain markdown, using the 5e build line:

```
<Name>
<Race> <Class> (<Subclass>), <Background>.
Hook: <one-line of how they tie into the region per the override's hook table>.
```
