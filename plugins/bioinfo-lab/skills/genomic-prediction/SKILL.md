---
name: genomic-prediction
description: 'Use when building, validating, or reporting genomic prediction or polygenic scores in crops, livestock, or humans: validation schemes, leakage, baselines, accuracy metrics, model benchmarking, and reporting standards.'
---

# Genomic prediction and polygenic scores

## Pipeline

1. Phenotype: use adjusted means or breeding values from a stated model (`quantitative-genetics`), not raw plot values, unless the model is one-stage.
2. Genotype: QC, imputation, and filters computed on the training set only when they use phenotype or fold information; record build, marker count, missingness, and minor allele frequency thresholds.
3. Model: start with GBLUP or ridge regression (rrBLUP). Add Bayesian, kernel, or machine-learning models only against that baseline, on the same folds.
4. Validate with a scheme that mirrors the use (below), then report.

## Validation scheme

* Choose the scheme from the question: new untested lines (leave-lines-out), new environments (leave-environment-out), new families (leave-family-out), future years (forward-in-time), or new populations and ancestries (leave-population-out). Random k-fold answers only the first, and overstates accuracy when relatives are split across folds, because relatedness alone gives accuracy (Habier et al., 2007).
* Fit every data-dependent step inside the training fold: scaling, imputation, feature selection, principal components, variance components.
* Multi-trait models: do not let the test records of secondary traits inform the prediction in a way the real use would not allow (Runcie & Cheng, 2019, *G3*, PMC6829121).
* Repeat the folds with stored seeds. Report the mean and the spread across repeats.

## Metrics

* Predictive ability: Pearson correlation between prediction and the (adjusted) phenotype in the test set. Divide by `h` to compare with breeding-value accuracy, and say so.
* Also report bias (regression slope of phenotype on prediction), error (RMSE), and, for selection, the mean phenotype of the top-ranked fraction against the population mean.
* Always show the baseline model next to every other model, with the training size, marker number, and relatedness between training and test sets. Benchmark studies show no model wins everywhere (Azodi et al., 2019, *G3*), so claims need your own data.

## Humans: polygenic scores

* Report with the PRS-RS framework (Wand et al., 2021, *Nature*): study population, score development and validation, ancestry, and limitations. Deposit the score in the PGS Catalog.
* Accuracy drops across ancestries. State the ancestry of the training and test sets and do not extrapolate.

## Output

Predictions as a table with ID, predicted value, and a prediction error or reliability where the model gives one. Never mix training and test IDs without a flag column.

DOIs of the cited papers: `${CLAUDE_SKILL_DIR}/references/sources.md`.
