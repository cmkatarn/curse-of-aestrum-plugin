---
id: quest_murder_of_rezibund_highbottom
codex_name: "A Death at the Dundelver Estate"
codex_name_updated: "The Murder of Rezibund Highbottom"
codex_name_update_trigger: victim_correctly_identified
type: side
triggers:
  - Party visits the Dundelver estate and is told about or discovers the skeleton
related_npcs: [npc_darwinnith_dundelver_2, npc_darwinnith_dundelver_1, npc_maret_dundelver, npc_rose_landon, npc_halimon, npc_tovy_holm, npc_tahen_atep, npc_tahen_oter, npc_pell_oster]
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
> Duskwall guards arrive at the estate each afternoon around the third hour past midday. Present your case and name your culprit. They will not act on suspicion alone — bring evidence.

**Mechanic:** The party names a suspect and presents their evidence to the arriving guards. The guards' willingness to act scales with the quality and accuracy of the case.

| Evidence quality | Persuasion DC |
|---|---|
| Correct culprit + alibi broken + letter | 1 |
| Correct culprit + one strong piece | 10 |
| Correct culprit + weak or circumstantial evidence | 16 |
| Wrong culprit + plausible-seeming evidence | 14 |
| Wrong culprit + weak evidence | 20 |

**On failure:** The guards decline to act. The party may reinvestigate and try again the following day — the guards reset with the cycle and will hear the case fresh.

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

**Finding Tovy:** He is not listed anywhere as a witness and will not volunteer. The party must go to Rockwood, speak to the wife, then canvass nearby houses. Tovy is a neighbor child who keeps late hours — he saw the carriage arrive and will say so plainly, with no awareness that it matters.

**Skeleton identity:** Nothing on the skeleton reveals who it was. Two identification paths: the letter in the servant's quarters (definitive), or process of elimination — witnesses place Rezibund at the estate recently and no one has seen him since. If neither path is taken, the codex name never changes, and the party may close the case without ever naming the victim.

**The loop:** Rezibund was killed before or on the first day of the loop. The loop recreates his skeleton each morning. Darwinnith resets with everyone else and rediscovers it without memory of repetition.
