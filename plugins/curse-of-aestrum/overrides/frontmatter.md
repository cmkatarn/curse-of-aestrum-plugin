---
id: override_frontmatter
name: Frontmatter Bindings — Curse of Aestrum
type: override
---

# Frontmatter Bindings — Curse of Aestrum

Curse of Aestrum's concrete answer to Aria's entity data spec. Aria
([`{{PLUGIN_ROOT}}/engines/story-engine/FRONTMATTER.md`]({{PLUGIN_ROOT}}/engines/story-engine/FRONTMATTER.md)) states what an
entity file must guarantee; this file states how **this campaign spells it**.

The split between the two is Aria's
[`authoring_entities.md#entity-authoring.bindings`]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_entities.md#entity-authoring.bindings):
invariants are the engine's and are not negotiable here, bindings are the work's and
are declared exactly once — in this file.

**Loaded by:** any skill that reads or authors campaign entity files — `scene`,
`create-npc`, `create-character`, `create-party`, `author`, and any future
authoring skill. It is a data-shape override, not a rules override: campaign
mechanics live in [`{{PLUGIN_ROOT}}/rules`]({{PLUGIN_ROOT}}/rules), which layers on Bailly. This file
layers on Aria.

---

## The Bindings

| Aria invariant | Curse of Aestrum binding |
|---|---|
| A reference resolves to exactly one entity | Type-prefixed ids in one shared namespace across the whole repo. |
| An id is minted once; other names are aliases | Prefixes below. No alias field in use yet — see *Known Gaps*. |
| Containment: one key, on the child | **`parent`**. |
| Peer relations: declared on both ends | Pairs table below. |
| Every entity's kind is resolvable, by one rule throughout | **Directory-kind binding.** The domain directory names the kind; `type:` carries this campaign's own classifier. |
| Each write goes to the correct layer | Path table below. |
| A goal carries a status from a closed set | Quests: `status: active \| complete \| failed`; `type: main \| side`. |

### Id prefixes

| Domain | Prefix | Example |
|---|---|---|
| `locations/` | `loc_` | `loc_dunleaven` |
| `npcs/` | `npc_` | `npc_rowan_deckard` |
| `party/` | `pc_` | `pc_sage` |
| `quests/` | `quest_` | `quest_breaking_the_cycle` |
| `factions/` | `faction_` | `faction_black_arrow` |
| `items/` | `item_` | `item_bloodline_compass` |

The prefix is what makes a bare mention resolvable, since this campaign uses one flat
namespace rather than per-directory scoping. An unprefixed id is not conformant.

### Peer relation pairs

