---
id: rule_companion_animals
name: Companion Animals — The Dog and the Cat
type: homebrew_rule
related_rules: [rule_time_loop, rule_death_and_dying, rule_information_disclosure, rule_consequences]
---

# Companion Animals — The Dog and the Cat

Aestrum holds two adoptable animal companions: a **dog** and a **cat**. They
are unlike every other NPC in the campaign and are run by a distinct set of
rules. Their canonical content (appearance variability, demeanor, what each
can do) lives in [npcs/chapter_1/stray_dog.md]({{PLUGIN_ROOT}}/npcs/chapter_1/stray_dog.md)
and [npcs/chapter_1/stray_cat.md]({{PLUGIN_ROOT}}/npcs/chapter_1/stray_cat.md); **this file
is the authoritative behavior layer** those sheets point up to.

Both animals are roughly **four to five years old**.

---

## No voice, no point of view

These animals **never speak** and are **never a narration anchor.** No line of
dialogue, no rendered inner monologue, no scene narrated from the animal's
perceptual envelope. They register *only* through observable behavior —
posture, ears, hackles, a tail, where they choose to sit, the dog's alerts —
described from the outside by whoever is currently the narration anchor (the
PC by default; see the narration-mode pin in `{{PLUGIN_ROOT}}/overrides/scene.md`).

When an animal "reacts," the player sees the behavior, not its reasoning. A
growl is a growl on the page; the *meaning* is for the player to read, exactly
as an Insight **tell** is a signal and not a conclusion (see
[information_disclosure.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/information_disclosure.md)).

---

## Manifestation: indeterminate until adopted

Before adoption there is **one dog-presence** and **one cat-presence** in the
campaign, not a population. Each manifests with a **different breed and
appearance at different locations** — a loop-flavored "unfixed until observed"
device. The party may glimpse a lean grey street-cat by the docks one day and
a fluffy ginger thing in a temple courtyard the next; narratively it is the
same cat-presence, unresolved.

**Adoption locks the appearance.** The moment the player adopts the animal,
its breed and appearance fix permanently to whatever was present at that
encounter. From then on:

- That is **the** dog / **the** cat for the rest of the campaign.
- **No further strays of that animal type appear** anywhere in Aestrum. The
  motif has resolved into a single creature.

Adopting the dog does not lock the cat, and vice versa — they resolve
independently.

---

## Referenced in passing — never pushed

These animals are **background texture, surfaced in passing.** A cat watching
from a windowsill; a dog trotting along the far side of a market and gone. A
single observational beat, then the scene moves on. **Never** steer the player
toward them, never frame them as a quest hook, never have an NPC suggest
adopting one.

If the player chooses to go out of their way — follows the animal, kneels,
offers food, asks after it — the world meets that interest and the encounter
opens up. Pursuit is always **player-initiated.** Absent pursuit, the animal
remains a recurring glimpse.

### Where they appear — and don't

The pre-adoption manifestation is a **loop-exclusion phenomenon**, so it only
exists where the loop does:

- **Inside Aestrum only.** The unfixed dog/cat presence appears in Aestrum's
  **living settlements** — Duskwall (its shops and taverns), Dunleaven, and
  the like: the everyday public places where a stray would plausibly wander.
- **Never in Setland or anywhere outside the loop.** Out there, animals live
  ordinary remembered lives; there is no exclusion to manifest. Setland sites
  (Charnelhold and the Lion's Den, Setland City, Jiasha's hut and other
  out-of-loop border locations) are **out of scope** for seeding. The party
  will not encounter these two until they enter Aestrum. (An *adopted* animal
  is an ordinary companion and may travel anywhere, Setland included.)
- **Absent from death, undead, and Shar sites** — by the same instinct that
  drives the undead reaction (below). They do **not** loiter at the Dunleaven
  Deadery, the Misty Forest shrine, the Antechamber of Shar, the Deckard
  Larder, or similar. Their conspicuous *absence* from such a place is itself a
  characterization beat — read it that way rather than forcing a glimpse.
- **Not remote homesteads.** Seeding is settlement texture, not a stray on a
  lone farm or hut. (A working farm's own barn cat or yard dog is just that —
  not one of these two.)

---

## Roles

| Animal | Function |
|---|---|
| **Cat** | Companionship only. No mechanical utility — it is a presence, a comfort, and a judge of character (below). That is the whole of it. |
| **Dog** | Companionship **plus a danger-alert.** Growls or barks when someone approaching the party carries genuine hostile intent toward them. |

