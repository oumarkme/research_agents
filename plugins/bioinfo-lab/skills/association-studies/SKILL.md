---
name: association-studies
description: 'Use when running or reviewing GWAS, QTL mapping, or Mendelian randomization in humans, crops, or livestock. Not for general design (study-design) or prediction models (genomic-prediction).'
---

# Association studies

## Capability

Test genotype-phenotype association with controlled structure, a stated correction, and replication. See also `plant-field-trial-gwas`, `livestock-genotype-qc-imputation`, `polyploid-genotyping-dosage`.

## Decide

1. QC samples and markers before any test: call rate, sex, heterozygosity, relatedness, Hardy-Weinberg (controls or founders only; not inbred lines), allele frequency. Fix thresholds first; log counts removed per step.
2. Structure: principal components; with relatives, a mixed model with kinship.
3. Phenotype: state transformation and covariates; crops use adjusted means or breeding values (`quantitative-genetics`). Analyze environments separately before a joint model.
4. Threshold: stated correction with the test count (effective independent tests, or FDR), or the field's convention.
5. Locus: define by LD, fine-map with a matched LD reference; candidate genes are hypotheses.
6. Mendelian randomization: defend relevance, independence, and exclusion. Use two or more estimators that relax different assumptions, plus heterogeneity and pleiotropy checks; match ancestry. Say "consistent with a causal effect".
7. Crops and livestock: kinship, subpopulation terms, LD decay (sets resolution and test count).

## Find current information

Follow `current-methods-lookup`. Ask:
* Which software fits our sample size, relatedness, trait? (Docs, then recent benchmarks.)
* Which threshold does the field use now for this ancestry and density?
* Which reporting checklist applies (STROBE-MR, journal, consortium)?
* Which LD reference and imputation panel match our population?
Check release date, maintenance, organism fit.

## Verify

* Inflation factor and QQ plot; polygenicity and sample size also raise it, so test the LD score regression intercept (humans) or permuted nulls before calling it confounding; do not rescale.
* Permuted phenotype gives a null QQ and no hits.
* A known or simulated causal variant is recovered with the right sign.
* Replicate independently; direction and size agree.
* Build, allele orientation, sample order match (`genomics-pitfalls`).

## Failure modes

Unmodeled structure; testing before QC; winner's curse; wrong-ancestry LD panel; overlapping MR samples; one-environment "stable" loci.

## Record and report

Effect, interval, allele and frequency, build, imputation panel, test count, threshold, inflation, software and version, QC counts. Seeds: `references/where-to-look.md`.