Every row is authored on **both** sides. Adding one side without the other is the
one-way-edge failure in
[`authoring_entities.md#entity-authoring.relations`]({{PLUGIN_ROOT}}/engines/story-engine/rules/authoring_entities.md#entity-authoring.relations).

| Relation | On one side | On the other |
|---|---|---|
| Place ↔ neighbouring place | `connected_locations: [loc_…]` | `connected_locations: [loc_…]` |
| Character ↔ where they are | `location: loc_…` (on the NPC) | `npcs_present: [npc_…]` (on the location) |
| Quest ↔ its cast | `related_npcs: [npc_…]` | *(quest side only)* |
| Quest ↔ its places | `related_locations: [loc_…]` | *(quest side only)* |
| Character ↔ group | `groups: [faction_…]` (on the character) | `members: [npc_…]` (on the faction) |
| Item ↔ its holder | `held_by:` / `attuned_by:` | `items_attuned:` on the character |

`related_npcs` / `related_locations` are **plural on the quest side always**, even
with one entry. The singular forms `related_npc` / `related_quest` are not part of
this binding.

### Placement: `location` or `location_status`, never both

`location:` is a **reference** — it holds a `loc_` id and nothing else, including no
trailing parenthetical. When a character has no place to point at, the reason goes in
`location_status:` instead, drawn from a closed set:

| Value | Means |
|---|---|
| `roaming` | No fixed location, permanently — the strays. |
| `hidden` | In hiding; the location is unknown **in fiction**, which is canon rather than a gap. |
| `itinerant` | Between postings or moving; no current seat. |
| `tbd` | An authoring decision not yet made. The only value expected to become a `loc_` id later. |

Every NPC sheet carries exactly one of the two. The point is that a *state* must
never be written into a reference field: a value like `roaming` or `hiding_unknown`
in `location:` can only ever dangle, and it silently breaks the character ↔ place
pair in both directions — the character becomes unreachable from the location side
too. Detail beyond the status word (which Setland town, hiding from whom) belongs in
the body prose, where it already lives.

### Membership is `groups:`, and it replaced `faction:`

**`faction:` no longer exists on any character sheet.** It was free text doing four
jobs at once — real organizations, status words like `independent`, places used as
affiliations, and deities — so nothing could resolve it and the character↔group edge
was invisible in both directions.

`groups:` is a **list of faction ids**, reciprocated by `members:` on the faction:

```yaml
groups: [faction_setland_court, faction_shar]   # dual membership, one of them secret
groups: [faction_black_arrow]
groups: []                                       # belongs to no organization
```

- **`groups: []` is an assertion**, same as `npcs_present: []` — this character is in
  nothing. It replaced both `independent` and `none`, which were a distinction without
  a difference.
- **Multiple memberships are just multiple entries.** Quellenna sits in the Setland
  court and in Shar's cell; the secrecy of the second lives in that faction's
  `known_to` column, not in her sheet.
- **What kind of member someone is — current, former, secret — is the faction's
  `role` column, not a suffix on the id.** `black_arrow_former` became
  `groups: [faction_black_arrow]` plus a role of "**former** member — deserted" on the
  roster, which is where a reader will actually look for it.
- **A contract is not a membership.** Mieke captains a Black Arrows-*contracted*
  mercenary band and carries `groups: []`; the arrangement is prose. Same rule that
  keeps Galadiil off the Shrikes' roster and Roland off the Setland court's.

### Faction secrecy is `known_to`, and it is machine-checked

`known_to` records **which members know a given member belongs** — the secrecy
graph of a cell. It is **directed** (Hati knows Judith serves Shar; Judith does not
know Hati does) and **member-to-member only**: what an outsider or the party has
learned is per-character state on their own sheets, never here.

It lives in faction **frontmatter** as a sparse map — the same split as `members:`
(frontmatter is the checked source, the Membership table is the human view):

```yaml
members: [npc_hati_heldrivver, npc_judith_asemyeer, npc_quellenna_ilphekiir]
known_to:
  npc_hati_heldrivver: [npc_judith_asemyeer]   # known to Judith only
  npc_quellenna_ilphekiir: []                  # known to no member
```

- **Sparse — absent means known to all.** An open faction (everyone knows everyone)
  carries **no `known_to` at all**; only a member whose visibility deviates is listed.
  A member mapped to `[]` is known to nobody.
- **Every key and every value must be a `members` id.** `entitycheck` enforces this
  (`[[domains.factions.scoped_map]]`): a `known_to` endpoint outside the roster is the
  secrecy graph naming a ghost, and is now a finding rather than prose nobody reads.
- **A non-entity knower stays in prose.** The Black Arrows' Theren is known to Roland
  *and Roland's wife*; the wife has no sheet, so frontmatter records
  `pc_theren_elakian: [npc_roland_elakian]` and the table keeps the wife.

### Devotion is `deity:`, not `faction:`

**A god is not a faction.** `faction:` names an organization a character belongs to;
`deity:` names who they worship. Keeping them apart stops a reference field from
holding a thing that can never resolve to a group.

The test — **if there were a faction around a deity, it would have its own proper
name.** The Selûne acolytes of the boundary are an order: a post, a lineage, a
succession, and a name of their own. "Kelemvor" is not an order; it is who Corva
prays to while doing a job in Dunleaven. Shar is the instructive case — she has a
faction file *because she runs an operation*, with instruments, adherents and pieces;
her devotees carry both `faction:` (the cell) and `deity:` (the god).

| Character | `groups:` | `deity:` |
|---|---|---|
| Jiasha | `selune_acolytes` — a real order with a name | `selune` |
| Corva | *(none — she belongs to no organization)* | `kelemvor` |
| Assaneela | `yuan_ti_detachment` — her cohort at the temple | `zehir` |

Assaneela shows the split cleanly: she belongs to the **Yuan-Ti detachment** at the
temple (`groups: [faction_yuan_ti_detachment]`) and worships **Zehir** (`deity: zehir`)
— a cohort and a god are different things, filed in different fields. There is still
**no `faction_zehir`**: her sheet states that she "is not a recurring faction agent" and
that **Zehir has no active presence in Aestrum** beyond her, and a deity-as-faction file
would contradict that. The detachment is a set-piece cohort (see
`{{PLUGIN_ROOT}}/factions/chapter_1/yuan_ti_detachment.md`), not a Zehir organization — the same
distinction that keeps a god out of the faction graph while a concrete group belongs in
it.

### `location:` is an anchor, not a claim of constant presence

**No character is *always* anywhere.** `location:` does not assert where someone is
at a given hour — it names the place they are **anchored to**, the answer to *"where
do I find them."* Their movement through the day belongs in the body, as a schedule
or route.

For a cycle-affected character the anchor has a non-arbitrary definition: **the reset
position** — where the loop puts them at the start of the day. It is identical every
cycle, it is where the party finds them if they go looking at day start, and it does
not drift with whatever the character does between waking and midnight.

The failure this prevents is anchoring a character to **a stop on their route** or,
worse, to **where a particular playthrough happened to find them**. Both look correct
in the file and both are wrong the moment a different run asks the question. A
character on a fixed daily route is not `itinerant` either — `itinerant` means *no
fixed base*, which is the opposite of a precise daily cycle. Anchor them to the reset
and put the route in prose.

Quest→entity references are one-directional by design: a location does not list the
quests that touch it, because a quest is a run-scoped thread and a location file is
canon. That asymmetry is deliberate and does not count as a one-way edge.

### Containment

`parent` only, on the child, for every kind:

```yaml
id: loc_dunleaven_deadery_trambeathen_tomb
parent: loc_dunleaven_deadery
```

`parent_location` is **not** part of this binding. Directory nesting
(`locations/chapter_1/duskwall/…`) is presentation; `parent` is the containment of
record and is declared even when the file already sits in the parent's directory.

### Layer paths

Per Aria's
[`file_layering.md#file-layering.tier-binding`]({{PLUGIN_ROOT}}/engines/story-engine/rules/file_layering.md#file-layering.tier-binding):

| Aria layer | Curse of Aestrum path |
|---|---|
| **Base / Chapter** | `<domain>/chapter_N/<file>.md` at the repo root |
| **Current** | `{{PROJECT_ROOT}}/campaign_state/<instance>/<domain>/saved/<file>.md` |
| **Instance rules** | `{{PROJECT_ROOT}}/campaign_state/<instance>/rules/<file>.md` |

This campaign folds base and chapter into one tier: the canon tree is chapter-scoped
from the start, and `chapter_1/` *is* the campaign-start state rather than a planned
overlay on a chapter-less base. A campaign-created entity — one that exists because a
run produced it — is written to the current layer as a self-contained file and never
into the canon tree.

---

## How kind is resolved

This campaign uses Aria's **directory-kind** binding: an entity's kind comes from the
domain directory its file sits in, and `type:` is free for the campaign's own
classifier — `type: shop`, `type: tavern`, `type: main`, `type: magical_jewelry`,
`type: npc_companion`.

Aria permits this alongside the explicit-kind binding (where `type` names the kind
from a controlled set), and requires only that a work pick **one** and hold to it.
Mixing them is the non-conformant case: a reader resolving kind by directory would
misread a `type` it did not expect. So a campaign entity file **must live in its
domain directory** — that placement is what carries its kind, and a file outside one
has no resolvable kind at all.

Keep `type` values short classifiers rather than sentences, so anything grouping by
subtype has comparable values. Descriptive prose belongs in the body Overview.

Existing files are already conformant on this point; no migration is needed.

---

## Conformance

The entity graph is **machine-checked**; there is no hand-maintained findings
list here, because one drifts out of true the moment a gap is closed. For the
live state, run

```
py -m runtime entitycheck --config {{PLUGIN_ROOT}}/entitycheck.toml
```

from `fiction-host`. It reports every open finding with a file and line, and it
is the authority — this file explains the bindings, the checker enforces them.

**What it covers.** Ids, prefixes, containment keys, placement, the
character↔place and character↔group edges, one-way edges, alias drift, and quest
status vocabularies. A binding described in this file but absent from
`{{PLUGIN_ROOT}}/entitycheck.toml` is unenforced — that gap is worth closing in the config, not
recording here.

Only kingdom- and duchy-scale names outside the filed set (`loc_aestrum`,
`loc_setland`, and the two road corridors) are **declared soft pointers**. Most
region-scale names that look like soft pointers — `loc_mikaelvad`, `loc_dalihad`,
`loc_mireval`, `loc_skaarsdaam`, `loc_nortmunde`, `loc_mirot`, `loc_rockwood` — are
**defined entities** in the standalone-locations roster, and declaring a defined
entity soft would suppress real findings against it.
