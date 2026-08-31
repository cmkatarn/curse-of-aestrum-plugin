# Character Memory — Generic Build Procedure

Reference loaded on demand from `scene/core.md`. Used at
scene start to construct each participant's working memory block.
Not needed mid-scene.

This file describes the **generic** procedure. The consuming game's
override file supplies the character-type table, path conventions,
time-anchor format, and any subsystem flags.

---

Repeat this process for every character in the scene. Do it before
the scene begins.

## 2a. Identify Character Type

The override file supplies a character-type table indicating, for each
type:

- Where the **base file** lives (canonical reset-state, tracked in the
  game repo).
- Where the **overlay file** lives (accumulated state from this
  playthrough, kept outside the game repo).
- Whether the character's memory is **time-filtered** (subject to a
  daily reset, in-fiction memory wipe, etc.) or **continuous** (linear
  accumulation).

Determine the character's type from the override's table or from the
character's base-file frontmatter (e.g., a flag like `memory_continuous:
true`).

## 2b. Load and Merge Files

1. `Read` the base file. Extract:
   - Character overview, personality, behavioral profile.
   - Speech pattern and voice notes.
   - The **Character Memory** section (reset-state knowledge for
     time-filtered characters; current canonical knowledge for
     continuous-memory characters).

2. `Read` the saved overlay file if it exists. Many characters may have
   no overlay yet — proceed with base only in that case.

3. **Merge with time filter:**

   **For time-filtered characters:** Include an overlay knowledge entry
   only if its time-tag is **strictly earlier** than the specified time
   anchor, **OR** if its time-tag matches the specified time anchor AND
   the event described has plausibly occurred before the specified time
   of day.

   **For continuous-memory characters:** Include all overlay entries
   without filtering by default — these characters accumulate state
   linearly.

   > *Exception:* If the user is intentionally loading a continuous-memory
   > character at an earlier in-game time to replay a scene, apply the
   > time-filter above. Default is no filtering.

   **Populate the asymmetric-aspect slots from existing content.** The
   block's known-languages, relationships/disposition, and agenda slots
   (see §2c) are filled at load from whatever the base and overlay already
   carry — including state written before these slots were named, in
   free-form prose. The override file supplies the **header conventions**
   that map prose sections onto these slots; consult them so a character
   whose data predates the schema still surfaces it. No file rewrite is
   required: the block is rebuilt from source every load.

4. **Reconcile base-file creation-snapshot claims against accumulated
   state.** A base file written at character creation often carries
   current-status statements as if they were perpetual present-tense —
   *"first meeting," "has not yet X," "newly arrived," "currently lives
   at Y," "the contract is unsigned,"* and similar. **These are baselines,
   not invariants.** Play accumulation can supersede them: by the time
   you resume, a "first meeting" may already be the *third* meeting; a
   "has not yet X" may already have X-d.

   Overlay deltas record only what **changed** in each scene (per the
   consuming game's true-delta discipline). An event that has happened
   may carry no delta saying *"this happened"* — overlays record state
   *shifts*, not full state. The build must therefore reach beyond the
   deltas for the **structural shape** of accumulated history
   (engagement / trip count, location-of-living, time-since-key-event,
   current-status of named relationships, whom-the-PC-has-already-met).
   The consuming game's override supplies the source — typically the
   **scene transcript frontmatter** (the YAML block: period, location,
   participants, scene_label, per `{{PLUGIN_ROOT}}/engines/prose-engine/scene/references/scene_lifecycle.md` §5b), which is
   cheap to read and exactly anchors the shape deltas don't.

   If an accumulated source supersedes a base-file claim, the live
   working-state value overrides; the base-file phrase is **not**
   treated as live present-tense. Note the override in the working
   block so later gate checks ground in the live value, not the
   superseded snapshot. A base-file claim that *is* still consistent
   with accumulated state stays in effect as written.

5. **Consult timeline files if needed.** If you're unsure what has
   happened to a character by a given time, the override file points to
   the relevant timeline overlays for both canonical events and
   the active overlay set's event logs.

## 2c. Write the Character Memory Block

For each character, produce a working Character Memory block. Keep this
internal — do not show it to the user. It should summarize:

- Who this character is, what they know, what they don't know.
- Their current emotional / situational state at this moment.
- Their voice and speech pattern.
- Any **knowledge flags**: things they MUST NOT know at this time.
- **Known languages / literacy**: the spoken-language set this character
  understands and the scripts they can read. Sourced from the consuming
  game's sheet (override-supplied field). This is the character's
  comprehension boundary — content in a language or script outside this
  set is not understood (enforced at the gate).
- **Relationships / disposition**: this character's trust, allegiance, and
  standing toward others present and absent — *and* their **read of** other
  characters (their own perception of others, bounded to what they have
  observed). A relationship-fact this character has no grounds to know is a
  boundary they MUST NOT display.
- **Agenda / goals**: this character's active intentions, hidden plans, and
  open threads. This is **boundary state** — other characters MUST NOT act
  on or assert it without in-fiction access.
- Any **subsystem state** the override flags (e.g., audio cues,
  etc.) — the override file specifies what to check and
  record.

**This block is the character's epistemic boundary.** You enforce it throughout the scene.

---

## Notes for the override author

If the game has multiple distinct character types with different memory
rules, the override's character-type table should specify each one's:

- Canonical base path.
- Overlay path.
- Time-filtering policy (filtered / continuous / hybrid).
- Frontmatter flags that indicate special behavior.

The override may also need to specify name-collision fallback order — if
an NPC name could resolve to multiple files, which path is checked first.
