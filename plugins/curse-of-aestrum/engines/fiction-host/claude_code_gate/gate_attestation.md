# Gate attestation — protocol for Claude Code play

When a scene is run inside Claude Code (rather than the standalone runtime), the
single gate (the drafting engine's epistemic-discipline + stylistic-variance
suites) is executed by you, the model. This protocol makes that execution
**observable and enforceable**: a deterministic Stop hook verifies every beat
carries an attestation and re-runs the closed-vocabulary token scan. A message
that fails either check is rejected and you must redraft — the hook never edits
your text.

## The dash-marker attestation

After drafting each beat, run **both** gate suites exactly as the engine core
requires (one pass, two suites, shared rewrite loop). Then end the message with
the attestation as a **dash marker on its own line, preceded by a blank line**,
as the last non-empty line of the message.

The marker has three positional `--` separators and two optional slots — the
epistemic suite's count first, the stylistic suite's count second:

```
--<E slot>--<S slot>--
```

Each slot is empty when that suite came up clean during drafting, or
`<count>(<row list>)` when findings fired and were resolved before posting.
The row list — `r3`, `r3,r13`, etc. — is **mandatory whenever the count is
nonzero**.

| Case | Form | How it renders |
|---|---|---|
| Both suites clean | `------` | Markdown `<hr>` — looks like an end-of-section break |
| Epistemic findings only | `--2(r3,r13)----` | Plain text (digits disqualify `<hr>`) |
| Stylistic findings only | `----1(r1)--` | Plain text |
| Both fired | `--2(r3)--1(r1)--` | Plain text |
| OOC turn | `--ooc--` | Plain text |

The clean form is the overwhelmingly common case; it hides as a horizontal
rule in the rendered view. The dirty forms are short, deliberately visible
signals that something was caught and resolved during drafting.

### The blank-line invariant

The line immediately above the marker **must be blank**. In CommonMark, a
sequence of `-` characters directly under a paragraph is interpreted as a
setext heading underline — `------` after a prose line turns that paragraph
into an `<h2>`. The blank line is what makes the marker a thematic break
instead of a heading. The Stop hook enforces this; a marker without a blank
line above it is rejected.

```
The last line of the beat lands here.
                                          ← this blank line is required
------
```

### OOC turns

Non-fiction turns during a scene session — setup questions, save
confirmations, player-requested mechanics clarifications, authoring asides —
use `--ooc--`. The Stop hook accepts these and skips the closed-vocabulary
token scan (player-requested meta is exempt from infrastructure-citation per
the engine's player-scoped OOC carve-out).

## Rules

1. **Every message during a scene session ends with exactly one marker**, on
   its own line, with a blank line above it, as the last non-empty line.
2. **Counts must reflect the scan you actually ran.** The marker is a record
   of work performed, not a formality. If you did not run the suites, you
   cannot attest — run them.
3. **A nonzero count requires its row list.** A findings-resolved pass is
   never collapsed to the clean form. `--2(r3,r13)----` is correct;
   `--2----` is rejected.
4. **Never reference the marker in prose**, never explain it to the player,
   never include it inside fiction sentences. It is not part of the fiction.
5. **On a hook rejection** (your message was blocked with feedback): treat
   it as a gate finding. Redraft the beat per the feedback — fix only what
   is flagged, keep every other in-fiction detail identical — re-run both
   suites, and re-emit with a fresh marker. Do not display, quote, or
   apologize for the rejected draft; simply emit the corrected beat.
6. The marker rides **on top of** the single gate; it does not replace any
   row, suite, or rewrite-loop behavior, and it adds no pass after the gate —
   the hook only accepts or rejects, and a rejection re-enters your full
   drafting gate.
7. **The gated beat + marker ends the turn — no trailing prose.** The beat's
   action-prompt (its in-register invitation to act) *is* the handoff; control
   has already returned to the player. Any state-writes the turn owes (the
   staging tail, a save flush) trail the marker as **tool calls**; when they
   return, the turn is over. Do **not** emit a further player-facing message
   with a trailing handoff, recap, or "your move" line. Such a line is a fresh
   assistant message that carries **no marker**, and the Stop hook rejects it —
   even though the beat it followed was correct and already handed control. A
   tool-use-only continuation (no player-facing text) is fine; if a post-write
   message with text is genuinely unavoidable, it is OOC and must itself end
   with `--ooc--`. This is the single most common false rejection: the beat was
   never the problem — the stray trailing line was.

## Rationale

The previous form was an HTML comment (`<!-- gate: E# S# -->`) stripped from
the on-screen view by a `MessageDisplay` hook. That made invisibility
renderer-dependent — on some clients the strip did not land and the comment
leaked to the player. The dash marker is renderer-safe by design: clean is a
thematic break in every CommonMark renderer; dirty is small inline text the
player can read as a "caught something" signal. The strip hook has been
retired.
