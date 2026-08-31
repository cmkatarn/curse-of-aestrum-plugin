"""Deterministic post-generation lint — the non-probabilistic half of the gate.

The model's own "single gate" (prompt-driven self-review) shares the drafter's
blind spots, so closed-vocabulary leaks slip through. This package catches the
*mechanizable* subset — fixed tokens that are a leak on sight (HP, d20, cantrip,
project-internal time indices) — with a deterministic scan that runs in the
runtime BEFORE a beat reaches the player. No model judgment, no blind spots,
regression-testable.

Token lists are authored as structured sidecars (TOML) owned per engine/consumer
tier; the runtime merges and enforces them. See runtime/lint/spec.py for the
schema and runtime/lint/engine.py for the matcher + re-prompt contract.
"""

from runtime.lint.engine import LintEngine, LintResult, Violation
from runtime.lint.spec import TokenSpec, load_specs

__all__ = ["LintEngine", "LintResult", "Violation", "TokenSpec", "load_specs"]
