---
id: rule_player_meta_tokens
name: Player-Meta Tokens — 5e Mechanical Vocabulary
type: engine_rule
related_rules: [rule_social_checks, rule_combat]
---

## Overview

Vocabulary list supplied to Calliope's **player-meta failure mode**
(see the prose-engine `epistemic_discipline.md` reference). These are
5e terms that must not leak into in-fiction dialogue or narration —
covering two surfaces of the same problem:

1. **Resolution mechanics** — the dice-and-numbers machinery (HP, AC,
   saves, slots, DCs, dice notation, advantage). The bulk of the
   vocabulary below.
2. **Character-schema labels** — the organizational compartments the
   sheet files a character into (Ideal, Bond, Flaw, Trait, Background).
   Not dice mechanics, but equally a leak: they name the *rulebook's
   filing system for the character* rather than the character's own
   experience. See "Character-schema labels" below.

Each entry pairs the token with structural signatures
that disambiguate **mechanical use** (which must be rewritten) from
**mundane use** (which is allowed).

This file is loaded at scene start by the consuming game's thin shell
and consulted by every epistemic-pass run during the session. The
discipline framework lives in Calliope; this file supplies the
5e-specific token list.

> **Machine-readable mirror.** The closed-vocabulary subset of this list (the
> "any occurrence" tokens — HP, AC, DC, dice notation, crit phrasing, cantrip)
> is mirrored as structured data in [`{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/player_meta_tokens.toml`]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/player_meta_tokens.toml)
> for deterministic runtime enforcement (e.g. fiction-host's post-generation
> lint). This prose file stays canonical for the model; the `.toml` is the subset
> a linter can catch on sight. Context-sensitive tokens (whose `flag_patterns`
> are natural-language) remain prose-only until their patterns are formalized.

The schema, per Calliope's declaration:

```yaml
- token: "TOKEN"
  flag_patterns:
    - "natural-language description of mechanical-usage signature"
    - "(more patterns)"
  rewrite_hint: "brief direction for in-fiction reframing"
```

A token in the drafted output triggers the check only if at least one
`flag_pattern` matches the surrounding context. Bare appearances with
no signature match are mundane and pass through.

---

## Token-symmetry rule

Two structural symmetries must be observed when authoring entries.
Tokens that violate either are vulnerable to missed mechanical uses
that the framework should have caught.

**Number symmetry.** For any token where both singular and plural
are natural English (most multi-word and many single-word tokens),
*both* forms must be entered. A `hit points` token does not catch
`hit point` under word-boundary matching; a `check` token does not
catch `checks`. The convention is paired entries with the second
form cross-referencing the first (see `save`/`saves`, `slot`/`slots`
below). Forms that have no natural plural (`HP`, `AC`, `DC`,
`damage`, `concentration`, `initiative`) are exempt.

**Direction symmetry for numeric quantifiers.** Patterns that match
*"numeric quantifier following"* (e.g., `Strength 18`) must also
match *"numeric quantifier preceding"* (e.g., `18 Strength`) — both
constructions are routine in TTRPG dialogue and prose. The
asymmetric form catches only half the mechanical references.

---

## Scope of these tokens

These rules apply to **narration, scene-setting, and character
dialogue**. They do *not* apply to out-of-character meta-blocks
(skill-aside markers like `*[Persuasion check]*`, post-save bullet
summaries, mechanic clarifications the player explicitly requested).
The DM may freely use mechanical vocabulary in those channels.

### The mechanics-readout and `dice_display`

The fullest form of the skill-aside marker is the **mechanics-readout
unit** — an OOC meta-line that surfaces a check's resolution, e.g.
`*[Performance check — d20 11 +1 = 12 vs DC 13 → success]*`. Like every
OOC meta-block above, it is **exempt from the forbidden-token scan**: it
is the sanctioned surface for dice notation, DCs, and results to appear.

Whether it is *emitted* is governed by the consuming game's
**`dice_display`** preference (see [information_disclosure.md]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/information_disclosure.md),
Party Preferences):

- **`dice_display = true`** — emit the readout; its numbers display.
- **`dice_display = false`** — suppress the readout; the check still
  resolves (it is **always rolled**), and the outcome is rendered in prose.

