"""Minimal integrity-checker CLI for the vendored (plugin) fiction-host runtime.

The full fiction-host `__main__` dispatches the whole host — engine, backends,
config, spec-drift — and pulls that entire import chain in with it. A plugin
install needs none of that: it ships the *checkers* so authored content can be
validated in place, not the runtime that replaces the harness.

So this entrypoint deliberately exposes only the two config-driven checks:

    py -m runtime refcheck    --config <path>/refcheck.toml
    py -m runtime entitycheck --config <path>/entitycheck.toml

`--config` is REQUIRED here. Upstream both commands fall back to `load_host()`
to discover the config from the active game — that fallback is what drags in
`runtime.config` and the rest of the host, and it has no meaning inside a
plugin, where the config path is known and passed explicitly by the skill.

`runtime.refcheck` and `runtime.entitycheck` are stdlib-only, so this file plus
those two modules (and `lint/`, used by the Stop hooks) is the whole vendored
surface. Report wording is kept identical to upstream `__main__.py` so output
matches between a plugin install and the source workspace.

Run it with this file's parent on sys.path, e.g. from `engines/fiction-host/`:

    cd <plugin>/engines/fiction-host && py -m runtime refcheck --config <plugin>/refcheck.toml
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def cmd_refcheck(args) -> int:
    from runtime.refcheck import check, load_config

    report = check(load_config(Path(args.config)))
    if report.clean:
        print(f"references in sync: {report.links} links across {report.files} files resolve.")
        return 0
    print(f"BROKEN REFERENCES: {len(report.issues)} of {report.links} links "
          f"across {report.files} files do not resolve:")
    for i in report.issues:
        print(f"  - {i.file}:{i.line}  [{i.reason}]  {i.target}")
    print("Fix the link target (file path or #anchor), or declare an intentional "
          "soft pointer under [scan].ignore_targets.")
    return 1


def cmd_entitycheck(args) -> int:
    from runtime.entitycheck import check, load_config

    cfg_path = Path(args.config)
    if not cfg_path.exists():
        print(f"no entitycheck.toml at {cfg_path} — nothing to check.")
        return 0
    report = check(load_config(cfg_path))
    if report.clean:
        print(f"entity graph in sync: {report.entities} entities, {report.refs} "
              f"references across {report.files} files resolve.")
        return 0
    print(f"ENTITY GRAPH: {len(report.issues)} issue(s) across {report.entities} "
          f"entities ({report.refs} references, {report.files} files):")
    for i in report.issues:
        where = f"{i.file}:{i.line}" if i.line else i.file
        print(f"  - {where}  [{i.reason}]  {i.detail}")
    print("Fix the entity, or declare an intentional soft pointer under "
          "[bindings].soft_ids.")
    return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="runtime",
        description="Integrity checkers for the vendored plugin runtime.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_ref = sub.add_parser("refcheck", help="check cross-reference integrity")
    p_ref.add_argument("--config", required=True, help="path to refcheck.toml")
    p_ref.set_defaults(func=cmd_refcheck)

    p_ent = sub.add_parser("entitycheck", help="check entity-graph integrity")
    p_ent.add_argument("--config", required=True, help="path to entitycheck.toml")
    p_ent.set_defaults(func=cmd_entitycheck)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
