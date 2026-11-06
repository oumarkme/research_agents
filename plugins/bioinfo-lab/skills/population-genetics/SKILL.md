---
name: population-genetics
description: 'Use when computing PCA, ancestry, admixture, kinship, IBD, Fst, or selection scans in any organism, or building a reference panel. Not for GWAS covariates and mixed models (association-studies).'
---

# Population genetics

## Capability
Describe structure, ancestry, relatedness, and selection from genotypes in any organism.

## Decide
1. SNP set: biallelic autosomal, one build, stated call-rate and MAF filters, palindromic sites checked. Compare cohort allele frequencies.
2. Relatedness before structure. Kinship cutoffs assume an outbred diploid; for inbred or selfing lines use `popgen-inbreeding-ne-germplasm` (judgment).
3. PCA on unrelated, LD-pruned samples. Project relatives and references with the same SNPs and orientation; correct shrinkage.
4. Ancestry. Human: project onto a public panel; add local samples if none represents the study (judgment). Other species: a species panel or the project's own samples.
5. Admixture models: several K, replicate seeds, a fit criterion. Barplots do not prove admixture; test it with f-statistics.
6. Fst: state estimator, how per-SNP values combine, SNP selection, sample sizes.
7. Haplotype-based scans (iHS, XP-EHH, nSL) and IBD segments need phased data; Fst, SFS, and KING-type kinship do not; scans also need a recombination map and demographic null; outliers are candidates.

## Find current information
Follow `current-methods-lookup`. Ask: which kinship, PCA-projection, admixture, and IBD tools fit this data and scale; which panel release fits this ancestry; which cutoffs fit this ploidy. Sources in order: official docs and release notes; panel consortium page; recent independent benchmarks (PubMed, Europe PMC); preprints, labeled. Check date, maintenance, benchmark, organism fit. Seeds: `references/`.

## Verify
* Duplicates and known pairs give the expected kinship class.
* PCs against batch, array, kit, and date; a batch-driven PC means stop.
* Reference samples of known origin fall with their group after projection.
* Two estimators agree in rank order, else report both.
* K and PCs stable across seeds and SNP subsets; else no claim.

## Failure modes
* Relatives drive PCs.
* Reference and target differ in build or strand.
* A PC position is no ancestry proportion.
* Human ancestry groups are similarity clusters, not race (`research-ethics`).

## Record and report
Log: question, date retrieved, sources, version chosen, not verified, recheck date. Report SNPs per filter, build, panel, versions, seeds, K and fit, cutoffs, removed samples.
