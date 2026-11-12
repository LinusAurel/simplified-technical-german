#!/usr/bin/env python3
from pathlib import Path
import argparse, collections, csv, hashlib, json, subprocess, sys, yaml

ROOT = Path(__file__).resolve().parents[1]


def release_version() -> str:
    for line in (ROOT / "CITATION.cff").read_text(encoding="utf-8").splitlines():
        if line.startswith("version:"):
            return line.split(":", 1)[1].strip().strip("'\"")
    raise SystemExit("version not found in CITATION.cff")


def fail(msg):
    print("FAIL:", msg, file=sys.stderr)
    raise SystemExit(1)


def main():
    ap = argparse.ArgumentParser(description="Validate STG-DE structured resources and release integrity")
    ap.add_argument(
        "--skip-manifest",
        action="store_true",
        help="Skip immutable release-manifest hash checks for development branches and pull requests.",
    )
    args = ap.parse_args()

    # Parse structured resources.
    for p in ROOT.rglob("*.yaml"):
        try:
            yaml.safe_load(p.read_text(encoding="utf-8"))
        except Exception as e:
            fail(f"YAML parse {p.relative_to(ROOT)}: {e}")
    for p in ROOT.rglob("*.json"):
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            fail(f"JSON parse {p.relative_to(ROOT)}: {e}")

    A = yaml.safe_load((ROOT / "dictionary/approved-words.yaml").read_text(encoding="utf-8"))["entries"]
    P = yaml.safe_load((ROOT / "dictionary/prohibited-words.yaml").read_text(encoding="utf-8"))["entries"]
    if len({e["entry_id"] for e in A}) != len(A):
        fail("duplicate dictionary entry_id")
    mids = [m["id"] for e in A for m in e.get("meanings", [])]
    if len(mids) != len(set(mids)):
        fail("duplicate controlled meaning id")
    app = {e["lemma"].casefold() for e in A}
    pro = {e["term"].casefold() for e in P}
    if app & pro:
        fail(f"approved/prohibited overlap: {sorted(app & pro)}")

    ri = yaml.safe_load((ROOT / "rules/rule-index.yaml").read_text(encoding="utf-8"))["rules"]
    if len(ri) != 75 or len({r["id"] for r in ri}) != 75:
        fail("expected 75 unique rules/recommendations")

    # ASD-STE100 Issue 9 traceability must stay complete.
    mp = yaml.safe_load((ROOT / "mapping/ste100-issue9.yaml").read_text(encoding="utf-8"))
    rule_ids = {r["id"] for r in ri}
    if len({m["ste"] for m in mp["mappings"]}) != 53:
        fail("expected 53 mapped ASD-STE100 Issue 9 writing rules")
    traced = {e["stg"] for e in mp["german_extensions"]}
    for m in mp["mappings"] + mp["general_recommendations"]:
        targets = set(m["stg"]) | set(m.get("related", []))
        if targets - rule_ids:
            fail(f"mapping {m['ste']} references unknown STG rule(s): {sorted(targets - rule_ids)}")
        traced |= targets
    if traced != rule_ids:
        fail(f"STG rules without ASD-STE100 traceability: {sorted(rule_ids - traced)}")

    # Legacy 0.1 sample corpus: declared counts must match the listed sources.
    src = yaml.safe_load((ROOT / "corpus/sources.yaml").read_text(encoding="utf-8"))
    if src.get("source_count") != len(src["sources"]):
        fail(f"corpus/sources.yaml: source_count {src.get('source_count')} != {len(src['sources'])} listed sources")
    inds = collections.Counter(s["industry"] for s in src["sources"])
    if dict(inds) != src.get("industries", {}):
        fail(f"corpus/sources.yaml: industries {src.get('industries')} != counted {dict(inds)}")

    # Full-text corpus: source list and metrics must describe the same sources.
    fsrc = yaml.safe_load((ROOT / "corpus/v0.2-sources.yaml").read_text(encoding="utf-8"))["sources"]
    fmet = yaml.safe_load((ROOT / "corpus/v0.2-fulltext-metrics.yaml").read_text(encoding="utf-8"))
    src_ids = [s["id"] for s in fsrc]
    if len(src_ids) != len(set(src_ids)):
        fail("corpus/v0.2-sources.yaml: duplicate source id")
    met_ids = [s["id"] for s in fmet["sources"]]
    if set(met_ids) != set(src_ids):
        fail(f"corpus source/metrics id mismatch: {sorted(set(src_ids) ^ set(met_ids))}")
    if fmet["aggregate"]["sources"] != len(src_ids):
        fail(f"corpus metrics aggregate.sources {fmet['aggregate']['sources']} != {len(src_ids)} sources")
    for key, field in (("partitions", "partition"), ("domains", "domain")):
        counted = collections.Counter(s[field] for s in fsrc)
        declared = {k: v["sources"] for k, v in fmet[key].items()}
        if dict(counted) != declared:
            fail(f"corpus metrics {key} {declared} != counted {dict(counted)}")

    # Skill must be synchronized.
    cp = subprocess.run(
        [sys.executable, str(ROOT / "tools/sync_skill.py"), "--check"],
        capture_output=True,
        text=True,
    )
    if cp.returncode:
        fail(cp.stdout + cp.stderr)

    # manifest.yaml describes an immutable release snapshot. Development branches
    # may legitimately differ from that snapshot before the next release manifest
    # is generated. Release checks keep this enabled; PR CI uses --skip-manifest.
    if not args.skip_manifest:
        man = yaml.safe_load((ROOT / "manifest.yaml").read_text(encoding="utf-8"))
        for item in man.get("files", []):
            fp = ROOT / item["path"]
            if not fp.exists():
                fail(f"manifest file missing: {item['path']}")
            if hashlib.sha256(fp.read_bytes()).hexdigest() != item["sha256"]:
                fail(f"manifest hash mismatch: {item['path']}")

    rows = list(csv.DictReader((ROOT / "corpus/coverage-curves.csv").open(encoding="utf-8")))
    final = float(rows[-1]["overall_coverage"]) if rows else 0
    print(
        json.dumps(
            {
                "status": "PASS",
                "release": release_version(),
                "validation_mode": "development" if args.skip_manifest else "release",
                "central_entries": len(A),
                "controlled_meanings": len(mids),
                "prohibited_or_review_entries": len(P),
                "rules_and_recommendations": len(ri),
                "public_corpus_sources": len(src_ids),
                "public_corpus_domains": len(fmet["domains"]),
                "legacy_sample_sources": len(src["sources"]),
                "final_public_controlled_surface_coverage": final,
                "agent_skill": "PASS",
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
