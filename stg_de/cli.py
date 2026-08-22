from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import __version__
from . import stg_analyze, stg_lint

PACKAGE_ROOT = Path(__file__).resolve().parent
TEXT_SUFFIXES = {".md", ".txt", ".rst", ".adoc"}


def expand_inputs(values: list[str]) -> list[Path | None]:
    expanded: list[Path | None] = []
    for value in values:
        if value == "-":
            expanded.append(None)
            continue
        path = Path(value)
        if path.is_dir():
            expanded.extend(
                candidate for candidate in sorted(path.rglob("*"))
                if candidate.is_file() and candidate.suffix.casefold() in TEXT_SUFFIXES
            )
        else:
            expanded.append(path)
    return expanded


def read_input(path: Path | None) -> tuple[str, str]:
    if path is None:
        return "<stdin>", sys.stdin.read()
    return str(path), path.read_text(encoding="utf-8")


def command_lint(args: argparse.Namespace) -> int:
    project = stg_lint.load_yaml(Path(args.project)) if args.project else {}
    results = []
    exit_code = 0
    for path in expand_inputs(args.inputs):
        name, text = read_input(path)
        result = stg_lint.audit_text(
            text,
            PACKAGE_ROOT,
            args.text_type,
            project,
            args.lexicon_report,
            args.profile,
        )
        result["input"] = name
        results.append(result)
        if args.fail_on_error and result["counts"].get("error", 0):
            exit_code = 1

    if args.format == "json":
        payload = results[0] if len(results) == 1 else {"tool": "stg lint", "results": results}
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for index, result in enumerate(results):
            if len(results) > 1:
                if index:
                    print()
                print(f"== {result['input']} ==")
            print(stg_lint.render_text(result))
    return exit_code


def command_analyze(args: argparse.Namespace) -> int:
    results = []
    for path in expand_inputs(args.inputs):
        name, text = read_input(path)
        result = stg_analyze.analyze(text)
        result["input"] = name
        results.append(result)
    if args.format == "json":
        payload = results[0] if len(results) == 1 else {"tool": "stg analyze", "results": results}
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for index, result in enumerate(results):
            if len(results) > 1:
                if index:
                    print()
                print(f"== {result['input']} ==")
            print(stg_analyze.render(result))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="stg", description="STG-DE controlled-language tools")
    parser.add_argument("--version", action="version", version=f"stg-de {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    lint = sub.add_parser("lint", help="Run deterministic STG-DE checks")
    lint.add_argument("inputs", nargs="+", help="UTF-8 files, directories, or - for stdin")
    lint.add_argument("--project", help="Optional .stg-de.yaml project terminology")
    lint.add_argument("--profile", choices=["procedure", "safety", "description", "requirement", "support", "consumer", "agent"])
    lint.add_argument("--text-type", choices=["auto", "procedure", "description"], default="auto")
    lint.add_argument("--format", choices=["text", "json"], default="text")
    lint.add_argument("--lexicon-report", action="store_true")
    lint.add_argument("--fail-on-error", action="store_true")
    lint.set_defaults(func=command_lint)

    analyze = sub.add_parser("analyze", help="Run review-only German-language analysis")
    analyze.add_argument("inputs", nargs="+", help="UTF-8 files, directories, or - for stdin")
    analyze.add_argument("--format", choices=["text", "json"], default="text")
    analyze.set_defaults(func=command_analyze)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
