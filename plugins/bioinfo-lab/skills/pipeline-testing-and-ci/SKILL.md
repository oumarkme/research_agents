---
name: pipeline-testing-and-ci
description: 'Use when adding tests, regression checks, or continuous integration to a Nextflow, Snakemake, Python, or R pipeline. Not for code style (coding-style) or clinical validation (clinical-pipeline-validation).'
---

# Pipeline testing and CI

## Capability
Tests that show a change did not break output or accuracy, run automatically.

## Decide
Build layers in this order:
1. Unit: pure functions and parsers, with edge cases (empty input, multi-allelic site, contig missing from the reference, 0- versus 1-based).
2. Smoke: the whole pipeline on a tiny input in minutes.
3. Regression: compare outputs with stored expectations after any change. Do not checksum files that carry dates or command lines; compare records or use numeric tolerances.
4. Accuracy: a truth-set slice scored and stratified (`sequencing-pipelines`); fail on a drop in any stratum, with a margin set from repeat runs on the unchanged pipeline.
Rules: tiny public or synthetic test data, fetched by checksum; pin seeds, tool versions, and images; change a pin in its own commit with the regression diff; each bug fix adds the failing case first.
CI: layers 1 and 2 on every push; layers 3 and 4 on release, on the compute host in CLAUDE.md (else ask). Runner matches production containers. No secrets or large downloads.

## Find current information
Follow `current-methods-lookup`. Ask: which test framework for this engine is maintained now; how it handles snapshots and tolerances; which CI limits apply; which truth sets are current.
Sources in order: framework docs and release notes; workflow community pages (nf-core, Snakemake); GA4GH benchmarking pages; recent reviews (PubMed, Europe PMC); preprints, labeled.
Check date, maintenance. See `${CLAUDE_SKILL_DIR}/references/where-to-look.md`.

## Verify
* Mutation check: break the pipeline on purpose (swap a sample, shift a coordinate, drop a filter); a test must fail.
* Two runs, same seed: outputs agree.
* Known-answer input with a hand-computed result.
* Accuracy score on the unchanged pipeline matches the stored baseline.
Failing: fix the code, not the expectation.

## Failure modes
Blind snapshot updates; network-dependent tests; recall quoted for high-confidence regions only; unfixed seeds; data that never reaches the failure branch.

## Record and report
Log: question, date retrieved, sources, versions, not verified, recheck date. Report layers present, tests and passes, runtime, uncovered parts, strata checked.