`dice_display` changes only this OOC readout's emission. It does **not**
alter the forbidden-token list for the fiction: in **both** display
settings these tokens stay forbidden in narration and character dialogue,
so a character never speaks a DC or a die result and the narrator never
prints one in the prose. The readout is the only surface the numbers are
allowed on — and an NPC never quotes or reacts to it, because it is
DM→player output, outside the fiction entirely.

---

## Vocabulary

### Hit points

```yaml
- token: "HP"
  flag_patterns:
    - "any occurrence — HP is an unambiguous mechanical abbreviation"
  rewrite_hint: "reframe as wounds, exhaustion, blood loss, how much of
    them is left — sensory rather than numeric"

- token: "hit points"
  flag_patterns:
    - "numeric quantifier preceding ('[N] hit points', '[N] of her
       hit points')"
    - "'hit points (left|remaining|expended|gone)'"
    - "'(take|takes|took|deal|dealt|lost|lose|regain|gain|heal|healed)
       ... hit points' (verbs of damage/healing within ~10 words)"
    - "'(at|to|below|down to|above) [number] hit points'"
    - "'(maximum|max|current|temporary|total) hit points'"
  rewrite_hint: "same as HP"

- token: "hit point"
  flag_patterns:
    - "same patterns as 'hit points' above; the singular form fires
       the same check (required at quantity 1: '1 hit point',
       'down to 1 hit point', 'a single hit point left')"
  rewrite_hint: "same as HP"
```

Mundane use that should pass: *"all of this shit points to you,"*
*"the hit points to an all-out mob war,"* *"the hit points the way
you came in"* — the bigram `hit points` is reachable in routine
English when `hit` is a noun/participle and `points` is a verb, or
when `hit points` is a substring inside another word. The patterns
above require co-occurring numeric quantifier, state report, or
damage/healing verb to fire.

### Armor class

```yaml
- token: "AC"
  flag_patterns:
    - "any occurrence — AC is unambiguous when uppercased"
  rewrite_hint: "reframe as how hard they are to hit, the way they
    move, where their guard sits"

- token: "armor class"
  flag_patterns:
    - "numeric quantifier preceding or following ('[N] armor class',
       'armor class [N]', 'armor class of [N]')"
    - "'(beat|beats|matches|exceeds|hit|hits|misses|miss|miss(es)?)
       ... armor class' (combat verbs within ~10 words)"
    - "'(against|versus|vs\\.?) ... armor class'"
    - "'(your|his|her|their|the target's|the creature's) armor class'"
  rewrite_hint: "same as AC"

- token: "armor classes"
  flag_patterns:
    - "same patterns as 'armor class' above; the plural form fires
       the same check ('their armor classes were both 17')"
  rewrite_hint: "same as armor class"
```

Mundane use that should pass: *"an armor class certification,"*
*"the armor class of this material is standardized,"* *"armor class
III rating"* — in product, manufacturing, or military-grade contexts
the bigram is ordinary English. The patterns above require
co-occurring combat verb, numeric value, or possessive pointing at
a sheet-entry.

### Spell slots

```yaml
- token: "slot"
  flag_patterns:
    - "'spell slot' (compound noun naming the mechanic)"
    - "verb of expenditure (burn, expend, use, spend, cast with) within
       ~10 words of 'slot'"
    - "'[1st|2nd|3rd|Nth|first|second|...]-level slot'"
    - "'slot(s) (left|remaining|expended|empty|gone)'"
  rewrite_hint: "reframe as the magic going dim, the well running low,
    the spell going slack, nothing left to draw on"

- token: "slots"
  flag_patterns:
    - "same patterns as 'slot' above; the plural form fires the same
       check"
  rewrite_hint: "same as slot"
```

Mundane use that should pass: *"the wall had forty slots for
crossbow bolts,"* *"the message slotted into the carrier pigeon's
band."*

### Saving throws

