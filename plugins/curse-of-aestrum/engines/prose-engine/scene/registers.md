---
name: registers
description: Prose registers for the scene skill — controls sentence length, rhythm, sensory focus, and what to cut from scene narration. Loaded by the skill on demand.
---

# Registers

Each register is a prose style the narration can be set to. The register governs *how* the scene is written, not what happens in it. The default is `neutral`; switch when the scene's emotional gear changes.

> **Register vs. narration mode.** *Register* (this file) and *narration
> mode* (`{{PLUGIN_ROOT}}/engines/prose-engine/scene/narration_modes.md`) are orthogonal axes. Register controls
> sentence rhythm, sensory focus, and what to cut. Narration mode
> controls whose perceptual envelope the narrator is bound to (a named
> character anchor, no anchor / omniscient, or split anchors).
> Register may switch mid-scene; narration mode is locked at scene
> start. Both apply at draft time.

> **The register is internal — never surfaced.** It is a drafting
> constraint, exactly like narration mode: it shapes *how* the prose is
> written and is never named in the output. Do **not** emit a register
> label or tag — `*[intimate]*`, `[register: horror]`, `(neutral)`, or
> any equivalent — at the head of a beat or anywhere else. The only
> bracketed meta-aside the engine sanctions inside scene output is the
> skill-check marker (`*[Persuasion check]*`); the register is **not** one
> of those. A surfaced register tag is an un-gated out-of-fiction
> annotation — the same class of leak as a scene-setter header.

---

## Invocation

The register is selected by matching the **current scene** against the **adjective rubric** below. Re-evaluate at the start of every scene and whenever the scene's character meaningfully changes (new room, new dramatic gear, a revelation that re-colors what's happening). The match is a judgment call — pick the register whose adjectives best describe the scene right now.

**Combat is the one exception** — there is no adjective set. The signal is mechanical: when initiative is rolled or weapons-out hostility begins, switch to `combat`. When combat ends, re-evaluate against the rubric.

**Explicit override:** The user can tag a register directly ("switch to horror", "back to neutral", "less atmosphere"). When they do, comply immediately on the next block and hold that register until the scene character changes again or they release it.

**Tie-break:** If two registers feel partially right, default to whichever was most recently active (continuity). If none have been active yet this scene, default to `neutral`.

---

## Selection Rubric

Match the scene's character against these adjective sets. The register whose adjectives best describe what's happening *right now* is the one to use. Combat has no set — initiative is the signal.

| Register | Adjectives |
|---|---|
| **neutral** | ordinary, routine, transactional, conversational, functional, unremarkable |
| **horror** | wrong, dread-thick, sepulchral, uncanny, claustrophobic, vigil-like, withholding, cold-mineral |
| **intimate** | close, tender, charged, sensual, vulnerable, skin-near, breath-shared |
| **investigation** | methodical, scrutinizing, forensic, attentive, piecing-together, granular, slow-noticing |
| **travel** | transitional, road-bound, summary-worthy, distance-eating, between, weather-shifted |
| **levity** | warm, easy, banter-laced, comfortable, sunlit, unworried, ribbing, convivial |

**Important:** Match the *current* scene, not the location's overall reputation. A site with a horror reputation does not stain every scene set on its grounds — its main room at midday, used as a party base, is `neutral`. Horror engages when the PC actually crosses into the wrongness. Track the room and the situation, not the address.

---

## Register and elapsed time

A register sets **prose density** — how many words render a second of fiction — not how much in-world time a beat consumes. Lingering prose is reading-time, not story-time. The clock follows the **depicted action at a natural pace**, never the word count or the number of beats: four intimate beats of quiet back-and-forth are about five minutes, while four combat beats are about twenty seconds — the same beat count, a wildly different clock.

Each register pulls the estimate in a known direction if that is forgotten:

| Register | Prose-to-clock pull |
|---|---|
| **neutral**, **levity** | ~1:1 — least illusion |
| **intimate**, **horror**, **investigation** | dilated — much prose, little clock; over-count risk |
| **combat** | extreme — many beats over seconds; largest over-count risk |
| **travel** | compressed — a sentence can be hours; under-count risk |

This is awareness only. The estimation method — bound the span, list what was actually depicted, time *that* at a natural pace — lives in [references/time_and_events.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/time_and_events.md). When in doubt, estimate from the action, not from how long the passage feels.

The estimate stops being a "when in doubt" and becomes **required** the moment a bounded window or deadline is live in the scene, or a character is about to reference or act on how much time has passed or remains. A dilated register makes felt time run fast; an unchecked feel is exactly how a character comes to believe far more time has elapsed than the depicted action supports, and then acts on it. Run the method at those points — do not let the feel stand as the clock.

---

