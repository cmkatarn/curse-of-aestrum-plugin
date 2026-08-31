# Location Memory — Generic Load Procedure

Reference loaded on demand from `scene/core.md`. Used at
scene start to load the scene's location, and again whenever the
scene moves to a new location mid-scene. Not needed otherwise.

The consuming game's override file supplies path conventions, the
location-tree shape, and any custom-NPC injection rules.

---

Before establishing the scene, load the location. The location file is
the authoritative source for layout, fixtures, ambient conditions, fixed
residents, and what is and isn't plausibly present. **Never improvise a
location's physical layout or contents when a file exists for it.**

## 2.5a. Find the Location File

Glob the override's location tree for files matching the scene's
location keyword. Locations may be flat files or organized into
subdirectories (districts, chapters, regions — whatever the override
documents). Some locations have multiple files — main location plus
sub-areas. Load all that are relevant to where the scene may go.

## 2.5b. Load Base and Overlay

For each relevant location file:

1. `Read` the base file from the canonical location tree.
2. `Read` the overlay at the override-defined location-saved overlay
   path, if it exists. Many locations have no overlay yet — proceed with
   base only in that case.

The overlay records persistent changes the party has made to the location
(items left behind, fixtures broken, structural alterations). Apply
overlay state on top of the base.

3. **Custom NPC injection** *(if the override defines this)*: glob the
   override-defined custom-NPC tree. For each file found, read its
   frontmatter and check the override-specified `home_location`-style
   field. If it matches the current location's filename stem or a value
   in a list, add that NPC to the effective residents list and load them
   via the character-memory procedure as normal. This step is silent —
   do not mention it to the user.

## 2.5c. Use the Location to Constrain the Scene

The loaded location governs:

- **Layout.** Rooms, floors, doors, fixtures, dimensions. Do not invent
  geometry.
- **Fixed residents.** The base file's residents field lists who lives
  or works here. Anyone else being present requires a plausible reason —
  and at isolated, hostile, or specially-restricted sites, "a stranger
  wandered in" is usually *not* plausible. The same constraint applies
  to **off-screen ambient activity** adjacent to the scene (sounds from
  outside, figures in the next room, signs of habitation): do not
  attribute such details to a named NPC — even hedged — unless a
  loaded source places that NPC at this location at scene-time T. See
  the off-screen-presence failure mode in
  [epistemic_discipline.md]({{PLUGIN_ROOT}}/engines/prose-engine/scene/references/epistemic_discipline.md) for the default attributions
  and the source-check on player queries.
- **Special properties.** Any magical, atmospheric, or rule-bending
  conditions defined in the file (game-specific — the override may add
  categories).
- **What's in the rooms.** Items, decorations, marks, hidden details —
  work from the file, not improvisation. If the file is silent on a
  detail the player asks about, you can extrapolate carefully, but flag
  in your own working memory that you extrapolated.
  - **Written artifacts carry their language / script.** For signage,
    inscriptions, books, letters, or any in-location text, note the
    language or script it is written in (from the file, or extrapolated
    and flagged). This is what lets the language-comprehension check
    gate a character "reading" text in a script they do not have — a
    character with the wrong literacy sees marks, not meaning.

## 2.5d. Reloading on Scene Change

**If the scene moves to a new location mid-scene, load that
location's files before describing it.** Stop, glob for the new location
file, read it (base + overlay), and only then continue narration. This
applies to traveling between sub-areas of a site only if those sub-areas
have their own files. It always applies to crossing to a different
documented location.

If the user takes the scene somewhere with no documented file, you may
improvise — but tell the user first so they can either create the file or
accept the improvisation.
