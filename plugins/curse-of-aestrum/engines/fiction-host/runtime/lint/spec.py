"""Token-spec schema and loader for the deterministic lint.

Each engine/consumer tier ships a sidecar TOML file holding its closed-vocabulary
forbidden tokens. The runtime reads them (read-only), merges across tiers, and
enforces them. TOML (not YAML) keeps the deterministic core stdlib-only, matching
the rest of fiction-host's config and `requirements.txt`'s no-third-party-dep
invariant.

Sidecar schema (v1):

    version = 1

    [[tokens]]
    token = "HP"
    match = "exact"          # "exact" = substring | "word" = word-boundary.
                             # "pattern" is reserved for v2 (context regex) and is
                             # skipped by the v1 loader.
    case_sensitive = true
    surfaces = ["narration", "dialogue"]   # forbidden surfaces (informational in v1;
                                           # all non-OOC text is treated as fiction)
    rewrite_hint = "reframe as wounds / exhaustion — sensory, not numeric"
    enabled = true           # optional; default true. Set false to park a v2 entry.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

if sys.version_info >= (3, 11):
    import tomllib
else:  # pragma: no cover
    import tomli as tomllib  # type: ignore

# Match modes the v1 deterministic matcher understands. "pattern" entries are
# valid in a sidecar (parked for v2) but are not loaded here.
V1_MATCH_MODES = {"exact", "word"}


@dataclass(frozen=True)
class TokenSpec:
    token: str
    match: str               # "exact" | "word"
    case_sensitive: bool
    surfaces: tuple[str, ...]
    rewrite_hint: str
    source: str              # sidecar filename, for diagnostics


def load_specs(paths: list[Path]) -> list[TokenSpec]:
    """Load and merge token specs from the given sidecar paths.

    Missing files are skipped (a tier may simply ship none). Entries with
    `enabled = false` or a non-v1 `match` mode are skipped, so a sidecar can
    carry parked v2 (pattern) entries without affecting v1 enforcement.
    """
    specs: list[TokenSpec] = []
    for path in paths:
        if not path.exists():
            continue
        with path.open("rb") as fh:
            data = tomllib.load(fh)
        for entry in data.get("tokens", []):
            if not entry.get("enabled", True):
                continue
            mode = entry.get("match", "exact")
            if mode not in V1_MATCH_MODES:
                continue
            token = entry.get("token")
            if not token:
                continue
            specs.append(
                TokenSpec(
                    token=token,
                    match=mode,
                    case_sensitive=bool(entry.get("case_sensitive", False)),
                    surfaces=tuple(entry.get("surfaces", ["narration", "dialogue"])),
                    rewrite_hint=entry.get("rewrite_hint", ""),
                    source=path.name,
                )
            )
    return specs
