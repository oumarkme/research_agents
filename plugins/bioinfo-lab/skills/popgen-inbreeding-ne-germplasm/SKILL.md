---
name: popgen-inbreeding-ne-germplasm
description: 'Use when estimating structure, inbreeding, ROH, or effective population size in non-model, crop, livestock, or genebank samples. Not for human ancestry and admixture workflows (population-genetics) or GWAS (association-studies).'
---

# Inbreeding, Ne, and germplasm diversity

## Capability
Estimate structure, inbreeding, Ne, and diversity for a defined population, with intervals. A correct result uses unrelated, non-duplicate samples and agrees with pedigree or passport. PCA, ADMIXTURE, kinship, Fst: `population-genetics`.

## Decide
1. State question and unit (breed, accession, cultivar); note mating system, ploidy, generation overlap.
2. Sample across range and groups; record accession and site.
3. Flag close relatives and clones before structure analysis; keep them for pedigree work.
4. Structure: PCA, then clustering over several K (K is descriptive). In selfers and clones, count multilocus genotypes.
5. Inbreeding: compare marker-based F (ROH, homozygosity) with pedigree F; set ROH parameters from marker density.
6. Ne: match method to mating system and sampling; use one homogeneous group; report interval and generation.
7. Genebank: compare diversity with passport data; find duplicates, gaps.
8. Polyploids: `polyploid-genotyping-dosage`.

## Find current information
Follow `current-methods-lookup`. Ask: which ROH and Ne methods are maintained and validated for our density, sample size, and mating system; which ROH parameters suit our density; which review compares inbreeding estimators.
Search: tool docs and release notes, recent reviews in PubMed, labeled preprints. Check release date, test species, sample size.

## Verify
* Simulate known F and Ne and recover both.
* Marker F correlates with pedigree F; incomplete pedigrees bias pedigree F low.
* Rerun ROH with other parameters and fewer markers; F_ROH changes little.
* Remove relatives: structure and Ne hold.
* F_ROH against depth: a trend means calling bias.

## Failure modes
* Relatives inflate structure and bias Ne downward.
* Pooled generations give Ne for no generation.
* Selfing breaks Hardy-Weinberg filters.

## Record and report
Log: question, date, sources, versions, not verified, recheck. Report counts per group, kinship filter, K and error, ROH parameters, F and Ne with method, interval, generation. Mind `access-benefit-sharing-and-data-governance`.

See `references/where-to-look.md`.