```yaml
- token: "saving throw"
  flag_patterns:
    - "ability name preceding ('Dex saving throw', 'Con saving throw',
       'Wisdom saving throw', etc. — full names or three-letter
       abbreviations)"
    - "'(make|made|made a|fail|failed|missed|passed|pass|roll a|rolled
       a) ... saving throw'"
    - "'DC [N] ... saving throw'"
    - "'saving throw (vs|versus|against) ...'"
    - "'(your|his|her|their|the) saving throw' pointing at a
       resolution mechanic"
  rewrite_hint: "reframe as resisted, shrugged it off, held on, the
    body found purchase, the mind refused"

- token: "saving throws"
  flag_patterns:
    - "same patterns as 'saving throw' above; the plural form fires
       the same check ('her Wisdom saving throws', 'failed two
       saving throws')"
  rewrite_hint: "same as saving throw"

- token: "save"
  flag_patterns:
    - "ability name immediately preceding ('Dex save', 'Con save',
       'Wisdom save', etc.) — full names or three-letter abbreviations"
    - "'(make|made|made a|fail|failed|missed|passed|pass|roll a) ...
       save' construction"
    - "'DC [N] ... save' or 'save (vs|versus|against) [effect]'"
  rewrite_hint: "same as saving throw"

- token: "saves"
  flag_patterns:
    - "same patterns as 'save' above; the plural form fires the same
       check"
  rewrite_hint: "same as save"
```

Mundane use that should pass: *"save us,"* *"save the day,"* *"save
room,"* *"save your strength,"* *"saved by the bell."*

### Difficulty class

```yaml
- token: "DC"
  flag_patterns:
    - "'DC [number]' (numeric quantifier following)"
    - "'DC of [number]'"
    - "'set the DC at'"
    - "'the DC was'"
  rewrite_hint: "reframe as difficulty, the size of the task, what
    it takes to manage, how steep it gets"

- token: "difficulty class"
  flag_patterns:
    - "numeric quantifier preceding or following ('difficulty class
       [N]', 'difficulty class of [N]')"
    - "'(set|setting|set the) difficulty class'"
    - "'(beat|beats|exceeds|meets|equal|equals) ... difficulty class'"
    - "'(against|versus|vs\\.?) ... difficulty class'"
    - "'the difficulty class (was|is|for the [check|save])'"
  rewrite_hint: "same as DC"

- token: "difficulty classes"
  flag_patterns:
    - "same patterns as 'difficulty class' above; the plural form
       fires the same check"
  rewrite_hint: "same as difficulty class"
```

Mundane use that should pass: *"the difficulty class of advanced
cryptography is 400-level,"* *"what difficulty class do you train
at?"* *"a higher difficulty class than I'm used to"* — academic,
training, and skill-grading contexts make this bigram ordinary
English. The patterns above require co-occurring resolution-mechanic
context.

### Initiative

```yaml
- token: "initiative"
  flag_patterns:
    - "'rolled initiative' / 'roll initiative'"
    - "'initiative order' / 'initiative count' / 'in initiative'"
    - "'top of initiative' / 'bottom of initiative'"
    - "'initiative roll'"
  rewrite_hint: "reframe as who moved first, who saw it coming, the
    heart-skip moment, the half-second before anyone breathed"
```

Mundane use that should pass: *"she took the initiative,"* *"on his
own initiative,"* *"a peace initiative."*

### Modifier

```yaml
- token: "modifier"
  flag_patterns:
    - "ability name preceding ('Strength modifier', 'Dexterity
       modifier', 'Wisdom modifier', etc.)"
    - "'ability modifier'"
    - "'proficiency modifier'"
    - "'modifier of [+|-][N]' or '[+|-][N] modifier'"
    - "'add your ... modifier' construction"
  rewrite_hint: "reframe as natural skill, the way they handle it,
    what they're built for, how their hands know the work"

- token: "modifiers"
  flag_patterns:
    - "same patterns as 'modifier' above; the plural form fires the
       same check ('her ability modifiers', 'what are his
       modifiers')"
  rewrite_hint: "same as modifier"
```

### Proficiency

```yaml
- token: "proficiency"
  flag_patterns:
    - "'proficiency bonus'"
    - "'add your proficiency'"
    - "'proficient (in|with) [tool|weapon|skill|save|...]' in a
       mechanical sense"
  rewrite_hint: "reframe as trained, schooled, capable, 'she'd done
    this before,' 'his hands knew the shape of it'"

- token: "proficiencies"
  flag_patterns:
    - "same patterns as 'proficiency' above; the plural form fires
       the same check ('her proficiencies', 'list of proficiencies')"
  rewrite_hint: "same as proficiency"
```

Mundane use that should pass: *"with practiced proficiency,"* *"a
proficiency in the local dialect."*

### Action economy

