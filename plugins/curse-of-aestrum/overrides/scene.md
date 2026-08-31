# Scene — Curse of Aestrum Override

Setting overrides for the prose-engine `scene/core.md`. Loaded by the game's
thin shell after the engine layers. Applies at draft time; extends the
epistemic-pass scan list (row 13 of the checklist).

---

## Aestrum location curation

In-Aestrum geography is author-curated; Claude does not introduce new
in-Aestrum locations during play. The rule, its scope (settlements,
structures, landmarks — *not* characters or architectural detail within an
established place), and the current known-destinations list are codified in
[rules/aestrum_location_curation.md]({{PLUGIN_ROOT}}/rules/aestrum_location_curation.md).
Loaded as a scene-time drafting constraint.

## Session-opening discipline

Any question shown to the player during STEP 1, or as a follow-up before the
opening narration in STEP 3, is subject to
[rules/session_opening_no_plot_leaks.md]({{PLUGIN_ROOT}}/rules/session_opening_no_plot_leaks.md).
The rule covers **the question text and every option label and description,
including options the player will not pick.** Read it before composing STEP 1.
Restrict setup questions to neutral framing (content rating, time of day,
where the PC is and what they are doing). Do not name hidden bounties,
NPC-private agendas, convergences, or upcoming reveals in any visible setup
text.

---

## Time-anchor system

**Aestrum Day [X]** + time of day (morning / midday / afternoon / evening /
night / specific). The Aestrum Day is project structure for loading state —
**never used in-fiction** (see Epistemic-pass Extensions).

**Resolving relative time references** ("the morning after we rescued Miri",
"before the Dunleaven incident"):

- Canonical: `{{PLUGIN_ROOT}}/timelines/chapter_1/nortmunde_regional.md`
- Per-campaign log: `{{PROJECT_ROOT}}/campaign_state/<C>/timelines/saved/aestrum_events.md`

If unresolvable, ask the user before loading characters.

---

## Narration mode default

Pinned to **`character_aligned`** for Curse of Aestrum, with the anchor
defaulting implicitly to the PC unless the user names otherwise at
scene start. The pin is explicit — *not* inherited silently from
Calliope's file-declared default — so that future engine changes do not
drift this campaign's narration. To change the mode for a specific
scene, the user declares it at scene start (e.g., *"this scene is
omniscient,"* *"split-anchor between X and Y"*); the mode is locked for
that scene and reverts to the pinned default on the next scene.

The sense-availability sub-rule applies per `narration_modes.md`.

CoA does not currently extend the perceptual envelope with
setting-specific magical senses; D&D 5e perception extensions
(darkvision, blindsight, tremorsense, true sight) belong in Canterbury
(`rpg-5e-engine`) when added.

---

## Content rating system

ESRB-style: **T / M / AO**. Default outside in-game sessions is **M**;
in-session default is whatever was active at the end of the previous saved
session. No record → require explicit selection.

T is the floor (the campaign carries too much occult horror, manipulation,
intimate themes to play lighter). The rating governs everything in the scene —
injury granularity, innuendo, threat bluntness, NPC anger.

| Rating | Violence | Sexual / Intimate | Language | Other |
|---|---|---|---|---|
| **T** | Real, consequential combat; broad-stroke wounds; no torture detail. | Romance and tension on page; intimacy fades to black. No anatomical description. | Mild profanity. No slurs, no graphic obscenity. | Horror and dread at full strength. Death, loss, addiction, abuse present but not graphic. |
| **M** | Graphic violence — wound specificity, physiology, sensory detail. Stops short of torture-porn dwelling. | Sex on page with explicit emotional and physical detail, short of pornographic anatomical specificity. | Strong profanity natural to character. | Drug use, manipulation, psychological cruelty depicted in detail when in service of the scene. |
| **AO** | Full graphic violence including torture, mutilation, prolonged suffering when narratively warranted. | Fully explicit, pornographic specificity. Anatomy, mechanics, fluids, sounds. Subject to hard limits below. | No restriction. | No softening of any depicted subject for taste — only for the hard limits below. |

**Hard limits regardless of rating:**

- Sexual content involving minors, or any character not a competent
  consenting adult in the fiction.
- Real-world non-consensual sexual content rendered as titillation. Sexual
  violence may be present in the world (off-page or briefly named) when the
  story requires it; never written as erotica.
- Operational instructions outside the fiction (synthesis routes for real
  drugs/weapons/etc.).

**Mid-session changes** ("switch to M", "drop to T", "go AO for this scene")
take effect on the next response, including retroactive softening/escalation
of a scene in progress. Acknowledge on one line; do not relitigate earlier
output.

**Tracking:** the active rating lives in working memory. Save STEP 5 includes
`content_rating: [T|M|AO]` in frontmatter so the next session resumes there.

---

## Display mode and dice resolution

Curse of Aestrum is a *game*: checks with real stakes are **rolled**, and the
character's sheet modifier decides the outcome. (A CoA run with no dice that
bite would be a Pandora-style anthology wearing CoA's coat — dice-that-bite are
the Canterbury layer CoA consumes and an anthology omits.) Two campaign-level
settings govern only how that resolution is *displayed*; they never change
*whether* it resolves.

**Settings (read at scene start, locked for the scene).** Read
`{{PROJECT_ROOT}}/campaign_state/<C>/preferences.md` if present, else the canonical defaults in
`{{PLUGIN_ROOT}}/party/preferences.md`:

- **`narrationDisplay`** — `Novelization` (default) or `Game`. Scene-rendering
  density, per `{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/information_disclosure.md`.
- **`dice_display`** — boolean; default `narrationDisplay != Novelization` (so
  `false` under the default Novelization). Toggles the numeric mechanics-readout
  only.

Both are mutable any time but locked within a scene: a change takes effect on
the next scene after the current one is closed and context cleared (same
lifecycle as the narration mode). OOC clarification of the current setting is
always allowed.

