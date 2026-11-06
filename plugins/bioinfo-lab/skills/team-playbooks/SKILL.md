---
name: team-playbooks
description: 'Use when you plan a multi-step workflow across team agents (pipeline, breeding, GWAS, diagnostic case, outbreak, comparative genomics, manuscript, figures, data release) and need the agent order.'
---

# Team playbooks

The deputy PI picks the matching line, briefs each group member (`agent-brief`), and reports to the PI. Step 0 of every line below: the member looks up current methods (`current-methods-lookup`) before choosing a tool.

* Small script or edit (3 tool calls or fewer): main session with `coding-style`. Larger or reusable: `software-engineer`.
* Sequencing pipeline: `bioinformatician` on a small input, then full run; `reviewer` once only if the output backs a reported result or a shared pipeline.
* Breeding analysis or genomic prediction: `breeder` sets objective and scheme, `statistician` fits and validates (`quantitative-genetics`, `genomic-prediction`), `bioinformatician` prepares genotypes, `writer` reports to the breeder (`stakeholder-communication`).
* GWAS or Mendelian randomization: `bioinformatician` QC, `statistician` model and thresholds (`association-studies`), `reviewer` on the claim.
* Plant or animal breeding project: `breeder` sets objective, population, and scheme; `data-steward` checks trial and pedigree metadata and permits (`breeding-metadata-and-archives`, `access-benefit-sharing-and-data-governance`); `bioinformatician` prepares genotypes and QC (`polyploid-genotyping-dosage`, `livestock-genotype-qc-imputation`); `statistician` fits and validates; `reviewer` once on the claim.
* Microbial or pathogen outbreak: `microbial-genomicist` assembles, calls AMR, and builds the tree; `data-steward` checks metadata and sharing terms; `statistician` only for a model beyond the tree; `reviewer` once before the report leaves the project.
* Comparative genomics project: `evolutionary-genomicist` sets taxon sampling, orthogroups, trees, and selection tests; `bioinformatician` prepares assemblies and annotations; `statistician` checks the tests; `reviewer` on the claim.
* Rare disease or diagnostic case: `assistant` batches public-ID lookups; `clinical-geneticist` classifies from the evidence table; `reviewer` (variant mode) classifies blind; adjudicate only discordant variants; the report goes to the physician (`stakeholder-communication`).
* Manuscript or grant: main fixes claims and the design statement (`study-design`, `research-planning`); `literature-reviewer` collects literature in parallel by question; `writer` drafts; one `reviewer` claims audit before delivery. Translation after the English text is final. Brief `translator` with source path, language pair, audience, output path, and glossary path. For a final submission, add one `reviewer` claims check on Methods and Results of the translation.
* Figures or talk: `figure-maker` from final numbers; `reviewer` is not needed unless the figure backs a reported claim.
* Data release: `data-steward` prepares; the user decides on any consent or sharing question (`research-ethics`).
