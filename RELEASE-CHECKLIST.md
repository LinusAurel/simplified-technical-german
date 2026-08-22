# STG-DE Release Checklist

Use this checklist for every tagged release.

## Scope and compatibility

- [ ] Set the intended version according to `VERSIONING.md`.
- [ ] Review all normative rule and dictionary changes since the previous release.
- [ ] Record restrictions, meaning changes, deprecations, and prohibitions in `CHANGELOG.md`.
- [ ] Verify published rule IDs were not accidentally renumbered or reused.
- [ ] Confirm application profiles reference valid rule IDs.

## Specification and dictionary

- [ ] Parse all YAML and JSON resources.
- [ ] Verify dictionary entry IDs and controlled meaning IDs are unique.
- [ ] Verify approved/prohibited canonical entries do not overlap unintentionally.
- [ ] Review accepted lexical proposals for the release.
- [ ] Confirm project/domain terminology was not absorbed into the central core solely to raise corpus coverage.

## Validator and quality

- [ ] Run `python -m unittest discover -s tests -v`.
- [ ] Run `python tools/sync_skill.py --check`.
- [ ] Run `python tools/validate_release.py --skip-manifest`.
- [ ] Verify `quality/rule-coverage.yaml` contains every published rule exactly once.
- [ ] Review any new deterministic checks for false-positive boundaries.
- [ ] Verify golden audit fixtures pass.

## Corpus and evidence

- [ ] Confirm development, validation, and holdout partitions are fixed before release evaluation.
- [ ] Confirm holdout evidence was not used to tune the same release dictionary/rules.
- [ ] Run the reproducible corpus workflow when the release changes corpus-sensitive behavior.
- [ ] Record source failures or extraction limitations.
- [ ] Publish only permitted metadata/derived metrics; do not add third-party raw text without redistribution rights.
- [ ] Record token counts and per-domain/per-partition metrics.

## Agent Skill

- [ ] Run Skill validation/packaging.
- [ ] Confirm bundled references and linter are synchronized with canonical repository files.
- [ ] Run available WRITE/REWRITE/AUDIT regression evaluations.
- [ ] Confirm default WRITE/REWRITE output behavior has not changed unintentionally.

## Artifact integrity

- [ ] Build standalone generated artifacts as applicable.
- [ ] Run `python tools/build_manifest.py` only after all release files are final.
- [ ] Run `python tools/validate_release.py` with manifest validation enabled.
- [ ] Generate SHA-256 checksums for downloadable release artifacts.
- [ ] Verify the tagged commit matches the release manifest.

## Publication

- [ ] Create the Git tag `vX.Y.Z`.
- [ ] Publish release notes from `CHANGELOG.md` and accepted proposals.
- [ ] Attach packaged Agent Skill and other release artifacts when available.
- [ ] Publish checksum file with the release assets.
- [ ] Verify README version/status information and installation examples.

## Post-release

- [ ] Check CI on the tagged/default-branch commit.
- [ ] Open follow-up issues for known limitations that were explicitly deferred.
- [ ] Do not retroactively modify holdout results for the tagged release.
