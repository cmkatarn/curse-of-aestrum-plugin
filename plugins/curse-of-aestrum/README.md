# Curse of Aestrum

An interactive Dungeons & Dragons 5e campaign. Arrive in the duchy of Aestrum, where something is
deeply and secretly wrong. This is **Chapter 1**.

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
