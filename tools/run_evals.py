#!/usr/bin/env python3
"""Generate and score STG-DE Agent Skill evaluation outputs.

Score existing outputs (one file per case, named <case-id>.md):

    python tools/run_evals.py --outputs evals/reference

Generate outputs with any CLI that reads a prompt on stdin and prints the answer,
then score them:

    python tools/run_evals.py --outputs runs/claude --command "claude -p"
    python tools/run_evals.py --outputs runs/codex --command "codex exec -"

All checks are deterministic. They measure rule compliance (linter), preservation
of protected content (stg_compare.py), required facts, output discipline, and audit
accuracy. They do not replace a human review of meaning.
"""
from __future__ import annotations

import argparse
import json
import re
import shlex
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from stg_compare import compare  # noqa: E402
from stg_lint import audit_text  # noqa: E402

PREAMBLE_RE = re.compile(r"^\s*(hier ist|hier sind|gerne|natürlich|klar|sure|here is|here's|okay|ok,)", re.I)
RESULT_RE = re.compile(r"Ergebnis:\s*(PASS WITH REVIEW|PASS|FAIL)")


def prompt_for(case: dict) -> str:
    profile = case.get("profile")
    head = "Verwende STG-DE (Simplified Technical German)"
    if profile:
        head += f" mit dem Profil `{profile}`"
    if case["operation"] == "WRITE":
        return f"{head}.\n\n{case['input']}\n"
    if case["operation"] == "AUDIT":
        return f"{head}. Prüfe diesen Text (AUDIT) und nenne die Regel-IDs:\n\n{case['input']}\n"
    return f"{head}. Schreibe diesen Text in STG-DE um (REWRITE):\n\n{case['input']}\n"


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def score_case(case: dict, output: str) -> dict:
    checks: dict[str, bool] = {}
    details: dict[str, object] = {}
    op = case["operation"]

    for needle in case.get("must_contain", []):
        checks[f"contains {needle}"] = needle in output
    for needle in case.get("must_not_contain", []):
        checks[f"avoids {needle.strip()}"] = needle.casefold() not in f" {output.casefold()} "

    if op in {"WRITE", "REWRITE"}:
        checks["no preamble"] = not PREAMBLE_RE.match(output)
        text = "\n".join(line for line in output.splitlines() if not line.startswith("Hinweis:"))
        lint = audit_text(text, ROOT, profile=case.get("profile"))
        allowed = set(case.get("allow_rules", []))
        errors = [f for f in lint["findings"] if f["severity"] == "error" and f["rule"] not in allowed]
        details["lint_errors"] = [f"{f['rule']}: {f['original'][:60]}" for f in errors]
        checks["no deterministic lint errors"] = not errors
        if case.get("expect_note"):
            checks["Hinweis line present"] = bool(re.search(r"^Hinweis:", output, re.M))
        if case.get("expect_unchanged"):
            checks["compliant input unchanged"] = normalize(output) == normalize(case["input"])

    if op == "REWRITE":
        fidelity = compare(case["input"], output)
        details["fidelity"] = fidelity["result"]
        details["fidelity_findings"] = [f"{f['severity']} {f['check']}" for f in fidelity["findings"]]
        checks["no lost protected content"] = fidelity["result"] != "FAIL"

    if op == "AUDIT":
        for rule in case.get("expected_rules", []):
            checks[f"names {rule}"] = rule in output
        match = RESULT_RE.search(output)
        details["audit_result"] = match.group(1) if match else None
        checks[f"result {case['expected_result']}"] = bool(match) and match.group(1) == case["expected_result"]

    passed = sum(checks.values())
    return {"id": case["id"], "operation": op, "passed": passed, "total": len(checks),
            "ok": passed == len(checks), "checks": checks, "details": details}


def generate(cases: list[dict], out_dir: Path, command: str, timeout: int) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for case in cases:
        target = out_dir / f"{case['id']}.md"
        if target.exists():
            continue
        cp = subprocess.run(shlex.split(command), input=prompt_for(case), text=True, capture_output=True, timeout=timeout)
        if cp.returncode:
            print(f"{case['id']}: command failed ({cp.returncode}): {cp.stderr.strip()[:200]}", file=sys.stderr)
            continue
        target.write_text(cp.stdout.strip() + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate and score STG-DE skill evaluation outputs")
    ap.add_argument("--cases", default=str(ROOT / "evals" / "cases.yaml"))
    ap.add_argument("--outputs", required=True, help="Directory with <case-id>.md outputs")
    ap.add_argument("--command", help="Generate missing outputs with this CLI (prompt on stdin)")
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--format", choices=["text", "json"], default="text")
    ap.add_argument("--min-score", type=float, default=0.0, help="Exit 1 below this share of passed checks (0-1)")
    args = ap.parse_args()

    cases = yaml.safe_load(Path(args.cases).read_text(encoding="utf-8"))["cases"]
    out_dir = Path(args.outputs)
    if args.command:
        generate(cases, out_dir, args.command, args.timeout)

    results = []
    for case in cases:
        path = out_dir / f"{case['id']}.md"
        if not path.exists():
            results.append({"id": case["id"], "operation": case["operation"], "passed": 0, "total": 1,
                            "ok": False, "checks": {"output exists": False}, "details": {}})
            continue
        results.append(score_case(case, path.read_text(encoding="utf-8")))

    passed = sum(r["passed"] for r in results)
    total = sum(r["total"] for r in results)
    score = passed / total if total else 0.0
    summary = {"cases": len(results), "cases_ok": sum(r["ok"] for r in results),
               "checks_passed": passed, "checks_total": total, "score": round(score, 3)}

    if args.format == "json":
        print(json.dumps({"summary": summary, "results": results}, ensure_ascii=False, indent=2))
    else:
        for r in results:
            mark = "OK  " if r["ok"] else "FAIL"
            print(f"{mark} {r['id']:<34} {r['passed']}/{r['total']}")
            for name, ok in r["checks"].items():
                if not ok:
                    print(f"     - {name}")
            for key in ("lint_errors", "fidelity_findings"):
                if r["details"].get(key) and not r["ok"]:
                    print(f"     {key}: {r['details'][key]}")
        print(f"\nScore: {passed}/{total} checks ({score:.1%}), {summary['cases_ok']}/{summary['cases']} cases fully passed")
    return 1 if score < args.min_score else 0


if __name__ == "__main__":
    raise SystemExit(main())