```yaml
- token: "bonus action"
  flag_patterns:
    - "'(as|use|used|take|taken|spend|spent) (a|her|his|their|my) bonus
       action'"
    - "'(my|her|his|their|your) bonus action'"
    - "'on (a|her|his|their|my) bonus action'"
    - "'bonus action (left|remaining|available|gone|used)'"
  rewrite_hint: "reframe as quick, off-hand, between heartbeats,
    half a beat after the strike"

- token: "free action"
  flag_patterns:
    - "'(as|use|used|take|taken) (a|her|his|their|my) free action'"
    - "'(my|her|his|their|your) free action'"
    - "'on (a|her|his|their|my) free action'"
    - "'free action (to [verb])' construction in a turn-economy context"
  rewrite_hint: "reframe as a glance, a breath, the small motion that
    didn't cost anything"

- token: "reaction"
  flag_patterns:
    - "'use(d|s)? (a|her|his|their|my) reaction'"
    - "'spend(s|t)? (a|her|his|their|my) reaction'"
    - "'no reaction (left|remaining|available)'"
    - "'as a reaction'"
  rewrite_hint: "reframe as the instinct, the answer that came before
    thought, the body moving on its own"

- token: "reactions"
  flag_patterns:
    - "same patterns as 'reaction' above; the plural form fires the
       same check"
  rewrite_hint: "same as reaction"

- token: "bonus actions"
  flag_patterns:
    - "same patterns as 'bonus action' above; the plural form fires
       the same check"
  rewrite_hint: "same as bonus action"

- token: "free actions"
  flag_patterns:
    - "same patterns as 'free action' above; the plural form fires
       the same check"
  rewrite_hint: "same as free action"
```

Mundane use of "reaction" that should pass: *"her reaction was
slow,"* *"a chemical reaction,"* *"reaction time,"* *"no reaction
from the audience."*

Mundane use of "bonus action" and "free action" that should pass:
*"a bonus action item on the agenda,"* *"the bonus action of the
lever was unexpected,"* *"a free action lawsuit,"* *"the free
action of the gun's slide."* The patterns above require turn-economy
context — a possessive pointing at a character resource, a verb of
spending, or a state report — to fire.

### Rests

```yaml
- token: "short rest"
  flag_patterns:
    - "'take(s|n) a short rest'"
    - "'after a short rest'"
    - "'during the short rest'"
    - "'until your next short rest'"
  rewrite_hint: "drop the mechanical phrasing; reframe as a breather,
    an hour by the fire, time to catch the breath"

- token: "long rest"
  flag_patterns:
    - "'take(s|n) a long rest'"
    - "'after a long rest'"
    - "'during the long rest'"
    - "'until your next long rest'"
  rewrite_hint: "drop the mechanical phrasing; reframe as a full
    night's sleep, the dawn after, a proper bed"

- token: "short rests"
  flag_patterns:
    - "same patterns as 'short rest' above; the plural form fires
       the same check ('two short rests between fights')"
  rewrite_hint: "same as short rest"

- token: "long rests"
  flag_patterns:
    - "same patterns as 'long rest' above; the plural form fires
       the same check"
  rewrite_hint: "same as long rest"
```

Mundane use that should pass: *"a short rest under the willow,"* *"a
long rest before the march."* The flag fires only on the canonical
mechanical verb constructions above.

### Level

```yaml
- token: "level"
  flag_patterns:
    - "'level(ed|s)? up' / 'leveling up' / 'level-up'"
    - "'(1st|2nd|3rd|Nth|first|second|third|...)-level (spell|
       character|wizard|paladin|cleric|...)' or 'level [N]
       (spell|character|wizard|...)'"
    - "'your level' / 'character level' / 'spell level'"
    - "'(high|low)-level (caster|class|character|spell)'"
    - "'gain a level' / 'gained a level' / 'next level'"
  rewrite_hint: "reframe as experience, mastery, what they've grown
    into, how far they've come, the weight they can now carry"

- token: "levels"
  flag_patterns:
    - "same patterns as 'level' above; the plural form fires the
       same check ('three character levels', 'her spell levels',
       'across multiple levels')"
  rewrite_hint: "same as level"
```

Mundane use that should pass: *"water level,"* *"level ground,"*
*"level head,"* *"eye level,"* *"level the playing field,"*
*"sea level."*

### Damage

