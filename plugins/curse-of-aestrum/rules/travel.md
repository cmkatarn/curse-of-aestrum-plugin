---
id: rule_travel
name: Travel
type: homebrew_rule
related_rules: [rule_time_loop, rule_dead_zones, rule_item_persistence, rule_death_and_dying, rule_companion_animals]
---

## Overview

Travel rules are still being solidified. Until they are, hold these defaults.

---

## Landmarks & Intersections — Always Declare Them

In a text-based game the player cannot see the map. They build their entire
mental model of the world from what the narration names — so a feature that
is not named does not exist for them. Therefore, whenever travel reaches or
passes a navigational feature, **declare it explicitly, every time.** Do not
compress it away, even when montaging a multi-leg journey for pace.

Declare, in order along the route:

- **Every intersection, fork, or junction the route crosses.** Name it (use
  its in-fiction name, not DM shorthand), say which directions its roads run
  and the named destinations they lead to, and state which way the party
  takes. **A branch the party does *not* take is still named** — it is a
  landmark and a standing future option the player may reference later
  ("the road south we passed," "back at the crossroads").
- **Every named settlement, landmark, or notable terrain feature the route
  passes within sight of** — name it and its bearing from the road ("the
  Misty Forest off to the south," "a spur branching south toward the
  Perisdottir house").
- **Signposts and waymarkers, where they exist** — read their destinations
  aloud.

Montaging the *texture* of a leg (weather, ordinary traffic, hours passing)
is fine and good for pace. What the montage must **not** drop is the **named
topology**: the junctions and landmarks passed, in order, so the player's
map stays accurate. Silently skipping a junction the route demonstrably
crosses is a navigation error, not a stylistic compression.

**Always check [locations/chapter_1/routes.md]({{PLUGIN_ROOT}}/locations/chapter_1/routes.md)
for the canonical topology before narrating inter-location travel,** so the
intersections and landmarks you declare — including the named villages each
road leads to and any signposts at the junctions — match the map.

---

## Encounters

- **No random encounters within Aestrum.** The bubble does not generate wandering threats — any encounter on a road inside the region is authored, not rolled. If the player travels and nothing has been seeded for that route, the trip is uneventful in the encounter sense (it may still carry roleplay, weather, or loop-mechanical beats).
- **No random encounters preceding entry into Aestrum.** Anything before the party crossed the bubble's edge is also encounter-free unless specifically written.
- **Chapter 2 will introduce random encounters.** Once the cycle is broken and Chapter 2 begins, a separate encounter framework will be added; do not improvise one in the meantime.

---

## On Foot Is the Only Sustainable Mode

**The campaign's mechanics assume the party travels on foot, and several of them break if it doesn't.** The locked [Duskwall ↔ Jiasha's Hut]({{PLUGIN_ROOT}}/locations/chapter_1/routes.md) leg is calibrated to an 18-hour dawn-to-midnight window at walking pace — mounted, it collapses from "highly unlikely" to trivial, and with it the trap that binds the party into the cycle. The same holds for every distance in `routes.md`: they are walking distances, chosen so Aestrum is small enough to know and large enough to cost a day.

### Never veto this. The loop enforces it for you.

**Do not tell a player they cannot buy, hire, borrow, or ride a horse.** A world where the party alone is barred from mounts is a world the player can feel the DM's hand on, and it invites precisely the argument you do not want to have. Let them look. What they find is an answer, not a refusal.

### What horses actually exist in Aestrum

This is the primary lock, and it is a fact about the duchy rather than a rule about players:

- **Farm horses only.** Some smallholdings keep a horse or two for labour — tilling, pulling a cart, turning a mill. They are draught animals: heavy, slow, worked, and worth a great deal to the household that depends on them.
- **There is effectively no riding tack.** None for sale, none for hire, and none in any barn a party is going to talk their way into. Nothing in Aestrum is worked under saddle, because nothing in Aestrum has needed to be.
- **The one exception is [Dolores]({{PLUGIN_ROOT}}/locations/chapter_1/dolores_cabin.md)**, who keeps a buckskin mare named Trotter at her cabin outside Dunleaven, with saddle and tack maintained, and rides her in slow loops around the property. She is a deliberate exception and stays one: her gear is hers, kept by someone who plainly used to be something before she was a woman with a vegetable garden. It is not for sale, it is not for borrowing, and a party that takes it has stolen from Dolores — which is its own answer.
- **No privately owned carriages.** The only private carriage horses in the duchy belong to Duke Tallwood, stabled **under guard inside Duskwall Castle.** Taking one is a theft from the Duke's household, committed inside a garrisoned castle — a heist, not a shopping trip, and priced accordingly.
- **One carriage for hire, and it is booked.** [À la Cart]({{PLUGIN_ROOT}}/locations/chapter_1/duskwall/a_la_cart.md), a hire yard in Duskwall, keeps carts and draught horses and exactly one coach. The coach is genuinely fast — about twice walking pace — and it is held on a standing daily reservation by Darwinnith Dundelver the First, who is too ill to walk home to Mirot. **This yard is the in-fiction face of this whole rule.** Send a party asking about transport here: they get a real answer from a real business, rather than an absence they will keep probing. They also get a lead on the Dundelver murder, because Hesper Dunn explains who has the booking and why.
- **One notable cart.** [Darwinnith Dundelver the Second]({{PLUGIN_ROOT}}/npcs/chapter_1/remaining_npcs.md) keeps a horse and cart in Rockwood — not a coach, and not a farm vehicle either. He does not work land; he simply prefers not to walk and can afford not to. A cart is no faster than walking, so it breaks nothing, but it is conspicuous: it is why a nine-year-old at a window recognised a vehicle on the road at midnight, and that recognition is the evidence that breaks a murderer's alibi.

So a party that wants to move faster is offered: a plough horse, bareback, from a farmer who needs it for tomorrow's work and does not want to sell. A draught animal ridden bareback over twelve or twenty miles is not meaningfully faster than walking and is considerably more miserable. **The answer to "can we get horses" is yes, and it does not help.**

### And if they get one anyway

Suppose they buy the plough horse, or take one from the castle. The cycle takes it apart on its own, the same night, every night, for reasons the party can discover and verify. That discovery is *good play* — it is the loop teaching them what it is.

### The four mechanisms

All of these are existing rules, not new ones. Applied together they mean **the party can never begin a day mounted.**

1. **The reset separates them from the animal.** Animals have no reset point and are not Teleported ([time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md)) — the party is scattered to their reset points at 3:00 AM and the horse simply stays where it lay. This is the same mechanic as [companion animal separation]({{PLUGIN_ROOT}}/rules/companion_animals.md); a mount is subject to it identically. Every morning: party at their reset points, horse wherever they stopped.
2. **Harness and vehicles snap back.** Tack, harness, carts and carriages are ordinary objects, Recreated to their original locations at 1:30 AM ([item_persistence.md]({{PLUGIN_ROOT}}/rules/item_persistence.md)). A party that solves the separation problem still wakes to a bare horse and a cart back in the yard it came from — and there was never any riding tack to begin with.
3. **The purchase un-buys itself.** Mundane wealth is snapshot contents — the coin returns to the party and the horse returns to the seller's ledger, except the seller has no memory of the sale. Whatever arrangement was made is gone and must be built again from nothing, with someone who has never met them.
4. **Nobody will hire them one.** Animals killed inside Aestrum stay dead — they are excluded from Recreate ([death_and_dying.md]({{PLUGIN_ROOT}}/rules/death_and_dying.md)). Aestrum's residents do not consciously know why, but the practice has settled: *nobody risks the asset.* Hired animal transport is rare here, and a stranger asking to take a horse out on the road gets a polite no.

### What a determined party can actually achieve

Be honest about this rather than overstating it — a player who finds the seam and is told "no" anyway has caught you cheating.

- **Within a single day, a mount works.** A party that acquires a horse in the morning genuinely moves faster that day. They lose it at midnight. That is a real, one-time advantage and they are welcome to it.
- **The stabled-horse pattern is the real seam.** A party that stables a horse close to their reset point could, in principle, wake, walk a short distance, and ride. What it costs them: no tack (it resets nightly), a stablemaster who has never met them and holds no record of payment, and a fresh negotiation every single morning with a man who found a strange horse in his stall overnight. It is more work than it saves, and it collapses the moment they are away from that one stable. Let a party who commits to it have it — they earned it — and make the friction real rather than invented.
- **What it never buys them** is the Jiasha run. That journey begins at the hut, outside the boundary, on a day they have not yet been snapshotted — see below.

### The arrival case — the one genuine gap

Everything above depends on the party having been snapshotted. On their first day they have not been, so nothing separates them from a mount they brought in. A party that rides in from Setland could make the dawn-to-midnight round trip comfortably and walk back out of the cycle, which collapses the Chapter 1 premise.

**The party arrives on foot, and the reason is the war.** Setland's horses are quietly spoken for. Malak's concealed military build-up ([setland_city.md]({{PLUGIN_ROOT}}/locations/chapter_1/setland_city.md)) has been drawing mounts and draft animals out of the duchy's civilian supply for months, on requisitions nobody discusses. A small contracted recovery team gets a sealed letter, a stipend, and the east road. Stables in Setland City are thin and expensive, hire is refused more often than not, and nobody explains why.

This is a *feature*, not a fence. A player who pushes on it — *why can't anyone in this city rent us a horse?* — is brushing against the campaign's central political secret several chapters early, and should be paid in the texture of that (an evasive ostler, a quartermaster's requisition chit, prices that make no sense for peacetime) rather than given a brush-off. The road is still walked; the reason it is walked is a clue.

> **Authoring note.** The requisition pressure is an inference from Malak's established concealment of war preparations, not a separately confirmed fact. It is the proposed in-fiction reason the party is outfitted on foot; swap it for a better one if a better one is authored, but keep *some* stated reason — an unexplained absence of horses is the kind of gap players probe hardest.

### Why the farms keep their horses and the party cannot

Do not sterilize the world to enforce this. Farms keep working animals and they are still there every morning. The asymmetry is real and worth letting a sharp player notice, but it is **not** that animals reset — they don't, for anyone.

- **A looped resident's day is a closed circuit.** The snapshot captured a routine that begins and ends at home, so the horse that pulls a cart to the mill is back in its own yard before dark and ends the night where it began. The loop does not return the animal; the routine does. This is why nothing looks wrong.
- **The party's day is not a circuit.** They go somewhere new and do not come back. An animal they take out is an animal left out — and at 3:00 AM they are pulled to a reset point it cannot follow them to.
- **The farmer does not get his horse back.** This is the sharp edge, and it should be allowed to cut. A party that takes a working animal out and abandons it twelve miles away has cost a household its livelihood — and because the household resets, the farmer wakes up tomorrow having lost it again, without ever learning how or being able to grieve it properly. Animals do not reset. That loss is permanent and it accumulates. A party that works this out has understood something real about what they are doing to this place.

> **Resolved.** Darwinnith Dundelver the Second's vehicle was formerly described as a *carriage* in three places (Tovy Holm's sighting, his own entry, the murder quest's DM Notes). It is a **cart** — a comfort purchase by a man with money and no land to work, not a coach. The Tovy sighting is unaffected and still breaks the alibi.

---

## Pace and Loop Edge

Travel time and pace can use 5e RAW for now. Loop-edge behavior (what happens if midnight catches the party mid-journey) is governed by the loop and dead-zone rules in [time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md) and [dead_zones.md]({{PLUGIN_ROOT}}/rules/dead_zones.md), not by anything in this section.
