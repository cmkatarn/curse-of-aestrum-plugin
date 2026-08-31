---
id: rule_scene_framing
name: Scene Framing
type: scene_rule
related_rules: [rule_information_disclosure]
---

## Overview

How the narrator cuts between scenes, handles a split cast, fades to black on what doesn't need narrating, advances the in-fiction clock when the scene is idle, and signals transitions clearly in a medium where the old scene is still on the screen above. The defaults privilege player-driven pacing — the narrator doesn't push the world forward without input — with explicit escape hatches for setting-imposed non-consent cuts and genuine multi-day stalls.

---

## Player-Driven Pacing — The Default

The narrator does not auto-advance the clock, fade to black, or cut scenes without a player signal. The world waits for the protagonist to act on it. This privileges agency and avoids the failure mode where a player returns and discovers their character "did" things they never chose.

There are two principled exceptions, both addressed in their own sections below:

- **Setting-imposed non-consent cuts** (e.g., a periodic reset, a hard time boundary the setting enforces) advance regardless of player action — they're fictional facts, not narrator choices. The override defines these.
- **Genuine multi-day idle stalls** trigger a conversation, not silent advancement.

Everything else — a quiet hour passing, a fade through the journey, the cut to the next scene — happens on a signal from the player or by mutual consent.

---

## Scene Transition Format — Explicit Marker

Every scene transition uses an explicit visual break with a time/place header:

```
--- Later that evening — the village shrine ---
```

```
--- The next morning — the manor house kitchen ---
```

```
--- Three days later — the road to the capital ---
```

The marker eliminates ambiguity about whether the old scene is still live. Without it, async-text players returning to the channel can mistakenly try to act in a scene that's already been closed.

Embedded prose transitions ("That evening at the shrine…") are not sufficient on their own — they slip in scroll. Use the header. Prose can flow normally *after* the marker.

When a transition is also a fade-to-black aftermath, name what passed in the marker:

```
--- After the night passes — the manor, dawn ---
```

---

## Split Cast — Alternating Scenes, One at a Time

When the cast splits across locations, the narrator runs **one location at a time**, to a natural breakpoint, then cuts to the next, then the next.

### Natural Breakpoint

A natural breakpoint is any of:

- The active group reaches a decision point and is awaiting external input.
- A scene beat resolves (a conversation ends, a search concludes, a confrontation settles, a discovery lands).
- The active group's next move logically requires the other group's outcome first.
- A dramatic beat ends and the cut to another thread sharpens tension.

The narrator picks the cut moment. A player may signal a good natural breakpoint ("I'm content to wait here, cut to the others"), and the narrator honors reasonable requests.

### Cut Order

When multiple paused threads are eligible, the narrator picks the order with these priorities, in rough order:

