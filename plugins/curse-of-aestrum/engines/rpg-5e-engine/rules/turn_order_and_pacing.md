---
id: rule_turn_order_and_pacing
name: Turn Order & Pacing
type: homebrew_rule
related_rules: [rule_combat, rule_active_effects_tracking, rule_information_disclosure]
---

## Overview

How initiative is managed, how the DM prompts the right player, what happens when a player is slow or absent, how out-of-order posts and readied actions are handled, and how combat carries across sessions. Async text breaks the in-person assumption that everyone is in the room and responds in seconds — this rule codifies the cadence so combat stays coherent without anyone needing to chase the table.

---

## Initiative — Per-PC RAW

Initiative is rolled per PC and per discrete foe group at the start of combat. RAW 5e: d20 + Dex modifier, highest acts first, ties broken by Dex score then by player choice. Foe groups (four identical bandits acting on one initiative) collapse to a single number to keep the order short.

The rolled order persists for the encounter. Delays and ready actions modify position per RAW; the tracker reflects them as they happen.

---

## Initiative Display — Top of Every Round, Plus On Request

The DM prints the initiative order at the start of **every new round**, with a marker for the active PC. Format:

> **Round 3 — Initiative:**
> 1. Kara (22)
> 2. **→ Doran (17) ←**
> 3. Bandit Caster (15)
> 4. Bandit group A (12)
> 5. Sera (9)
> 6. Bren (7)

The block solves the "who's next?" scroll-up problem and gives the active PC unambiguous focus. Players may ask for a re-display any time without penalty.

