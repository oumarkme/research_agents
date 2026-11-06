---
name: long-read-ont-pacbio
description: 'Use when processing ONT or PacBio reads: basecalling, alignment, small variants, SV, phasing, methylation, assembly, or run metrics. Not for run pass or fail (run-qc-and-demultiplexing) or short-read SV (sv-cnv-calling).'
---

# Long-read ONT and PacBio

## Capability
Raw long reads become alignments, variants, phase, methylation, or assemblies. Correct: one chemistry, basecaller, and model per cohort; results checked against a truth set or replicate.

## Decide
1. Record flow cell, kit, pore type, raw data type, goal. Stop if chemistry and model mismatch.
2. Basecall with the model for the chemistry; keep raw signal. Add modified-base models only for methylation; contexts differ by organism (plants also need CHG and CHH), so check the tool docs.
3. Align to the project build with the preset for the platform. Keep supplementary alignments; assert build and contig names.
4. Check read length, quality, depth before calling; needed depth depends on the goal.
5. Use callers trained for the chemistry and basecaller. Homopolymer indels are the known ONT weak point; filter or confirm.
6. Choose SV, phasing, methylation, assembly tools per goal; phase before allele-specific methylation. Log filters.
7. Ask when depth is below plan or the model is unknown.

## Find current information
Follow `current-methods-lookup`. Ask: which basecaller and model match this chemistry; which aligner preset and small-variant, SV, phasing, methylation, and assembly tools are current; what the tool docs say about contexts; whether benchmarks cover your organism. Search vendor documentation, release notes, tool docs, then recent benchmarks (PubMed, Europe PMC; preprints labeled). Check date, maintenance, fit.

## Verify
* Human: score a GIAB sample per stratum; others: replicates or short-read concordance.
* Methylation: compare a subset with bisulfite or another orthogonal assay.
* Assembly: contiguity, base accuracy, completeness against a reference set.
* Failing: model mismatch or batch shift; re-basecall before calling.

## Failure modes
* Build or contig mismatch; wrong-chemistry model.
* Dropped supplementary alignments; ONT homopolymer indels read as true.

## Record and report
Log (`analysis-log`): question, date, sources, versions, unverified, recheck. Report chemistry, basecaller, model, depth, read length, quality, settings.

Seeds: `${CLAUDE_SKILL_DIR}/references/where-to-look.md`.
