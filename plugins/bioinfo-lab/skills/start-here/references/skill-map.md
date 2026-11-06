# Skill map by task

Names only. Open the skill, not this file, for steps. Single-cell and nf-core tasks are in the optional separate bio-research plugin (if installed).

| Area | Skills |
|---|---|
| Entry and rules | `start-here`, `lab-rules`, `lab-team`, `agent-brief`, `team-playbooks`, `update` |
| Calling and QC | `run-qc-and-demultiplexing`, `short-read-germline-calling`, `exome-and-panel-analysis`, `sample-identity-and-contamination`, `sv-cnv-calling`, `somatic-calling`, `repeat-expansions`, `long-read-ont-pacbio`, `difficult-genes-and-mito`, `genome-browser-review` |
| Assembly, annotation, references | `genome-assembly-and-curation`, `gene-annotation-te-repeats`, `pangenome-and-pav`, `reference-genome-selection`, `reference-genomes-and-liftover` |
| Interpretation (human) | `variant-interpretation`, `annotation-and-databases`, `rare-disease-prioritization`, `pharmacogenomics-and-hla`, `clinical-pipeline-validation` |
| Plant and animal breeding | `quantitative-genetics`, `genomic-prediction`, `non-human-genomes-and-polyploidy`, `polyploid-genotyping-dosage`, `reduced-representation-genotyping`, `livestock-genotype-qc-imputation`, `array-genotyping-and-imputation`, `plant-field-trial-gwas`, `popgen-inbreeding-ne-germplasm`, `breeding-metadata-and-archives`, `agricultural-microbiome` |
| Microbial and pathogen | `bacterial-genome-assembly-annotation`, `amr-genotype-phenotype`, `pangenome-analysis-prokaryote`, `pathogen-genomic-epidemiology`, `fungal-genomics`, `metagenomics`, `amplicon-metabarcoding-analysis` |
| Evolution and comparative | `phylogenetic-inference`, `species-tree-and-selection`, `orthology-comparative-genomics`, `population-genetics`, `model-organism-resources` |
| Omics assays | `rna-seq-and-splicing`, `methylation-and-epigenomics`, `proteomics-metabolomics-integration` |
| Engineering and HPC | `workflow-engines-and-containers`, `sequencing-pipelines`, `hpc-resource-planning`, `troubleshooting-failed-jobs`, `pipeline-testing-and-ci`, `performance-profiling`, `storage-and-data-lifecycle`, `omics-data-wrangling`, `coding-style`, `genomics-pitfalls` |
| Statistics | `study-design`, `association-studies`, `omics-statistics-and-batch`, `deep-learning-genomics` |
| Planning and data | `sample-and-assay-planning`, `research-planning`, `data-stewardship`, `analysis-log` |
| Research conduct | `research-ethics`, `animal-research-ethics-3rs`, `access-benefit-sharing-and-data-governance`, `open-science-reproducible-paper`, `trusted-sources`, `current-methods-lookup`, `ai-tools-in-analysis` |
| Writing and figures | `writing`, `humanizer`, `translator`, `plotting`, `slides`, `project-readme`, `stakeholder-communication` |

## By user type

| If the user is | Example request | Route |
|---|---|---|
| Plant or animal breeder | "Rank my lines with genomic prediction" | `breeder`; `quantitative-genetics`, `genomic-prediction` |
| Microbiologist or pathogen researcher | "Assemble this isolate and call resistance genes" | `microbial-genomicist`; `bacterial-genome-assembly-annotation`, `amr-genotype-phenotype` |
| Evolutionary or comparative biologist | "Build a species tree and test selection" | `evolutionary-genomicist`; `phylogenetic-inference`, `species-tree-and-selection` |
| Physician or clinical geneticist | "Classify this variant" | `clinical-geneticist`; `variant-interpretation` |
| Wet-lab scientist or technician | "Plan QC and batches for 96 samples" | `sample-and-assay-planning`, `data-stewardship` |
| Bioinformatician | "Build and benchmark a calling pipeline" | `bioinformatician`; `sequencing-pipelines` |
| Statistician | "Check this mixed model" | `statistician`; `study-design` |
| Newcomer to a method | "Explain GWAS, then show the steps" | `association-studies` in plain language |
| Project lead | "Plan aims; check my manuscript claims" | `research-planning`; `writer`, `reviewer` |
| Data manager or curator | "Document this dataset for sharing" | `data-steward`; `data-stewardship` |
| Anyone with a consent, permit, or privacy question | "Can I share these data or samples?" | `research-ethics`, `access-benefit-sharing-and-data-governance` (stop and ask the data owner) |
| Anyone needing one fact or reference | "Is this PMID real?" | `assistant`; `trusted-sources` |
| Anyone needing a translation | "Translate this abstract" (target language from CLAUDE.md, else ask) | `translator` |
| Anyone needing slides, a talk, or a figure | "Make a 10-minute talk" (HTML default, PDF on request) | `figure-maker`; `slides`, `plotting` |
| Anyone needing a literature review | "What is known about this gene?" | `literature-reviewer`; `trusted-sources` |
| Anyone asking about plugin version or updates | "Is there a newer version?" | `update` |
| Anyone with a long, multi-step analysis | "Resume the pipeline from last week" | `analysis-log` |
| Anyone planning a multi-agent workflow | "Plan a GWAS with the team" | `lab-team`; `team-playbooks`, `agent-brief` |
