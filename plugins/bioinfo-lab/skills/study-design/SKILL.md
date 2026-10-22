---
name: study-design
description: 'Use when designing an analysis, choosing statistics, interpreting results, or auditing claims: design statement, confounders, multiple testing, power, and claim-versus-evidence audit.'
---

# Study design and claim audit

Be conservative and neutral. Weigh evidence for and against; do not favor the preferred hypothesis. Cite only verified sources (`trusted-sources`).

## Design statement (needed for every claim)

Sample and its source; comparison; model and covariates; multiple-testing method and number of tests; effect size with interval; prespecified or exploratory. No causal language from association.

## Checks

* Confounding: population structure (PCs, kinship), batch, ascertainment, sex, age. Relatedness between cases and controls or train and test.
* Multiple testing: state the family of tests; FDR or Bonferroni with the count; genome-wide thresholds for GWAS.
* Power and precision: report intervals; small panels inflate effects (winner's curse); rare-variant tests need aggregation and a stated frequency cutoff.
* Genomic prediction: validation scheme matches the use (within-family, across-family, across-environment, forward in time); preprocessing inside folds; accuracy as correlation with the (adjusted) phenotype and scaled by square-root heritability when comparing; baseline (GBLUP) on the same folds; seeds and repeats.
* Rare disease: phenotype-driven gene prioritization is a hypothesis; segregation, de novo status, and functional or clinical-concordance evidence are what support a diagnosis.
* Breeding: load `quantitative-genetics`. Prediction: `genomic-prediction`. GWAS and Mendelian randomization: `association-studies`.

## Claim audit

For each claim: what data show, what literature supports (verified PMID or DOI), what is assumed. Flag: claim stronger than the design, number not reproducible from the files, citation not found or not supporting, missing limitation. Challenge the premise when it is weak and propose the smallest decisive analysis.

## Answer format

Answer first with the main number and its uncertainty; then evidence, assumptions, limits, next decisive step.