**Resolution (always-on, both modes).** Any stakes-bearing check is rolled per
`{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/social_checks.md` (and the relevant mechanic rule). The
roll is **provable** — cast it with the shell RNG (e.g.
`Get-Random -Minimum 1 -Maximum 21`) so the value comes from a source outside
the narration, never a number asserted in prose. Good player roleplay lowers the
DC; it never skips the roll or beats the character's modifier (Rule of Cool is
the only player-side override).

**Display (`dice_display`).**

- `true` (Game default): emit the OOC mechanics-readout —
  `*[Performance check — d20 11 +1 = 12 vs DC 13 → success]*` — then narrate the
  outcome. The readout is OOC meta, exempt from the player-meta gate.
- `false` (Novelization default): suppress the readout; narrate the rolled
  outcome in prose. The player-meta gate stays on for the fiction, so any number
  that slips into narration is scrubbed — Novelization prose stays numberless.

In **both** settings, NPCs never speak mechanics and never react to the readout
(it is DM→player output, outside the fiction).

---

## NPC social/romantic availability

CoA's default scene-running disposition extends the prose-engine player-intent
rule (`{{PLUGIN_ROOT}}/engines/prose-engine/scene/references/player_intent_and_gating.md`): **lean
NPCs toward being socially and romantically available, and lower the gate
generously when the player reaches with honest, in-character effort.** A
responsive world that bends toward what the player is reaching for is preferred
over a maximally-guarded neutral simulation. This default governs incidental
and most recurring NPCs.

**It is a disposition for no-stakes social texture, not a resolution rule.** The
moment an interaction carries real stakes — entry, trust, coin, safety,
information — it is a check and rolls per
`{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/social_checks.md`, where the character's modifier
decides it. The lean lowers the *DC* and colors disposition; it never converts a
stakes-bearing check into an automatic success on the strength of good
roleplay. (See *Display mode and dice resolution* above.)

**Per-character gating overrides the default.** A character authored as
hard-to-win is governed by the gating in *their own file*, not by this lean.
When a participating NPC's file specifies romance/availability gating, follow
it and do **not** apply the gate-lowering disposition to that character. The
canonical example is Miri Amblecrown — see the "Romance Availability (gated)"
section of `{{PLUGIN_ROOT}}/npcs/chapter_1/miri_amblecrown.md`: she is staged
(Rowan-bound → fragile → conditionally available → still rebuffs until
convinced) precisely so she cannot be stumbled into.