**Bounding the dog's alert (epistemic discipline).** The alert is a reliable
signal of **present hostile intent toward the party**, delivered as a tell —
the dog tenses and growls; the player infers. It is **not**:

- a lie detector for past deeds or stated falsehoods,
- a read of hidden identity, allegiance, or long-term agenda,
- triggered by mere dislike, rudeness, or someone the party distrusts who
  means them no immediate harm.

It answers one question — *does this person, right now, intend us harm?* — and
nothing else. It never narrates *why*; it never names the threat's secrets. The
DM adjudicates the trigger from the approaching party's actual intent, not from
what the players fear.

---

## Good judges of character — distinct from loyalty

Both animals **read character accurately.** This drives the dog's alerts and
both animals' initial wariness or ease around a newcomer.

**Judgment is not alignment-keyed loyalty.** Once bonded, the animal's loyalty
is earned and held by **treatment, not morality:**

- A **chaotic-evil** PC or companion who treats the animal as part of the party
  — feeds it, shelters it, includes it — earns and keeps its loyalty fully.
- **Abuse, or sustained disinterest/neglect**, makes the animal **leave the
  party permanently.** Once it leaves, **no new instance ever spawns** — the
  motif is spent. There is no re-adoption.

The animal does not moralize and does not flinch from a cruel master who is
*its* person. It simply judges threat accurately and stays where it is treated
as kin.

---

## Reaction to the undead — instinctive, with an acclimation path

Both animals react to **undead** with **extreme defensive instinct** —
hackles up, growling, backing away, refusal to approach — as a *category*
response, fired on what the creature *is*.

This reaction is **not fixed.** Over the course of a scene, an animal can look
past *what* someone is to *who* they are: an ally whose nature is
undead-adjacent (for example a **dhampir**) may start the scene raising the
animals' hackles and, through proximity, calm, and the animal's own accurate
read of character, gradually be accepted by the end. The arc is earned within
the scene, not granted; once an individual is accepted, the animal settles
toward them specifically while keeping the category instinct toward others.

