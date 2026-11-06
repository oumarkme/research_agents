---
name: quantitative-genetics
description: 'Use when designing or analyzing breeding data in plants or animals: heritability, BLUP, GBLUP, single-step models, multi-environment trials, G x E, selection response, genetic gain. Not for validation (genomic-prediction).'
---

# Quantitative genetics for breeding

## Capability

Estimate genetic variance, breeding values, and gain from breeding data. Definitions and derivations: `references/methods.md`. See also `popgen-inbreeding-ne-germplasm`, `plant-field-trial-gwas`, `livestock-genotype-qc-imputation`, `genomic-prediction`.

## Decide

* Before modeling: breeding objective, target environments, trait, selection unit, cycle length. Fix or report pedigree errors, layout, missing cells, contemporary groups, outliers.
* Write the model equation: fixed and random effects, covariance of the genetic effect, REML for variance components.
* Relationship matrix: pedigree `A`, genomic `G`, or single-step `H` when only some animals are genotyped. State the `G` construction (centering, scaling, base allele frequencies) and keep it identical in training and prediction; `A` and `G` need the same base population.
* Plants, multi-environment: two-stage (stage 1 adjusted means with design and spatial terms; stage 2 weighted by stage-1 error) or one-stage; say which and why. Compare any G x E structure with the main-effect model.
* Animals: animal model, contemporary groups fixed, maternal and permanent-environment effects when data call for them.

## Find current information

Follow `current-methods-lookup`. Ask:
* Which mixed-model software handles our model, size, and G x E structure now?
* Which spatial or G x E model do recent trial-analysis papers support for our design?
* What does the breed association, breeding program, or evaluation service require?
* Which current text defines the quantity we report?

## Verify

* Convergence, singular fits, variance components at the boundary, residual plots.
* Simulate data with known variances and recover them.
* Heritability lies in [0, 1]; entry-mean heritability increases with replicates and environments; `G` diagonal averages about 1+F (near 2 in fully inbred lines), off-diagonals about 0, under its base.
* Accuracy is estimated on data not used for selection.

## Failure modes

Adjusted means treated as error-free in stage 2; heritability and accuracy estimated on the selection data; accuracy of selected parents applied to the whole population; mixed `A` and `G` bases.

## Record and report

Heritability with type, formula, and standard error. Response `R = h² S` and gain `ΔG = i r σA / L`, with accuracy defined. Inbreeding rate or effective size (animals); variance and relatedness after selection (plants). Software, versions, model equation. Seeds: `references/where-to-look.md`.
