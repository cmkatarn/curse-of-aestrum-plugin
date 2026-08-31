---
id: rule_session_opening_no_plot_leaks
name: Session Opening — No Plot Leaks in Setup
type: homebrew_rule
related_rules: [rule_information_disclosure, rule_private_information]
---

## Overview

Any setup question shown to the player at the start of a session, scene, or new campaign instance is **part of the player's experience** — not a neutral administrative channel. Names, places, and framings that appear in option text are read by the player as facts about the world before the first line of fiction is delivered. The setup is therefore subject to the same disclosure discipline as in-fiction narration: it must not surface anything the player's PC would not yet know.

The discipline runs **both directions**. Setup text must neither **surface** real hidden content (the *leak* failure, governed below) nor **assert invented** content the source does not establish (the *fabrication* failure, governed under [Grounding](#grounding--no-invented-canon-in-setup)). A player reads invented canon as real exactly the way they read leaked canon as real; both corrupt the player's model of the world before the first line of fiction.

This rule applies to **every skill that opens play** — currently `scene` and `create-party`, and any future opener — and to **every layer that asks the player a question on that skill's behalf** (the override file, the engine layer it inherits from, and the DM's freeform follow-ups).

---

## What Counts as a Setup Leak

A setup question leaks plot when its visible text — the question, an option label, or an option description — surfaces any of:

- **Names** of hidden bounties, contracts, commissions, writs, or their targets.
- **Proof terms** or operational specifics of any hidden contract (e.g., "eye and hand", "the ring").
- **Convergence framing** — pre-announcing that the PCs will meet at a specific location, or that NPCs are converging on the same place, before the fiction has surfaced the convergence.
- **NPC-private agendas, secrets, or hidden state flags** (a companion's cover story, an unspoken motive, a sealed object on their person).
- **Reveals, twists, or scene-structure** that the campaign intends to surface in play (an upcoming betrayal, a hidden room, a planned NPC arrival).
- **Moral-standing-gated content** named under a "no" option (offering "if you have Black Arrows ties, do you know about X?" leaks X regardless of which option the player picks — the name is in the option set).

The phrase *"select this if you don't know about Y"* is not a defense. The leak is the appearance of Y in the question, not the player's choice.

---

## What Setup Questions May Ask

Restrict batched setup questions to **neutral framing only**:

- **Content rating** for the session.
- **Time of day** the PC's day begins, or where they are in a recurring cycle.
- **Where the PC themselves is and what they are doing** at the open — phrased so every option reflects something the PC could decide for themselves without external knowledge ("you've just arrived in the city," "you've been here for a few days").
- **Ratings-adjacent or comfort-adjacent options** that govern delivery rather than plot.
- **Loading a saved snapshot** (by neutral identifier — "resume the last session," "load the Day 4 save"), with no plot summary in the option label.

If the opener genuinely needs to branch on hidden state (e.g., did the PC overhear a private conversation, did they take a particular contract), do not ask the player about the hidden state. Resolve it silently through the PC's own choices in the opening fiction — what time they arrive, where they go, who they talk to — and let the branch fire from those neutral inputs.

---

## How to Apply

1. **Before showing any setup question, scan the rendered text** (question + every option label + every option description, including ones the player will not pick) for the leak categories above. Treat the option set as a whole — a leak in one option leaks regardless of which option is chosen.
2. **If a leak is found, rewrite** to neutral framing. If the question can't be asked without naming hidden content, the question itself is wrong — restructure the open so the branch fires from in-fiction choices instead.
3. **The discipline applies to follow-up questions during setup too** — not only the initial batched set. A "by the way, do you happen to know about…" mid-setup question carries the same leak risk.
4. **If a leak escapes and surfaces to the player**, acknowledge it openly to the player (do not paper over it in fiction), and adjust the open so the leaked information lands as a plot beat in play rather than as setup metadata.

---

## Grounding — No Invented Canon in Setup

The leak rule above guards one direction of setup fidelity: not surfacing real
hidden content. The opposite failure is **fabrication** — setup text (a question,
an option description, a guided-creation suggestion, the opening orientation line,
a resume refresher) asserting a world fact that the campaign source does not
establish: a location, NPC, faction, event, date, or quantity invented to fill a
slot.

Any setup text that asserts a world fact is subject to the **grounding-family**
discipline of the scene skill's epistemic gate — quantity grounding,
spatiotemporal binding, and fabricated-concrete (rows 14 / 15 / 19 of
[epistemic_discipline_checklist.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline_checklist.md)).
The fact must trace to campaign source data, or it must not be asserted.

How to apply:

- **Resolve, don't invent.** If the open needs a world fact (a place name, a
  date, who is where), read it from the relevant campaign file. If it isn't
  established and the open genuinely needs it, **ask the user before inventing** —
  never fabricate to fill the slot. The `create-character` flow already carries
  the build-side form of this rule (*"Does not invent canonical lore. If a hook
  would require new canon, ask the user before fabricating"* —
  [{{PLUGIN_ROOT}}/engines/rpg-5e-engine/create-character/core.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/create-character/core.md));
  this clause generalizes it to **every** opener and every setup surface,
  including the `scene` open and the resume refresher.
- **Orientation blocks are the high-risk surface.** A resume refresher or an
  opening "where you are" line reaches to sound concrete and oriented — exactly
  where an invented "three days ago," an unplaced tavern, or a misremembered date
  slips in. Render quantities and when/where only at a precision the source
  supports; if no grounded value exists, use a non-committal phrasing or omit it.

---

## Relationship to Other Disclosure Rules

- [information_disclosure.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/information_disclosure.md) governs in-fiction disclosure during play. This rule extends the same discipline to the setup channel — they are continuous, not separate regimes.
- [private_information.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/private_information.md) governs DM-side hidden state across play. Setup is one of the surfaces hidden state can leak through; this rule names the surface.
- The prose-engine scene skill's epistemic discipline applies once the scene is running. This rule applies *before* it — to the question flow that brings the scene up. It borrows one part of that discipline forward: the **grounding-family rows (14/15/19)** apply to any setup text that asserts a world fact (see [Grounding](#grounding--no-invented-canon-in-setup)).

---

## Why This Rule Exists at the Campaign Layer

This is not a per-installation preference — it is a campaign-integrity rule. A player who is told the campaign's reveals in option text cannot un-know them, and the campaign loses the scenes those reveals were architected to power. Codifying the rule at the campaign layer (rather than per-user memory) makes the discipline portable across machines, sessions, and any agent loading the campaign.
