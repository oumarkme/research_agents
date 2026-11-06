# Metagenomics checks (durable)

| Control | Purpose | Read as |
|---|---|---|
| Extraction blank | reagent and kit contaminants | taxa here and in low-biomass samples are suspect |
| No-template PCR or library control | amplification contamination | same |
| Mock community | bias of the whole workflow | observed against expected |
| Positive replicate | run-to-run drift | between-batch distance |

Low-biomass samples (tissue, blood, lung) need all four.

Read-loss log: raw, trimmed, host-removed, classified, assigned to species.

Statistics log: transformation, zero handling, prevalence filter, differential-abundance methods, covariates, multiple-testing method. Fix them in the analysis plan before unblinding groups.

STORMS items: design and sampling, lab methods, sequencing, bioinformatics (versions, databases), statistics, results, discussion. Add MIxS fields for environmental samples. Fill the checklist from the log, not from memory.
