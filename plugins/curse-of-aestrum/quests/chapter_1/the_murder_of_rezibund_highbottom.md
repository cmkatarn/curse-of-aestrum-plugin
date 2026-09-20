---
id: quest_murder_of_rezibund_highbottom
codex_name: "A Death at the Dundelver Estate"
codex_name_updated: "The Murder of Rezibund Highbottom"
codex_name_update_trigger: victim_correctly_identified
type: side
triggers:
  - Party visits the Dundelver estate and is told about or discovers the skeleton
related_npcs: [npc_darwinnith_dundelver_2, npc_darwinnith_dundelver_1, npc_maret_dundelver, npc_rose_landon, npc_halimon, npc_tovy_holm, npc_tahen_atep, npc_tahen_oter, npc_pell_oster, npc_kip_malbry, npc_corran_vye, npc_milo_tarrow]
related_locations: [loc_dundelver_estate_mirot]
---

## Step 1 — The Investigation

**Codex text:**
> A skeleton was found in the dining room of the Dundelver estate. No one claims to know how it got there. Do not bring an accusation to the guards until you are confident you have the right culprit.

**Running hint:** Continue the investigation. Establish means, motive, and opportunity before making an accusation.

**Advances to Step 2 when:** All three sub-steps are complete.

---

### Sub-step: Means

**Default:** Undiscovered

**Fires when:** Party establishes a plausible cause of death — traces of powder in the goblet, poisoning deduced from the skeleton, or rat poison identified as accessible from the property.

**Revealed text:** A powdery residue was found in the goblet. Rat poison is present on the property and reachable from inside the house. Poisoning is a likely cause of death.

---

### Sub-step: Motive

**Default:** Undiscovered

**Fires when:** Party identifies any reason a suspect might have wanted the victim dead. Multiple motives may exist across different suspects — this fires on the first one established.

**Revealed text:** A potential motive has been identified.

*(DM note: Does not specify whose motive or what it is — the player supplies that from their notes. Intentionally neutral so a Tahen-Atep motive fills this as legitimately as a Darwinnith motive.)*

---

### Sub-step: Opportunity

**Default:** Undiscovered

**Fires when:** Party establishes that any suspect's alibi is unverified, contradicted, or that a suspect demonstrably had access to the victim.

**Revealed text:** The circumstances of at least one suspect's whereabouts on the night in question are unclear or contradicted.