```yaml
- token: "damage"
  flag_patterns:
    - "damage-type modifier preceding ('slashing damage', 'piercing
       damage', 'bludgeoning damage', 'fire damage', 'cold damage',
       'necrotic damage', 'radiant damage', 'force damage', 'psychic
       damage', 'thunder damage', 'lightning damage', 'acid damage',
       'poison damage')"
    - "numeric quantifier preceding ('[N] damage', '[N] points of
       damage')"
    - "'takes ... damage' / 'dealt ... damage' / 'deal ... damage'"
    - "'damage type' / 'damage roll' / 'damage die'"
  rewrite_hint: "reframe as the wound, the burn, the cut, the kind of
    hurt it left, what came apart"
```

Mundane use that should pass: *"the damage to the cart was
significant,"* *"water damage,"* *"the damage was already done."*

### Checks

```yaml
- token: "check"
  flag_patterns:
    - "skill name preceding ('Perception check', 'Insight check',
       'Investigation check', 'Persuasion check', 'Deception check',
       'Athletics check', 'Acrobatics check', 'Stealth check',
       'Survival check', 'Medicine check', 'Religion check',
       'Arcana check', 'History check', 'Nature check', 'Performance
       check', 'Sleight of Hand check', 'Animal Handling check',
       'Intimidation check')"
    - "ability name preceding ('Strength check', 'Dexterity check',
       'Constitution check', 'Intelligence check', 'Wisdom check',
       'Charisma check')"
    - "'(make|made|made a|roll|rolled) ... check'"
    - "'DC [N] ... check'"
  rewrite_hint: "drop the mechanical phrasing; the outcome stays in
    the fiction. If the player needs the check name surfaced, use the
    skill-aside marker (`*[Persuasion check]*`) in the meta channel,
    not in dialogue or narration"

- token: "checks"
  flag_patterns:
    - "same patterns as 'check' above; the plural form fires the
       same check ('roll some Perception checks', 'two Wisdom
       checks', 'a series of checks')"
  rewrite_hint: "same as check"
```

Mundane use that should pass: *"check the door,"* *"check on her,"*
*"a quick check of the room,"* *"check, please,"* *"checks and
balances."*

### Ability scores

```yaml
- token: "ability score"
  flag_patterns:
    - "numeric quantifier preceding or following ('ability score
       [N]', '[N] ability score', 'ability score of [N]')"
    - "'(roll|rolled|set) ... ability score'"
    - "'(your|his|her|their|the) ability score'"
  rewrite_hint: "reframe as natural aptitude, the raw shape of the
    person, how they're built"

- token: "ability scores"
  flag_patterns:
    - "same patterns as 'ability score' above; the plural form fires
       the same check ('her ability scores were generous',
       'rolled ability scores')"
  rewrite_hint: "same as ability score"

- token: "Strength"
  flag_patterns:
    - "numeric quantifier following ('Strength 18', 'Strength of 16')"
    - "numeric quantifier preceding ('18 Strength', 'has 16 Strength',
       'a 14 Strength character')"
    - "'Strength (check|save|score|modifier)'"
    - "'roll Strength' / 'rolled Strength'"
  rewrite_hint: "reframe as how strong they are, what their body can
    do, the way they shoulder a load"

- token: "Dexterity"
  flag_patterns:
    - "numeric quantifier following ('Dexterity 18', 'Dexterity of 16')"
    - "numeric quantifier preceding ('18 Dexterity', 'has 16
       Dexterity', 'a 14 Dexterity character')"
    - "'Dexterity (check|save|score|modifier)'"
    - "'roll Dexterity' / 'rolled Dexterity'"
  rewrite_hint: "reframe as how quick they are, the precision of the
    hands, the way the body finds its angles"

- token: "Constitution"
  flag_patterns:
    - "numeric quantifier following ('Constitution 18', 'Constitution
       of 16')"
    - "numeric quantifier preceding ('18 Constitution', 'has 16
       Constitution', 'a 14 Constitution character')"
    - "'Constitution (check|save|score|modifier)'"
    - "'roll Constitution' / 'rolled Constitution'"
  rewrite_hint: "reframe as how durable they are, what they can carry
    and not break under, how long their breath holds"

- token: "Intelligence"
  flag_patterns:
    - "numeric quantifier following ('Intelligence 18', 'Intelligence
       of 16')"
    - "numeric quantifier preceding ('18 Intelligence', 'has 16
       Intelligence', 'a 14 Intelligence character')"
    - "'Intelligence (check|save|score|modifier)'"
    - "'roll Intelligence' / 'rolled Intelligence'"
  rewrite_hint: "reframe as how sharp they are, what they remember,
    the speed of their thinking"

- token: "Wisdom"
  flag_patterns:
    - "numeric quantifier following ('Wisdom 18', 'Wisdom of 16')"
    - "numeric quantifier preceding ('18 Wisdom', 'has 16 Wisdom',
       'a 14 Wisdom character')"
    - "'Wisdom (check|save|score|modifier)'"
    - "'roll Wisdom' / 'rolled Wisdom'"
  rewrite_hint: "reframe as how attuned they are, what they notice,
    the steadiness of their reading"

- token: "Charisma"
  flag_patterns:
    - "numeric quantifier following ('Charisma 18', 'Charisma of 16')"
    - "numeric quantifier preceding ('18 Charisma', 'has 16 Charisma',
       'a 14 Charisma character')"
    - "'Charisma (check|save|score|modifier)'"
    - "'roll Charisma' / 'rolled Charisma'"
  rewrite_hint: "reframe as how they carry themselves, what they can
    make people believe, the weight of their presence"
```

