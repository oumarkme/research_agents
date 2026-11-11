---
name: metagenomics
description: 'Use when analyzing 16S or shotgun microbiome data: host removal, profiling, assembly and binning, contamination controls, compositional statistics, STORMS reporting. Not for isolate genome assembly (bacterial-genome-assembly-annotation).'
---

# Metagenomics

## Capability
Composition, function, or genomes of a community. A correct result separates signal from contaminants and host reads, and treats counts as compositional.

## Decide
1. Question first (composition, function, new genomes); it sets marker gene versus shotgun.
2. Controls per batch: extraction blank, no-template control, mock community, positive replicate; low-biomass samples are dominated by reagent contaminants.
3. Remove host reads before profiling or sharing; record the reference.
4. Choose profiler and database for the aim; the release changes results.
5. Bin only for genomes; label bins by a community quality standard.
6. Use a compositional method with batch and host covariates; fix filters before unblinding. Differential-abundance methods disagree: run two, report the overlap.
7. Report with STORMS (human) and MIxS (environmental).
8. Ask if blanks are missing or share taxa with samples, batch equals group, or sharing consent is unclear.

## Find current information
Follow `current-methods-lookup`. Questions: profilers and databases for this sample type; contaminant and compositional methods; bin standard; current STORMS and MIxS versions. Sources in order: tool docs and release notes; GSC (MIxS), CAMI, STORMS pages; independent benchmarks (PubMed, recent years); preprints, labeled. Check date, maintenance, benchmark on this sample type.

## Verify
* Mock community: observed against expected.
* Taxa in blanks and low-biomass samples are suspect.
* Two profilers on the mock and one real sample agree.
* Read-loss log (raw, trimmed, host-removed, classified): most reads lost at host removal means too little microbial signal; flag, do not rescale.
* Replicates cluster together; no batch separation.
Failure: fix controls or pipeline first, then rerun.

## Failure modes
* Relative abundance read as absolute.
* Filters chosen post hoc; batch confounded with group.
* Database releases mixed.

## Record and report
Analysis-log: question, date, sources, versions, not verified, recheck date. Report samples, controls, kits, host reference, databases, versions, read counts per step.

Seeds: `references/where-to-look.md`, `metagenomics-checks.md`.
