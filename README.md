# Curse of Aestrum — Claude Code plugin

An interactive Dungeons & Dragons 5e campaign, set in the duchy of Aestrum where something is deeply and secretly wrong, played in [Claude Code](https://claude.com/claude-code). This repo is a **Claude Code marketplace** hosting the campaign as an installable plugin.

## Install & play

**Play in the Claude desktop app**, not in a Terminal or Command Prompt window. A terminal prints
every character, location, and quest file Claude reads to run a scene, so it can show you what the
story is holding before you've met it. The app's **Summary** transcript view shows the story and
nothing else, and its **Auto** permission mode keeps prompts from interrupting a scene.

To install, open **Settings → Plugins** in the desktop app, click **Add → Add marketplace**, and
paste `https://github.com/cmkatarn/curse-of-aestrum-plugin`, then click **Sync**. Then find **Curse of Aestrum** on the
**Discover** tab and choose **Install for me**. The
[plugin README](plugins/curse-of-aestrum/README.md#install) walks through each click, and also
gives the two terminal commands if you prefer the command line.

Then, in the desktop app, start a session with a dedicated play folder as the **Project folder**
(your play-state is written there) and run `/curse-of-aestrum:create-party`, then
`/curse-of-aestrum:scene`. See [plugins/curse-of-aestrum/README.md](plugins/curse-of-aestrum/README.md)
for requirements (you'll need Python for the play-time gate), permissions, and full instructions.

## Content rating

**Written for adults** — occult horror, violence, manipulation, and intimate themes, played at a
content rating you set per session that reaches fully explicit at its top tier. Scale, defaults, and
the limits that hold regardless: [plugin README](plugins/curse-of-aestrum/README.md#content-rating).

## Support

The campaign is free and will stay that way. That being said, it is a one-person project — the
campaign, the (massive) bundled engines, and the build that assembles them — so if you enjoy your
time in Aestrum and want to say thanks, consider donating here:
**[ko-fi.com/cmkatarn](https://ko-fi.com/cmkatarn)**. Any contribution is entirely optional and
unlocks nothing, because nothing is locked.

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
