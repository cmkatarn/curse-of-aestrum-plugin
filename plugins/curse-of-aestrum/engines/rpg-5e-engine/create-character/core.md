# Create Character — RPG 5e Engine Core

The engine body of the character-building skills. Generic D&D 5e
character authoring — **PCs and NPCs** — decoupled from any specific
campaign. A consuming game wires this in via a thin shell `SKILL.md`
(one for PCs, optionally a second for NPCs) that loads:

1. This file (the 5e walkthrough).
2. The game's own override file (spoiler discipline, blood-relation
   restrictions, faction hook tables, anatomy extensions, output path
   conventions).

The same spine builds a PC and an NPC; **STEP 0** picks the subject type
and switches on a small set of NPC-only concerns. This file knows nothing
about specific settings, factions, or named NPCs. Everything
campaign-specific is supplied by the override.

This walkthrough has **two axes** (set in STEP 1):

- **Authoring source** — *provided* (user pastes a sheet), *guided* (you
  walk them through it), or *random* (you roll it, per
  `rules/random_character_generation.md`).
- **Completeness** — *complete* (fill everything now) or *stub* (runnable
  mechanics + thin seed + deferred facets, fleshed out later, per
  `{{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_progressive.md`).

They compose freely. Quick NPC creation is *random + stub*; a deep PC
build is *guided + complete*.

---

## Hard Rules — Read First

### Interaction style

**Never assume a desktop client.** Do not use structured-option pickers
(AskUserQuestion-style UI). Present all choices as plain markdown —
numbered lists, headings, code blocks. The user is reading text only.

### Spoiler discipline

A new PC is an outsider to the campaign's standing canon. The override
file defines the specific knowledge boundary — what canon facts must not
be revealed in conversation, sheet content, or backstory hooks. **Apply
the override's spoiler list rigidly.** Recommend backgrounds and hooks
without explaining why they fit — never lecture the player about which
canon thread the hook is adjacent to.

### Canon-load-bearing NPCs

The override file may name specific NPCs whose arcs are structurally
load-bearing and to whom blood relation by a new PC would break the
campaign. **Never assign or suggest blood relation to any NPC the
override lists as load-bearing.** The override may also define narrow
exceptions (a specific lineage that is allowed only if the user volunteers
it without prompting). Honor those exactly as written.

### Canon PC arcs are fair game

The existing campaign PCs have arcs, factions, items, and backstory
elements. **A new character has no knowledge of those PCs and is not
constrained by their niches.** A new dwarf can be a member of any clan; a
new warlock can have any patron; backgrounds may overlap with canon PCs
without comment. The new character simply does not know the canon PC
exists.

When a hook overlaps with a canon PC's territory, **do not** mention
which canon PC shares the element, do not summarize the canon PC's arc,
and do not steer the player around it. Just write the character.

### PCs vs NPCs

A few concerns apply only when the subject is an NPC (set in STEP 0):

- **Control.** An NPC carries a `control:` field — `player` or `claude` —
  recording who drives it in play. Ask when it is not implied. PCs do not
  carry this field.
- **Secret / hidden state.** NPCs may hold state the player is not told
  (a hidden agenda, a concealed identity, a bounty). The override decides
  whether and how such state is seeded, and it is gated on the control
  mode — secret state is only coherent for a `claude`-controlled NPC. Mark
  such a sheet `secret_state: true` and keep the hidden material in a
  clearly DM-only section. Never seed secret state into a PC.
- **Connectability.** A *companion* NPC (one built to travel with the
  party) must be authored to be reachable — see STEP 10 and
  `{{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_connectable.md`.

PCs are owned by the player; never write a PC with hidden agendas against
its own player or with knowledge the player shouldn't have.

---

## Output Location

The override file specifies the output path convention, **per subject
type**. The state directory, campaign slug, instance identifier, and
slug convention (typically lowercase `firstname_lastname`) are all
override-defined, as is the list of directories the skill must **never**
write to (the canonical roster). Typical shapes:

- **PC** — a per-campaign, per-instance saved location, e.g.
  `<state-dir>/<campaign-slug>/party/saved/<instance>/<slug>.md`.
- **NPC** — the campaign's NPC tree, e.g. a companion base file at
  `<state-dir>/<campaign-slug>/npcs/<slug>.md` with play-surfaced state in
  the `saved/` overlay, or an incidental NPC written straight to the
  `saved/` overlay.

Create the directory if it does not exist. Honor the override's
write-scope restrictions absolutely.

---

## STEP 0 — Subject Type

Determine what is being built:

- **PC** — player character. Owned by the player.
- **Companion NPC** — an NPC built to travel with the party over time.
  Connectability rules apply (STEP 10).
- **Incidental NPC** — an NPC who is not a standing companion (a contact,
  a one-scene figure, a minor recurring face).

