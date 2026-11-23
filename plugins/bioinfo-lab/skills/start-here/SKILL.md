---
name: start-here
description: 'Use when a user asks what this plugin can do, where to start, or which skill to use, or when the request is vague.'
---

# Start here

Skills look up current methods and verify results; Claude Code's built-in agents (`Explore`, `Plan`, `general-purpose`) and `/advisor` help with bulk work, planning, and review (`lab-team`).

This plugin supports research in bioinformatics, genetics, genomics, and breeding on any organism: human, animal, plant, microbial, viral, fungal, and wild populations. Ask only if the organism, goal, or data would change the route (no data yet is fine). Infer the user's level from their words; no programming skill is required.

By need (full table in `references/skill-map.md`):

* Calling and QC: `run-qc-and-demultiplexing`, `short-read-germline-calling`, `sv-cnv-calling`, `long-read-ont-pacbio`, `genome-assembly-and-curation`.
* Human variants: `rare-disease-prioritization`, `variant-interpretation`.
* Breeding: `quantitative-genetics`, `genomic-prediction`, `plant-field-trial-gwas`.
* Microbial: `bacterial-genome-assembly-annotation`, `pathogen-genomic-epidemiology`, `metagenomics`.
* Evolution: `phylogenetic-inference`, `species-tree-and-selection`.
* Omics: `rna-seq-and-splicing`, `methylation-and-epigenomics`, `proteomics-metabolomics-integration`.
* Engineering: `workflow-engines-and-containers`, `hpc-resource-planning`, `troubleshooting-failed-jobs`.
* Statistics: `study-design`, `omics-statistics-and-batch`, `association-studies`.
* Conduct: `research-ethics`, `data-stewardship`, `open-science-reproducible-paper`.

Other routes: `translator`, `plotting`, `literature-review`, `analysis-log` (long work), `lab-team` (delegation), `claude-md-setup` (your CLAUDE.md files).

Single-cell and nf-core: the optional separate bio-research plugin, if installed; otherwise use `sequencing-pipelines` and `current-methods-lookup` (`bio-research:single-cell-rna-qc`, `bio-research:scvi-tools`, `bio-research:nextflow-development`).

For delegation guidance see `lab-team`.
