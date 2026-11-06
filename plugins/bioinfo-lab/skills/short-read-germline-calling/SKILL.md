---
name: short-read-germline-calling
description: 'Use when aligning short reads and calling, joint genotyping, filtering, or benchmarking germline SNVs and indels from WGS, WES, or panels. Not for SV or CNV (sv-cnv-calling), tumor samples (somatic-calling), or annotation.'
---

# Short-read germline calling

## Capability
A cohort VCF of germline SNVs and indels with error profile per stratum. Correct: one reference and tool set; accuracy shown on a truth set or replicates.

## Decide
1. Fix the reference (`reference-genomes-and-liftover`). A change of reference, aligner, or caller means re-calling.
2. Align, mark duplicates; record depth and insert size.
3. Choose the caller once, state why, and test it on a truth sample run through your kit.
4. Call per sample as gVCF, then joint-genotype. Never merge single-sample VCFs by position: a missing site is not homozygous reference.
5. Joint-call samples from one kit; check batch effects before merging.
6. Pick filtering by cohort size and truth resources. Without them (most non-human species), tune hard filters on replicates.
7. Normalize (split, left-align, check REF) before annotation. Set ploidy per sample and locus (`polyploid-genotyping-dosage`). chrM: `difficult-genes-and-mito`.

## Find current information
Follow `current-methods-lookup`. Ask: which aligner and caller are supported for this data and organism; the documented filtering for this cohort size; which truth-set release applies; whether benchmarks cover your ancestry or species. Search tool documentation and release notes, GIAB and GA4GH pages, then recent independent benchmarks (PubMed, Europe PMC; preprints labeled). Check release date, maintenance, fit.

## Verify
* Human: score a GIAB sample per stratum, including difficult regions, not one F1. Other species: replicates, Mendelian consistency, array concordance.
* Per-sample call count, Ti/Tv, het/hom, X/Y ploidy match the per-kit history; trios have few Mendelian errors.
* Two callers on a subset disagree mainly in repeats.
* Failing: errors cluster by kit, batch, or stratum. Find the cause first.

## Failure modes
* Regions outside the truth set are untested.
* Mixed kits in a joint call: false reference calls.
* Filters reused across cohorts.

## Record and report
Log (`analysis-log`): question, date, sources, versions, not verified, recheck. Report reference, versions, filters, cohort QC, per-stratum benchmark.

Seeds: `${CLAUDE_SKILL_DIR}/references/where-to-look.md`.
