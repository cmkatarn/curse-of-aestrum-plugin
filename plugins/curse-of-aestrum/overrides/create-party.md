# Create Party — Curse of Aestrum Override

Setting overrides for the rpg-5e-engine `create-party/core.md`. Inherits
all spoiler discipline, blood-relation rules, restricted features, and
hook tables from [create-character.md]({{PLUGIN_ROOT}}/overrides/create-character.md). This file
adds only the multi-PC and opening-scene specifics.

---

## Session-Opening Discipline — No Plot Leaks in Setup

Every question shown to the player during party creation and the opening-scene framing is subject to [rules/session_opening_no_plot_leaks.md]({{PLUGIN_ROOT}}/rules/session_opening_no_plot_leaks.md). The rule applies to the question text and every option label and description, including options the player will not pick. Read it before composing any batched question to the player. Hidden NPC state (companion cover stories, secret-carried objects, contracted targets) must not appear in visible setup text, even as a "no" option or a comfort-rating gate.

---

## State-Directory and Instance Conventions

Inherited from [scene.md]({{PLUGIN_ROOT}}/overrides/scene.md#state-directory-location-and-path-table).
Summary for this skill:

- **State root:** `{{PROJECT_ROOT}}/campaign_state/`
- **Active campaign indicator:** `{{PROJECT_ROOT}}/campaign_state/.active`
- **New-campaign scaffold:** create
  ```
  {{PROJECT_ROOT}}/campaign_state/<slug>/
    npcs/chapter_1/
    npcs/saved/
    party/saved/
    locations/saved/
    factions/saved/
    items/saved/
    rules/
    timelines/saved/
    conversation_states/
  ```
- **Within-campaign instance:** `{{PROJECT_ROOT}}/campaign_state/<C>/party/saved/<instance>/`
- **Rule-override scaffold:** write `{{PROJECT_ROOT}}/campaign_state/<slug>/rules/rule_overrides.md`
  with all toggles at their default (`false`), so the available overrides are
  discoverable for the new campaign. See the catalog in
  [../rules/optional_rules.md]({{PLUGIN_ROOT}}/rules/optional_rules.md) for the current toggle
  set; mirror its keys with `false` values.
- **Display-preferences scaffold:** write `{{PROJECT_ROOT}}/campaign_state/<slug>/preferences.md`
  seeded to the campaign defaults — `narrationDisplay: Novelization`,
  `dice_display: false` — as an instance overlay of
  [../party/preferences.md]({{PLUGIN_ROOT}}/party/preferences.md). These are mutable later
  (a change applies on the next scene). See
  [scene.md]({{PLUGIN_ROOT}}/overrides/scene.md#display-mode-and-dice-resolution), *Display mode and dice
  resolution*.

If the user picks "new campaign" with a slug that already exists, error
and ask for a different name (or to use the existing). After creating,
write the new slug to `.active`.

---

## Anti-Conflict Additions

Per the engine's anti-conflict rule, do not randomly assign in this
setting:

- A direct blood relation to Quellenna, Galadiil, Evandur, Malak, or
  Rowan (per [create-character.md]({{PLUGIN_ROOT}}/overrides/create-character.md#blood-relation-list-canon-load-bearing-npcs)).
- Amblecrown lineage. (Only allowed if the user volunteers it for a
  player-build slot, never randomized.)
- A Shar acolyte or Shar-aligned cleric/paladin.
- Membership in The Shrikes (including historical Setland branch — too
  entangled with current plot threads).
- Any origin or residency inside Aestrum.
- A character who claims pre-existing knowledge of the loop, dead zones,
  Shar's operations, or the suppression of Selûne in Aestrum.
- A character whose backstory requires knowledge of any canon PC.

If the user explicitly requests something on this list via mode 1 or 2
hints, allow it only if it is not a hard rule (Amblecrown is the one
allowed exception; blood relations to the five named NPCs remain
absolute).

---

## Outsider Rule

No new PC may originate inside the Aestrum region or carry pre-knowledge
of anything inside it. All hooks are Nortmunde-side only, per the
create-character override's hook tables.

---

## Opening Locations List

For STEP 5 (Case A and Case B Beat 1), the opening location is chosen
to fit the strongest party background hook. Candidates:

- **The Lion's Den** — Setland Duke's general assembly chamber. Fits
  noble, guild artisan, soldier reporting in, anyone with Setland court
  ties.
- **Charnelhold streets / lower districts** — fits urchin, criminal,
  charlatan, entertainer.
- **Setland docks** — fits sailor, smuggler.
- **A Setland temple or shrine** — fits acolyte.
- **A trade road into Setland** — fits outlander, folk hero, soldier
  arriving from another duchy.

Before writing the opening, read the relevant location file(s) so the
scene is accurate:

```
locations/chapter_1/setland_city.md
locations/chapter_1/the_lions_den.md
```

If slot 1's background points to a different opening location (docks,
temple, trade road), read the corresponding location file as well.

---

## Random-Slot Seeding of the Galadiil Bounty

If the user requests **two or more random / guided-random slots** during
party creation **AND has selected Claude-Directed NPC control** (per
engine [STEP 2 / NPC control mode]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/create-party/core.md#create-party.per-slot-mode)),
at least one of those random NPCs must roll a **questionable background**
and must, *secretly from the player-controlled PC*, be seeded with the
Galadiil writ. The player is never told this during creation or in the
opening scene.

**If the user selected Player-Directed NPC control, do not seed the
writ.** The secret-betrayal mechanic depends on Claude holding hidden
state on the NPC; if the player will be directing every NPC action, the
secret cannot exist coherently. The bounty simply is not in play through
the party. (A player who later takes control of an NPC and gains insight
into the writ's presence — fine. Let it happen. Do not program around
mid-campaign control swaps.)

### What counts as a questionable background

Drawn from [create-character.md § Background → Faction Hooks]({{PLUGIN_ROOT}}/overrides/create-character.md#background--faction-hooks):

- **Urchin** or **Criminal** (Erethezra or Black Arrows tie).
- **Charlatan** (identity-theft schemes against minor noble names).
- **Sailor** when rolled with the smuggler / coded-shanty angle.
- **Entertainer** when rolled with the signal-carrier angle.
- **Dwarf** of any subrace with the **Blooddigger** bounty-hunter tie
  (race-hook qualifier; can layer on an otherwise clean background and
  still count).

All other backgrounds are clean for this rule.

### Seeding rule

1. Roll the random slots normally per the engine walkthrough.
2. After all random slots have backgrounds drafted, scan the resulting
   set:
   - **If at least one questionable background was rolled organically**,
     pick the NPC whose backstory best supports an extant Black Arrows
     or Erethezra contact and seed the writ to that NPC. Do not re-roll.
   - **If zero questionable backgrounds were rolled**, re-roll the
     background on the random slot whose other choices (race, class,
     class-hook) most readily accept a questionable reframe, until a
     questionable background lands.
3. Mark the chosen NPC's saved sheet with a private DM-notes block:
   `holds_galadiil_writ: true` and a short note describing the contact
   chain (e.g., "received the writ from a Black Arrows runner in
   Charnelhold three weeks before the campaign opens"). This block is
   never surfaced to the player.

### Mid-campaign behavior

Gameplay mechanics, kept here because they are conditional on the
seeding above.

**Spread.** An NPC holding the writ will, at some point during the
campaign, share knowledge of the bounty with **other party members
(PC or NPC) who also have a questionable background**. This sharing
happens off-screen — the player does not witness it and is not told.
**There is no floor on when this can happen** — DM discretion, any
point from Session 1 onward, as soon as the holder has any plausible
private moment with a fellow questionable-background party member.
The holder never shares with clean-background party members. The
holder never volunteers the writ to the player-controlled PC unless
the PC has been seeded with a questionable background of their own.

**Betrayal threshold.** Any NPC party member with knowledge of the
writ carries a **non-zero, DM-judged chance** of either:

1. **Turning on the party** — proposing the bounty openly to the subset
   of party members the NPC reads as receptive, attempting to recruit
   allies for a coordinated claim against opposition from the honorable
   members; or
2. **Pre-empting the party** — moving on the writ solo, or with a single
   chosen accomplice, the moment Galadiil is accessible and the tactical
   picture allows.

**Gating condition.** Both behaviors are gated on the NPC's reading of
the party's character. The NPC must believe the party is **of the type
that would consider the bounty** for option 1; for option 2, the NPC
must believe the party would *not* consider it (and would therefore
obstruct a successful claim if asked). An NPC who reads the party as
mixed may withhold, wait, and re-read across sessions.

**Betrayal probability — fuzzy DM judgement call.** The percentage
chance is never rolled against a fixed table; it is the DM's running
read of three pressures, and it grows as those pressures grow:

1. **NPC's affinity for the party.** The less the NPC likes the party
   — abuse, disregard, repeated insult, ideological friction, the
   NPC's read that the party would never share a payout — the higher
   the chance. A well-treated NPC who feels genuinely included sits
   near the floor of the range.
2. **Time in Aestrum.** The longer the party has been trapped, the
   higher the chance. Loop fatigue, despair, the suspicion that there
   is no payout *because* there is no escape, all push the NPC toward
   cashing out on the one contract they still carry.
3. **Proximity to breaking the cycle.** As the party approaches the
   end of Chapter 1 — the actual breaking of the loop — the chance
   spikes. The NPC does not know breaking the cycle is imminent and
   does not know it would invalidate the writ (the cancellation
   propagates through the Charnelhold → Roland → contractor chain,
   see [factions/chapter_1/black_arrow.md]({{PLUGIN_ROOT}}/factions/chapter_1/black_arrow.md)).
   The DM knows. A late-Chapter-1 betrayal is the gameplay twist most
   parties will not see coming: the NPC moves on a writ that is about
   to go cold, and the party loses an ally to a contract that would
   not have paid out.

These three pressures combine — a disliked NPC late in a long-loop
campaign approaching the cycle break is at the top of the range; a
well-liked NPC early in a short campaign sits near the bottom. The
chance is never zero once the NPC holds the writ.

**Mechanical hooks.**

- The writ requires Galadiil's right eye and her right hand bearing the
  Ilphekiir ring as proof of identification (see
  [npcs/chapter_1/galadiil_ilphekiir.md § The Ilphekiir Ring]({{PLUGIN_ROOT}}/npcs/chapter_1/galadiil_ilphekiir.md#the-ilphekiir-ring)).
  An NPC pre-empting must have line-of-sight access to Galadiil and
  time to take both, or accept reduced payout by surfacing only the
  ring as proof of meeting.
- If Quellenna later cancels the bounty (see
  [factions/chapter_1/black_arrow.md]({{PLUGIN_ROOT}}/factions/chapter_1/black_arrow.md)),
  the cancellation propagates through the Charnelhold → Roland →
  contractor chain. An NPC who has not yet received word continues to
  operate on a defunct contract and would not be paid out.

**Engine-rule override — murder-in-the-night, dead-zone exception.**
The engine's harm-limits rule (see
[{{PLUGIN_ROOT}}/engines/rpg-5e-engine/create-party/core.md § Claude-controlled party NPCs and PC harm]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/create-party/core.md#create-party.claude-controlled-party))
forbids Claude-controlled party NPCs from murdering the PC in their
sleep. **CoA relaxes this limit conditionally, and only for the
bounty-seeded NPC:**

- The bounty-seeded NPC **may** murder the PC in their sleep **if and
  only if** the PC is sleeping outside a dead zone. A PC outside a
  dead zone resets at midnight; the killing does not stick, and the
  morning-after scene (see Reset aftermath below) is the gameplay
  payoff.
- The bounty-seeded NPC **may not** murder the PC in their sleep if
  the PC is sleeping inside a dead zone or is otherwise protected from
  the daily Modify Memory reset. Inside a dead zone the death is
  permanent; the engine limit holds.
- The other two engine limits hold unchanged in all cases: no killing
  the PC without a fair chance to defend; no coming to blows absent
  obvious, previously surfaced relationship friction (the
  betrayal-probability scaling above *is* the surfaced friction).

**Reset aftermath.** A betrayal executed inside the loop does not stick
the way a betrayal would outside it. At the next midnight:

- Galadiil resets to her snapshot — eye, hand, and ring all restored,
  whether or not they were taken (the ring is on her `holds_at_reset`
  list; her body resets with everything else). The proof the betrayer
  needed walks out of their satchel and back onto Galadiil's finger.
- Any party members the betrayer killed or injured during the move
  are restored by the loop.
- The betrayer themselves resets physically — wounds, exhaustion,
  whatever they spent — but as a loop-aware party member they retain
  memory of what they did. So do the party members they moved
  against. Nobody got hurt in a way the world remembers; everybody
  remembers anyway.

This sets up the morning-after conversation, which is the gameplay
payoff: the betrayed party members wake up alive, with the NPC who
tried to kill or sell them sitting at the same fire. The DM should
play the resulting scene without softening it — the NPC's reasons
haven't changed, the writ is still on the board, and the party now
has to decide what to do with someone whose intentions are no longer
deniable. A second attempt is plausible. So is a tense reconciliation.
So is the party killing the NPC and waking up to them again the next
morning.

**Recordkeeping.** When an NPC's writ-related decision triggers during
play, log it in that NPC's saved-state DM notes — what they decided,
what condition flipped them, and who else now knows. Log loop-reset
betrayal attempts cumulatively; repeated attempts are themselves a
party-dynamic data point.

---

## Case B Beat 2 — The Expedition Pitch

For Case B (party has random characters), Beat 2 fires when the player
brings the player-built PCs to the pitch presentation.

The pitch is delivered publicly by:

- **Quellenna Ilphekiir**
- **Duke Malak du Leon**

This is the invitation event at which contractors are sought for the
Aestrum expedition. They present the **surface job** (taxes / scouting /
diplomatic envoy / retrieval — whatever fits the scene Setland is
publicly running). Apply spoiler discipline rigidly — nothing about the
loop, dead zones, Shar, the Ilphekiir family, or any internal Aestrum
state. Quellenna and Malak speak as the public personas Setland citizens
would see — composed, confident, formal. Do not show their private
agendas.

---

## Campaign Time Anchor — Stamp the Sign-On Day (load-bearing)

The campaign's primary time anchor is the **Nortmunde Day the party signs
on** for the Aestrum expedition. Every later scene reads it to place the
world **Before Day 0** (King alive — the entire in-loop span) versus the
King's death; a party finished without it leaves the political era to
silently default and get mis-rendered (see `{{PLUGIN_ROOT}}/lore/key_lore_summary.md` →
Political Situation, and [scene.md]({{PLUGIN_ROOT}}/overrides/scene.md) → Roster-at-T parameters).

**At the moment the party is formally contracted** — the expedition pitch
is accepted and the members sign on (Case B Beat 2 above; for Case A, the
equivalent contracting beat) — stamp the anchor:

1. **On every PC's frontmatter**, write:
   ```yaml
   joined_expedition_nortmunde_day: -14
   ```
   Default **`-14`** (Kythorn 11, 1490 DR — the day Malak dispatches the
   expedition and contractors sign on, per
   `{{PLUGIN_ROOT}}/timelines/chapter_1/nortmunde_regional.md`). A PC who joins in-fiction
   after departure takes the Day they actually joined. **PCs only** — NPC
   companions are forbidden this field (per `{{PLUGIN_ROOT}}/overrides/scene.md`); their join is the
   prose `traveling_with_party_since`, set by `create-npc`.
2. **Seed the per-instance regional overlay**
   `{{PROJECT_ROOT}}/campaign_state/<C>/timelines/saved/nortmunde_regional.md` with a
   one-line declaration of the sign-on Day, so the start day is recorded
   campaign-level and not only distributed across PC sheets (the canonical
   timeline points party-instance dates here).

This stamp is **not optional.** If party formation finishes and any PC
lacks `joined_expedition_nortmunde_day`, that is a setup defect — add it
before the STEP 6 hand-off.

---

## Hand-Off Region Name

For the engine's STEP 6 hand-off prompt:

```
The party is in Setland. What do you do?
```

---

## Content Rating

Per [scene.md]({{PLUGIN_ROOT}}/overrides/scene.md#content-rating-system). Ask
for an explicit rating during STEP 1 if the user hasn't set one for the
instance.
