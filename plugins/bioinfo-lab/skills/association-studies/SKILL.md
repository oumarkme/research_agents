---
name: association-studies
description: 'Use when running or reviewing GWAS, QTL mapping, or Mendelian randomization in humans, crops, or livestock: sample and marker QC, population structure, mixed models, thresholds, inflation, fine-mapping, replication, and reporting.'
---

# Association studies

## Steps

1. QC samples and markers before any test: call rate, sex check, heterozygosity, relatedness and duplicates, Hardy-Weinberg (controls or founders only), minor allele frequency. Record thresholds and counts removed at each step (Anderson et al., 2010; tools: PLINK, Purcell et al., 2007; Chang et al., 2015).
2. Control structure: principal components (Price et al., 2006) and, with relatives or strong structure, a mixed model with a kinship matrix (GCTA, Yang et al., 2011; GEMMA, Zhou & Stephens, 2012; BOLT-LMM, Loh et al., 2015). Choose by sample size and relatedness.
3. Phenotype: state the transformation, covariates, and for crops the adjusted means or breeding values (`quantitative-genetics`). Analyze environments separately before any joint model.
4. Test, then check inflation: genomic inflation factor and a QQ plot. Inflation with a mixed model points to residual structure or a phenotype problem; do not fix it by rescaling statistics.
5. Threshold: human common-variant GWAS use 5e-8; for other panels use a stated correction (Bonferroni on the effective number of independent tests, or FDR, Benjamini & Hochberg, 1995) and say how many tests.
6. Interpret: define the locus by LD, fine-map with the right LD reference, name candidate genes as hypotheses, and replicate in an independent sample or environment before claiming a locus.
7. Report effect size with interval and allele, frequency, build, imputation panel, and the software version (Uffelmann et al., 2021).

## Mendelian randomization

* State the three instrument assumptions (relevance, independence from confounders, exclusion restriction) and the evidence for each.
* Report the main estimate with at least two methods that relax different assumptions, heterogeneity, and a pleiotropy check. Ancestry of exposure and outcome samples must match.
* Follow STROBE-MR for reporting (Skrivankova et al., 2021). Write "consistent with a causal effect", not "caused", unless the instrument assumptions hold.

## Crops and livestock

* Use kinship and, where the panel is structured, subpopulation terms. Report LD decay, because it sets the mapping resolution and the number of independent tests.
* Multi-environment data: test per environment and jointly, and keep G x E in mind before calling a locus stable.

##

DOIs of the cited papers: `${CLAUDE_SKILL_DIR}/references/sources.md`.
