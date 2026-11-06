---
name: sv-cnv-calling
description: 'Use when detecting, merging, filtering, or benchmarking structural variants or copy-number changes from short-read, exome, or long-read data. Not for repeats (repeat-expansions) or paralogs (difficult-genes-and-mito).'
---

# SV and CNV calling

## Capability
SV and CNV calls reported as evidence, recall known by type and size. Correct: build, contigs, and sample order agree; each reported call has independent support.

## Decide
1. Confirm build, contigs, and sample order across BAM, VCF, panels. Stop on mismatch.
2. Check depth, insert size, read length. Low coverage loses split reads.
3. Pick callers by data type. One caller is a screen; merge two methods.
4. Capture CNV: same-kit, same-batch, same-sex reference set; drop samples apart on a coverage PCA.
5. Merge on type, size ratio, breakpoint distance, never exact position; record parameters.
6. Filter by size, support, flags, segmental duplications, centromeres, low mappability. Compare with a population SV set.
7. Inspect each reported call in a read viewer (long reads: also phase).
8. Human clinical: classify CNVs by ACMG/ClinGen. Other species: evidence, not a class.
9. Confirm orthogonally (array, MLPA, qPCR, long reads, PCR) before reporting.
10. Ask when a call is in a paralog region, possibly mosaic, or callers disagree.

## Find current information
Follow `current-methods-lookup`. Ask: which callers fit this data type and depth; which truth-set release and comparison tool apply; which merge settings were benchmarked; which population SV set fits. Search tool documentation, the GIAB page, then recent independent benchmarks (PubMed, Europe PMC; preprints labeled). Check date, maintenance, fit.

## Verify
* Human: score against the GIAB SV truth set by type and size bin, inside and outside benchmark regions, on its build. Other species: replicates, pedigrees, an assembly of the same individual, PCR on a subset.
* Trio inheritance fits; a second caller agrees.
* Failing: accuracy far below earlier runs, or a batch-wide shift. Fix the reference set.

## Failure modes
* Exact-match joins; one insertion counted as two.
* Wrong ploidy on sex or polyploid regions.
* Complex events split; mosaics read as germline.

## Record and report
Log (`analysis-log`): question, date, sources, versions, unverified, recheck. Per call: type, breakpoints (CIPOS), size, callers, support, genotype, frequency, validation.

Seeds: `${CLAUDE_SKILL_DIR}/references/where-to-look.md`.
