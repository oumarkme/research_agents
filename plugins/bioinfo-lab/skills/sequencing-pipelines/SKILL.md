---
name: sequencing-pipelines
description: 'Use when building or validating sequencing analysis: short- and long-read QC, alignment, variant calling, benchmarking, assembly, pangenomes, and workflow managers. Not for tests and CI (pipeline-testing-and-ci).'
---

# Sequencing pipelines

## Capability
Raw reads to validated calls or assemblies in a reproducible workflow. Methods change often; the checks do not.

## Decide
1. Record instrument, chemistry, read length, expected depth. Check raw QC first; report a failed run instead of analyzing it.
2. Match aligner and caller to data type, organism, and variant class. Mark duplicates; check coverage, insert size, and sample identity.
3. Normalize variants; follow `genomics-pitfalls`.
4. Benchmark before trusting: score against a truth set, stratified by region and variant type, precision and recall per stratum. Outside high-confidence regions a truth set says nothing.
5. Human clinical pipelines: validate on a representative set, define accuracy per variant class, freeze versions, keep a change log.
6. Assembly: check completeness, contiguity, phasing. Pangenomes: keep a linear reference for coordinates.
7. Workflows: pin every tool version, validate the sample sheet, use resumable runs, store command and config; test on a small input first.
8. Do not tune on the truth set, mix builds, or re-run finished steps.

## Find current information
Follow `current-methods-lookup`. Ask: which aligner, caller, or assembler is current and independently benchmarked for this platform, organism, and variant class; which truth set and stratifications are current; which workflow templates exist.
Sources in order: tool docs and release notes; GIAB, GA4GH, nf-core pages; independent benchmarks of recent years (PubMed, Europe PMC); preprints, labeled.
Check release date, maintenance, chemistry fit. Seeds: `${CLAUDE_SKILL_DIR}/references/where-to-look.md`.

## Verify
* Truth-set concordance per stratum, same comparison tool each run.
* Sanity metrics (duplication, mapped fraction, coverage evenness, Ti/Tv, het/hom, sex check) within the project's earlier range.
* Replicate or pedigree concordance; Mendelian errors in trios.
* Two methods on one sample; known-answer small input first.
Failing: locate the step and rerun; never filter to pass.

## Failure modes
Sample swap; build mix; tuning on the truth set; unpinned versions; recall quoted for high-confidence regions only.

## Record and report
Log: question, date retrieved, sources, versions, NOT verified, recheck date. Report tools, command, references, per-stratum metrics, untested items.

## Long jobs
Run in the background with a project log; record command, PID or job ID. Start `Monitor` on progress and failure words (`error`, `Traceback`, `killed`, `OOM`, `exit`); send one to three lines on news, none otherwise. At the end report outcome, exit status, outputs, first real error. Done means expected outputs exist.
