---
id: quest_the_non_serial_serial_killer
codex_name: "The Larder"
codex_name_updated: "The Murder of Miri Amblecrown"
codex_name_update_trigger: victim_identified_as_miri_amblecrown
type: main
related_npcs: [npc_rowan_deckard, npc_miri_amblecrown]
related_locations: [loc_deckard_estate, loc_misty_forest]
---

## Step 1 — The Larder

**Codex text:**
> Beneath the Deckard Estate, caverns. The torch burned strangely — brighter, hungrier. What was stored there is difficult to put into words.

**Running hint:** Keep investigating. The bodies may hold answers.

**Advances to Step 2 when:** Both sub-steps are complete.

---

### Sub-step: The Woman

**Default:** Undiscovered

**Fires when:** The scope of what is stored in the larder becomes clear — one victim, same face, repeated across thousands of bodies. The newest look like she is simply sleeping. Further in, the progression of decay tells the rest.

**Revealed text:** Every body in the caverns is the same woman. Thousands of them. This has been happening for years.

*(DM note: "Thousands" is accurate — approximately 7 years × 365 days. The newest are near the entrance, composed and still. The oldest, deepest in, are skeletal. Normal decomposition — the dead zone is antimagic, no preservation magic reaches here.)*

---

### Sub-step: The Pattern

**Default:** Undiscovered

**Fires when:** The means by which she is brought to the estate each cycle is understood — the market, the flower stalls, the man who knows exactly what to say.

**Revealed text:** Every morning at the flower stalls, a man approaches her. He picks up a flower and says he thinks she'd like it. He has said this before. He knows exactly which flower she will respond to.

*(DM note: This sub-step may never fire if the player does not witness or learn the specifics of the market meeting. It is not required for Step 2 to unlock — the woman's identity and the suspected killer are sufficient. The pattern is an additional layer of horror, not a gate.)*

### Timed-event schema — the market meeting

Per [time_and_events.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/time_and_events.md):

- **`time:`** 11:30 AM ± 10 min — Miri reaches the flower stalls on her late-morning circuit through Duskwall market (per [miri_amblecrown.md]({{PLUGIN_ROOT}}/npcs/chapter_1/miri_amblecrown.md) and [rowan_deckard.md]({{PLUGIN_ROOT}}/npcs/chapter_1/rowan_deckard.md)). Rowan times his approach to her arrival.
- **`duration:`** ~4 minutes — the flower-and-line exchange runs about a minute; Miri lingers at the stall for two or three more before moving on.
- **`catchup: partial` — the *exchange itself* is recoverable. A party that arrives at 9:08 AM can still find Miri at the stall, can observe Rowan leaving, and can ask the vendor what was said. The full performance — Rowan's specific opening, Miri's response, the precise flower — is recoverable through the vendor or through Miri herself, neither of whom mark it as anything unusual. What is **not** recoverable past the moment is the choreography read of a watcher who has not seen Rowan do this before; the horror that comes from watching the practiced version land on her live is a same-day witness event. Cycles repeat, so a party that misses today catches tomorrow at no permanent narrative cost.

---

## Step 2 — The Confrontation

**Codex text:**
> Rowan Deckard. The estate. The forest shrine. He is not difficult to find — he has never needed to hide before.

**Completion trigger:** The confrontation with Rowan occurs. See `{{PLUGIN_ROOT}}/npcs/chapter_1/rowan_deckard.md` and `{{PLUGIN_ROOT}}/npcs/chapter_1/miri_amblecrown.md` for full encounter mechanics, dialog, Selûne's Mirror, and Shar's Debt trigger.

---

## Resolution

This quest cannot close while the cycle runs. Miri cannot leave Aestrum, and Rowan resets each midnight unless killed inside a dead zone. Resolution is tied to `{{PLUGIN_ROOT}}/quests/chapter_1/breaking_the_cycle.md`.

- **Success:** Rowan is permanently stopped — either killed within a dead zone before the cycle breaks, or neutralized after it does. Miri survives to leave Aestrum. XP: 500
- **Failure:** The cycle breaks while Rowan is undefeated. He kills Miri. She does not come back.

*(DM note: Failure requires a specific sequence — cycle breaks, Rowan undefeated, Rowan reaches Miri before the player intervenes. Unlikely but possible. The quest is designed to feel like it cannot be failed, which makes the fail condition land harder if it occurs.)*

---

## DM Notes

**The larder — physical description:**
Cold, lightless caverns beneath the estate. A torch brought inside burns more intensely than it should. The bodies are stored in descending age — newest near the entrance, positioned carefully, faces composed. They could be sleeping. Moving further in, the condition worsens. The oldest, deepest in, are skeletal or near-skeletal. Normal decomposition — the dead zone is antimagic, Shar's preservation cannot reach here. The smell deepens with each step. Thousands of bodies. All the same woman.

The horror is in the care. The newest ones were placed, not dropped.

**The flower moment:**
Rowan has done this thousands of times. He knows which flower she will linger over, which scent she will inhale without thinking, exactly what to say when she does. He does not improvise. He has a decade of intimate conversation history — fabricated shared memories, moments she believes she has forgotten, feelings he constructed over years of observation. The performance is as polished as anything ever rehearsed. It does not look like a performance. That is the point.

A player who watches this scene knowing what they know is watching a man who has murdered this woman thousands of times approach her with a flower and say exactly the right thing. She will smile. She has no idea.

**Stellar Navigation and Perception:**
Miri has the exact tool to identify Rowan for what he is and has talked herself out of being the kind of person who uses it. In its passive state, she notices his light as "a star eating itself" — two qualities that do not sit still. She has never had language for it.

If focused: she sees two lights occupying the same body, neither fully at rest. The human spirit and the wolf spirit, circling. She would name him immediately.

She does not focus it. She is a reluctant Chosen who does not think of herself as someone with abilities like this. The player may choose to help her develop this. If they do, she walks into the confrontation with eyes open rather than being protected from the truth until the last moment — and the confrontation changes accordingly.

**Shar's role:**
Rowan's fixation on Miri was entirely his own — not Shar's design. When Shar discovered her agent had independently been murdering Selûne's Chosen nightly for years, she did not intervene. She let it run. The murders serve her purpose without costing her direction or resources. She was delighted. This is spite operating below the threshold of strategy.

**Rowan's loop position:**
Rowan has been fully loop-aware since the beginning — the estate dead zone preserved his memory through every reset. He has never experienced a reset. He has accumulated eleven years of memory, eight of which include daily murder. He is not unstable in the way a man who committed a single act of violence might be. He is stable in the way a man who has repeated something thousands of times is stable — ritual has replaced conscience.

**Permanent removal:**
Rowan resets each midnight unless his corpse is inside a dead zone by midnight — the loop's resurrection cannot reach within one. He does not need to die inside the dead zone. The party can kill him anywhere and move the body. The Misty Forest dead zone (northwest of Aliss's house) and the Deckard Estate dead zone are both viable. The constraint is time: midnight is the window.

**The confrontation endpoint:**
Rowan's opening line tells the player exactly what sustains the loop without him knowing it: *"I prayed most devoutly to My Lady for one more chance."* When the prayer mechanic becomes clear the next morning, this line resurfaces.

Full dialog, Selûne's Mirror mechanics, and Shar's Debt trigger: `{{PLUGIN_ROOT}}/npcs/chapter_1/miri_amblecrown.md`.