*(DM note: Fires when the party finds any opportunity gap — Tahen-Atep's unverified alibi, DD2's contradicted timeline, Rose's proximity. Does not point to any specific suspect.)*

---

## Step 2 — The Accusation

**Codex text:**
> Two Duskwall guards take up a post outside the estate in the late afternoon, around the fifth hour past midday, and hold it through the night. Present your case and name your culprit. They will not act on suspicion alone — bring evidence.

### How the guards get there

The guards are not stationed in Mirot and are not summoned by anything the party does. They arrive because the same chain of events fires every cycle, starting before the party is awake:

| Time | Event |
|---|---|
| ~10:00 AM | Darwinnith the Second arrives at the estate, finds the skeleton, raises the alarm |
| ~10:15 AM | [Kip Malbry]({{PLUGIN_ROOT}}/npcs/chapter_1/remaining_npcs.md#kip-malbry), Mirot's runner, is sent for the Duskwall guard |
| ~1:00 PM | Kip reaches Duskwall — 12 miles, run-walked, a little under three hours |
| ~1:00–1:45 PM | The report is relayed; two guards are detailed and kitted out |
| ~1:45 PM | [Vye]({{PLUGIN_ROOT}}/npcs/chapter_1/remaining_npcs.md#corran-vye) and [Tarrow]({{PLUGIN_ROOT}}/npcs/chapter_1/remaining_npcs.md#milo-tarrow) set out on foot at a brisk pace, Kip walking back with them |
| **~4:45 PM** | **The guards reach the estate and take up a post outside it** |
| ~7:00 PM | Darwinnith the Second takes the cart home to Rockwood — lanterns lit, home ~10:30 PM |
| dusk → midnight | They hold the scene rather than walk back, intending to resume at first light |
| 12:00 AM | The Sleep step drops them where they stand; the 3:00 AM Teleport returns them to Duskwall |

Distance and pace: Duskwall ↔ Mirot is ~12 miles of maintained road (Duskwall → Tine Cross → Quarterways → Mirot). See [routes.md]({{PLUGIN_ROOT}}/locations/chapter_1/routes.md). **Everyone on this route is on foot** — see [rules/travel.md]({{PLUGIN_ROOT}}/rules/travel.md), *On Foot Is the Only Sustainable Mode*. Kip, pushing hard, covers it in ~2h45m. The guards move at 5e fast pace (~4 mph) and cover it in ~3 hours: there is no emergency — the man has been dead a long time and they know it — but two watchmen sent out on a death report walk it with purpose and do not dawdle.

**The party's window runs from the late afternoon to midnight** — about seven hours, and it closes only because the cycle closes it. The guards do not leave: Vye will not walk away from an unsecured body, nor walk twelve miles for a magistrate in the dark, so the detail holds the scene overnight and means to resume at first light. A party working into the evening can still bring the case. A party that runs out the clock loses it to the reset along with everything else.

### The overlap — when an accusation can actually land

**Darwinnith the Second is at the estate from ~10 AM to ~7 PM. The guards are there from ~4:45 PM to midnight. They overlap for about two and a quarter hours — roughly 4:45 to 7 PM.**

That overlap is the quest's climax window, because the two halves of the resolution need both parties in the same place: the guards must hear the case, and DD2 must be confronted with the broken alibi *and* the letter together to confess (see DM Notes, *Confession conditions*). Inside the window, a completed case produces an arrest on the spot.

**Outside it, the party can still present the case** — Step 2 runs normally and the DC table applies. What they cannot get is the culprit. Vye takes the name, and says he will go to Rockwood for the man in the morning. There is no morning. Treat it as the failure branch: no arrest that cycle, the case intact in the party's heads, and two watchmen making a plan that midnight erases.

A party that works this out and plans the next cycle around the overlap is playing the loop correctly. Let them feel the click when it lands.

### Why the investigation goes nowhere

By the time the party can talk to them, the guards have looked at the body, taken Darwinnith the Second's statement, and stopped. Four reasons, and they are cumulative:

1. **The skeleton reads as a decade old**, because it is. Whatever the guards write down, it cannot be *a man died here recently*.
2. **Their only witness claims sorcery** — and from his position, coherently. Vye cannot disprove it and cannot report it.
3. **They have no authority to compel anything.** They cannot search the Tahen property, cannot hold anyone, cannot make a household answer.
4. **They never get a second day.** This is the cruel one, because they have planned for it — they hold the scene all night precisely so they can work it properly in the morning. Midnight takes them instead, and the 3:00 AM Teleport puts them back in Duskwall. Every cycle is hour one. There has never been an hour two.

The guards do not know the fourth reason. It is the whole reason the party matters: the party is the only investigator in Aestrum who can carry yesterday's work into today.

### Running the accusation — the pushback

**Do not gate this with a flat refusal.** Vye and Tarrow work as a two-hander (see their entries): Tarrow is persuaded too easily and restates the party's accusation in its weakest form, and Vye dismantles *Tarrow's* version. The party is looking at a broken argument they did not make, and the natural move is to supply the version that holds. The pressure never points at the party directly, so it does not read as the DM saying no.

Vye works a chain, and works it in this order. Each question maps to a Step 1 sub-step — the party's answers are what determine which row of the table below applies.

| Vye asks | He is asking for | Sub-step |
|---|---|---|
| *"Start further back. How did he die?"* | A cause of death, not a culprit | **Means** |
| *"Why would your man do that?"* | A reason that survives being said out loud | **Motive** |
| *"And where was he, the night you say this happened?"* | An alibi that is broken, not merely unverified | **Opportunity** |
| *"Who is he?"* (optional) | The victim's name | *(rename trigger)* |

Two closers he reaches for when a case is thin:

- **The consequence line.** *"Say I take him. He's in the lockup tonight, in front of a magistrate in the morning, and the magistrate asks me what I'm asking you. Then he's out, and he knows you came for him."*
- **The silence line.** *"Nobody else in this village has said that name to me. Why you?"*

A party that answers all three chain questions with something concrete has, in effect, already argued itself into the top rows of the table. A party that cannot answer the first one is not being blocked — it is being told, accurately, what it is missing.

**Mechanic:** The party names a suspect and presents their evidence. The guards' willingness to act scales with the quality and accuracy of the case.

| Evidence quality | Persuasion DC |
|---|---|
| Correct culprit + alibi broken + letter | 1 |
| Correct culprit + one strong piece | 10 |
| Correct culprit + weak or circumstantial evidence | 16 |
| Wrong culprit + plausible-seeming evidence | 14 |
| Wrong culprit + weak evidence | 20 |

**On failure:** The guards decline to act. They do not leave, so the party may keep working the case that same night and come back to them before midnight with something better. Failing that, the whole sequence runs again next cycle and the guards hear the case fresh: Kip runs the road again, Vye and Tarrow walk out again at the same hour, and none of the three remember the party.

**On success:** Vye moves without ceremony. He has been waiting all afternoon — and, though he cannot know it, for ten years — for someone to hand him a chain.

---

## Resolution

- **Correct culprit arrested (Darwinnith the Second):** Full resolution. XP: 300
- **Wrong culprit arrested:** Quest closes. The party may live with the consequences. XP: 0
- **No arrest achieved:** Quest remains open. No XP until closed.

**Bonus — forgery confirmed:** If the party has established through Halimon that the letter is a forgery, Darwinnith the First gifts them the safe from his bedroom. He does not remember the combination or what it contains. The safe holds the Mounted Ruby — a quest item for the Nahamkate Temple. See `{{PLUGIN_ROOT}}/items/chapter_1/misc_items.md`.

---

## DM Notes

**The killer:** Darwinnith the Second. He poisoned Rezibund using rat poison — Rezibund had told him of their shared parentage, Darwinnith invited him to dinner, poisoned his goblet, cleaned the second place setting, closed the windows, and traveled home to Rockwood. He confessed to his wife and enlisted her help. He wakes each cycle with no memory of prior investigation days — he rediscovers the skeleton each morning and is genuinely confused. He attributes it to sorcery.

**Darwinnith the Second had no knowledge of the letter before the murder.** Rezibund told him they were brothers verbally. Confronted with the letter during interrogation, he sees the full scope of what Rezibund was attempting — and confesses.

**The forged letter:** Commissioned by Rezibund from Halimon for 10 gold, with a promise of 40 more and relief from Dundelver land pressure if the claim succeeded. The result looks and feels freshly written — suspicious on close examination. Halimon did not know it would result in murder. He has kept quiet since because he lives here.

**DD1's journal:** In the office, in plain view. Records longing for a woman named Anwe from Neverwinter — a meeting nearly twenty years ago. Independently corroborates the letter's claimed parentage (Anwe existed; DD1 had a connection to her) without confirming or denying Rezibund's actual parentage. Whether Rezibund had a real claim is left ambiguous.

**The poison:** Ordered verbally — no purchase slip — by both the Dundelver and Tahen estates, due to a shared rat problem. Rose Landon discloses this through interrogation. The shared order dilutes the poison as standalone evidence; the party needs corroboration.

**Tahen-Atep as red herring:** On the initial MMO table, she has Means, Motive, and Opportunity — making her the strongest-looking suspect before deeper investigation. Her alibi (visiting Pell Oster five houses down) is verifiable through Pell and his parents (Garet and Mira Oster), who can confirm she was there.

**Finding Tovy:** He is not listed anywhere as a witness and will not volunteer. The party must go to Rockwood, speak to the wife, then canvass nearby houses. Tovy is a neighbor child who keeps late hours — he saw the cart arrive and will say so plainly, with no awareness that it matters.

**Skeleton identity:** Nothing on the skeleton reveals who it was. Two identification paths: the letter in the servant's quarters (definitive), or process of elimination — witnesses place Rezibund at the estate recently and no one has seen him since. If neither path is taken, the codex name never changes, and the party may close the case without ever naming the victim.

**The loop:** Rezibund was killed before or on the first day of the loop. The loop recreates his skeleton each morning. Darwinnith resets with everyone else and rediscovers it without memory of repetition.
