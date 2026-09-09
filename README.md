# Curse of Aestrum — Claude Code plugin

An interactive Dungeons & Dragons 5e campaign, set in the duchy of Aestrum where something is deeply and secretly wrong, played in [Claude Code](https://claude.com/claude-code). This repo is a **Claude Code marketplace** hosting the campaign as an installable plugin.

## Install & play

```
/plugin marketplace add cmkatarn/curse-of-aestrum-plugin
/plugin install curse-of-aestrum@curse-of-aestrum
```

Then open Claude Code in a fresh, empty folder (your play-state is written there) and run
`/curse-of-aestrum:create-party`, then `/curse-of-aestrum:scene`. See
[plugins/curse-of-aestrum/README.md](plugins/curse-of-aestrum/README.md) for requirements
(you'll need Python for the play-time gate) and full instructions.

## Content rating

**Written for adults** — occult horror, violence, manipulation, and intimate themes, played at a
content rating you set per session that reaches fully explicit at its top tier. Scale, defaults, and
the limits that hold regardless: [plugin README](plugins/curse-of-aestrum/README.md#content-rating).

## Support

The campaign is free and stays that way. It is a one-person project — the campaign, the
bundled engines, and the build that assembles them — so if it gave you a good night at the
table and you want to say thanks: **[ko-fi.com/cmkatarn](https://ko-fi.com/cmkatarn)**.
Entirely optional, and it unlocks nothing, because nothing is locked.

## Repo layout

- **`plugins/curse-of-aestrum/`** — the generated, installable plugin (self-contained: the
  campaign content plus the bundled Calliope / Aria / Bailly / gate engine files, with all
  paths made portable). This is what the marketplace installs.
- **`build/`** — the assembler that generates the plugin from the source repos (campaign +
  engines). Run with `py build/assemble.py`; point it at the source repos via the `COA_SRC`
  environment variable if they aren't sibling directories.
- **`.claude-plugin/marketplace.json`** — the marketplace manifest.

The generated plugin under `plugins/` is a build artifact — edit the source repos and re-run the
assembler rather than editing it by hand.
