---
name: deep-learning-genomics
description: 'Use when training, validating, or applying neural models to genomic data (variant effect predictors, sequence models, basecallers). Not for polygenic or genomic prediction (genomic-prediction) or ACMG classification (variant-interpretation).'
---

# Deep learning in genomics

## Capability
Train or apply a neural model whose reported accuracy holds on new data. Correct: leakage-free split, baseline beaten with intervals, calibrated scores, reproducible run.

## Decide
1. State the task, the unit of prediction, and the decision the score feeds. Run a simple baseline on the same split; no claim without beating it.
2. Split by the unit that blocks leakage (chromosome block, gene or family, sample or run, pedigree). Assert zero shared IDs in code.
3. Keep one test set untouched; add an external set. Check target-population subsets.
4. Rare positives need precision-recall measures and prevalence. Check calibration. Bootstrap over genes or families, not rows.
5. A published model is a versioned artifact: pin weights, build, transcripts; check training-label overlap with your test set. Convert scores to evidence by calibration (`variant-interpretation`).
6. One model version per comparison. One job per GPU; ask before taking all.
7. Fix seeds, run several, save config, commit, image digest, checkpoint checksum.

## Find current information
Follow `current-methods-lookup`. Questions:
* Which models fit this task, with what training data and independent evaluation?
* Which reporting standard for ML validation is current?
* What calibration guidance exists for the intended use?
Sources, in order: model repository, release notes, license; the reporting-standard paper; independent benchmarks of recent years (PubMed, Europe PMC); preprints, labeled.
Check: release date, training-data overlap with our test set.

## Verify
* Shuffled labels give chance performance; a trivial baseline sets the floor.
* Re-split by a stricter unit; a large drop means leakage. Failing: do not report; fix the split.
* Calibration curve on held-out data; other seeds agree.

## Failure modes
* Tuning on the test set; normalizing before splitting.
* A pooled score hiding gene-level failure.
* Scores read as probabilities.

## Record and report
`analysis-log`: question, date, sources, versions, not verified, recheck date. Report split rule, baseline, metrics with intervals, calibration, versions, hardware, seeds.

Seeds: `references/where-to-look.md`.