Usually the invoking shell or the request makes this obvious (a PC-creation
skill vs. an NPC-creation skill; "build me a companion" vs. "I want to
play a…"). If it is genuinely ambiguous, ask in one plain line. Set the
`type:` frontmatter accordingly (`player_character`, `npc_companion`, or
the override's incidental-NPC type).

The subject type sets the **defaults** for STEP 1:

- **PC →** guided + complete (players want ownership and a finished sheet).
- **NPC →** random + stub (the fast path: roll it, make it runnable, flesh
  out in play). The user can override either axis.

---

## STEP 1 — Pick the Two Axes

A build is defined by an **authoring source** and a **completeness target**.
State the default for the subject type in one line and let the user adjust.

**Axis 1 — Authoring source:**

```
1. Provided — you paste a sheet (stats / inventory / spells / background)
   and I convert it to the campaign format.
2. Guided — I walk you through 5e creation step by step, weaving in
   region hooks.
3. Random — I roll the build and a basic background for you.
```

If the request already includes a full sheet, assume **Provided**. If it
names only a concept ("a dwarf cleric"), assume **Guided** for a PC or
**Random** for an NPC, and confirm.

**Axis 2 — Completeness:**

```
A. Complete — fill everything now.
B. Stub — runnable mechanics + a thin personality seed now; flesh out
   the rest in play.
```

State the composed default plainly, e.g. *"I'll roll her up as a runnable
stub and we'll flesh her out as she comes up — say the word if you'd
rather build her in full."* Proceed unless the user redirects.

Also ask, if not yet known (batch as one plain-text block, not a picker):

- **Starting level** (default 1, or match an existing party).
- **Ability score method** for guided/random — standard array
  (15,14,13,12,10,8), point buy (27 points), or 4d6-drop-lowest.

**Routing:**

- Provided → STEP 2A.
- Guided → STEP 2B.
- Random → STEP 2C.

Completeness (A/B) is applied at STEP 4 regardless of source.

---

## STEP 2A — Provided Source

1. Accept whatever the user pastes. Don't reformat their numbers —
   preserve their choices exactly.
2. If anything required for the campaign file is missing (race, class,
   level, alignment, ability scores, HP, AC, equipment list, name), ask
   for the missing pieces in **one batched plain-text question**.
3. Offer optional campaign hooks (see STEP 3) but do NOT impose them —
   for a PC, the player owns this character.
4. Confirm content rating context if the user wrote backstory with
   mature themes. The override defines the rating taxonomy and default.
5. Apply the override's spoiler discipline. Reject (with explanation)
   any backstory element that requires canon-internal pre-knowledge or
   violates the override's blood-relation rules.
6. Build the file (STEP 4).

---

## STEP 2B — Guided Source

Walk through these stages in order. Confirm each before moving on. Keep
each prompt focused — one decision at a time unless the choices are
tightly coupled. All prompts are plain markdown.

1. **Concept** — One-line vision.
2. **Race + subrace** — Standard 5e races plus published subraces. Warn
   the player (without explanation) if their race carries signatures the
   override flags as "reads loudly" in this setting. Reject races whose
   features would break the campaign premise (e.g., at-will plane-shift
   in a sealed setting, innate time manipulation in a time-loop setting)
   per the override's restricted list — find a reskin if the player wants
   the flavor.
3. **Class + subclass** — Standard 5e classes. Non-standard / homebrew
   is allowed if the player is confident, but apply the override's
   spoiler discipline: do not let the player select a feature that
   requires them to already know things they shouldn't know. Reject
   features that would short-circuit the campaign premise per the
   override's restricted list. Reskin if needed.
4. **Ability scores** — Use the chosen method. Show the rolled /
   assigned numbers + racial modifiers + final stats.
5. **Background** — Standard 5e backgrounds. When the player picks one,
   follow STEP 3 to offer regional hooks before locking it in.
6. **Skills / proficiencies / languages** — From class + background +
   race.
7. **Equipment** — Class + background starting equipment. Ask if they
   want to take starting gold instead of the package.
8. **Spells** (if applicable) — Cantrips known, spells known / prepared.
9. **Combat stats** — HP (max at level 1, then average or rolled for
   higher levels — ask), AC, initiative, speed, attack bonuses, save DCs.
10. **Personality** — Trait, ideal, bond, flaw (from background table or
    custom). `Read` `{{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_personality.md` and author
    against it: the 5e four are a *format*, not a generator, and filled in as
    adjectives they produce a character the narrator plays from its own defaults.
    Its floor — standing want, guarded thing, contradiction, pressure behavior
    (boredom included), and what the voice does under stress — is what this step
    owes, whatever the four fields are called on the sheet. **If the subject is a
    companion NPC,** also `Read`
    `{{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_connectable.md` and apply it to the flaw/bond
    design: the companion must be reachable, and its flaws must complicate
    bonds rather than prevent them.
11. **Name + appearance** — Brief. **Then run the anatomy pass — see
    STEP 3.5 below.** Do not consider the appearance section complete
    until the pass is done.
12. **Backstory** — Tied to the hook from STEP 3. For a PC, outsider
    perspective only — the character has heard rumors of the campaign
    region but no specifics. For an NPC, the override governs origin and
    knowledge (an NPC may legitimately originate inside the region or hold
    knowledge a PC could not, where the override allows it).

---

## STEP 2C — Random Source

`Read` `{{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_random.md` (the neutral procedure:
sub-modes, diversity bias, anti-conflict contract) **and** its 5e overlay
`rules/random_character_generation.md` (party role coverage + the `<Race>
<Class> (<Subclass>)` build line), then follow them to roll the build and a
basic background. Honor any hints the user gave (guided random) or roll the
whole thing (fully random), under the diversity bias and the override's
anti-conflict list described there.

Then walk the STEP 2B stages **silently**, making each decision yourself,
consistent with the rolled build — pick a campaign hook from the override's
tables that matches the rolled background / race / class (STEP 3), run the
anatomy pass (STEP 3.5), and apply
`{{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_personality.md` at the personality stage — plus
`{{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_connectable.md` for a companion NPC. A rolled
character has nobody pushing back on it, so the personality rule's bleed test is what
keeps a random build from staying a build line. The anatomy pass is
**not** skippable for random characters.

Surface the result briefly before writing (the format is in
`random_character_generation.md`), then build the file (STEP 4) at the
chosen completeness.

---

## STEP 3 — Campaign Hooks (Guided / Random)

When a player picks a background, race, or class, offer regional ties
**as suggestions, not requirements**. Frame as "Want a hook into the
region? Some options…". Player may decline and write something
disconnected — that's fine, set `faction: none`.

**Offer 2–3 options, not all of them.** Match the player's stated
concept. Always present "unconnected to any of this" as a valid choice.

The override file provides the **concrete hook tables**:

- **Background → faction hooks** for this setting.
- **Race → cultural / clan hooks** for this setting.
- **Class → patron / institution hooks** for this setting.

Apply the override's tables. The engine does not prescribe specific
factions or hooks — those are setting content.

### Hook Etiquette (engine-level)

- **2–3 options per offer.** Match the concept.
- Always present "unconnected to any of this" as a valid choice.
- If a hook is accepted, write it into the backstory and set `faction:`
  accordingly.
- Never lock the character into knowing campaign secrets.
- Never reference canon PC arcs even when the hook overlaps.

---

## STEP 3.5 — Anatomy Pass (Required Before Finalizing Appearance)

Before the appearance section is considered complete — in **any** source
mode (provided, guided, or random) — run the anatomy pass. The pass is
**innate-knowledge-first**: you already know what these races look like;
the reference file is consulted only for this setting's *departures*,
*depth conventions*, and any *pinned* entries — not as the source of the
feature list.

**This pass runs even for a stub.** A stub may defer appearance *details*
via an `[appearance]` Open Slot, but the race-distinguishing features must
be addressed or explicitly deferred with a reason (per
`{{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_progressive.md`, the runnable floor).

**Procedure:**

1. **Recall** the character's race's distinguishing features from canon
   (PHB / Volo's / Monster Manual / Mordenkainen's) — the features prose
   tends to drop: tails, horns, wings, claws, non-human eyes, lineage
   marks, build, sensory organs. Do this from knowledge, for **any** race.
2. **Consult** the race anatomy reference (the engine's own
   `rules/race_anatomy.md`; the consuming game's `SKILL.md` resolves the
   path into the engine) for: this setting's **departures** from baseline,
   the campaign's required **depth conventions** (e.g. how much detail a
   tiefling tail needs), and any **pinned** entry for this race. A race
   **absent** from the file is **not** a blocker — proceed from recall.
   Pin a new section there only if a departure, an unusual depth need, or
   cross-session consistency warrants it; this is optional and never gates
   finishing the character.
3. For each recalled (and depth-convention) feature, confirm the
   character's appearance section either:
   - **Names the feature** with the character's specific choice in or near
     the canonical range, *or*
   - **Explicitly flags the feature as a deliberate world-departure** in
     the appearance section or frontmatter, with a brief reason.
4. If any feature is silently omitted, raise it to the user before
   finalizing. Plain markdown question, all gaps in one batched message:

   ```
   Your character's race calls out the following features that the
   appearance section doesn't yet address:

   - <feature 1>
   - <feature 2>
   - ...

   For each, either describe how this character's looks (within the
   typical range) or confirm a deliberate departure (e.g.,
   "tailless — born without one").
   ```

5. Apply the user's answers to the appearance section. Do not finalize
   the file until all features are addressed.

**Why this step exists:** prose write-ups consistently drop the features
that distinguish a race from human baseline — most often the tail on
tieflings, the lack of tail on dragonborn, the lineage marks on aasimar
and genasi, the lithoderms on goliaths. This step catches those
omissions at creation time instead of when the character first appears
in a scene three months later.

---

## STEP 4 — Write the File

Use this template. Match the conventions of existing files in the
consuming game (the override may add fields or sections).

**Frontmatter by subject type.** The PC block is the base. An NPC swaps
`type`, drops `identity_known_to_party`, and adds the NPC-only fields:

- **PC:** `type: player_character`, `identity_known_to_party: true`.
- **NPC:** `type: npc_companion` (or the override's incidental-NPC type);
  add `control: player|claude`; add `traveling_with_party: true` for a
  companion; add `secret_state: true` **only** if the override seeded
  hidden state (claude-controlled NPCs only).

**Completeness field.** Add `status:` per `{{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_progressive.md`
— `stub`, `developing`, or `complete`. A complete character may omit it.

```markdown
---
id: <pc|npc>_<slug>
name: <Full Name>
type: player_character        # or npc_companion / override's incidental type
race: <Race / Subrace>
class: <Class / Subclass (multiclass with slash)>
level: <N>
alignment: <Alignment>
faction: <faction_id or none>
items_attuned: []
identity_known_to_party: true # PC only
# NPC-only fields:
# control: player|claude
# traveling_with_party: true
# secret_state: true          # only if the override seeded hidden state
status: complete              # or stub / developing
---

## Overview

<2–4 sentences: who they are, what they do, why they're heading toward
this region right now.>

## Stats

- **AC** <n>  **HP** <n>  **Speed** <n>ft  **Init** <±n>  **Prof** +<n>
- **STR** <n> (<±mod>)  **DEX** <n> (<±mod>)  **CON** <n> (<±mod>)  **INT** <n> (<±mod>)  **WIS** <n> (<±mod>)  **CHA** <n> (<±mod>)
- **Saves:** <list proficient saves>
- **Skills:** <list proficient skills>
- **Languages:** <list>
- **Tools / other proficiencies:** <list>

## Combat

- **Attacks:** <weapon — to hit, damage, properties>
- **Spell save DC** <n> (if applicable) — **Spell attack** +<n>
- **Class features in play:** <bullet list>

## Spells

(omit if non-caster)

- **Cantrips:** <list>
- **<Level N>:** <list known / prepared>
- **Slots:** <n>/<n> per level

## Equipment

- <bullet list — weapons, armor, kit, notable items, coin>

## Background

<Full backstory paragraph(s). Outsider perspective on the campaign
region. Tie to chosen hook concretely — specific names, places, prior
events from the override's listed canon only.>

## Personality

- **Trait:** <…>
- **Ideal:** <…>
- **Bond:** <…>
- **Flaw:** <…>

## DM Notes

<Anything the DM needs that isn't shown to the player — hook entry
points, knowledge gaps, planned reveals, content-rating flags. This
section may reference what the character does NOT know about the canon.
For an NPC with secret_state, keep the hidden material here or in a
clearly DM-only subsection.>

## Open Slots — To Develop in Play

<Stub / developing characters only — omit for complete ones. Deferred
facets, one bullet each with a category prefix per {{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_progressive.md:
[relation] [reveal] [bond] [mechanics] [backstory] [appearance] [name].>
```

### Completeness handling

- **Complete:** fill every section. Omit `## Open Slots` and set
  `status: complete` (or omit `status`).
- **Stub:** meet the runnable floor (full stat block, ≥1 personality seed
  line, the Overview concept, anatomy pass done). Leave the rest as
  prefixed bullets under `## Open Slots — To Develop in Play`, set
  `status: stub`, and tell the user in one line what was deferred. The
  sheet must be droppable into a scene as-is.

Later flesh-out (on demand or play-triggered) follows the two procedures
in `{{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_progressive.md`.

After writing, summarize for the user in 3 lines: name, concept, hook (or
for a stub: name, concept, what's deferred). Ask if they want any
adjustments.

---

## What This Skill Does NOT Do

- Does not start the campaign. If invoked standalone, end after the
  sheet is saved and ask the user what's next.
- Does not modify the canonical roster paths (the override's
  write-scope restrictions are absolute).
- Does not invent canonical lore. If a hook would require new canon, ask
  the user before fabricating.
- Does not save transcripts, generate portraits, or run NPC
  conversations.
- Does not assume a desktop client. All interaction is plain
  text/markdown.
