#!/usr/bin/env python3
"""Build aggregate STG-DE v0.5 corpus metrics from public source URLs.

The script downloads source documents into memory, extracts text, computes hashes and
aggregate lexical metrics, and writes only derived metadata. Raw third-party text is
never written to the repository output.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import io
import json
import re
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß0-9_:+/.-]*|\d+(?:[.,]\d+)?", re.UNICODE)


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def download(url: str, timeout: int = 90) -> tuple[bytes, str]:
    response = requests.get(
        url,
        timeout=timeout,
        headers={"User-Agent": "STG-DE-corpus-audit/0.5 (+https://github.com/LinusAurel/simplified-technical-german)"},
    )
    response.raise_for_status()
    return response.content, response.headers.get("content-type", "")


def extract_pdf(data: bytes) -> str:
    reader = PdfReader(io.BytesIO(data))
    pages: list[str] = []
    for page in reader.pages:
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        if text:
            pages.append(text)
    return "\n".join(pages)


def extract_html(data: bytes) -> str:
    soup = BeautifulSoup(data, "html.parser")
    for node in soup(["script", "style", "noscript", "svg"]):
        node.decompose()
    main = soup.find("main") or soup.find("article") or soup.body or soup
    return "\n".join(part.strip() for part in main.stripped_strings if part.strip())


def extract_text(data: bytes, source_type: str, content_type: str) -> str:
    if source_type == "pdf" or "application/pdf" in content_type:
        return extract_pdf(data)
    if source_type == "html" or "text/html" in content_type:
        return extract_html(data)
    return data.decode("utf-8", errors="replace")


def token_list(text: str) -> list[str]:
    return WORD_RE.findall(text)


def approved_surfaces() -> set[str]:
    data = load_yaml(ROOT / "dictionary" / "approved-words.yaml")
    entries = data.get("entries", [])
    canonical = {str(e.get("lemma", "")).casefold() for e in entries if e.get("lemma")}
    surfaces = set(canonical)
    for entry in entries:
        for surface in entry.get("surface_forms", []) or []:
            surfaces.add(str(surface).casefold())
        if entry.get("part_of_speech") == "noun" and entry.get("plural"):
            plural = str(entry["plural"]).casefold()
            if plural not in canonical:
                surfaces.add(plural)
    contractions = load_yaml(ROOT / "dictionary" / "contractions.yaml")
    for item in contractions.get("entries", []) or []:
        form = item.get("form") or item.get("surface") or item.get("term")
        if form:
            surfaces.add(str(form).casefold())
    return surfaces


def source_metrics(source: dict, approved: set[str]) -> tuple[dict, collections.Counter[str]]:
    data, content_type = download(source["url"])
    text = extract_text(data, source["type"], content_type)
    tokens = token_list(text)
    normalized = [t.casefold().strip(".-") for t in tokens]
    normalized = [t for t in normalized if t]
    controlled = sum(1 for t in normalized if t in approved)
    unknown = collections.Counter(t for t in normalized if t not in approved)
    token_count = len(normalized)
    return {
        "id": source["id"],
        "domain": source["domain"],
        "partition": source["partition"],
        "title": source["title"],
        "url": source["url"],
        "version": source.get("version"),
        "source_type": source["type"],
        "http_content_type": content_type,
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "token_count": token_count,
        "controlled_token_count": controlled,
        "controlled_surface_coverage": round(controlled / token_count, 6) if token_count else 0.0,
        "extraction_status": "ok" if token_count else "empty",
    }, unknown


def aggregate(rows: list[dict], unknowns: dict[str, collections.Counter[str]]) -> dict:
    by_partition: dict[str, dict] = {}
    by_domain: dict[str, dict] = {}
    for key_name, output in (("partition", by_partition), ("domain", by_domain)):
        groups: dict[str, list[dict]] = collections.defaultdict(list)
        for row in rows:
            groups[row[key_name]].append(row)
        for key, group in sorted(groups.items()):
            tokens = sum(r["token_count"] for r in group)
            controlled = sum(r["controlled_token_count"] for r in group)
            output[key] = {
                "sources": len(group),
                "tokens": tokens,
                "controlled_tokens": controlled,
                "controlled_surface_coverage": round(controlled / tokens, 6) if tokens else 0.0,
            }

    total_tokens = sum(r["token_count"] for r in rows)
    total_controlled = sum(r["controlled_token_count"] for r in rows)
    combined_unknown = collections.Counter()
    for counter in unknowns.values():
        combined_unknown.update(counter)

    return {
        "sources_attempted": len(rows),
        "tokens": total_tokens,
        "controlled_tokens": total_controlled,
        "controlled_surface_coverage": round(total_controlled / total_tokens, 6) if total_tokens else 0.0,
        "by_partition": by_partition,
        "by_domain": by_domain,
        "top_unknown_tokens": combined_unknown.most_common(100),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default=str(ROOT / "corpus" / "v0.5-sources.yaml"))
    parser.add_argument("--output", default=str(ROOT / "corpus" / "v0.5-fulltext-metrics.json"))
    parser.add_argument("--allow-failures", action="store_true")
    args = parser.parse_args()

    manifest = load_yaml(Path(args.manifest))
    approved = approved_surfaces()
    rows: list[dict] = []
    unknowns: dict[str, collections.Counter[str]] = {}
    failures: list[dict] = []

    for source in manifest.get("sources", []):
        try:
            row, unknown = source_metrics(source, approved)
            rows.append(row)
            unknowns[source["id"]] = unknown
            print(f"OK {source['id']}: {row['token_count']} tokens", flush=True)
        except Exception as exc:
            failures.append({"id": source.get("id"), "url": source.get("url"), "error": f"{type(exc).__name__}: {exc}"})
            print(f"FAIL {source.get('id')}: {type(exc).__name__}: {exc}", flush=True)
            if not args.allow_failures:
                raise

    report = {
        "schema_version": "0.5",
        "method": "transient public-source full-text extraction; raw text not persisted",
        "lexicon_release": "0.4.0",
        "sources": rows,
        "failures": failures,
        "aggregate": aggregate(rows, unknowns),
    }
    output = Path(args.output)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("REPORT_JSON=" + json.dumps(report["aggregate"], ensure_ascii=False), flush=True)

    if report["aggregate"]["tokens"] < 100_000:
        print(f"WARNING: corpus has {report['aggregate']['tokens']} tokens; v0.5 target is at least 100000", flush=True)
        return 2
    if not report["aggregate"]["by_partition"].get("holdout", {}).get("tokens"):
        print("ERROR: holdout partition is empty", flush=True)
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