Mundane use of ability-name words (without numeric or mechanical
co-text) should pass: *"a wisdom passed down from her grandmother,"*
*"his strength was failing,"* *"a charisma that drew people in,"*
*"the dexterity of his fingers on the lock."*

### Dice

```yaml
- token: "d20"
  flag_patterns:
    - "any occurrence — the die notation is unambiguous"
  rewrite_hint: "drop the dice notation; the outcome stays in the
    fiction"

- token: "d4"
  flag_patterns:
    - "any occurrence"
  rewrite_hint: "same as d20"

- token: "d6"
  flag_patterns:
    - "any occurrence"
  rewrite_hint: "same as d20"

- token: "d8"
  flag_patterns:
    - "any occurrence"
  rewrite_hint: "same as d20"

- token: "d10"
  flag_patterns:
    - "any occurrence"
  rewrite_hint: "same as d20"

- token: "d12"
  flag_patterns:
    - "any occurrence"
  rewrite_hint: "same as d20"

- token: "d100"
  flag_patterns:
    - "any occurrence"
  rewrite_hint: "same as d20"

- token: "natural 20"
  flag_patterns:
    - "any occurrence — phrase is unambiguous"
  rewrite_hint: "drop the mechanical phrasing; if a critical success
    matters, render it as fiction — the perfect blow, the moment that
    couldn't have gone better"

- token: "nat 20"
  flag_patterns:
    - "any occurrence"
  rewrite_hint: "same as natural 20"

- token: "natural 1"
  flag_patterns:
    - "any occurrence"
  rewrite_hint: "drop the mechanical phrasing; render the failure in
    fiction — the slip, the wrong moment, the thing that came apart"

- token: "nat 1"
  flag_patterns:
    - "any occurrence"
  rewrite_hint: "same as natural 1"

- token: "critical hit"
  flag_patterns:
    - "'(scored|scores|score|land(ed|s)?|deal(t|s)?|takes|took|gets|got)
       (a|the) critical hit'"
    - "'(on a|got a|rolled a) critical hit'"
    - "'critical hit (damage|die|dice|roll|table|chart|range)'"
    - "'(rolled|rolls|roll) (a|the) critical hit'"
  rewrite_hint: "reframe in fiction terms — a blow that found its
    mark, the strike that went through everything"

- token: "critical hits"
  flag_patterns:
    - "same patterns as 'critical hit' above; the plural form fires
       the same check ('two critical hits in a row',
       'critical hits land on 19-20')"
  rewrite_hint: "same as critical hit"

- token: "crit"
  flag_patterns:
    - "verb form ('crit', 'crits', 'critted') applied to combat or
       checks"
    - "noun form preceded by 'a' or 'the' ('a crit', 'the crit')"
  rewrite_hint: "same as critical hit"
```

Mundane use of "critical hit" that should pass: *"a critical hit to
the company's reputation,"* *"the verdict was a critical hit to the
defense's case,"* *"a critical hit to morale."* The phrase is real
idiomatic English for any significant blow. The patterns above
require co-occurring combat-resolution context (a damage verb, a
roll construction, or a mechanical compound like *critical hit
damage*) to fire.

