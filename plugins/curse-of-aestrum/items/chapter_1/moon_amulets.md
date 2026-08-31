---
id: item_moon_amulets
name: Moon Amulets
type: magical_jewelry
school: Abjuration
source: jiasha (at Selûne's direction)
effect: blocks_modify_memory
---

## Description

Small pendants worn at the throat, each bearing a stylized crescent moon. The crescent is the same on every amulet; the **material varies per recipient** — carved stone, carved bone, carved wood, unworked metal, and others. The material is the amulet's most distinctive feature and is the part keyed to the wearer.

Each amulet is a piece of jewelry to look at; the magic is not visible. A casual observer sees a small pendant on a leather thong or fine chain, more devotional than ornamental.

## Origin

The amulets are a **single Selûne-directed commission**, crafted by Jiasha at her hut on the Aestrum threshold over the course of several weeks. They are made specifically for the party of travelers Selûne foretold would arrive — one amulet per party member, no extras. Their material is keyed by Selûne's instruction to each wearer's race, class, or background, so that an amulet *feels* like it was made for the person who receives it.

The amulets are the **only** Moon Amulets Jiasha has ever made. There are no others in circulation, no historical record of similar amulets elsewhere, no copies. If the set is destroyed or lost, it cannot be replaced from this source — Selûne would need to commission another acolyte, or none, in response. See [npcs/chapter_1/jiasha.md]({{PLUGIN_ROOT}}/npcs/chapter_1/jiasha.md) for the commission's authoring context.

## Mechanics

### What the amulet does

- **Blocks the Modify Memory step of the daily reset** (see [rules/revert.md]({{PLUGIN_ROOT}}/rules/revert.md)). A wearer inside Aestrum at 4:30 AM is not targeted by the revert at all; their memories of the day's events persist.
- The amulet is **passive and continuous** while worn and attuned. No activation, no expenditure, no charges.

### Attunement

- **The amulet requires attunement.** A wearer must complete attunement (standard process — typically a short period of focused contact, e.g., a short rest spent in attunement) before the Modify Memory protection takes effect.
- **Only the attuned wearer receives protection.** Wearing the amulet without attuning to it provides no protection; the Modify Memory revert will fire normally.
- **Attunement is single-subject at a time.** An amulet attuned to one wearer cannot also be active for another. Attunement transfers if the amulet is given to a new person and they complete the attunement process — the previous wearer's attunement ends when the new attunement is established.

### Transferability — The Amulets Are Not Locked to a Single Wearer

The amulets are **not bound to a specific recipient.** Selûne's instruction keyed each amulet's *material* to the original recipient (so that it feels personal — see Personalization, below), but the magic is portable. If the party chooses to give an amulet to someone else — another traveler entering Aestrum, an NPC ally, a captured loop-resident they want to free from the revert — the recipient can attune to it and gain the protection in place of the original wearer.

Consequences of transfer:

- The new wearer attunes; the original wearer's attunement ends. Only one subject is protected at any given time.
- The original wearer, once unattuned, becomes subject to the Modify Memory revert at the next midnight (unless they have another protection in place).
- The material-personalization no longer matches the new wearer. The amulet still works, but the "this was made for me" sensation is gone — the wearer is using an amulet visibly made for someone else.
- Material-personalization is cosmetic and emotional, not mechanical. A stone amulet works for a dragonborn the same as a bone amulet would, mechanically. The personalization affects whether the *original* wearer is more likely to wear it, not whether it functions for whoever ends up holding it.

This makes the amulets a meaningful tactical resource. The party could, for example, give one to Galadiil to free her from the revert; or hand one to a snapshot resident to test the campaign's "amulet around an existing resident" edge case directly.

### What the amulet does NOT do

- **Does not prevent the snapshot from being taken** (see [rules/snapshot.md]({{PLUGIN_ROOT}}/rules/snapshot.md)). A subject entering Aestrum wearing an amulet still has a snapshot recorded at their first midnight. If they later lose or remove the amulet, the snapshot is on file and the revert will fire at the next midnight they sleep outside a dead zone.
- **Does not block the Sleep step** (12:00 AM) — the wearer falls unconscious like everyone else.
- **Does not block the Recreate step** (1:30 AM) — physical restoration still applies.
- **Does not block the Teleport step** (3:00 AM) — the wearer is still moved to their reset position.
- **Does not block the fuzzball** (see [rules/fuzzball.md]({{PLUGIN_ROOT}}/rules/fuzzball.md)). The wearer is still planted with one. However, because the wearer's memories continue to match the world's actual state, the fuzzball has nothing to correct and functionally does nothing. Treat the fuzzball as benign for amulet-bearers under normal conditions.

### Functional name

The mechanically accurate name would be "Amulet of Protection from Modify Memory." The name *Moon Amulet* is preserved because it is what Jiasha (and Selûne, through her) calls them. Players generally will not know the full mechanical scope until they attune to one, examine it carefully, or pry the answer from Jiasha.

### Concealment

The amulets work whether worn openly, tucked under clothing, or hidden in a pouch on a cord around the neck. Function does not depend on visibility. A wearer who prefers to conceal the amulet can do so without losing the protection.

### Visible Amulets and Sharran Followers

A visibly-worn Moon Amulet is **recognizable to followers of Shar as a Selûne artifact** and provokes reactions ranging from controlled disregard to open hostility. The amulets are not subtle — the crescent is the obvious mark of Selûne — and a Sharran who looks at one knows what it is.

Per-NPC reactions to a visibly-worn amulet (canon):

- **Hati Heldrivver** — disciplined enough to ignore it. She registers the amulet, factors it into her assessment of the wearer, and proceeds with whatever her current operational posture is. She will not act on the amulet alone.
- **Judith Asemyeer** — toss-up. Her reaction depends on her current state and on what else is happening in the scene. She may ignore it, may comment, may escalate. DM discretion based on the surrounding context.
- **Rowan Deckard** — visibly agitated by it. Holds the line on attacking in public spaces (his discipline is real, and exposing his Shar devotion in public would compromise his cycle), but **private spaces are dangerous in Rowan's presence while wearing one.** A party member alone with Rowan, wearing a visible amulet, is at meaningful risk of a violent reaction.

**Implication:** PCs who anticipate Sharran encounters should consider concealing their amulets. The protection is identical either way; the social signal is the variable. Concealment is the standard precaution for any PC operating in spaces where Sharran presence is suspected or known.

Other Sharran NPCs not listed here should be played per their individual files. The general rule: **Shar's followers recognize the amulets, and their reactions track their personality and operational discipline.**

### Removal and loss

- **Removed temporarily.** If the wearer takes the amulet off and then puts it back on before the next midnight, no revert fires; memory continues uninterrupted.
- **Removed at midnight.** A wearer who is not wearing the amulet at the 4:30 AM Modify Memory step is fully subject to the revert. Their memory rolls back to the snapshot.
- **Lost or stolen.** Same outcome — the protection only applies while worn. A separated amulet can be retrieved and put on again; protection resumes at that moment but does not retroactively restore reverted memories.
- **Destroyed.** The amulet is a physical object and can be broken. A destroyed amulet provides no further protection. There is no documented method to repair one within the campaign world; replacement would require a new Selûne-directed commission.

### Dead zone interaction

- Inside a dead zone, all magic ceases to function (see [rules/dead_zones.md]({{PLUGIN_ROOT}}/rules/dead_zones.md)). The amulet's protection is moot inside a dead zone because the revert itself does not fire there.
- The amulet is **not** rendered permanently inert by exposure to a dead zone — it resumes function on exit, the same as other magical items.

### The amulet around an existing Aestrum resident

Untested in canon. The amulet's protection is keyed to blocking the revert; if it were placed on a loop-resident mid-cycle, it would presumably prevent that resident's next revert. The campaign has not deployed this experiment. Treat as DM discretion if the party tries.

## DM Notes

- **The amulets are the campaign's central mechanical protection against the loop.** Without them, party memory rolls back nightly and the campaign cannot run as designed. Surfacing them to every party member is treated as a mandatory campaign beat — see [npcs/chapter_1/jiasha.md]({{PLUGIN_ROOT}}/npcs/chapter_1/jiasha.md) for handling.
- **Personalization is real, not flavor.** Selûne directed Jiasha to use materials specifically keyed to each PC. The "this amulet feels like it was made for me" sensation is intentional and is the campaign's hook for getting players to wear them voluntarily.
- **Looting an amulet from Jiasha's body still gives a working amulet.** It is an object, not a divine grant tied to her presence. The party loses Jiasha's other utility but retains the protection.
- **A PC who refuses to wear theirs** is making a Tier 1 player choice (see [rules/consequences.md]({{PLUGIN_ROOT}}/rules/consequences.md)). Let it happen. They will be reverted on their first midnight inside Aestrum and experience the loop as a resident does. The other PCs can argue with them; the consequences will play out naturally.
- **Party-specific assignments and wear status live in [saved/moon_amulets.md](saved/moon_amulets.md).**