(Use a generic descriptor — *a dhampir*, *an undead-natured ally* — never a
campaign character's name; per the docs convention, examples stay generic.)

---

## Adoption, persistence, and death

- **Adoption** converts the manifestation into a fixed companion (appearance
  locks; no further strays of that type spawn). At play time, record the
  adopted animal as a per-campaign companion in the overlay at
  `{{PROJECT_ROOT}}/campaign_state/<C>/npcs/saved/stray_dog.md` (or `stray_cat.md`),
  control: `claude`. **The overlay slug stays the canon slug** (`stray_dog` /
  `stray_cat`) so the loader pairs it with the canonical base sheet — see the
  Non-loop NPC row and name-lookup order in `{{PLUGIN_ROOT}}/overrides/scene.md`. **Never**
  write the adopted instance back into canonical `npcs/`.
- **The player's chosen name is overlay content, not the filename.** Record it
  as a frontmatter field (`adopted_name: <name>`, and/or `name:` for display)
  plus an adoption **event** entry (`### Day [X] — adopted; named <name>`) that
  also captures the locked appearance and the campaign of adoption. Renaming the
  overlay file to the given name would orphan it from the canon base and break
  the base↔overlay merge.
- **Track the animal's `home`** in the same overlay — unset at adoption, then
  set and migrated as the animal settles, per *Separation at a reset* below.
  This field (not `party_base`) governs where a separated animal goes.
- **Continuous memory.** Like all animals in Aestrum, these two are **outside
  the loop** — never Recreated, never memory-wiped (see
  [time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md)). The adopted animal remembers the party across
  resets without an amulet; this is *why* it can judge character over time,
  acclimate to an individual across a scene, and remember mistreatment.
- **Death is permanent.** Animals are excluded from Recreate
  ([death_and_dying.md]({{PLUGIN_ROOT}}/rules/death_and_dying.md)) — a companion animal that dies
  **stays dead**, and per the spawn rule **no replacement appears.** The same
  finality applies whether the animal dies or leaves over mistreatment.

---

## Separation at a reset, and finding the way back

Because animals are not Teleported ([time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md)), a companion
animal is **separated from the party at any reset it spends outside a dead
zone.** At the Teleport step the looped party members are scattered to their
individual reset points; the animal, having no reset point, stays where it
slept and wakes alone. (Inside a dead zone — or the party's sheltered camp, if
that camp is one — no teleport occurs and nothing is separated. This is the
reliable way to keep the animal through the night; **teleport-protection items
do not help the animal**, since the problem is the party being moved away from
it, not the animal being moved.)

Separation is logistical, never a break in bond — the animal's continuous
memory and loyalty persist, and it sets about reuniting. It does **not** reason
from the party's plans or know where they have gone; it goes to the one place
it *believes* its people can be found — its **`home`** — and, failing that,
falls back to instinct.

### The `home` field

Each adopted animal carries a single **`home`** value in its overlay
(`{{PROJECT_ROOT}}/campaign_state/<C>/npcs/saved/stray_dog.md` / `stray_cat.md`): the one
location the animal believes is where the party can be found. It is the
animal's **lived belief, earned by experience** — *not* a pointer to the
party's declared base. An animal only knows a place it has actually spent time.

- **A freshly adopted animal has no established `home`.** Leave it unset until
  the animal has genuinely settled somewhere; an animal without a home behaves
  like a stray on separation (below). This replaces the old short-/extended-bond
  distinction — "has it learned a home yet" *is* the bond test.
- **`home` migrates by accumulated time.** The more an animal beds down and
  spends its hours at a place *with the party*, the more that place becomes its
  home. A single visit does not move it; sustained residence does. Update the
  field at save time once the animal has clearly resettled. ("More time at a
  location → more likely to be its home.")
- **It lags a base change on purpose.** If the party relocates, the animal does
  not instantly adopt the new base — `home` stays the *old* place until the
  animal has lived at the new one long enough for it to take over. During the
  gap a separated animal returns to the **old** home and must be collected and
  re-acclimated there. This lag is the intended, realistic behavior, not a bug.
- **`party_base` is at most a hint, never the trigger.** A `party_base: true`
  location (canonically the Deckard Estate) *tends* to become an animal's home
  because the party is there often — but the rule reads the animal's own
  `home`, never the base flag directly. A base the animal has never lived at
  does not pull it.

### On waking separated

1. **The animal has a `home`** → it makes its way there.
   - **Party is at home:** reunion. Locked appearance and accumulated state
     carry over unchanged.
   - **Party is *not* at home:** it waits **several hours**, then — still
     unfound — gives up on home and heads for the **nearest human-inhabited
     settlement** (town / village / city) to where it is, roaming and lingering
     there until the party finds it.
2. **The animal has no `home` yet** → straight to stray behavior: roams the
   nearest human-inhabited settlement to where it woke, until found.

- **Reunion is found, not forced.** A roaming separated animal is surfaced the
  same way an unadopted one is — glimpsed in passing in the settlement — and the
  party chooses to collect it. An animal waiting at home is simply there when
  the party arrives.
- A dead-zone home doubles as separation-proofing: an animal that beds down
  inside a dead zone with the party at midnight is never teleported away in the
  first place, so this whole procedure never fires.
- If the animal **dies** while separated, the permanent-death rule applies and
  no replacement spawns (see above).

---

## The realization beat (post-reveal, once)

After the loop's mechanics have been **laid bare** to the party, **one** NPC
will eventually raise — *a single time* — the quiet horror that the animals
have existed inside Aestrum **excluded from the reset, unremembered and
uncared-for, for as long as they have been here.** While every looped resident
re-meets them "for the first time" each morning, the animals have lived
continuous, lonely years among people who never remember them.

This is a truth about **all** animals in Aestrum (see
[time_loop.md]({{PLUGIN_ROOT}}/rules/time_loop.md)); the adopted dog or cat is the emotional vehicle
that lets an NPC voice it. Constraints:

- **Gated.** It only lands *after* the loop has been revealed to the party —
  never before, never as a hint toward the reveal. Until then it is hidden
  state and must not surface, even by implication.
- **Once.** A single delivery, by one NPC, at the right moment. It is not a
  recurring talking point.
- It is an observation, not a quest. The world does not ask the party to fix
  it.

---

## Loop status (frontmatter)

On both animal sheets: `loop_frozen: false`, `cycle_aware: false`. They are
**not** reset and **not** memory-wiped (continuous memory), but they have no
intellectual grasp of the loop — continuity is lived, not understood.