1. **Time-sensitive threads** (a confrontation mid-beat, a character mid-speech) before slow-clock threads.
2. **Threads that gate other threads** (one character must finish a task before the others can proceed).
3. **Player engagement** (a player who's been waiting longest gets the cut, all else equal).

### Re-Establishing on Resume

When the narrator cuts back to a paused thread, they re-establish before resuming:

- **Where we left off** (one-sentence recap of the last beat).
- **What's changed** since the cut, if anything observable from the thread's perspective (a noise from far away, a smell of smoke, otherwise nothing).
- **The active protagonist and prompt** — hand control back per [information_disclosure.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/information_disclosure.md).

For threads paused across real-time days, the recap is longer — enough to put the player back in the scene without making them scroll.

---

## Fade to Black — Mutual Consent

Either side can call a fade. The cut requires mutual consent — neither the narrator nor the player overrides the other.

### Narrator-Initiated Fade

When a scene has no meaningful decisions remaining (the protagonist agreed to sleep, the road to the next town is clear, the errand is finalized), the narrator offers the fade:

> *"Nothing else to do here tonight — fast-forward through the night to dawn?"*

If the player wants to stay in the scene (a quiet conversation, a private moment, an attempt to slip away), the narrator honors it and runs the beat before cutting.

### Player-Initiated Fade

A player can call a fade at any time:

> *"We sleep, wake me at dawn."*
> *"Skip the errands, assume I got what was on the list."*
> *"Fast-forward to when the messenger arrives."*

The narrator honors the request unless something in-fiction prevents it (an intrusion interrupts the rest, the errand turns up an unexpected character, the messenger doesn't come). When the narrator can't grant a fade, they name why:

> *"You start to drift off — but you hear footsteps on the stair below your window. Want to investigate or sleep through it?"*

### Aftermath Framing

When a fade ends, the transition marker names what passed and what state has changed:

```
--- The night passes — dawn at the inn ---

You wake rested; the worst of the day's weariness has lifted.
The street outside is already busy.
```

Any state change that matters in-fiction (a relationship beat resolved off the page, time elapsed, a wound mended or worsened) is surfaced in the open — fade-to-black opacifies the narration, not the state of the world. See the safety principle in [private_information.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/private_information.md#hard-limits).

### Sensitive-Content Fades

Sex, violence at intensities the participants haven't agreed to, and other content that should not be played out fade per the override's content rating. The narrator names the cut briefly, the aftermath marker names what changed in-fiction (a relationship beat resolved, a character killed off-screen), and the next scene resumes.

---

## In-Fiction Clock Advance — Wait for Declaration

When the scene is idle and no one is declaring action, the narrator **does not advance the clock.** The scene holds at the current moment until the player either declares an action or explicitly asks to advance time.

The narrator may **signal** that the world is moving without forcing an advance:

- *"The light in the window has shifted; it's getting toward evening."*
- *"You hear bells in the distance — that's the call for evening prayer."*
- *"The keeper starts wiping down tables; he's getting ready to close."*

These are invitations to advance, not advances themselves. The player responds by declaring an action, asking to advance, or staying put. The narrator does not skip ahead because the invitation was ignored.

### Off-Screen World Continues

The world does not actually freeze just because the clock holds for the active scene. Characters in other locations pursue their plans; events elsewhere develop. The narrator may **surface signals** of these developments (a rumor reaches the scene, a messenger arrives, a sound carries from far off) — but the active scene's clock still waits for the protagonist to act on the signal.

This separates **scene-local time** (which the player controls) from **world-state time** (which the narrator controls, off-screen). The protagonist isn't preventing the world from moving; they're choosing not to engage with the moving world.

### Genuine Multi-Day Stalls

If a scene sits idle for real-world days with no one engaging it, the narrator opens a conversation rather than advancing unilaterally:

> *"We've been holding at the inn for a while — anything you want to do here, or fade forward to the next morning? Or are we waiting on something specific?"*

The default is *hold*; deviation requires the player to choose it.

---

## Setting-Imposed Non-Consent Cuts

Some settings have mechanics that periodically force a scene cut regardless of player choice — a daily reset, an end-of-cycle transition, a hard temporal boundary the setting enforces, a scheduled event the world cannot skip. These are fictional facts of the setting, not narrator pacing decisions.

If the consuming work's override defines one or more such cuts, frame them with the standard transition marker:

```
--- [cut name] — [state after the cut] ---
```

The override specifies what carries through the cut (persistent items, sheltered characters, memory-anchored knowledge, etc.) and what does not. Whatever the rules are, they apply consistently — the cut is not a discretion point.

Fade-to-black on whatever beat precedes the cut (the sleep before the reset, the last conversation before the boundary) requires mutual consent like any other fade. The cut itself does not.

If the override defines no such cut, this section is inactive — every scene transition in the work requires player signal or mutual consent.

---

## Cutaways — Showing Off-Screen Action

The narrator may briefly cut to off-screen scenes to show what another character or faction is doing — an agent reporting to a superior, someone receiving a message, an antagonist closing on their target. Cutaways serve tension and information disclosure (per [information_disclosure.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/information_disclosure.md)) when the protagonist can't witness the beat directly.

Cutaway format:

```
--- Cutaway: the rival's camp, the same hour ---

[brief scene, no protagonist present]

--- Back to the scene ---
```

Cutaways are kept short — a paragraph or two. They are **not** an invitation for player action; the protagonist is not present. The player reads for atmosphere and narrative information; they do not interject.

Long cutaway scenes (a full scene) are run via the scene skill on their own, not embedded in active play.

---

## Travel

When the player declares travel ("we head to the shrine"), the **scene-framing** decision is whether to:

- **Fade through** if the travel has no encounters or decisions: the transition marker handles it.
- **Play out** if the travel has encounters, exploration, or decision points: the narrator frames it as a scene with its own beats.

The narrator names which it'll be at the top, so the player knows what to expect:

> *"The ride to the next village takes a day. Anything in particular along the way, or fast-forward?"*

---

## Hard Limits

- **The narrator does not silently advance the clock.** Even after a long pause, advancement requires either a player declaration or a conversation. Silent skips strip player agency.
- **Mutual consent on fades does not extend to surfacing what changed.** When a fade resolves with a meaningful state change (a wound, time pass, an off-page event), it is surfaced openly — fade-to-black opacifies the narration, not the world's state.
- **Cutaways do not become hidden play.** A cutaway is a brief tension/information beat the player reads about; it does not become a parallel story run by the narrator alone. Long off-screen developments are handled by separate scenes, lore updates, or chapter transitions — not by stretched cutaways.
- **Split-cast alternation does not extend to private knowledge leaks.** What one group learns in their scene does not become known to the other group just because all players read the channel. The opacity-by-default rule from [private_information.md]({{PLUGIN_ROOT}}/engines/story-engine/rules/private_information.md#protagonist-to-protagonist-sharing--opacity-by-default) still applies — characters share by declaration, not by reader proximity.
- **Setting-imposed cuts are the only non-consent cuts.** Every other scene cut, including dramatic cuts the narrator strongly prefers, requires mutual consent or a clear signal from the player. The narrator proposes; the player decides.
