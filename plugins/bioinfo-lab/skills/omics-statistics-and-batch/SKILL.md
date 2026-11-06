---
name: omics-statistics-and-batch
description: 'Use when testing expression, methylation, or count data, sizing replicates, or detecting and correcting batch effects. Not for the design statement (study-design) or GWAS and QTL (association-studies).'
---

# Omics statistics and batch

## Capability
Test omics differences with batch modeled. Correct: effect separable from batch, independent replicates, a sound p-value histogram, effect sizes with intervals.

## Decide
1. Tabulate every batch variable against condition. Fully confounded: stop, no analysis separates them; ask for a design fix (`study-design`).
2. The replicate is the biological sample; cells from one donor are pseudoreplicates.
3. Size replicates from empirical studies and pilot simulation.
4. Look first: ordination by batch, condition, quality; check sample swaps.
5. Use a model that fits the data type (counts: count model).
6. Known batch goes in the model, not subtracted first; corrected values are for display.
7. Unknown factors: surrogates or negative controls; state their number and that they do not track condition.
8. Control FDR within one hypothesis family; state test count and filter; test against a stated effect-size threshold.

## Find current information
Follow `current-methods-lookup`. Questions:
* Which testing and batch methods fit this data type and design, with independent benchmarks?
* What replicate numbers do recent empirical studies support for our effect sizes?
Sources, in order: method docs and release notes; Bioconductor-type landing pages; recent independent benchmarks (PubMed, Europe PMC); preprints, labeled.
Check: release date, maintenance, benchmark data like ours.

## Verify
* P-value histogram: flat plus a spike near 0 is expected; humps or U shapes mean a model problem.
* Run with and without batch terms; flipped conclusions are fragile.
* Permuted condition labels give few hits.
* Replicates agree within and across batches.
* Failing (inflation, flips): report it; do not trim the list.

## Failure modes
* Batch removal in unbalanced groups creates false differences.
* Clustering, then testing the clusters.
* Correcting before a split.
* Filters chosen after seeing results.

## Record and report
`analysis-log`: question, date, sources, versions, not verified, recheck date. Report n per group and batch, the batch-by-condition table, formula, normalization, filter, FDR method and test count, effect sizes with intervals, seeds.

Seeds: `references/`.
