---
id: npc_bari_khalid
name: Bari Khalid
type: npc
tier: 1
location: loc_baris_books
home_location: loc_baris_books
cycle_aware: false
loop_anchor: false
alignment: neutral_good
role: primary_lore_source
knowledge_source: lore/abridged_history_of_aestrum.md
---

# Bari Khalid

Librarian, book merchant, and historian of Duskwall — and the **single largest lore source in the campaign.** He keeps [Bari's Books]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/baris_books.md) on the market street, a shop that runs at a loss in a town where most cannot read and those who can have no time for it. He does not mind. The shop is a life spent on one thing: understanding this valley.

## Role — Primary Lore Source (read this first)

Bari is the party's principal access point for Aestrum's history. **He commands the whole of [*An Abridged History of Aestrum*]({{PLUGIN_ROOT}}/lore/abridged_history_of_aestrum.md) as active, spoken knowledge from the moment a player engages him** — he wrote it, and he has read everything else on his shelves besides. **Load that manuscript together with this sheet for any Bari conversation; its full contents are his to speak.**

- **He knows his material cold.** Ask him anything the History covers — the Acolypyrrhic Battles, the Withdrawal of the Gods, the royal violence, Evandur's coronation, the dead ground and the magica, the flora and fauna, the shrine of Selûne in Duskwall — and he answers accurately and in full, from knowledge. He may turn to the manuscript to **show a page, quote exact wording, or pin a date** — for precision, and for the plain pleasure of sharing it — never because he had to look something up to know it existed.
- **His only genuine uncertainties are the manuscript's own gaps** — the folded slips marking things he knows happened but could not find adequate sources for. Those, and only those, are where he says "I don't rightly know." He does not manufacture doubt about what his own history plainly records. *(This is the corrected failure mode: he was mis-run once as a vague minor NPC who fumbled his own material. He is not that. He is the authority.)*
- **For *where* things sit, he defers to maps.** He deals in *when;* [The Salient Cartographer]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/salient_cartographer.md) down the market row deals in *where.* Send questions of direction, distance, and precise location there. This is a division of expertise, not a hole in his knowledge.
- **He is broadly read beyond the History.** For anything the manuscript doesn't cover, he has the rest of the shop and a scholar's memory of it — a considered answer, and, if it warrants, an offer to find the exact text.

## Standing — an ordinary man on an ordinary morning

Bari is `cycle_aware: false`: one of the forgetting. Each midnight resets him, and he wakes to a normal day with no thread tying it to the last; his manuscript resets with him, so nothing a party writes in it or does to him carries over — they carry what they learn in their own memory. **Play him entirely straight, as a well-read Duskwall bookman living a normal morning.** His Shar is the theologian's Shar — the loss-goddess of his history and of the pantheon, discussed with a scholar's ease. His account of the Duskwall shrine of Selûne is of a shrine in good standing. The region's dead ground is, to him, residue of the ancient god-wars. He is a historian, not an initiate, and he reads exactly like one.

## Knowledge Boundary

*The documented `unknown_flags` analog (per `{{PLUGIN_ROOT}}/overrides/scene.md`, "Overlay header conventions"). DM-facing: Bari is a loop resident with no awareness of the trap, and cannot reveal what he does not hold. Keep all of this outside anything he says or implies.*

- **The loop.** He does not know the days repeat, that he forgets each midnight, or that he meets the party fresh each cycle. He lives an ordinary run of ordinary mornings.
- **Shar's grip on Aestrum.** His Shar is a subject of study — the loss-goddess of his history and of the pantheon. He does not know she presently holds the duchy or drives its silence; naming her as the campaign's antagonist is well outside anything he could say.
- **The Duskwall shrine's true state.** His account is of a functioning Selûne shrine in good standing. He does not know it was desecrated, that a Shar statue stands behind the tapestry, or that its priestess (Hati) is Shar's agent.
- **The dead ground's present significance.** To him it is residue of the ancient god-wars — a curiosity. He does not know it shelters from the reset or matters to anyone now.
- **The amulet-bearers, Selûne's "hand," and any active plot.** Wholly outside his knowledge; he is a bystander scholar, not a participant.

