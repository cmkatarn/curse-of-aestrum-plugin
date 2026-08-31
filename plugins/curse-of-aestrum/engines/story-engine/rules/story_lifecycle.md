---
id: rule_story_lifecycle
name: Story Lifecycle
type: scene_rule
related_rules: [rule_scene_framing, rule_file_layering]
---

## Overview

The **work** is the container concept the prose engine (Calliope) deliberately does
not carry: a multi-scene story that groups a cast, a saved-state set, and a running
timeline across many sittings. Calliope knows only the **scene** and a generic
overlay set. This rule supplies the work concept and the player-facing lifecycle
commands, and maps each onto Calliope's generic scene-lifecycle operations in its
`scene_lifecycle.md` reference.

A consuming work's thin-shell `SKILL.md` loads this rule alongside the Calliope
scene layers; the work's override supplies the concrete bindings (the active-set
indicator path, the cast roster location, the time-anchor system).

---

## Resume
<!-- anchor: story-lifecycle.resume -->

**Player commands (and synonyms):** "resume", "continue", "resume the story",
"continue the story", "load my story", "pick it back up", or simply "resume" in a
saved-work context.

**Maps onto:** Calliope's **RESUME** operation in `scene_lifecycle.md`, scoped to
the work:

1. Resolve the **active work** from the override's active-set indicator (e.g., a
   single-line active-set file). If the indicator is missing, surface the override's
   error — never guess the work, and **never pick one by file modification time**.
2. Pass Calliope the work scope: the **viewpoint character** (the protagonist), the
   **cast roster**, and the **last-saved time anchor** for this work (from the most
   recent overlay delta entry / saved frontmatter).
3. Calliope builds the protagonist's working-memory block at that time anchor and
   produces the **gated refresher** — a player-facing recap bounded by the
   protagonist's knowledge (see the recap carve-out in Calliope's
   `epistemic_discipline_checklist.md`). The refresher passes the single gate before
   display.
4. Hand off to live play at that time anchor.

If the active work has an **in-flight staged scene** (one whose confirmed beats
were composed into a staging artifact but not yet saved — see Staging below),
that scene is the resume target: its staged running deltas seed the working
memory and live play continues *that* scene rather than opening a fresh one. A
work with no staging artifact resumes from the last saved state as above.

The refresher is the place hidden state most easily leaks (a character's secret, an
unrevealed identity, an off-screen plan). It is **not** a free-form out-of-character
summary: it carries only what the protagonist has observed, plus the override's
allowed out-of-character orientation (the time anchor for bearings, the content
rating). It never names another character's hidden state, and never surfaces a fact
the protagonist does not know — not even by negation ("you don't know X").

---

## Switch

**Player commands (and synonyms):** "switch to `<id>`", "load the `<id>` story",
"change to `<id>`", "play the `<id>` story".

**Maps onto:** Calliope's **overlay-set switch**, then a Resume:

1. **Refuse if an unstaged beat exists.** If the current work has a
   confirmed-but-unstaged latest beat (played and confirmed, but not yet staged or
   saved — see Staging below), **refuse the switch** with a one-line
   out-of-character notice and stop. That beat lives only in the conversation;
   switching away would strand it. The player saves (which stages and flushes) or
   pauses and resolves it first. (A beat already *staged* on disk is safe; only the
   single unstaged latest beat blocks a switch.)
2. Verify the target work exists per the override's path convention. If not, surface
   the override's error wording.
3. Write the target slug to the override's active-set indicator.
4. Acknowledge the switch on one line.
5. Discard in-memory character / location state from the previous work.
6. Resume against the new work (the section above), so the player lands in a gated
   refresher for the work they switched to.

---

## Save / Close
<!-- anchor: story-lifecycle.save-discipline -->

Save and close are Calliope-generic (its `scene_lifecycle.md` "SAVE AND CLOSE"
protocol). **A save is a checkpoint, not an ending:** it folds the play so far into
overlay state and leaves the scene ready to either continue or be closed out — it
never ends the work on its own, and its confirmation is not a sign-off. Closing is a
separate act the player signals explicitly. This layer adds nothing structural; a
work's override may re-supply the **player-facing wording** so the save/close prompt
reads in the work's own terms instead of the generic "Save scene state?". The
write-scope rule (overlay paths only, canonical edits need explicit approval) is
unchanged.

---

## Staging (work-scoped)
<!-- anchor: story-lifecycle.staging -->

Calliope's `scene_lifecycle.md` (§5a-bis) defines the staging **mechanism** —
composing each confirmed beat's deltas into a staging artifact during play so the
save is a near-pure flush. This layer owns the **work-level lifecycle** of that
artifact: where it lives, and how Resume / Switch / pause / close treat it. A work
opts into staging by supplying a staging path in its override; a work that does not
opt in composes its deltas at save time (correct, just slower).

- **Location.** One staging artifact per in-flight scene, under the active work's
  overlay set at the override-defined staging path
  (`<active-set>/staging/<scene-id>`). It is working scaffolding, **not** part of
  the saved overlay set, and is never loaded by normal participant resolution.
- **Resume picks it up.** On Resume, an existing staging artifact for the active
  work is the continuation target (see Resume, above): its staged deltas seed
  working memory and play continues that scene.
- **Switch refuses an unstaged beat.** The single confirmed-but-unstaged latest
  beat is in-conversation only; switching would strand it, so Switch refuses while
  one exists (see Switch, step 1). A *staged* beat is safe on disk and does not
  block a switch.
- **Close without save leaves it.** Ending a session without saving leaves the
  staging artifact in place; the next Resume of that work continues from it. It is
  **never** auto-flushed into the saved overlay set without an explicit save
  (Calliope D1). An abandoned work keeps a harmless staging artifact until the
  player returns or deletes it by hand.

---

## Hard Limits

- **The work is the container; the scene is Calliope's.** This rule supplies the
  container and the commands. The actual resume/close mechanics live once, in
  Calliope's `scene_lifecycle.md` — this rule maps to them, it does not reimplement
  them.
- **The refresher is gated, never free-form.** Resuming a work never authorizes
  dumping saved-sheet contents to the player. Hidden state stays hidden; the recap
  is bounded by the protagonist's knowledge and runs the gate.
- **The active work is resolved from the indicator, not from recency.** A resume
  reads the override's active-set indicator. Picking the most-recently-edited save
  is a bug, not a fallback.
- **Staging is scaffolding, never a save.** Only an explicit save (Calliope D1)
  flushes staging into the overlay set. Resume may read it and Switch may be blocked
  by it, but nothing auto-commits it — a paused or closed session leaves it on disk
  untouched.
