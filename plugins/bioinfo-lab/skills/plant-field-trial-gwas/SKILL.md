---
name: plant-field-trial-gwas
description: 'Use when running GWAS or QTL mapping on replicated, spatially modelled field trials, single or multi-environment. Not for generic association QC (association-studies) or variance components and selection (quantitative-genetics).'
---

# Plant field-trial GWAS

## Capability
Map markers on adjusted means that carry the trial design and stage-1 uncertainty. A correct result has no gradient posing as a QTL, calibrated statistics, replicating QTL. QC and reporting: `association-studies`; G x E: `quantitative-genetics`.

## Decide
1. Record design, replicates, plot row and column, and check lines. No coordinates, stop.
2. Stage 1 per environment: design plus spatial terms, chosen by information criterion and residual maps.
3. Carry each mean's weight into stage 2; unweighted means distort unbalanced data.
4. Stage 2 across environments: environment, genotype, G x E terms. One environment: use stage-1 means.
5. Report plot and entry-mean heritability; justify exclusions.
6. Mixed model with kinship and structure control; the tested region stays out of its own kinship.
7. Multiple-testing rule (effective tests or permutation): state which.
8. G x E: per-environment tests plus meta-analysis, or marker-by-environment terms.
9. Name the validation set (other year, held-out environment) before the scan.

## Find current information
Follow `current-methods-lookup`. Ask: which mixed-model and GWAS software is maintained and handles our design, weights, and markers; what recent plant GWAS reviews say on kinship and thresholds; which multi-environment methods were benchmarked.
Search: software docs and release notes, recent reviews in PubMed, labeled preprints. Check release date, crop, benchmark size.

## Verify
* Stage-1 residual maps show no row or column structure.
* QQ plot and inflation calibrated; compare raw plot values with adjusted means.
* Permuted genotype labels give no hits.
* Known-answer: spike a simulated QTL into real genotypes and recover it.
* QTL replicate in the validation set; edge effects overstate.

## Failure modes
* Unmodeled gradient called a QTL.
* Unweighted means, unbalanced data.
* Kinship includes the tested chromosome.
* Winner's curse.

## Record and report
Log: question, date, sources, versions, not verified, recheck. Report design, spatial model, heritability, weights, threshold rule, per-environment effects, validation.

See `references/where-to-look.md`.
