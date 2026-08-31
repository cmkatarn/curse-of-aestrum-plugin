---
id: rule_random_character_generation
name: Random Character Generation
type: authoring_module
related_rules: [rule_progressive_authoring, rule_connectable_companions]
---

# Random Character Generation

Shared procedure for rolling a character's concept and basic background when the
**authoring source is Random** (you make the choices) rather than guided or
user-provided.

This file is work-agnostic. The consuming work's override supplies the hook tables
and the anti-conflict list this procedure honors.

---

## Two Random Sub-Modes

**Guided random.** The user gives hints — any subset of the work's defining axes
(e.g. sex, origin, role, archetype, concept). Honor every hint. Fill only the gaps
with biased-random choices per the rules below.

**Fully random.** No hints. Every choice is rolled by you under the same bias.

In both, pick a hook from the override's hook tables that matches the resulting
background, exactly as a guided build would.

---

## Diversity Bias

When rolling a character's defining axes, skew toward internal variety so the
character is tonally and dramatically distinct.

**Single-character form** (no cast context — building one character):
- Bias toward a concept that is *internally* coherent and not a genre default. Avoid
  reflexively rolling the most common archetype for the setting.
- If the character is being added to an existing cast the caller names (e.g. "someone
  to travel with this group"), and the caller supplies the existing members, apply
  the cast form below against those members.

**Cast form** (building or extending a group, comparing across slots):
- Reject an archetype already present unless the user requested duplicates.
- Aim for variety across the cast on the axes the work cares about — temperament,
  register, social role, relationship to the protagonist, background. Weight
  under-represented axes higher on each pick.
- Backgrounds / hooks: avoid duplicates. Prefer backgrounds with strong hooks per the
  override's table for at least part of the randomized cast.

The cast form is a superset: it adds cross-slot comparison to the single-character
bias. A caller with no cast context simply skips the comparison clauses.

---

## Anti-Conflict Rules

The override defines the anti-conflict list. **Never randomly assign** anything the
override flags as "never randomized" — typically including:

- Blood relations to load-bearing canon characters.
- Hook tables flagged as "by user request only."
- Patrons / factions / origins flagged as "intentionally not random."
- Any origin inside a story-internal restricted region.
- Any character who claims pre-existing knowledge of canon secrets.
- Any character whose backstory requires knowledge of the protagonist.

If the user explicitly requests something on the override's anti-conflict list via a
guided-random hint, allow it only per the override's exception rules.

---

## Output

A Random build feeds back into the standard builder stages (concept through
background) and the standard output template. Random is a *source* of choices, not a
different file format — the completeness axis (complete vs. stub, see
[authoring_progressive.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_progressive.md)) decides how much gets filled now.

Surface a rolled character briefly as plain markdown:

```
<Name>
<one-line concept: archetype / role / origin>.
Hook: <one line of how they tie into the work per the override's hook table>.
```