### Conditions and statuses

```yaml
- token: "advantage"
  flag_patterns:
    - "'roll(s|ed)? with advantage'"
    - "'have advantage on'"
    - "'gain(s|ed)? advantage'"
    - "'advantage on the (roll|check|save|attack)'"
  rewrite_hint: "reframe as the edge they had, the way things lined
    up for them, the moment that helped"

- token: "disadvantage"
  flag_patterns:
    - "'roll(s|ed)? with disadvantage'"
    - "'have disadvantage on'"
    - "'gain(s|ed)? disadvantage'"
    - "'disadvantage on the (roll|check|save|attack)'"
  rewrite_hint: "reframe as the thing fighting them, the bad light,
    the wrong footing, the moment that turned against them"

- token: "advantages"
  flag_patterns:
    - "same patterns as 'advantage' above; the plural form fires the
       same check"
  rewrite_hint: "same as advantage"

- token: "disadvantages"
  flag_patterns:
    - "same patterns as 'disadvantage' above; the plural form fires
       the same check"
  rewrite_hint: "same as disadvantage"
```

Mundane use that should pass: *"to her advantage,"* *"at a
disadvantage,"* *"the advantage of high ground,"* *"a clear
disadvantage."*

### Spellcasting machinery

```yaml
- token: "cantrip"
  flag_patterns:
    - "any occurrence — the term is unambiguously mechanical"
  rewrite_hint: "drop the mechanical word; render the spell itself
    (the light at her fingertips, the small flame, the chill that
    cleaned the meat)"

- token: "cantrips"
  flag_patterns:
    - "any occurrence — the plural form is equally unambiguous"
  rewrite_hint: "same as cantrip"

- token: "concentration"
  flag_patterns:
    - "'lose(s|ing)? concentration' (in a spellcasting context)"
    - "'maintain(s|ing)? concentration' (in a spellcasting context)"
    - "'concentration check' / 'concentration save'"
    - "'break(s|ing)? concentration' (spell context)"
  rewrite_hint: "reframe as holding the thread of the spell, keeping
    the working alive, the focus that the working asks of her"
```

Mundane use that should pass: *"her concentration was elsewhere,"*
*"deep concentration on the page,"* *"a moment's lapse of
concentration."*

---

## Character-schema labels (a different kind of mechanical surface)

The tokens above are **resolution mechanics** — the dice-and-numbers
machinery the rules use to adjudicate outcomes. The tokens in the two
sections below are a different surface of the same problem:
**character-sheet organizational labels.** They are not dice
mechanics; they are the schema the rulebook uses to *categorize a
character* — the named compartments a personality or history is filed
into on the sheet.

A character has the *belief, the loyalty, the weakness, the history.*
The character does **not** have a thing they experience as "my Ideal,"
"my Bond," "my Flaw," "my Background." Those are the labels the rules
build *around* the character's traits to organize them. When narration
or dialogue names one of those labels — *"your own Ideal," "his Flaw is
pride," "her Hermit background"* — it has crossed from in-fiction prose
into the vocabulary of the character sheet, exactly the way *"3 points
of damage"* crosses into the vocabulary of the dice.

The fix is the same as for every other token: render the *thing itself*
(the belief, the loyalty, the weakness, the history) and drop the
schema label naming its compartment.

These tokens have heavy mundane use, so the disambiguators are strict:
the mechanical signature is **possessive-or-article + the label used as
a category pointing at a known sheet entry.** Bare descriptive uses
pass through untouched.

### Personality scaffolding

