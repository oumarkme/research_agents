---
name: start-here
description: 'Use when a user asks what this plugin can do, where to start, or which skill or agent to use, or when the request is vague.'
---

# Start here

Vision: skills look up current methods and verify results; agents are the group members; the user is the PI who decides; the main session is the deputy PI.

This plugin supports research in bioinformatics, genetics, genomics, and breeding on any organism: human, animal, plant, microbial, viral, fungal, and wild populations. Ask at most two questions, only if the answers change the route: what is the organism and goal, and what data exist (none is fine). Infer the user's level from their words; no programming skill is required.

By need (full table in `references/skill-map.md`):

* Calling and QC: `run-qc-and-demultiplexing`, `short-read-germline-calling`, `sv-cnv-calling`, `long-read-ont-pacbio`, `genome-assembly-and-curation`.
* Human variants: `rare-disease-prioritization`, `variant-interpretation`; agent `clinical-geneticist`.
* Breeding: `quantitative-genetics`, `genomic-prediction`, `plant-field-trial-gwas`; agent `breeder`.
* Microbial: `bacterial-genome-assembly-annotation`, `pathogen-genomic-epidemiology`, `metagenomics`; agent `microbial-genomicist`.
* Evolution: `phylogenetic-inference`, `species-tree-and-selection`; agent `evolutionary-genomicist`.
* Omics: `rna-seq-and-splicing`, `methylation-and-epigenomics`, `proteomics-metabolomics-integration`.
* Engineering: `workflow-engines-and-containers`, `hpc-resource-planning`, `troubleshooting-failed-jobs`.
* Statistics: `study-design`, `omics-statistics-and-batch`, `association-studies`.
* Conduct: `research-ethics`, `data-stewardship`, `open-science-reproducible-paper`.

Other routes: `translator`, `figure-maker`, `literature-reviewer`, `analysis-log` (long work), `lab-team` (team plan).

Single-cell and nf-core: the optional separate bio-research plugin, if installed; otherwise use `sequencing-pipelines` and `current-methods-lookup` (`bio-research:single-cell-rna-qc`, `bio-research:scvi-tools`, `bio-research:nextflow-development`).

The deputy PI (main session) routes each step to the best-matching member (`lab-team`). Defaults: user's language and level, next step, what was not checked.