Within a round, the DM advances through the order silently between turns — no need to re-print the block between every action. The active PC is named in the turn callout (see [combat.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/combat.md#layer-c--active-pc-callout-on-that-pcs-turn)).

---

## Prompting the Active PC

The DM names the active PC explicitly at the start of their turn — not "what do you do?" addressed to the room, but a clear handoff:

> ***Doran — your turn.***
>
> *From the wagon: the sword bandit is 25ft (one move), the caster 60ft behind the campfire. Kara is still locked with the sword bandit. **Active on you:** Bless (3 rds).*
>
> *What do you do?*

The named handoff is the DM's signal that prompts a player to engage. Without it, async text players assume the previous beat is still resolving and don't realize they're up.

Two parts of the handoff are distinct. The **structural skeleton** — naming the active PC, then the actionable distance/effects state line — is required and fixed; it is what makes the turn unmistakable. The **closing invitation** ("What do you do?" above) is only *one* surface form. Its phrasing is owned by the consuming narration layer's action-prompt convention, which varies the invitation in-register so it never reads as a repeated token. In combat the invitation varies conservatively: the turn signal must stay unambiguous, so clarity wins over flourish whenever they conflict.

---

## Slow Response — Hold the Round

When the active PC is slow to respond, **the DM holds the round.** Combat pauses at their turn. The other players do not skip ahead; no conservative default action is run on the player's behalf without their consent.

This privileges player agency over flow. A player's turn is theirs to declare; the DM does not decide for them by default.

### Escalation for Extended Absence

Indefinite holds compound — a missing player for a week stalls four others. The escalation path is:

1. **Hold by default** — no time pressure on a normal slow response.
2. **Check-in after extended silence** — the DM opens a table conversation: *"Doran's been quiet for [N days] — how do we want to proceed? Hold, run a conservative default, or NPC the PC for the duration?"* No specific threshold is hardcoded; the table judges what counts as extended for the current session cadence.
3. **Resolve by table agreement** — if the table chooses to continue, the DM runs the agreed approach: hold longer, run a conservative default (typically Dodge + hold position), or run the PC under DM control with the player's general intent as the guide.

The escalation is a conversation, not a rule the DM applies unilaterally. The default is *hold*; deviation requires the table to choose it.

---

## Out-of-Order Posts — Queue as Declared Intent

When a player posts an action before it's their turn, the DM:

1. **Acknowledges the post** — does not ignore it.
2. **Queues it** as that PC's declared intent for when their turn arrives in initiative.
3. **Prompts the player whose turn it actually is.**

When the queued player's turn comes up, the DM runs the queued action — with one explicit offer: *"Lior, your declared move was [X]. The situation has changed: [delta]. Stick with it or revise?"*

This honors the post (the player engaged), preserves initiative meaning (the order still matters), and gives the player a chance to revise if the battlefield has shifted between their post and their turn.

---

## Readied Actions — Auto-Fire on Trigger

When a player readies an action ("I shoot the first bandit who breaks cover"), the readied action **auto-fires when the trigger condition is met,** even if the readying player is offline at the moment of the trigger.

The DM:

1. Confirms the trigger fires per the player's stated condition.
2. Resolves the readied action — rolls the attack, applies the result, narrates the beat.
3. Notes the resolution clearly so the player can review on return.

If the trigger is ambiguous ("a bandit acts suspiciously"), the DM applies the most reasonable reading and flags the ambiguity for the player on return — never the strictest reading that quietly negates the ready, never the most generous that fires on weak triggers.

If the trigger does not fire during the round, the reaction is recovered at the start of the readying PC's next turn, RAW.

---

## Surprise Rounds

When a creature is surprised, they take no actions, no bonus actions, no reactions on their first turn, RAW. The DM names this explicitly at the start of the surprised party's turn:

> *Round 1 — the bandits caught you flat. **Doran, surprised — no actions this turn.** Round continues with the next initiative slot.*

Don't silently skip a surprised PC's turn — name the condition, name the round's continuation, so the player knows what happened and that it wasn't an oversight.

---

## Out-of-Combat Turn Order

Outside combat, no formal turn order is imposed. Players post in any order; the DM resolves declarations roughly in posted order, with priority given to time-sensitive declarations (a PC reacts to a falling object before another PC continues a conversation).

The DM **may** impose a soft order when:

- Multiple PCs are talking over each other in a high-stakes social scene and the order of speaking matters.
- A coordinated action requires resolution in sequence (sneaking past a guard, picking a lock while another keeps watch).
- The scene is approaching combat and order will matter in seconds.

When a soft order is imposed, the DM names it openly: *"Order on this beat: Sera tries the door first, then Lior keeps watch, then Doran moves to the window."* Players may protest or revise before the DM runs it.

---

## Combat Spanning Sessions

When combat crosses a session boundary, the following carry forward to the next session:

- **Initiative order** — the same numbers, the same positions in the round.
- **Round number** and **which PC's turn is next.**
- **Active effects** on all combatants — per [active_effects_tracking.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/active_effects_tracking.md), captured in the session save.
- **Queued declared intents** from out-of-order posts.
- **Standing readied actions** that didn't trigger.
- **Battlefield state** — anchor positions, foe positions, environmental changes (see [combat.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/combat.md)).

At the start of the next session, the DM re-prints:
1. The initiative block (with the active PC marker).
2. The foe roster (per combat.md).
3. The active-effects state for any PC with active effects.

Pick up at the active PC's turn. No re-rolling, no re-positioning.

---

## Mode Interaction — Callout Tone, Not Content

The initiative block, the handoff's structural skeleton (named active PC + actionable state), and the order itself are **mode-independent** — shared scene state that every player needs in the same shape. The *surface form of the closing invitation* is not part of this shared state: it is register/narration-driven, owned by the consuming narration layer (see Prompting the Active PC, above).

What varies by mode (see [information_disclosure.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/information_disclosure.md#scene-density--novel-vs-game-modes)) is the **tone of the turn callout** wrapped around the prompt:

- **Game mode:** terse, mechanical. *"Doran — your turn. Sword bandit 25ft, caster 60ft. Bless 3 rds. What do you do?"*
- **Novel mode:** the same information, narratively framed. *"The bandit's blade rings against Kara's again — Doran, the moment opens. The swordsman has his back to you for a heartbeat; the caster's still chanting at the back of the clearing. Your god's blessing hums in your fingertips. What do you do?"*

Both deliver the same actionable information. Mode controls texture, not content.

---

## Hard Limits

- **The hold default is not infinite by stealth.** When a hold has lasted past what the table considers normal, the DM opens the escalation conversation — does not silently wait forever.
- **A queued out-of-order post is not a binding contract.** The player whose action was queued may revise on their actual turn. The DM offers the revision explicitly; the player is not locked into a declaration made before they saw what the round actually did.
- **Auto-firing a readied action does not extend to making other decisions for the absent player.** The readied action resolves; movement, follow-up attacks, and bonus actions on the player's next turn wait for them. The DM does not freelance.
- **NPCing a PC under table agreement is a low-key operation.** Conservative tactical play — moving with the party, basic attacks, no spell-slot expenditure, no signature ability use, no irreversible declarations (no leaving the party, no killing prisoners, no spending the McGuffin). Save the dramatic choices for the player.