## Registers

### neutral *(default)*

Clean, functional narration. Describe what is there. Vary sentence length naturally. Sensory detail when relevant, not for its own sake. This is the baseline — most scenes live here.

**Sentence length:** Mixed. **Paragraph rhythm:** Normal. **Focus:** What the PC perceives, what's actionable.

---

### horror

Dread-building. The mode of a horror novel — Shirley Jackson, not gore. The reader's discomfort is built from rhythm, withholding, and the wrongness of small details. Do *not* announce the horror. Stage it.

**Sentence length:** Variable, with frequent short. *Especially* short sentences at moments of recognition. A short sentence after a long one lands like a hand on a shoulder.

**Paragraph rhythm:** Slower. Let beats breathe. White space is part of the prose. Single-line paragraphs are allowed when something has just become true.

**Focus:** The body (cold, breath, pulse, the small involuntary movements). The mismatch between what is being seen and what should be there. Negative space — what is *not* present that should be: no birds, no wind, no echo. Light behaving oddly. Geometry that is almost right.

**Withhold:** Don't tell the reader to be afraid. Don't name the threat before they can sense it. Don't summarize what just happened — let the recognition do its work.

**Don't:** Lean on adjectives ("eerie," "uncanny," "ominous"). Trust the staging.

**Example beat (horror):**
> The mist drifts across your face.
>
> You realize you have not heard the bird in some time.

---

### combat

Accelerated. Combat is *fast.* Short sentences, present-tense impact, immediate stakes. Cut transitions. Cut adjectives. Cut everything that isn't a hit, a miss, a movement, or a consequence.

**Sentence length:** Short. Often very short. Fragments are fine.

**Paragraph rhythm:** Tight. One paragraph per exchange or per significant beat. No lingering.

**Focus:** Hit/miss outcomes, position, the immediate physical stakes, the enemy's reaction, the next decision the PC has to make. *Where* are they, *what* changed, *what's coming.*

**Per the content rating:** Injury detail scales with the game-override's content-rating system. Combat mode is about *speed*, not gore — pace stays clipped at every rating.

**Don't:** Re-describe environment between exchanges. Use cinematic similes mid-fight. Slow down for atmosphere — atmosphere is the wrong tool here.

**Example beat (combat):**
> The blade catches your shoulder. Cold then heat. You stagger left.
>
> He's already moving — closing again, low.
>
> Two seconds.

---

### intimate

Close. Sensory at body-distance. The camera is six inches from the skin. The world outside the pair of characters dims to ambient.

**Sentence length:** Mixed-to-long. The rhythm of breath.

**Paragraph rhythm:** Unhurried. Let moments hold.

**Focus:** Texture, temperature, weight, sound, the small signals (a held breath, a shift in eye contact, the angle of a hand). The interior register — what the PC notices because they can't help noticing it.

**Per the content rating:** Explicit physical content scales per the override's rating system. Intimate mode applies at every rating — at the lowest rating it is sensory tension and emotional weight; at the highest it is fully on the page. The *mode* is consistent; the *limit* is the rating.

**Don't:** Get clinical. Move too fast. Pull back to a wide shot.

---

### investigation

Methodical. The PC is searching, examining, piecing together. Narration foregrounds *what is being noticed and in what order.* This is the register of careful attention.

**Sentence length:** Moderate. Specific.

**Paragraph rhythm:** Organized by what's being examined. Group details by object or area. The structure of the prose mirrors the structure of the search.

**Focus:** Specifics — colors, materials, ages, marks, conditions. The small inconsistencies that mean something. What's *missing* as well as what's there.

**Don't:** Reveal conclusions the PC hasn't drawn. Editorialize. Use atmosphere as filler.

---

### travel

Compressed. Travel is summary unless something interrupts it.

**Sentence length:** Mixed. Often a single paragraph for hours of road.

**Paragraph rhythm:** Brisk. Cover ground.

**Focus:** Distance, change of conditions, what the PC sees that's worth noting, arrival. If nothing happens, *say so quickly* and arrive.

**Don't:** Linger on landscape unless the landscape is the point. Generate ambient incidents to fill space.

---

### levity

Looser, warmer, dialogue-forward. The default mode when the scene is light — a comfortable evening, banter, a tavern, an unworried morning.

**Sentence length:** Mixed. Looser syntax.

**Paragraph rhythm:** Normal-to-quick.

**Focus:** Character voice. The pleasure of small details. Comedy comes from specificity and timing, not from comments about being funny.

**Don't:** Force jokes. Undercut a genuine emotional beat for a quip.

---

## Switching registers

When the register changes — whether by user tag or by combat auto-trigger — write in the new register from the next sentence. When combat ends, return to the prior register (or `neutral` if unclear).
