---
name: sv-cnv-calling
description: 'Use when detecting, merging, filtering, or benchmarking structural variants or copy-number changes from short-read, exome, or long-read data. Not for repeats (repeat-expansions) or paralogs (difficult-genes-and-mito).'
---

# SV and CNV calling

Goal: calls reported as evidence, with recall known by type and size. Build, contigs, and sample order must agree across BAM, VCF, and panels (stop on mismatch), and each reported call needs independent support.

## What decides quality

* **Data:** depth, insert size, and read length set what is callable; low coverage loses split reads.
* **Callers:** choose by data type. One caller is a screen; merge at least two methods.
* **Merging:** on type, size ratio, and breakpoint distance, never exact position; record parameters.
* **Capture CNV:** needs a same-kit, same-batch, same-sex reference set; drop samples that sit apart on a coverage PCA.
* **Filters:** size, support, flags, segmental duplications, centromeres, low mappability; compare with a population SV set.
* **Review and confirmation:** inspect each reported call in a read viewer (long reads: also phase); confirm orthogonally (array, MLPA, qPCR, long reads, PCR) before reporting.
* **Interpretation:** human clinical CNVs follow ACMG/ClinGen; other species report evidence, not a class.
* **Stop and ask** when a call is in a paralog region, possibly mosaic, or callers disagree.

## Find current information

Follow `current-methods-lookup`. Ask: which callers fit this data type and depth; which truth-set release and comparison tool apply; which merge settings were benchmarked; which population SV set fits. Search tool documentation, the GIAB page, then recent independent benchmarks (PubMed, Europe PMC; preprints labeled). Check date, maintenance, fit.

## Verify

* Human: score against the GIAB SV truth set by type and size bin, inside and outside benchmark regions, on its build. Other species: replicates, pedigrees, an assembly of the same individual, PCR on a subset.
* Trio inheritance fits; a second caller agrees.
* Accuracy far below earlier runs, or a batch-wide shift, means the reference set needs fixing.

## Failure modes

Exact-match joins; one insertion counted as two; wrong ploidy on sex or polyploid regions; complex events split; mosaics read as germline.

## Record and report

Log (`analysis-log`): question, date, sources, versions, unverified, recheck. Per call: type, breakpoints (CIPOS), size, callers, support, genotype, frequency, validation. Seeds: `${CLAUDE_SKILL_DIR}/references/where-to-look.md`.
