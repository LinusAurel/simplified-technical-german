"""Command-line interface `stg` for STG-DE.

The subcommands run the canonical tools from `tools/`, copied into this package by
`tools/sync_package.py`. The package contains no second implementation.
"""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

from . import __version__

PACKAGE_ROOT = Path(__file__).resolve().parent
COMMANDS = {
    "lint": ("stg_lint", "Deterministische STG-DE-Prüfung (Linter)"),
    "analyze": ("stg_analyze", "Heuristische Belege für die Prüfung (Analysewerkzeug)"),
    "compare": ("stg_compare", "Bedeutungsprüfung: Original und Umschreibung vergleichen"),
}
USAGE = "usage: stg {lint,analyze,compare} ... | stg --version\n\n" + "\n".join(
    f"  {name:<8} {description}" for name, (_, description) in COMMANDS.items()
)


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in {"-h", "--help"}:
        print(USAGE)
        return 0
    if args[0] == "--version":
        print(f"stg-de {__version__}")
        return 0
    command = args.pop(0)
    if command not in COMMANDS:
        print(f"stg: unknown command '{command}'\n\n{USAGE}", file=sys.stderr)
        return 2
    module = importlib.import_module(f"stg_de.{COMMANDS[command][0]}")
    if command == "lint" and not any(a == "--root" or a.startswith("--root=") for a in args):
        args = ["--root", str(PACKAGE_ROOT), *args]
    previous = sys.argv
    sys.argv = [f"stg {command}", *args]
    try:
        return module.main()
    finally:
        sys.argv = previous


if __name__ == "__main__":
    raise SystemExit(main())
