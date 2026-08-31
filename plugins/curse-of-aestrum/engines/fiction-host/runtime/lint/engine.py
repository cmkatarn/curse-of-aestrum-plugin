"""The deterministic matcher + re-prompt contract.

`LintEngine.validate(text)` strips sanctioned OOC/meta spans, then scans the
remaining (in-fiction) prose for each forbidden token. On a hit the caller
(runtime.engine) re-prompts the model to regenerate the beat; see
`correction_prompt`. Pure and deterministic — no model calls, no I/O beyond the
one-time spec load.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional

from runtime.lint.spec import TokenSpec, load_specs

if TYPE_CHECKING:  # avoid an import cycle at runtime
    from runtime.config import LintConfig

# OOC / meta spans are NEVER scanned: they are the sanctioned surfaces where
# mechanical vocabulary may legitimately appear (skill-aside / mechanics-readout,
# admin OOC, player-scoped OOC). Stripped before the fiction scan so a `d20`
# inside `*[Attack — d20 ...]*` does not fire.
_OOC_SPANS = (
    re.compile(r"\*\[.*?\]\*", re.DOTALL),        # *[Persuasion check]* / mechanics-readout
    re.compile(r"<<.*?>>", re.DOTALL),            # <<admin OOC>>
    re.compile(r"<[^<>\n][^>\n]*>", re.DOTALL),   # <player-scoped OOC> (conservative)
)


@dataclass
class Violation:
    token: str
    rewrite_hint: str
    excerpt: str


@dataclass
class LintResult:
    violations: list[Violation] = field(default_factory=list)

    @property
    def is_clean(self) -> bool:
        return not self.violations


class LintEngine:
    def __init__(
        self,
        specs: list[TokenSpec],
        *,
        enabled: bool = True,
        max_retries: int = 2,
        on_exhausted: str = "warn",
    ):
        self.specs = list(specs)
        # A lint with no specs is effectively disabled (nothing to scan for).
        self.enabled = bool(enabled) and bool(self.specs)
        self.max_retries = int(max_retries)
        self.on_exhausted = on_exhausted if on_exhausted in ("warn", "fail") else "warn"
        self._matchers: list[tuple[TokenSpec, re.Pattern]] = [
            (s, self._compile(s)) for s in self.specs
        ]

    @classmethod
    def from_config(cls, lint: "Optional[LintConfig]") -> "LintEngine":
        if lint is None or not lint.enabled:
            return cls([], enabled=False)
        return cls(
            load_specs(lint.spec_paths),
            enabled=True,
            max_retries=lint.max_retries,
            on_exhausted=lint.on_exhausted,
        )

    # -- matching ---------------------------------------------------------- #

    @staticmethod
    def _compile(spec: TokenSpec) -> re.Pattern:
        flags = 0 if spec.case_sensitive else re.IGNORECASE
        if spec.match == "word":
            # Word-boundary on both sides. Use lookarounds (not \b) so multi-word
            # tokens like "Aestrum Day" and "natural 20" behave.
            return re.compile(rf"(?<!\w){re.escape(spec.token)}(?!\w)", flags)
        # "exact" = substring. Used for dice notation (so "1d20" is caught even
        # though a digit precedes the token).
        return re.compile(re.escape(spec.token), flags)

    @staticmethod
    def _strip_ooc(text: str) -> str:
        for rx in _OOC_SPANS:
            text = rx.sub(" ", text)
        return text

    def validate(self, text: str) -> LintResult:
        result = LintResult()
        if not self.enabled or not text:
            return result
        scan = self._strip_ooc(text)
        for spec, rx in self._matchers:
            m = rx.search(scan)
            if m:
                result.violations.append(
                    Violation(
                        token=spec.token,
                        rewrite_hint=spec.rewrite_hint,
                        excerpt=_excerpt(scan, m.start(), m.end()),
                    )
                )
        return result

    # -- caller-facing messages ------------------------------------------- #

    def summary(self, result: LintResult) -> str:
        toks = ", ".join(sorted({v.token for v in result.violations}))
        return f"forbidden token(s): {toks}"

    def correction_prompt(self, result: LintResult) -> str:
        lines = [
            "[host lint — out-of-character; do not acknowledge this in-fiction]",
            "Your immediately preceding beat used out-of-fiction mechanical "
            "vocabulary that must never appear in narration or dialogue. Reproduce "
            "that beat exactly, with ONLY the forbidden token(s) below replaced per "
            "their hints — keep every other word and in-fiction detail identical.",
            "",
            "Forbidden tokens:",
        ]
        for v in result.violations:
            hint = f" — {v.rewrite_hint}" if v.rewrite_hint else ""
            lines.append(f'  - "{v.token}"{hint}')
        return "\n".join(lines)

    def failure_message(self, result: LintResult) -> str:
        toks = ", ".join(sorted({v.token for v in result.violations}))
        return (
            f"[host lint blocked this beat: forbidden token(s) {toks} could not be "
            f"removed after {self.max_retries} attempt(s)]"
        )


def _excerpt(text: str, start: int, end: int, pad: int = 24) -> str:
    a = max(0, start - pad)
    b = min(len(text), end + pad)
    return ("…" if a > 0 else "") + text[a:b].strip() + ("…" if b < len(text) else "")
