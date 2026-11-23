---
name: team-playbooks
description: 'Use when you plan a multi-step workflow (pipeline, breeding, GWAS, diagnostic case, outbreak, comparative genomics, manuscript, figures, data release) and want a typical order of skills and checks. Not for a single task (lab-team).'
---

# Team playbooks

Typical orders, not fixed chains: pick the line that matches and skip any step the task does not need. Look up current methods (`current-methods-lookup`) before choosing a tool. Call `reviewer` once before a result leaves the project, only if it backs a reported claim.

* Small script or edit: `coding-style`. Reusable tool: `coding-style` with `pipeline-testing-and-ci`.
* Sequencing pipeline: `sequencing-pipelines` on a small input, then the full run (`long-analysis-job` if heavy).
* Breeding analysis or genomic prediction: objective and scheme (`quantitative-genetics`), genotype prep (`array-genotyping-and-imputation`), fit and validation (`genomic-prediction`, `study-design`), report to the breeder (`stakeholder-communication`).
* GWAS or Mendelian randomization: QC, then model and thresholds (`association-studies`).
* Plant or animal breeding project: `quantitative-genetics`; trial and pedigree metadata and permits (`breeding-metadata-and-archives`, `access-benefit-sharing-and-data-governance`); genotypes (`polyploid-genotyping-dosage`, `livestock-genotype-qc-imputation`).
* Microbial or pathogen outbreak: assembly, AMR, and tree (`bacterial-genome-assembly-annotation`, `amr-genotype-phenotype`, `pathogen-genomic-epidemiology`); metadata and sharing terms (`data-stewardship`).
* Comparative genomics: taxon sampling, orthogroups, trees, and selection tests (`orthology-comparative-genomics`, `phylogenetic-inference`, `species-tree-and-selection`).
* Rare disease or diagnostic case: public-ID lookups to `assistant`; classify from the evidence table (`variant-interpretation`); `reviewer` classifies blind; adjudicate only discordant variants; the report goes to the clinician (`stakeholder-communication`).
* Manuscript or grant: claims and design statement (`study-design`, `research-planning`); `literature-review` in parallel by question; `writing`; `reviewer` claims audit; `translator` after the English text is final.
* Figures or talk: `plotting` or `slides` from final numbers.
* Data release: `data-stewardship`; the user decides any consent or sharing question (`research-ethics`).
