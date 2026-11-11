---
name: annotation-and-databases
description: 'Use when annotating variants in any organism: consequence tools, transcript sets, frequency, constraint, and clinical database releases, or species databases. Not for classification (variant-interpretation).'
---

# Annotation and databases

## Capability
Add consequence, HGVS, frequency, scores, and clinical evidence to normalized variants. Pin tool, transcript set, and database release.

## Decide
1. Normalize first: left-align, split multiallelics, check REF against the FASTA.
2. One tool per project; never mix tools in one table.
3. Transcript. Human: MANE (Select, plus Plus Clinical). Other species: the reference's annotation release. Use versioned IDs. One row per variant by a stated rule; keep the per-transcript table.
4. Frequency: version and subset in the column name. Human dominant filtering uses a filtering allele frequency, not raw AF; add local frequency as a second column. Other species: project cohort. "Absent" is not "rare": check filters and coverage.
5. Scores: keep raw score, tool version, transcript. Thresholds come from `variant-interpretation`.
6. Constraint metrics support only a loss-of-function mechanism; state the release.
7. ClinVar: keep release date, review status, conflicts, submitter count.
8. Re-annotate after a build change; never lift columns.
9. Stop and ask: no MANE transcript; tools disagree on an indel.

Version log: `${CLAUDE_SKILL_DIR}/references/version-log.md`.

## Find current information
Per `current-methods-lookup`, ask: which tool and cache fit this organism and build; which transcript, frequency, and ClinVar releases are current; which scores are independently evaluated.
Sources in order: release notes; MANE, gnomAD, ClinVar, Ensembl pages; independent evaluations of recent years (PubMed, Europe PMC); preprints, labeled.
Check release date and build. Seeds: `references/where-to-look.md`.

## Verify
* Annotate known ClinVar variants: each HGVS mismatch is a transcript or normalization difference.
* Row counts match before and after.
* Reproduce a few frequencies from the source file.
* A second tool on a sample: explain each difference.
Failure: check cache build and release against the FASTA.

## Failure modes
Transcript or release mismatch; versionless columns; wrong-build databases; unstated subsets.

## Record and report
Log: question, date retrieved, sources, versions chosen, NOT verified, recheck date. Report tool, cache, transcript rule, releases, build.