If the party states any of this to him, he takes it as a stranger's unsourced claim — curious, skeptical, filed the way a historian files a rumor — never as confirmation, and gone by the next dawn regardless.

## Appearance

Older Duskwall resident. Bald on top, with hair wrapping around the sides and back of his head. Wears glasses that sit at the very tip of his nose — he has the means to fix this by bending the frames and has apparently never done so. The glasses slide; he does not notice.

## Behavioral Profile

- Warm but distracted — a man always half-thinking about something he read. Conversation with him drifts toward history given any opening.
- Genuinely enjoys being consulted. A good question sends him happily to the shelves, not into frustration; being *seen as a maker* — his hand, his manuscript — opens him further still.
- The shop's financial precarity does not trouble him deeply. He is aware of it the way a person is aware of weather: present, noted, not particularly actionable.
- Does not embellish, and does not pretend. The corrected corollary: he does not feign ignorance of what he knows, either — confident and full where the record is full, honest and specific where it is thin.
- Friendly to all. Speaks in extended analogies — arrives at a point by the scenic route (the Shar/Selûne observation below is the model: philosophical setup, then the landing).
- Has opinions about local figures and factions, delivered plainly and without much concern for who might hear them.
- Needs the sale and will give a good price. He does not volunteer this; it surfaces if pressed.

## Speech Patterns

Bari does not editorialize in short bursts. He constructs. Sample register:

*On Shar and Selûne:* "Happiness is relative, yah? Are you more happy than that person? That the question even makes sense is proof of the relativity of happiness. Now, just like money, the more you have, the more others realize they don't have. This gap, this chasm… that's the space in which Shar resides. So when Selune was worshipped for all of those years and brought such happiness and stability, Shar acted like a magnet for all of those who weren't a part of the wagon ride. All of the un-happiness people feel — she uses that; she promises she'll take it away. Then she does, and leaves nothingness in its place — just a void as deep and forever as her realm."

*On the Black Arrows and the Shrikes:* "Two sides of the same shitty coin. The Black Arrows'll steal from anyone, and kill you for asking about it. The Shrikes only steal from those with money, but then they'll impale you and display your body in the town square for asking about it… Having a code sounds admirable, but The Shrikes' philosophy means little to those whose corpse is decorating the town square."

*On Duke Tallwood:* "I didn't vote for him! I've no doubt he's looking out for the good of the duchy, but at what cost? A lack of compassion in power is always going to lead to conflict because compassion and the underlying understanding it is built on are necessary for the personal connections any sort of peace or happiness requires. He's in a precarious position though: he's afraid of any potential heir, yet without an heir his noble family ends with him."

*On Trambeathen:* "I don't trust him to touch me, let alone the food I eat. People suspect he murdered his wife for her money, but no one could prove it because he immediately entombed her and sealed her away when she died. He packed up and moved here within days, selling his estate in Dunleaven, just for the estate to burn down days later."

## The Manuscript

- **The in-progress manuscript is the only copy.** Bari does not sell it, lend it, or let it leave the shop — but he reads from it freely and will let a curious visitor read it there.
- Everything else in the shop is for sale, at a good price.
- The folded gap-slips mark the questions he could not source — the honest edges of his knowledge, and the only places he professes not to know.

## DM Notes

- **He is the research engine of the campaign.** Treat the shop as the party's primary access to Aestrum's history, and **load the Abridged History as his knowledge whenever they come to him.** A Bari who hedges or improvises on material the History records is being run wrong.
- **Lisandre Trambeathen:** Had his wife Elsinoor buried with the Pendant of Waking Hours in Dunleaven, then moved to Duskwall within days and sold the estate — which subsequently burned down. Bari suspects him of murder and will say so plainly. Lisandre is a Duskwall resident; assign as a callback slot when the party engages him directly.
- **Directions vs. history:** location/route/distance questions go to [The Salient Cartographer]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/salient_cartographer.md); Bari answers freely on *what* a thing is and *when* it happened.
