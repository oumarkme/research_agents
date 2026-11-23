---
name: long-read-ont-pacbio
description: 'Use when processing ONT or PacBio reads: basecalling, alignment, small variants, SV, phasing, methylation, assembly, or run metrics. Not for run pass or fail (run-qc-and-demultiplexing).'
---

# Long-read ONT and PacBio

Goal: raw long reads become alignments, variants, phase, methylation, or assemblies, with one chemistry, basecaller, and model per cohort and results checked against a truth set or replicate.

## What decides quality

* **Provenance:** record flow cell, kit, pore type, raw data type, and goal; stop if chemistry and model mismatch.
* **Basecalling:** use the model for the chemistry and keep raw signal. Add modified-base models only for methylation; contexts differ by organism (plants also need CHG and CHH), so check the tool docs.
* **Alignment:** the project build with the platform preset; keep supplementary alignments; assert build and contig names.
* **Pre-call checks:** read length, quality, and depth; needed depth depends on the goal.
* **Callers:** trained for the chemistry and basecaller. Homopolymer indels are the known ONT weak point; filter or confirm.
* **Tools by goal:** SV, phasing, methylation, assembly; phase before allele-specific methylation; log filters.
* **Stop and ask** when depth is below plan or the model is unknown.

## Find current information
Follow `current-methods-lookup`. Ask: which basecaller and model match this chemistry; which aligner preset and small-variant, SV, phasing, methylation, and assembly tools are current; what the tool docs say about contexts; whether benchmarks cover your organism. Search vendor documentation, release notes, tool docs, then recent benchmarks (PubMed, Europe PMC; preprints labeled). Check date, maintenance, fit.

## Verify
* Human: score a GIAB sample per stratum; others: replicates or short-read concordance.
* Methylation: compare a subset with bisulfite or another orthogonal assay.
* Assembly: contiguity, base accuracy, completeness against a reference set.
* On failure, suspect model mismatch or batch shift; re-basecall before calling.

## Failure modes
* Build or contig mismatch; wrong-chemistry model.
* Dropped supplementary alignments; ONT homopolymer indels read as true.

## Record and report
Log (`analysis-log`): question, date, sources, versions, not verified, recheck date. Report chemistry, basecaller, model, depth, read length, quality, settings.

Seeds: `${CLAUDE_SKILL_DIR}/references/where-to-look.md`.
