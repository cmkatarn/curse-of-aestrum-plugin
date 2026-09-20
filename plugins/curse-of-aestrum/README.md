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

**Content notes (subject, not intensity).** The tiers above govern *how* a thing
is rendered; these name *what* the campaign contains, so a player can decline a
**subject** rather than a rating. Chapter 1 includes:

- Reproductive coercion and repeated pregnancy loss — a husband forcing a
  contraceptive on his wife.
- Domestic abuse and intimate-partner murder, including a killing by confinement
  and enforced sleeplessness that ends in the victim's suicide.
- Stalking and obsessive "courtship," and the repeated murder of the same named
  woman over years, her bodies kept.
- A grave dug for a living child by a parent who believes it is a kindness.
- Captivity, imprisonment, and prolonged loss of autonomy.
- Memory violation as the setting's premise — people rewritten nightly without
  knowledge or consent.
- Corpse imagery at scale; desecrated religious sites.
- Animal companions can die permanently — the reset does not return them.

Most of these are discovered or background rather than staged, and the list is
not a promise that any of them is dwelt on. It exists so a player who needs to
avoid one can say so before the first session, and the DM can route around it.

## Requirements

- **The Claude desktop app** (macOS, Windows, or Linux beta) — strongly recommended; see below.
  Terminal Claude Code also works. Either way you need your own Claude access (Pro/Max, or API).
- **Python 3.11+** on your PATH — `py`, `python3`, or `python`, whichever your platform provides;
  the play-time epistemic-gate hooks find it for you. (3.9 also works if you have the `tomli`
  package installed; the gate reads TOML lint specs.)

## Play in the desktop app

Play Curse of Aestrum in the **Claude desktop app**, not in a Terminal or Command Prompt window.
The rules and the story are the same either way; what differs is what you see around them.

- **No spoilers from the machinery.** To run a scene, Claude reads character, location, and quest
  files. A terminal prints every one of those reads, filenames included, so it can show you who
  and what the story is holding before you've met them. The app's **Summary** transcript view
  shows Claude's responses and nothing else. Switch to it from the **Transcript view** menu or
  with **Ctrl+O**. (The default **Normal** view collapses that activity into one-line summaries:
  better than a terminal, but still visible.)
- **Fewer interruptions.** The app's permission-mode selector offers **Auto** mode, which removes
  most approval prompts. See *Permissions* below.
- **Your play folder is a click away.** Pick it as the session's **Project folder** before your
  first message.

## Install

Everything happens in the Claude desktop app:

1. Open **Settings**, and in the Settings sidebar under **Customize**, choose **Plugins**.
2. On the Plugins page, click **Add** (top right), then **Add marketplace**.
3. In the Add marketplace dialog's **URL** field, paste `https://github.com/cmkatarn/curse-of-aestrum-plugin`
   (the short form `cmkatarn/curse-of-aestrum-plugin` works too) and click **Sync**. The dialog's warning about
   third-party plugins applies here: Curse of Aestrum is published by its author, not by Anthropic.
4. On the Plugins page, open the **Discover** tab and find **Curse of Aestrum**.
5. Click the arrow beside **Add** on the Curse of Aestrum row and choose **Install for me**. That
   makes the campaign available in every folder, so each new play folder works without installing
   again.

### From a terminal instead

If you prefer the command line, these two commands do the same thing. Run them once from any
terminal, and the desktop app picks the campaign up in your next session:

```
claude plugin marketplace add cmkatarn/curse-of-aestrum-plugin
claude plugin install curse-of-aestrum@curse-of-aestrum
```

Inside a running terminal session of Claude Code, the same steps are
`/plugin marketplace add cmkatarn/curse-of-aestrum-plugin` and `/plugin install curse-of-aestrum@curse-of-aestrum`.

## Start playing

Start a session whose **Project folder** is a dedicated play folder with nothing else of yours in
it: your play-state is written there, under `campaign_state/`. Then:

- `/curse-of-aestrum:create-party` — build your party, then
- `/curse-of-aestrum:scene` — begin play.

`/curse-of-aestrum:mechanics` loads the core cycle mechanics if you want the how-it-works first.

## Permissions — for an uninterrupted session

Play reads the plugin's bundled files, runs its scene-loader and save scripts, and writes your
play-state to `campaign_state/`. If you're asked about each of those, the prompts land mid-scene,
which is exactly where they hurt most.

**In the desktop app, choose Auto** in the permission-mode selector next to the send button. Claude
then acts without asking and runs background safety checks that its actions match your request.
Auto mode needs a Pro or Max plan (or API access) and a supported model: Claude Opus 4.6,
Sonnet 4.6, or later. Together with the **Summary** view, a scene reads as prose and nothing else.

Without Auto, **Accept edits** is the next best choice. It approves file writes automatically but
still asks before running the loader and save scripts. **Manual** asks about everything.

**Bypass permissions** also removes the prompts, but it turns off every check for the whole
session, and it has to be enabled in the app's Settings first. If you use it, use it only in a
dedicated play folder with nothing else of yours in it, and only with campaigns you trust.

**In a terminal**, answer the first prompt of each kind with **"Yes, and don't ask again"** where
it's offered. Claude Code saves each approval as a rule in the play folder's
`.claude/settings.local.json`. `claude --dangerously-skip-permissions` is the terminal's bypass, and
the same cautions apply.

## Bugs & feedback

Found a bug, a dead link, or a scene that went sideways? Open an issue:
**[github.com/cmkatarn/curse-of-aestrum-plugin/issues](https://github.com/cmkatarn/curse-of-aestrum-plugin/issues)**

A useful report names the skill you were running (`scene`, `create-party`, …), the version from
`claude plugin details curse-of-aestrum`, and what you expected instead. Your play-state lives in your
own `campaign_state/` folder, so paste from it only what the report needs — an issue is public.

## Support

The campaign is free and will stay that way. That being said, it is a one-person project — the
campaign, the (massive) bundled engines, and the build that assembles them — so if you enjoy your
time in Aestrum and want to say thanks, consider donating here:
**[ko-fi.com/cmkatarn](https://ko-fi.com/cmkatarn)**. Any contribution is entirely optional and unlocks nothing,
because nothing is locked.

## Credits & license

Curse of Aestrum by Cody Mallonee. Built on the Calliope (prose), Aria (story), and Bailly (5e)
engines, bundled here. See each `engines/*/` subtree for its own license/contract.
