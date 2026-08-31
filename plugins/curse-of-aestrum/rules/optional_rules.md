---
id: rules_optional
name: Optional / Toggleable Override Rules
---

# Optional / Toggleable Override Rules

This file is the **catalog** of override rules a single campaign may opt into.
Each entry defines a toggle key, the RAW (Engine/Campaign) rule it overrides, the
exact behavior when ON, and any carve-outs.

The rule prose lives **here, once**. An individual campaign turns a rule on or off
via a flat toggle map in its instance file:

```
{{PROJECT_ROOT}}/campaign_state/<C>/rules/rule_overrides.md
```

Absence of that file, or absence of a given key, means the rule is **off
(default)** — i.e. standard Engine/Campaign behavior applies. Load order is
Engine → Campaign → Instance (last-loaded wins), per
[file_layering.md]({{PLUGIN_ROOT}}/rules/file_layering.md). When a toggle is `true`, apply the matching
behavior below as a drafting constraint for that campaign.

---

## `ignore_material_components`

**Default:** false (off).

**Overrides:** the 5e RAW requirement that a caster possess (and, where the spell
consumes them, expend) a spell's material components.

**When ON:** casters are treated as always having and expending the material
components a spell requires, even when those components are not in the caster's
inventory. The component requirement never blocks or interrupts a cast; narration
and adjudication proceed as if the component were present and consumed as normal.

**Carve-out — components with a listed gp cost still require actual possession.**
Any material component the spell lists with a gold-piece value (whether or not it
is consumed) is **not** covered by this override. The caster must genuinely have
it. This preserves [death_and_dying.md]({{PLUGIN_ROOT}}/rules/death_and_dying.md) unchanged: resurrection
diamonds (Revivify, Raise Dead, etc.) and similar costly materials apply per RAW
and refund at the next reset exactly as that rule describes. The same applies to
any other costed component (e.g. Glyph of Warding's consumed materials).
