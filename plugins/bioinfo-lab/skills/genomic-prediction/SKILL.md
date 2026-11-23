---
name: genomic-prediction
description: 'Use when building, validating, or reporting genomic prediction or polygenic scores in crops, livestock, or humans. Not for general design (study-design) or association testing (association-studies).'
---

# Genomic prediction and polygenic scores

Goal: predict phenotype or breeding value from genotype and report accuracy that holds in the intended use. Related: `quantitative-genetics`, `livestock-genotype-qc-imputation`, `plant-field-trial-gwas`, `genomics-pitfalls`.

## What decides validity

* **Phenotype:** adjusted means or breeding values from a stated model, not raw plot values, unless one-stage.
* **Genotype:** record build, marker count, and missingness; any QC or imputation that uses phenotype or fold information is fit on training data only.
* **Model:** a linear baseline (GBLUP or ridge) first; other models only against it, on the same folds.
* **Scheme mirrors use:** new lines, environments, families, future years, or populations and ancestries. Random k-fold answers only the first and overstates accuracy when relatives straddle folds.
* **Leakage:** every data-dependent step (scaling, imputation, feature selection, PCs, variance components) is fit inside the training fold.
* **Humans:** development and validation sets are separate; accuracy drops across ancestries, so state the ancestry and do not extrapolate.

## Find current information

Follow `current-methods-lookup`. Ask: which models recent multi-species benchmarks support for this architecture and training size; which maintained software fits the model and scale; which reporting standard and score repository apply; whether the benchmark's validation scheme matches ours.

## Verify

* A baseline beside every model, same folds, with training size, marker number, and train-test relatedness.
* A permuted phenotype gives accuracy near zero; repeated folds with stored seeds give mean and spread.
* Predictive ability is the test-set correlation; divide by the square root of heritability to compare with breeding-value accuracy. Add bias (slope), RMSE, and for selection the top-fraction mean against the population mean.
* Accuracy should rise with training size and heritability; a jump after a new feature suggests leakage.

## Failure modes

Relatives across folds; preprocessing on all data; tuning on test data; selected-parent accuracy applied to everyone; no baseline.

## Record and report

Table: ID, prediction, error or reliability, train/test flag. Record scheme, seeds, software, versions, QC, ancestry. Seeds: `${CLAUDE_SKILL_DIR}/references/where-to-look.md`.
