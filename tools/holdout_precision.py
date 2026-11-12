#!/usr/bin/env python3
"""Measure linter precision on the holdout partition of the public corpus.

Two steps keep third-party text out of the repository:

1. `sample` downloads the holdout sources, runs the linter, and writes a labeling sheet
   with text excerpts to a directory OUTSIDE the repository. A fixed seed selects the
   findings. Each finding has an ID: the SHA-256 of source ID, rule, and sentence.
2. `score` reads the completed sheet and writes only aggregate counts and the finding IDs
   with their labels to `corpus/holdout-precision.yaml`.

Labels:
  tp          the finding is a real violation of the rule
  fp          the linter is wrong
  extraction  the finding comes from PDF/HTML extraction (merged lines, page headers)
  fn          (negative sample only) the sentence violates an implemented check that
              the linter did not report
  ok          (negative sample only) no missed violation
  skip        exclude the item from all counts (for example a sampling error)

The sheet records the source IDs, their SHA-256 hashes, and the linter version. Web pages
change, so a later `sample` run can select other sentences. Keep the sheet of a measurement
outside the repository if a person must review it later. `--prefill` copies the labels of a
published report into the sheet as `model_label` for such a review.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import random
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from build_corpus import download, extract_text, package_version  # noqa: E402
from stg_lint import audit_text  # noqa: E402
from stg_markdown import prose_blocks  # noqa: E402
from stg_lint import split_sentences  # noqa: E402

SEED = 20261112
OUTPUT = ROOT / "corpus" / "holdout-precision.yaml"


def finding_id(source_id: str, rule: str, text: str) -> str:
    return hashlib.sha256(f"{source_id}\0{rule}\0{text}".encode("utf-8")).hexdigest()[:16]


def holdout_sources(ids: list[str] | None = None) -> list[dict]:
    data = yaml.safe_load((ROOT / "corpus" / "fulltext-sources.yaml").read_text(encoding="utf-8"))
    if ids:
        by_id = {s["id"]: s for s in data["sources"]}
        missing = [i for i in ids if i not in by_id]
        if missing:
            raise SystemExit(f"unknown source IDs: {', '.join(missing)}")
        return [by_id[i] for i in ids]
    return [s for s in data["sources"] if s["partition"] == "holdout"]


def flagged(text: str) -> bool:
    """True when the linter reports an error or warning for this text alone."""
    return any(f["severity"] in {"error", "warning"} for f in audit_text(text, ROOT, profile="description")["findings"])


def sample(out_dir: Path, per_source: int, negatives: int, ids: list[str] | None = None,
           prefill: Path | None = None) -> None:
    rng = random.Random(SEED)
    sheet = {"seed": SEED, "linter": package_version(), "sources": [], "positives": [], "negatives": []}
    for source in holdout_sources(ids):
        data, content_type = download(source["url"])
        sheet["sources"].append({"id": source["id"], "sha256": hashlib.sha256(data).hexdigest()})
        text = extract_text(data, source.get("type", ""), content_type)
        result = audit_text(text, ROOT, profile="description")
        findings = [f for f in result["findings"] if f["severity"] in {"error", "warning"}]
        rng.shuffle(findings)
        for f in findings[:per_source]:
            excerpt = f["original"][:400]
            sheet["positives"].append({
                "id": finding_id(source["id"], f["rule"], f["original"]),
                "source": source["id"], "rule": f["rule"], "severity": f["severity"],
                "term": f.get("term"), "excerpt": excerpt, "label": None, "note": None,
            })
        # A finding can name only the first sentence with a term. Check each candidate
        # sentence on its own, so that no sentence with a reported term counts as clean.
        candidates = [s for b in prose_blocks(text) for s in split_sentences(b) if len(s.split()) >= 4]
        clean = [s for s in dict.fromkeys(candidates) if not flagged(s)]
        rng.shuffle(clean)
        for sentence in clean[:negatives]:
            sheet["negatives"].append({
                "id": finding_id(source["id"], "NONE", sentence), "source": source["id"],
                "excerpt": sentence[:400], "label": None, "note": None,
            })
        print(f"{source['id']}: {len(findings)} findings, sampled {min(per_source, len(findings))}")
    if prefill:
        report = yaml.safe_load(prefill.read_text(encoding="utf-8"))
        labels = {x["id"]: x["label"] for x in report.get("labels", [])}
        for item in sheet["positives"] + sheet["negatives"]:
            item["model_label"] = labels.get(item["id"])
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "holdout-labels.yaml"
    target.write_text(yaml.safe_dump(sheet, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
    print(target)


def score(sheet_path: Path, labeler: str) -> None:
    sheet = yaml.safe_load(sheet_path.read_text(encoding="utf-8"))
    unlabeled = [x["id"] for x in sheet["positives"] + sheet["negatives"] if not x.get("label")]
    if unlabeled:
        raise SystemExit(f"{len(unlabeled)} items have no label")
    sheet["positives"] = [x for x in sheet["positives"] if x["label"] != "skip"]
    sheet["negatives"] = [x for x in sheet["negatives"] if x["label"] != "skip"]
    per_rule: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    for item in sheet["positives"]:
        per_rule[item["rule"]][item["label"]] += 1
    rules = {}
    for rule, counts in sorted(per_rule.items()):
        judged = counts["tp"] + counts["fp"]
        rules[rule] = {
            "sampled": sum(counts.values()), "tp": counts["tp"], "fp": counts["fp"],
            "extraction": counts["extraction"],
            "precision_excluding_extraction": round(counts["tp"] / judged, 3) if judged else None,
        }
    total = collections.Counter(item["label"] for item in sheet["positives"])
    neg = collections.Counter(item["label"] for item in sheet["negatives"])
    judged = total["tp"] + total["fp"]
    report = {
        "schema_version": "0.3",
        "method": ("Fixed-seed sample of linter findings (severity error/warning, profile description) on the "
                   "holdout partition; full text downloaded transiently, never stored in the repository."),
        "seed": sheet["seed"],
        "labeler": labeler,
        "linter": sheet.get("linter"),
        "sources": [s["id"] if isinstance(s, dict) else s for s in sheet.get("sources", [])]
        or [s["id"] for s in holdout_sources()],
        "positives": {
            "sampled": sum(total.values()), "tp": total["tp"], "fp": total["fp"], "extraction": total["extraction"],
            "precision_excluding_extraction": round(total["tp"] / judged, 3) if judged else None,
            "precision_including_extraction": round(total["tp"] / sum(total.values()), 3) if total else None,
        },
        "negatives": {"sampled": sum(neg.values()), "missed_violation": neg["fn"], "ok": neg["ok"]},
        "rules": rules,
        "labels": [{"id": x["id"], "rule": x["rule"], "label": x["label"]} for x in sheet["positives"]]
        + [{"id": x["id"], "rule": "NONE", "label": x["label"]} for x in sheet["negatives"]],
    }
    OUTPUT.write_text(yaml.safe_dump(report, allow_unicode=True, sort_keys=False), encoding="utf-8")
    print(OUTPUT)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="command", required=True)
    s = sub.add_parser("sample")
    s.add_argument("--out", required=True, help="Directory OUTSIDE the repository for the labeling sheet")
    s.add_argument("--per-source", type=int, default=50)
    s.add_argument("--negatives", type=int, default=15)
    s.add_argument("--sources", nargs="+", help="Source IDs instead of the current holdout partition")
    s.add_argument("--prefill", type=Path, help="Published report; copy its labels into the sheet as model_label")
    c = sub.add_parser("score")
    c.add_argument("sheet")
    c.add_argument("--labeler", required=True)
    args = ap.parse_args()
    if args.command == "sample":
        out = Path(args.out).resolve()
        if ROOT in out.parents or out == ROOT:
            ap.error("--out must be outside the repository (third-party text)")
        sample(out, args.per_source, args.negatives, args.sources, args.prefill)
    else:
        score(Path(args.sheet), args.labeler)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
