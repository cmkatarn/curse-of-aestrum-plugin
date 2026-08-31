# Curse of Aestrum

An interactive Dungeons & Dragons 5e campaign. Arrive in the duchy of Aestrum, where something is
deeply and secretly wrong. This is **Chapter 1**.

## Content rating

**Written for adults.** Occult horror, violence, manipulation, and intimate themes run through the
campaign, and **T is the floor** — it does not play lighter than that.

You choose a rating when a session starts; **M** is the default, and a saved campaign resumes at
whatever it was last set to. The rating governs the whole scene, not just sex — injury granularity,
innuendo, threat bluntness, NPC anger.

| Rating | Violence | Sexual / Intimate | Language | Other |
|---|---|---|---|---|
| **T** | Real, consequential combat; broad-stroke wounds; no torture detail. | Romance and tension on page; intimacy fades to black. No anatomical description. | Mild profanity. No slurs, no graphic obscenity. | Horror and dread at full strength. Death, loss, addiction, abuse present but not graphic. |
| **M** | Graphic violence — wound specificity, physiology, sensory detail. Stops short of torture-porn dwelling. | Sex on page with explicit emotional and physical detail, short of pornographic anatomical specificity. | Strong profanity natural to character. | Drug use, manipulation, psychological cruelty depicted in detail when in service of the scene. |
| **AO** | Full graphic violence including torture, mutilation, prolonged suffering when narratively warranted. | Fully explicit, pornographic specificity. Anatomy, mechanics, fluids, sounds. Subject to hard limits below. | No restriction. | No softening of any depicted subject for taste — only for the hard limits below. |

Say *"switch to M"*, *"drop to T"*, or *"go AO for this scene"* at any point; it takes effect on the
next response.

**Hard limits regardless of rating:**

- Sexual content involving minors, or any character not a competent
  consenting adult in the fiction.
- Real-world non-consensual sexual content rendered as titillation. Sexual
  violence may be present in the world (off-page or briefly named) when the
  story requires it; never written as erotica.
- Operational instructions outside the fiction (synthesis routes for real
  drugs/weapons/etc.).

## Requirements

- **Claude Code** and your own Claude access (Pro/Max/API).
- **Python** on your PATH (the `py` launcher on Windows, or `python3`) — used by the play-time
  epistemic-gate hooks.

## Install

```
/plugin marketplace add <owner>/curse-of-aestrum
/plugin install curse-of-aestrum@curse-of-aestrum
```

## Start playing

Open Claude Code in a **fresh, empty folder** (your play-state is written there, under
`campaign_state/`). Then:

- `/curse-of-aestrum:create-party` — build your party, then
- `/curse-of-aestrum:scene` — begin play.

`/curse-of-aestrum:mex` loads the core cycle mechanics if you want the how-it-works first.

## Credits & license

Curse of Aestrum by Cody Mallonee. Built on the Calliope (prose), Aria (story), and Canterbury (5e)
engines, bundled here. See each `engines/*/` subtree for its own license/contract.
