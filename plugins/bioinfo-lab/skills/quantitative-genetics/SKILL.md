---
name: quantitative-genetics
description: 'Use when designing or analyzing breeding data in plants or animals: heritability, BLUP, GBLUP, single-step models, multi-environment trials, G x E, selection response, and genetic gain.'
---

# Quantitative genetics for breeding

## Before modeling

* State the breeding objective, the target population of environments, the trait definition, the selection unit (plot, plant, animal, family), and the cycle length.
* Check the data: pedigree errors (Mendelian inconsistencies, duplicate IDs), trial layout, missing cells, contemporary groups for animals, and outliers. Fix or report each before fitting.

## Model

* Write the model equation. Name the fixed and random effects, the covariance of the random genetic effect, and the estimation method (REML for variance components). Report software and version.
* Relationship matrix: pedigree `A`, genomic `G`, or single-step `H` when only a subset is genotyped. Give the `G` construction (centering, scaling, base allele frequencies) and keep it identical between training and prediction runs.
* Plants, multi-environment trials: prefer a two-stage analysis (stage 1 adjusted means per environment with design and spatial terms; stage 2 across environments, weighted by stage-1 error) or a one-stage model. Say which, and why. Compare any G x E structure (factor analytic, unstructured, reaction norm) with the main-effect model.
* Animals: animal model with pedigree, contemporary groups as fixed effects, maternal and permanent-environment effects when the data call for them. Use single-step when genotyped and ungenotyped animals mix.
* Check convergence, singular fits, variance components at the boundary, and the residual structure.

## Quantities to report

* Heritability with its type (narrow-sense, broad-sense, entry-mean, realized), formula, and standard error. Entry-mean heritability depends on the number of replicates and environments.
* Selection response and genetic gain per year: `R = h² S`, and `ΔG = i r σA / L` (intensity, accuracy, additive standard deviation, cycle length). Define accuracy (correlation with the true breeding value, or with the phenotype divided by `h`).
* Diversity and inbreeding: rate of inbreeding or effective population size for animals; genetic variance and relatedness after selection for plants. Selection reduces variance, so report it.

## Common failures

* Treating adjusted means as error-free in stage 2.
* Estimating heritability and accuracy on the same data used to select.
* Mixing a pedigree `A` and a genomic `G` that use different base populations.
* Reporting the accuracy of a model fitted to selected parents as if it applied to the whole population.

Methods and sources: `${CLAUDE_SKILL_DIR}/references/methods.md`. For validation of predictions, load `genomic-prediction`. For test choice and multiple testing, load `study-design`.
