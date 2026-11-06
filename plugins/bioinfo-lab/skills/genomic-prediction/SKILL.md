---
name: genomic-prediction
description: 'Use when building, validating, or reporting genomic prediction or polygenic scores in crops, livestock, or humans. Not for general design (study-design) or association testing (association-studies).'
---

# Genomic prediction and polygenic scores

## Capability

Predict phenotype or breeding value from genotype and report accuracy that holds in the intended use. See `quantitative-genetics`, `livestock-genotype-qc-imputation`, `plant-field-trial-gwas`, `genomics-pitfalls`.

## Decide

1. Phenotype: adjusted means or breeding values from a stated model, not raw plot values, unless one-stage.
2. Genotype: QC or imputation using phenotype or fold information is fit on training data only; record build, marker count, missingness.
3. Model: linear baseline (GBLUP or ridge) first; add other models only against it, on the same folds.
4. Scheme mirrors use: new lines, environments, families, future years, or populations and ancestries. Random k-fold answers only the first and overstates accuracy when relatives straddle folds.
5. Every data-dependent step (scaling, imputation, feature selection, PCs, variance components) is fit inside the training fold.
6. Humans: development and validation sets are separate; accuracy drops across ancestries, so state ancestry and do not extrapolate.

## Find current information

Follow `current-methods-lookup`. Ask:
* Which models do recent multi-species benchmarks support for our architecture and training size?
* Which maintained software fits our model and scale?
* Which reporting standard and score repository apply?
* Does the benchmark's validation scheme match ours?

## Verify

* Baseline beside every model, same folds, with training size, marker number, train-test relatedness.
* Permuted phenotype gives accuracy near zero.
* Repeat folds with stored seeds; report mean and spread.
* Predictive ability is the test-set correlation; divide by the square root of heritability to compare with breeding-value accuracy. Add bias (slope), RMSE, and for selection the top-fraction mean against the population mean.
* Accuracy should rise with training size and heritability; a jump after a new feature suggests leakage.

## Failure modes

Relatives across folds; preprocessing on all data; tuning on test data; selected-parent accuracy applied to everyone; no baseline.

## Record and report

Table: ID, prediction, error or reliability, train/test flag. Record scheme, seeds, software, versions, QC, ancestry. See `references/where-to-look.md`.