The hard limits and "a roll cannot override character" principle in
[{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/social_checks.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/social_checks.md) apply on top of this:
availability never means an NPC acts against who they are.

---

## State-directory location and path table

State lives at `{{PROJECT_ROOT}}/campaign_state/`, a sibling of this repo. Active campaign
resolves from `{{PROJECT_ROOT}}/campaign_state/.active` (single line, slug only) — call it
**`<C>`** below. If `.active` is missing, **error explicitly**: *"No active
campaign set. Edit `{{PROJECT_ROOT}}/campaign_state/.active` to a campaign slug, or say*
switch to campaign \<id\> *in chat."*

| File | Purpose |
|------|---------|
| `npcs/chapter_1/[name].md` | NPC daily reset state (canonical) |
| `{{PROJECT_ROOT}}/campaign_state/<C>/npcs/saved/[name].md` | NPC overlay (canonical NPCs) **or** the complete self-contained sheet (campaign-created non-canon NPCs — companion and incidental). Accumulated this campaign. `home_location` frontmatter on a self-contained sheet auto-loads at matching locations. |
| `npcs/chapter_1/[name].md` | PC companion baseline (Miri, Jiasha) — alongside NPC baselines |
| `party/[name].md` | Canonical PC baseline |
| `{{PROJECT_ROOT}}/campaign_state/<C>/party/[name].md` | Custom PC baseline (this campaign's custom PCs) |
| `{{PROJECT_ROOT}}/campaign_state/<C>/party/saved/[name].md` | PC companion AND Player PC overlay |
| `{{PROJECT_ROOT}}/campaign_state/<C>/party/saved/<instance>/[name].md` | *(Optional)* save-snapshot subdir |
| `{{PLUGIN_ROOT}}/timelines/chapter_1/nortmunde_regional.md` | Canonical Nortmunde regional events |
| `{{PROJECT_ROOT}}/campaign_state/<C>/timelines/saved/nortmunde_regional.md` | Per-campaign Nortmunde overlay |
| `{{PROJECT_ROOT}}/campaign_state/<C>/timelines/saved/aestrum_events.md` | Per-campaign in-loop session log |
| `{{PROJECT_ROOT}}/campaign_state/<C>/conversation_states/` | Saved completed conversations |
| `{{PROJECT_ROOT}}/campaign_state/<C>/staging/<sid>.md` | Pre-save running delta for the in-flight scene (one file). Built post-prose during play; flushed to the overlays + deleted on save. Not loaded by normal resolution; the resume path reads it to continue an unsaved scene. |
| `locations/chapter_1/`, `locations/chapter_2/` | Canonical locations, organized by chapter; city subdirs (e.g., `locations/chapter_1/duskwall/`) live inside the chapter folder |
| `{{PROJECT_ROOT}}/campaign_state/<C>/locations/saved/` | Location overlays |
| `{{PROJECT_ROOT}}/campaign_state/<C>/factions/saved/` | Faction overlays |
| `{{PROJECT_ROOT}}/campaign_state/<C>/items/saved/` | Item overlays |
| `{{PROJECT_ROOT}}/campaign_state/<C>/preferences.md` | Per-campaign display settings (`narrationDisplay`, `dice_display`) — instance overlay of `{{PLUGIN_ROOT}}/party/preferences.md` |

All paths relative to the campaign repo root. **`<C>`** = resolved active
campaign slug.

**Mid-session campaign switching** ("switch to campaign \<id\>"): verify
target dir exists, write the new slug to `{{PROJECT_ROOT}}/campaign_state/.active`,
acknowledge on one line, discard in-memory character / location state. Next
scene load re-reads from the new campaign's overlays.

---

## Character-type table

Replaces the engine's generic character-type table.

| Type | Description | Files |
|---|---|---|
| **Loop NPC** | Subject to daily Modify Memory reset. | `npcs/chapter_1/[name].md` + `{{PROJECT_ROOT}}/campaign_state/<C>/npcs/saved/[name].md` (time-filtered) |
| **Non-loop NPC** | Outside / immune to the loop. Continuous memory. | `npcs/chapter_1/[name].md` + `{{PROJECT_ROOT}}/campaign_state/<C>/npcs/saved/[name].md` (no filter) |
| **Custom NPC** | Added by this campaign (companion or incidental); non-canon. Loop status per frontmatter. | `{{PROJECT_ROOT}}/campaign_state/<C>/npcs/saved/[name].md` — one self-contained sheet, no separate base (filter per loop status) |
| **PC companion** | Miri, Jiasha. NPCs by type; travel with party. Overlay lives in per-campaign `party/` tree (reflects their in-fiction party role). | `npcs/chapter_1/[name].md` + `{{PROJECT_ROOT}}/campaign_state/<C>/party/saved/[name].md` (time-filtered) |
| **Player PC (canonical)** | Thagnog, Zephyra, Sage, Belmita, Theren. Continuous memory. | `party/[name].md` + `{{PROJECT_ROOT}}/campaign_state/<C>/party/saved/[name].md` if it exists (no filter) |
| **Player PC (custom)** | Off-roster PCs (Aelthas, etc.). Continuous memory. | `{{PROJECT_ROOT}}/campaign_state/<C>/party/[name].md` + `{{PROJECT_ROOT}}/campaign_state/<C>/party/saved/[name].md` if it exists |

**Loop status** lives in base-file frontmatter: `loop_frozen: true/false`,
`cycle_aware: true/false`, `loop_memory_notes`. Confirmed non-loop NPCs:
Nessa.

**NPC name lookup order:** for a **canonical** NPC, the base is
`npcs/chapter_1/[name].md` (project-root canon roster; chapter-bounded) and its
campaign overlay is `{{PROJECT_ROOT}}/campaign_state/<C>/npcs/saved/[name].md`. A
**campaign-created (non-canon) NPC** has *no* base — its complete self-contained
sheet is `{{PROJECT_ROOT}}/campaign_state/<C>/npcs/saved/[name].md`. So `{{PROJECT_ROOT}}/campaign_state/<C>/npcs/saved/[name].md`
is always the campaign-side file to load; whether a canon base sits above it is
decided by the project-root roster. (There is no `{{PROJECT_ROOT}}/campaign_state/<C>/npcs/chapter_1/`
tier — campaign NPCs are never chapter-organized.)

---

## Time-filter format

- **Loop characters and PC companions (Miri, Jiasha):** include an overlay
  entry only if its day tag is **strictly earlier** than the specified
  Aestrum Day, OR matches AND the event has plausibly occurred by the
  specified time of day.
- **Non-loop characters and Player PCs:** include all overlay entries; no
  filter.

> Example: Loading Miri at Aestrum Day 6, noon. Entries tagged "Day 6"
> describe events she learned that day — by noon she has likely had the
> morning conversation but not afternoon events. Entries tagged "Day 6+"
> cover ongoing observation; include those that would have begun
> accumulating by Day 6, noon.

**Exemption — `### Cycle response —` entries.** Any NPC-overlay entry whose
heading is prefixed **`### Cycle response —`** (the loop-recurrence response
repertoire — approach-keyed dialogue *and* location-independent event-experience
reactions, per [../rules/cycle_recurrences.md]({{PLUGIN_ROOT}}/rules/cycle_recurrences.md)) is
**not** time-filtered — it loads in full regardless of the specified Aestrum Day.
It is deterministic baseline behavior the loop always reproduces, not experience
the character accumulates. The **prefix is the machine contract** (the flush
appends these blocks like any delta, so they may sit anywhere in the monolith; the
`## Cycle Responses` heading is human-readable grouping only). The same is
intrinsic to a **location** overlay's `### Cycle recurrence —` entries (locations
carry no time-filter to begin with).

---

## Named-character voice notes

- **Nessa** — Marion Lavorre cadence. Weighted, warm, considered.
- **Miri (Amblecrown)** — Idealistic, earnest, quietly regal.

Additional voice notes live in each NPC's base file. A dwarf doesn't speak
like a half-elf. Voices don't bleed.

---

## In-fiction time-reference rule (Harptos)

**Never expose the day-index numeric system in narration or dialogue.** Day
numbers ("Day −29", "Aestrum Day 6") are project structure for loading state
— not in-fiction units. Characters do not count days from the king's death;
narration does not name those indices.

In-fiction references use either:

- The **Calendar of Harptos** for absolute dates ("the 14th of Mirtul",
  "Greengrass morning"), or
- Natural-language relative phrasing ("three days ago", "the morning before
  the council", "last tenday").

Scope: spoken lines, internal NPC thought rendered as dialogue, scene-setter
timestamps the user sees in-scene, narration asides.

**No scene-establishment header (engine default, reaffirmed for CoA).** Per
the engine's STEP 3, a scene opens through gated narration — there is no
`**[Character]** | [time anchor] | [location]` header and no out-of-fiction
scene-setter digest, at scene start or at the head of any beat. For CoA this
doubles as a hard time-reference safeguard: the **Aestrum Day index must
never appear in such a header**, because a header bypasses the epistemic gate
and the index is project structure, not in-fiction time. The player gets
time/location bearings from the resume orientation line and from OOC
clarification on request — the Aestrum Day index remains available OOC per
the rule above, just never as a standing header.

**Out-of-character clarification is always allowed.** If the player asks
*as player* what day it is or how long ago something happened, answer
plainly with the Aestrum Day index. Players need to keep their bearings; the
ban is on the index leaking *into* the fiction, not on the user retrieving
it.

---

## Epistemic-pass extensions (row 13 of the gate checklist)

Add to the gate's scan list, for narration and NPC dialogue only:

- **`Aestrum Day`** — day-index frame, banned in-fiction.
- **`Day [N]`** / **`Day −[N]`** / **`Day +[N]`** — numeric forms, banned
  in-fiction.
- **`Cycle [N]`** — banned in-fiction.

When any of these appear in narration or dialogue (not user-facing meta),
rewrite using the Calendar of Harptos or relative phrasing per the rule
above.

**Machine-readable mirror.** The closed-vocabulary subset of these extensions
(v1: the `Aestrum Day` frame) is mirrored as structured data in
[gate_lint/forbidden_tokens.toml]({{PLUGIN_ROOT}}/overrides/gate_lint/forbidden_tokens.toml) for
deterministic runtime enforcement (fiction-host's post-generation lint). The
numeric index forms (`Day [N]`, `Cycle [N]`) are digit-bearing *patterns* —
parked in that file until the v2 regex matcher lands — because bare `day` and
bare `cycle`/`the cycle` are legitimate in-fiction and must not be flagged.

### Roster-at-T parameters

- **Field name:** `joined_expedition_nortmunde_day:` — **PC file frontmatter
  only**.
- **Time-anchor:** Nortmunde Day; Day 0 = the King's death = Kythorn 25,
  1490 DR; negative = days before.
- **Scope: PCs only.** Forbidden on NPC files of any type, including
  PC-companion NPCs (Miri, Jiasha). Their in-fiction join-point belongs in
  the per-campaign overlay (`{{PROJECT_ROOT}}/campaign_state/<C>/party/saved/[name].md`),
  not the canonical baseline.
- **Value:** the Nortmunde Day the PC signed the Aestrum tax-collection
  expedition contract; or, for a PC who joined the party in-fiction after
  departure, the Day they first joined.
- **Field absent:** surface to the user (per the engine).

### Player-meta vocabulary

Activated by `rpg-5e-engine/rules/player_meta_tokens.md` (loaded at scene
start). Canterbury supplies the 5e vocabulary — HP, AC, spell slots, saves,
DCs, initiative, modifiers, dice notation, advantage/disadvantage, ability
scores — with structural disambiguators.

CoA does not extend the vocabulary. Loop-specific terms (*the loop, the
cycle, dead zone, revert, Recreate, Modify Memory*) are **in-fiction
concepts** characters can know and use — not player-meta tokens. If a future
CoA-specific mechanical subsystem produces dialogue leaks (e.g., a
house-rule resource the party tracks numerically), add tokens here in
Calliope's schema — not in Canterbury's shared file.

### Future-state and identity-through-disguise

CoA does not define a per-character **foresight field**. Galadiil's
foresight, Belmita's hunches, and any prophecy-bearing characters are
handled by narrative judgment. The future-state check runs strict-default:
indicative future claims fall back to conditional or are cut unless they
emerge from shared scene planning.

CoA does not define a **recognition-state field**. Disguise and concealment
are handled scene-by-scene through narrative tracking. The check is
dormant. If recurring disguise becomes a campaign-level subsystem, define
field name and semantic here.

### Language, disposition, and agenda (rows 16–18)

CoA **activates** the three asymmetric-aspect checks the engine appends as
rows 16–18 of the gate.

- **Language-comprehension (row 16) — ACTIVE.** Field source is the
  Canterbury 5e sheet's spoken-language list, plus any readable-script
  literacy noted on the sheet or accrued in the campaign overlay. A
  character comprehends spoken content only in a language on that list, and
  reads only scripts in their literacy set. **Strict default if a character
  has no language data:** comprehension limited to Common only. Written
  artifacts in a location carry their script (per the location template);
  text in a script the character lacks is marks, not meaning.
- **Disposition-surfacing (row 17) — ACTIVE.** Reads the character's
  relationships / disposition block, built at load from the overlay header
  conventions below.
- **Agenda-surfacing (row 18) — ACTIVE.** Reads the character's agenda block,
  built at load from the overlay header conventions below.

Rows 17–18 are knowledge-boundary kin: a character must not display a
relationship, allegiance, or hidden plan among others that their own block
does not ground. The loop context makes this load-bearing — a Modify-Memory
reset can strip a Loop NPC's knowledge of a relationship or plan they held
the previous cycle, and the time-filter on overlay entries already governs
what they retain.

---

## Stylistic-pass extensions (stylistic suite — CoA rows)

Add to the gate's **stylistic-variance** suite
([{{PLUGIN_ROOT}}/engines/prose-engine/scene/references/stylistic_variance_checklist.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/stylistic_variance_checklist.md)),
which CoA runs as the craft-side half of the single gate. Per that file's
"Extending this suite," a consuming game may add rows in the same shape; the
override **extends the scan list** and never introduces a pass that runs after
the gate. These rows run in the **same** gate pass as the engine's S1–S5 and
report in the dash marker's S-slot alongside them.

| # | Check | Trigger surface | Forbidden | Rewrite move | Rule source |
|---|---|---|---|---|---|
| S-CoA1 | **PC spoken line dropped or summarized** | The rendering of the player's plain-text spoken input in the beat — the utterance the turn owes the reader | The PC's line **not rendered as a quoted, unlabeled utterance**: collapsed into reported / indirect speech (*he said he had no mind to storm the shrine*), summarized into narration, dropped entirely, or the beat opened at the NPC's reaction so no quoted PC line appears. "Woven into an action beat" is licensed **only** as an attributed quote (*He turned from the wind. "…"*), never as paraphrase. | Render the player's words as a quoted, unlabeled line — plain (*"…," Hessian said*) or woven into an action beat — lightly polished into the PC's voice per the plain-text rule, then the NPCs' labeled responses. | Dialogue format (`{{PLUGIN_ROOT}}/skills/scene/SKILL.md`, "Dialogue format"; engine twin [`dialogue_format.md`]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/dialogue_format.md)) |

**Read on fire (S-CoA1):** the player's just-submitted plain-text input —
already in context, no file read. The check is comparative and simple: does a
quoted PC utterance carrying the words the player spoke appear in the beat? A
**pure-action input** (a directive with no spoken content) has no line to quote
and the row **does not fire** — it governs speech the player put in the PC's
mouth, not narrated action.

---

## Lore loader

For mechanics context (cycle, dead zones, dead-zone shelter, Moon Amulets,
loop anchors), the `mex` skill loads `{{PLUGIN_ROOT}}/lore/key_lore_summary.md`. The scene
skill does not auto-load this; be aware it exists if the user asks for
mechanics clarification mid-scene.

---

## In-scene mechanics (CoA-only rules)

The thin shell handles the engine-side mechanics (`../rpg-5e-engine/rules/`).
The CoA setting-specific rules, loaded on demand when the mechanic fires:

- `{{PLUGIN_ROOT}}/rules/time_loop.md`
- `{{PLUGIN_ROOT}}/rules/loop_anchors.md`
- `{{PLUGIN_ROOT}}/rules/dead_zones.md`
- `{{PLUGIN_ROOT}}/rules/revert.md`
- `{{PLUGIN_ROOT}}/rules/snapshot.md`
- `{{PLUGIN_ROOT}}/rules/fuzzball.md`
- `{{PLUGIN_ROOT}}/rules/magic_immune_runes.md`
- `{{PLUGIN_ROOT}}/rules/magical_item_conversion.md`
- `{{PLUGIN_ROOT}}/rules/rest_and_recovery.md` (overrides engine RAW stub)
- `{{PLUGIN_ROOT}}/rules/death_and_dying.md` (overrides engine RAW stub)
- `{{PLUGIN_ROOT}}/rules/item_persistence.md` (overrides engine stub)
- `{{PLUGIN_ROOT}}/rules/travel.md` (overrides engine default)
- `{{PLUGIN_ROOT}}/rules/consequences.md` (extends engine framework — cycle-blindness
  corollary + tier examples)
- `{{PLUGIN_ROOT}}/rules/companion_animals.md` (the adoptable dog and cat — load when either
  animal is seeded, pursued, present, or adopted; content sheets at
  `{{PLUGIN_ROOT}}/npcs/chapter_1/stray_dog.md` and `{{PLUGIN_ROOT}}/npcs/chapter_1/stray_cat.md`)
- `{{PLUGIN_ROOT}}/rules/cycle_recurrences.md` (loop replay of emergent recurring beats —
  location `## Cycle Recurrences` and NPC `## Cycle Responses`; load when the
  party re-enters a location, re-opens a conversation with a resident, or puts a
  resident through a repeat situation-type)

### Cycle-aware drafting (mandatory load trigger)

**The cycle rules are not on-demand at the moment a beat crosses or spans
midnight inside Aestrum — they are mandatory drafting constraints.**

**Load trigger (unconditional).** Before composing any beat in which
in-fiction time approaches, crosses, or spans an Aestrum-local midnight
and any character or witness in the beat is physically inside the Aestrum
boundary, you **must** load (or have loaded earlier this session):

- `{{PLUGIN_ROOT}}/rules/time_loop.md` — the timed Sleep → Recreate → Teleport → Modify
  Memory → Wake sequence and its boundary-crossing precision.
- `{{PLUGIN_ROOT}}/rules/snapshot.md` — first-midnight snapshot, reset-point assignment,
  amulet interaction.
- `{{PLUGIN_ROOT}}/rules/revert.md` — what revert does to memory and what the amulets shield
  from.
- `{{PLUGIN_ROOT}}/rules/dead_zones.md` — the shelter rule, evaluated per subject below.

The trigger is **unconditional on dead-zone presence**: you cannot decide
shelter without the load itself, the world *outside* a sheltered location
still cycles, and mixed-party cases (some in a dead zone, some not) need
the same files. Dead-zone shelter is a per-subject *application* question,
not a precondition for loading.

**Per-subject application.** Once loaded, evaluate each affected character
and witness at the firing instant of each step (12:00, 1:30, 3:00, 4:30,
6:00 AM Aestrum-local):

- *Inside a dead zone at firing* → that step does not affect them. Body is
  continuous; memory is preserved; they are not Teleported. Snapshot
  persistence still holds (`dead_zones.md`, "Persistent-Snapshot Rule").
- *Outside a dead zone at firing* → step applies as written in
  `time_loop.md`.
- *Partly across the boundary at firing* → DM ruling per both source files.

**World-state, not character knowledge.** The reset sequence governs who
is conscious, where they are, who can knock on a door, who can be on a
stool, whether the inn is "quiet" or *post-Sleep* silent. These are
physics of the night; the prose must honor them even when the POV
character has no idea why. The world *outside* any dead zone cycles on
schedule regardless of who is sheltered — a Rowan-style character inside
a dead zone wakes into a world that just went through reset around them.

**The reset resets the day's clock.** A reset morning begins the day fresh
at the Wake step — early morning, a full day of light ahead. Do **not**
carry a prior cycle's time-of-day, its late-day light, or its
shelter-before-dark urgency into a reset morning; re-derive the time-of-day
from the current day's own timeline before rendering any part-of-day label,
light cue, or time-pressure. This is the CoA manifestation of the engine's
clock-position grounding (row 14, the ambient-time carry-over twin): a
prior cycle's afternoon race-the-dark feeling is exactly the ambient time
that rides into the new day if left unchecked, because the loop returns the
party to a morning while the drafter's hand is still holding the last day's
dusk.

**Loop-gated NPC knowledge — testimony is bounded by propagation and the day's
intake.** Before putting a rumor, report, or piece of local intelligence in a
**Loop NPC's** mouth, run two loop-specific grounding checks (the loop-context
form of gate rows 2 and 19):

- **Propagation.** A phenomenon whose only witnesses are themselves loop-reset —
  a transient camp, a nightly event, anyone who forgets at the next midnight —
  cannot seed an *accumulating* rumor. Those witnesses carry no memory across the
  reset, so the report never reaches the NPC's ear (or her persistent store) day
  over day. **A resetting source yields no standing rumor;** the NPC's honest
  answer is the gap, not a fill.
- **The day's intake-so-far.** A Loop NPC begins each cycle holding only what
  persists for her (a continuous-memory exception such as a dead box) plus
  whatever she has actually been told *since this morning's Wake*. Check the
  in-fiction clock first: early-morning / pre-client, she has had **no intake
  today**, so *"my visitors have been saying…"* / *"I've been hearing…"* has no
  source event and is cut. A persistent store holds only what a same-day witness
  carried to her before a prior midnight — which the propagation test already
  gates.

The failure is handing a Loop NPC a convenient report the loop's own physics
forbid her to hold — a confirmation-mirror for the party's theory. Stop-the-line
if it slips.

**Amulet bearers are NOT cycle-exempt.** Moon Amulets shield only against
Modify Memory; **Sleep, Recreate, and Teleport still apply** unless
separately protected. A wearer who fell asleep before midnight feels no
transition — Sleep is invisible to a subject already unconscious — and
wakes at the 6:00 AM Wake step in the position Sleep locked them into (at
first midnight, that is their snapshot location; on subsequent midnights,
Teleport will have moved them to the reset point).

**Failure mode (stop the line).** Rendering the night after first midnight
as if it were an ordinary night — NPCs walking around, watch rotations
continuing, locals awake at 2 AM — is a setting-fidelity break and stops
the line per the global Calliope leak protocol.

**Night-danger tone scoping — sheltered nights are safe harbors.** The reset's
danger is a *bounded window,* not an ambient condition of darkness. The hazard
is the midnight **Sleep** step and the reset sequence that follows it (12:00 AM
onward, [../rules/time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md)), and it falls on
subjects who meet it **exposed** — caught out, unsheltered, somewhere that "a
place where being found in the morning will not undo you" fails to describe
(Jiasha's charge; Aliss's corroboration that people do not always wake where
they lay, and now and then someone is simply gone). It is **not** a property of
nightfall as such, and it is no licence for sustained dread across a whole
evening.

The same warning that names the danger also prescribes the safety: **be behind
a barred door — or in a dead zone — before midnight.** Once the party has met
that condition, they are as safe as this duchy allows, and the tone must flip to
**downtime.** A sheltered dusk-to-midnight stretch is a **safe harbor:** the
venue where the crew decompresses, talks, and bonds, and where romance and
relationships have the room to form. Render those hours as rest, not as extended
threat-assessment; guards come down there, and the NPCs' openings for connection
*live* there. A barred room before midnight is a solved problem — render it
solved, and let the evening breathe.

So the loop nights carry **two paired failure modes,** and this section owns
both:

- **Under-play** (the paragraph above): rendering a reset-night as an ordinary
  night — figures abroad at 2 AM, watch rotations continuing — is a
  setting-fidelity break.
- **Over-play** (this note): letting *the night is the hand's hour* bleed into
  *any darkness is a threat; get indoors and stay vigilant,* so that
  **sheltered** time never breathes. This silently chills the campaign's
  downtime and, with it, every bonding and romantic beat that needs a safe
  moment to exist. A standing "it's dark, we must get indoors" posture that
  persists *after* the party is safely barred in is the tell; scope it back.

The danger tone is reserved for exactly three cases: approaching midnight while
still **unsheltered**; a deliberate choice to be **out** through the reset
window; and the reset sequence itself. Everywhere else after dark — sheltered,
barred, in company — the tone is **safe,** and the scene is free to be about the
people in the room.

### Cycle recurrences (loop replay)

Aestrum residents reset nightly and re-live the same day, so their reactions are
**deterministic from baseline** — the same stimulus reproduces the same beat and
line every cycle, a different approach branches into new dialogue, and the same
*kind of experience* draws the same reaction **even in a different place** (the
Westworld/Lawrence texture). Capture and replay these per
[../rules/cycle_recurrences.md]({{PLUGIN_ROOT}}/rules/cycle_recurrences.md) (load it when the
party re-enters a location, re-opens a conversation with a resident, or puts a
resident through a repeat situation-type). Draft-time behavior:

- **On entering a location,** consult its overlay's `## Cycle Recurrences`
  (`{{PROJECT_ROOT}}/campaign_state/<C>/locations/saved/<loc>.md`). **On opening an NPC
  conversation, or when a resident undergoes an event of a stored type
  (anywhere),** consult that NPC's overlay `## Cycle Responses`. Match the current
  circumstances / approach / situation-type against the stored triggers.
- **Match → replay faithfully** (behavior + line near-verbatim), and surface the
  party's *recognition* of the repetition — they remember, the resident does not.
- **New approach → branch:** author the new response from the actor's baseline,
  render it, and stage it as a new stored branch.
- **Producing condition removed** (resident permanently killed and dead-zoned,
  place changed) → the recurrence **lapses**; do not replay it.
- **Capture is during staging.** A newly observed recurrence (or branch) is
  written into the staging file as a self-marked `### Cycle recurrence —` /
  `### Cycle response —` block under `## locations/<id>` / `## npcs/<name>`, and
  flushed to the overlay on save — the same staging-tail pipeline and D1
  explicit-save discipline as any other delta (see
  [../rules/cycle_recurrences.md]({{PLUGIN_ROOT}}/rules/cycle_recurrences.md), *Capture*).

**Loader note:** NPC `### Cycle response —` entries are **exempt from the overlay
time-filter** (see *Time-filter format* above) — baseline determinism, not
retained experience; they load in full regardless of Aestrum Day. The **prefix**
is the contract, not the `## Cycle Responses` grouping heading.

### Instance rule overrides (per-campaign toggles)

At scene start, read the active campaign's instance toggle file:

- `{{PROJECT_ROOT}}/campaign_state/<C>/rules/rule_overrides.md` (if present) — `<C>` resolves from
  `{{PROJECT_ROOT}}/campaign_state/.active` per the state-directory section above.

For each toggle set to `true`, apply the matching behavior from
[../rules/optional_rules.md]({{PLUGIN_ROOT}}/rules/optional_rules.md) (the catalog) as a drafting
constraint for this campaign. Load order is Engine → Campaign → **Instance**
(last-loaded wins), per [../rules/file_layering.md]({{PLUGIN_ROOT}}/rules/file_layering.md).
Absence of the file, or of a given key, means default (RAW) behavior.

---

## Resume / lifecycle — CoA specifics

Per the engine's generic scene-lifecycle (RESUME in
[{{PLUGIN_ROOT}}/engines/prose-engine/scene/references/scene_lifecycle.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/scene_lifecycle.md#scene-lifecycle.resume)),
Aria's
[{{PLUGIN_ROOT}}/engines/story-engine/rules/story_lifecycle.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/story_lifecycle.md)
(the work-container mapping onto it), and Canterbury's RPG overlay
[{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/campaign_lifecycle.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/campaign_lifecycle.md),
this override supplies:

- **Active-set indicator:** `{{PROJECT_ROOT}}/campaign_state/.active` (single-line slug),
  per the state-directory section above. The resume operation **must** read
  `.active` to choose the campaign — **never** pick by file modification
  time. If `.active` is missing, error with the wording in that section.
- **Last-saved time anchor:** the most recent `### Day [X] — …` delta entry
  in the active campaign's overlays (PC overlay / `aestrum_events.md`).
- **Allowed OOC orientation in the refresher:** character level and 5e
  mechanics; the **Aestrum Day index** for the player's bearings (OOC
  clarification is always allowed — see the Harptos rule); the active
  content rating. Everything else in the refresher is bounded by the PC's
  knowledge.
- **Player-facing wording stays "campaign":** show "Resume campaign" /
  "Save campaign state?" to the player (not the engine-generic "scene"
  wording). The operation is unchanged; only the visible noun differs.

## Save protocol — CoA specifics

> **Doctrine lives upstream; this section is CoA's concrete application.**
> The staging *mechanism* (compose-during-play, one-beat lag, retcon
> deferral, save = flush, transcript carve-out) is defined once in
> [Calliope's `scene_lifecycle.md` §5a-bis]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/scene_lifecycle.md),
> and its *work-level lifecycle* (resume picks up staging, switch refuses an
> unstaged beat) in
> [Aria's `story_lifecycle.md`]({{PLUGIN_ROOT}}/engines/story-engine/rules/story_lifecycle.md)
> ("Staging (work-scoped)"). What follows is CoA's binding: the staging-file
> format with CoA's domains, and the flush wiring.

CoA **stages** each confirmed beat's deltas during play and **flushes** them
at save time via `scripts/flush_campaign_staging.ps1` (the scene skill's
"Save handling" invokes it). Two consequences for the save cost:

- **The model never reads or writes an overlay at save time.** §5a's
  cost-flat concern — a `Read`-whole + `Write`-back is a multi-thousand-token
  round-trip *in the model's context* on a mature overlay — is avoided
  entirely: composition happens incrementally during play (staging tail), and
  the flush is a deterministic script. The script's own read-existing +
  append on a 31 KB monolith is sub-second and costs zero model tokens, so the
  prohibition does not bind it.
- **CoA stays monolith (no sharding).** The flush **appends** each delta block
  to the existing per-entity overlay in the exact byte format fiction-host
  writes (`runtime/state.py::format_delta` / `append_delta`), so a campaign
  played through the runtime stays parse-compatible. The D4 *latest-entry-wins*
  invariant orders entries within each monolith as before; the objective event
  logs (`aestrum_events.md`, the Nortmunde overlay) accumulate the same way.

This override supplies:

- **State directory:** `{{PROJECT_ROOT}}/campaign_state/<C>/` (per the path table).
- **Time-tag format for delta entries:** `### Day [X] — [short descriptor]`.
  Delta entries are always **level-3 headers** (`###`, never `##`) — the
  host's entry parser and time-filter only see level-3 entries, so a `## Day`
  header silently breaks loading.
- **Field vocabulary (per the engine's §5a envelope/vocabulary split):** CoA
  delta entries use the engine's six default fields (*Now knows*, *Now
  believes / suspects*, *Relationship shift*, *Emotional / situational state*,
  *Unresolved*, *Items / changes*) **plus** the asymmetric-aspect slots below
  (*Relationships / disposition*, *Agenda / intentions*, *Knowledge boundary*),
  each written as a `- **Label:** value` bullet inside the entry. Drop any
  label that doesn't apply.
- **Overlay frontmatter:** a saved overlay that shadows a canonical base sheet
  declares `overlay_for: <repo-relative path to the base file>` (e.g.
  `overlay_for: npcs/chapter_1/[slug].md`) — always a real file path, never a
  campaign label. Self-contained sheets (custom PCs with an inline log) omit it.
- **Overlay categories:** npcs, party, locations, factions, items, timelines
  (per path table).
- **Transcript path:**
  `{{PROJECT_ROOT}}/campaign_state/<C>/conversation_states/[npc_name]_day[X]_[short_descriptor].md`.
  The staging filename **is** the scene id `<sid>`, so name it by this
  convention — the flush writes the transcript to
  `conversation_states/<sid>.md`.
- **Transcript frontmatter:** include `content_rating: [T|M|AO]` and
  `aestrum_day: [X]`.

### Staging file format

One staging artifact per in-flight scene at
`{{PROJECT_ROOT}}/campaign_state/<C>/staging/<sid>.md`. It is working scaffolding, not state:
not loaded by normal participant resolution; only the resume path reads it.
The flush splits it on top-level (`#`) sections and routes each:

```markdown
---
scene_id: <sid>
campaign: <C>
aestrum_day: <X>
last_staged_beat: <N>
---

# Objective log
### Day <X> — <descriptor>
- <terse fact; index, not transcript (D6)>

# Experience deltas
## party/<name>          (Player PC or PC companion → party/saved/<name>.md)
### Day <X> — <descriptor>
- **Now knows:** ...
## npcs/<name>           (NPC → npcs/saved/<name>.md)
### Day <X> — <descriptor>
- **Relationship shift:** ...

# Entity overlays
## factions/<id>         (→ factions/saved/<id>.md)
## items/<id>            (→ items/saved/<id>.md)
## locations/<id>        (→ locations/saved/<id>.md)
### Day <X> — <descriptor>
- <delta bullet>

# Transcript
---
<transcript frontmatter>
---
<full transcript body — always the LAST section (carve-out)>
```

- **Header levels.** `#` = section; `##` = per-entity sub-section whose header
  is the routing token `<save-domain>/<name>`; `###` = the delta entry that
  lands in the overlay (the same `### Day X — …` envelope above). The flush
  appends the whole `##` body (the `###` block) to its target monolith.
- **`# Experience deltas` is required**; the others are optional.
- **`# Transcript` is always last** — the flush carves it to EOF before
  splitting sections, so transcript prose beginning with `#` is never mistaken
  for a section header (Calliope §5a-bis carve-out).
- **Routing recap:** experience `party|npcs/<name>` → `<domain>/saved/<name>.md`;
  entity `factions|items|locations/<id>` → `<domain>/saved/<id>.md`; objective
  log → `timelines/saved/aestrum_events.md`; transcript →
  `conversation_states/<sid>.md`.

### Save discipline (inherited — D1–D6)

The engine's save invariants
([{{PLUGIN_ROOT}}/engines/prose-engine/scene/references/scene_lifecycle.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/scene_lifecycle.md#scene-lifecycle.save-discipline),
"Save discipline (invariants D1–D6)") bind every CoA save. Their CoA-specific
application:

- **D1 — explicit only.** State is written **only** on an explicit
  **"save campaign state"** (or the player's yes to the close prompt). Pausing,
  resuming, switching the active campaign, an OOC question, or a dice
  clarification never writes to `{{PROJECT_ROOT}}/campaign_state/<C>/`. Never save proactively.
- **D2 — corrected fiction only.** Re-prompts, in-scene corrections, a
  director's directive, or a Rule-of-Cool override that revised a beat mean the
  saved deltas reflect the fiction **as it finally stands** — not the superseded
  roll or passage. Reconcile against in-session retcons before appending.
- **D3 — in-scene experience only.** Overlays take only in-fiction content.
  The **dice mechanics readout** (`*[Performance check — d20 … vs DC … → …]*`),
  the player-meta vocabulary, OOC clarifications, and the day-index discussed
  OOC are all meta and are **never** written into an NPC/PC overlay or timeline —
  only the rolled *outcome as it played in the fiction* is saved. (This is the
  canonical CoA case of D3: the readout is DM→player output, outside the
  fiction.)
- **D4 — latest entry wins.** The most recent `### Day [X] — …` entry in the
  objective event logs (`aestrum_events.md`, the Nortmunde overlay) is the
  latest event; earlier entries that contradict it lose and are flagged. D4
  governs the **chronological ordering of the objective logs only** — it is *not*
  the loop's memory model. What a Loop NPC *retains* across a Modify-Memory reset
  is handled by the time-filter (see *Time-filter format*), not by D4; the two
  are orthogonal.
- **D5 — record only what changed.** A delta entry carries what changed in this
  scene; state that persists unchanged from a prior entry (a standing fact the
  NPC already knew, an unshifted disposition, a still-withheld secret) is
  conveyed by silence, not re-asserted every entry. The time-filtered load
  rebuilds standing state by replaying entries; a re-asserted "still does not
  know X" each scene is noise that bloats the overlay. Only transitions earn a
  bullet.
- **D6 — the objective record stays terse.** The objective logs
  (`aestrum_events.md`, the Nortmunde overlay) are an index, not a transcript:
  terse fact bullets, no verbatim dialogue, no "carried forward" working-state
  snapshots. The full prose is in the saved transcript.

### Overlay header conventions (asymmetric-aspect slots)

So that the load-time build (`character_memory_template.md` §2b) can populate
the relationships/disposition and agenda slots reliably, save accumulated
state under these standardized sub-headers within a delta entry. These
codify the free-form headers already in use. Saved overlays conform to the
entry envelope above (`### Day [X] — …` level-3 entries, `- **Label:** value`
bullets); unrecognized label phrasing inside an entry is normalized
opportunistically the next time the character is saved.

- **Relationships / disposition** ← rapport / relationship / read-of-[other
  character]. The character's trust, allegiance, and standing toward others,
  and their own read of them.
- **Agenda / intentions** ← open threads / queued / unresolved. The
  character's active intentions, plans, and open questions.
- **Knowledge boundary** ← still does NOT know. The existing `unknown_flags`
  analog — already aligned; named here for completeness.

Languages need no overlay header: comprehension is read from the 5e sheet
(per rows 16–18 above), with only newly-learned scripts recorded as overlay
literacy when they occur.

**Hard write-scope rule:** never write to canonical in-repo paths
(`npcs/chapter_1/`, `locations/`, `rules/`, etc.); never to
`{{PROJECT_ROOT}}/campaign_state/_shared/**`; never to another campaign's subtree. Surface
canonical edits to the user and wait for explicit approval.