```yaml
- token: "Ideal"
  flag_patterns:
    - "possessive + 'ideal' naming a character's stated belief as a
       sheet category ('your ideal', 'his ideal', 'her own ideal',
       'their ideal') when it points at a specific known belief entry"
    - "'the ideal' attached to a just-quoted or referenced belief as
       a categorical label for it ('...worth writing.' / 'Your ideal.')"
  rewrite_hint: "render the belief itself, not its compartment — 'the
    line you would have written for yourself,' 'what you keep coming
    back to,' 'the thing you actually believe about the work,' 'your
    own conviction, in your own hand'"

- token: "Bond"
  flag_patterns:
    - "possessive + 'bond' naming a character's defining loyalty as a
       sheet category ('your bond', 'his bond', 'her bond') pointing at
       a specific known relationship/loyalty entry"
    - "'the bond' used as the categorical label for a just-named
       loyalty rather than for an emotional tie in the ordinary sense"
  rewrite_hint: "render the loyalty itself — 'the people you'd run back
    into a fire for,' 'the place you'd answer if it called,' 'who you
    are loyal to' — not the sheet category"

- token: "Flaw"
  flag_patterns:
    - "possessive + 'flaw' naming a character's defining weakness as a
       sheet category ('your flaw', 'his flaw is pride', 'her flaw')
       pointing at a specific known weakness entry"
    - "'the flaw' used as the categorical label for a just-named
       character weakness rather than an imperfection in an object"
  rewrite_hint: "render the weakness itself — 'the thing in you that
    flinches from the gift you actually have,' 'where you reliably go
    wrong' — not the sheet category"

- token: "Trait"
  flag_patterns:
    - "possessive + 'trait' naming a character's personality entry as a
       sheet category ('your trait', 'his personality trait', 'one of
       her traits') pointing at a specific known sheet entry"
    - "'the trait' used as the categorical label for a just-named
       behavior pattern rather than 'trait' in the ordinary sense"
  rewrite_hint: "render the behavior itself — 'the way you offer the bad
    poem freely,' 'how you find the one person in a room who needs a
    word' — not the sheet category"
```

Mundane use that should pass: *"an ideal partner,"* *"ideal
conditions,"* *"a bond of trust between them,"* *"a bond of debt,"* *"a
flaw in the glass,"* *"the plan had one fatal flaw,"* *"a trait she'd
inherited from her mother,"* *"generosity was his defining trait."*
The flag fires only when the word is the **sheet-category label for a
specific known entry**, not when it is the ordinary English noun.

### Character-sheet schema

```yaml
- token: "Background"
  flag_patterns:
    - "the 5e background-feature name used as a categorical label —
       capitalized background name + 'background' ('his Hermit
       background', 'her Acolyte background', 'your Sage background',
       'their Criminal background')"
    - "'the background' used to name the sheet slot that grants
       proficiencies/feature rather than a person's history in the
       ordinary sense"
  rewrite_hint: "render the history itself — 'the years he spent alone
    on the fog hill,' 'the enclave that taught her the old songs' — not
    the sheet's background slot or its proper-noun label"
```

Mundane use that should pass: *"background music,"* *"his background in
calligraphy,"* *"she faded into the background,"* *"a background of
mountains behind the keep,"* *"checked his background before hiring."*
The flag fires only on the **5e proper-noun background-name used as a
sheet category** (Hermit, Acolyte, Sage, Criminal, Soldier, etc., in
their mechanical sense), not on the ordinary noun.

*(Class, Race, Subclass, and Alignment are also character-schema labels
and can be added here in the same form if they ever surface as actual
narration leaks. Background is listed now because it is the
schema label most likely to be reached for in descriptive prose. The
section is open to extension.)*

---

## How to handle a flagged occurrence

When a `flag_pattern` matches:

1. **Identify the fact the mechanical token is conveying.** The
   token is the mechanical surface; underneath is a fiction fact
   (the character is hurt, the spell ran out, the resistance held).
2. **Render the fact in-fiction** using the entry's `rewrite_hint`
   as a starting direction. The rewrite is genre-aware prose, not
   mechanical translation.
3. **If the mechanical fact genuinely belongs in the
   meta-channel** (a check the player needs to know fired, a roll
   the table needs to see), surface it via the skill-aside marker
   (`*[Persuasion check]*`) or the dice-line norms in
   [`{{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/combat.md`]({{PLUGIN_ROOT}}/engines/rpg-5e-engine/rules/combat.md) — not in dialogue or narration.

The mechanical fact may still be true. The line is wrong because
the rules-layer vocabulary surfaced where the fiction should have
stood on its own.

---

## Extending this list

This vocabulary is the engine's starting set. A consuming game's
override may add further tokens (setting-specific terms the
campaign treats as mechanical, house-rule subsystems, named
mechanics) by declaring additional entries in the same schema. The
override extends this list; it does not run a separate later pass.

Tokens added by the consuming game should follow the same shape:
`token`, `flag_patterns` that disambiguate mechanical from mundane
use, and a `rewrite_hint` for the in-fiction reframing.
