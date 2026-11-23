---
name: methylation-and-epigenomics
description: 'Use when analyzing methylation (human arrays, bisulfite, EM-seq, ONT), ChIP-seq or ATAC-seq peaks, human episignatures, or cell composition, in any organism. Not for expression analysis (rna-seq-and-splicing).'
---

# Methylation and epigenomics

Goal: compare methylation, histone marks, or accessibility apart from batch, cell mixture, age, and sex.

## What decides quality

* **Assay:** arrays are human only; bisulfite, EM-seq, and ONT suit any organism. Plants: report CG, CHG, and CHH separately.
* **QC and normalization:** per-sample QC and one recorded normalization. Human arrays: mask SNP-affected and cross-reactive probes; combine array generations only on shared masked probes.
* **Conversion rate:** from a spike-in or non-CpG context (not CHH in plants; judgment). ONT: record the modified-base model and filter; haplotag reads for imprinting (`sequencing-pipelines`).
* **Thresholds:** set coverage floors and cutoffs before testing (judgment).
* **Cell composition:** estimate from a matched reference; model it with age, sex, and batch.
* **ChIP-seq and ATAC-seq:** consortium QC, replicate reproducibility, blacklist removal, consensus peaks, batch in the design.
* **Human episignatures:** platform-matched controls and a published classifier; a result supports, never replaces, variant evidence; classification belongs to a clinical geneticist.

## Find current information
Follow `current-methods-lookup`. Ask: which methylation tools fit this organism and platform; which modified-base model matches the chemistry; which probe masks, blacklists, and QC standards are current. Sources in order: official docs and release notes; recent independent benchmarks (PubMed, Europe PMC); preprints, labeled. Check date, maintenance, benchmark, fit. Seeds: `references/`.

## Verify
* Predicted sex matches recorded; replicates correlate.
* PCA by batch, slide, age, sex, cell mix before testing; batch tied to group: stop and ask.
* Same-batch positive and negative controls behave.
* Two normalizations or callers give concordant top regions.
* Peaks reproduce across replicates.

## Failure modes
* Age, sex, cell mixture confound.
* Array platform differs from the control set (looks like disease).
* Probe manifest build mismatch; blacklist omitted.

## Record and report
Log: question, date retrieved, sources, versions, not verified, recheck date. Report platform, build, QC removals, normalization, conversion rate, coverage floor, model, covariates, controls.
