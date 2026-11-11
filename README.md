# research_agents

A Claude plugin marketplace that adds a complete research group for bioinformatics, genetics, genomics and breeding across all organisms (research use only). You are the PI and decide. The main session is the deputy PI: it plans, splits work, briefs the 14 agents (the group members), and checks and integrates their results. The 84 skills are capabilities: each says where to find current information, looks up version-sensitive facts through `current-methods-lookup`, and states how to verify results.

Status: stable · Version: 2.0.1 · License: MIT · Plugin: `bioinfo-lab` (install as `bioinfo-lab@research_agents`)

Ask in plain language, and the right method loads: genomic prediction for breeders, outbreak phylogenetics for pathogen work, species trees and selection tests for evolutionary biology, ACMG/AMP variant classification for clinicians, pipeline QC for bioinformatics. No server, conda, or container is required.

## Install

Claude web app: Customize > Plugins > Add > Add marketplace, enter `oumarkme/research_agents`, then select `bioinfo-lab` and Add. For a private repository, connect GitHub and allow the Claude GitHub App when asked.

Claude Code:

```text
/plugin marketplace add oumarkme/research_agents
/plugin install bioinfo-lab@research_agents
```

Skills work in chat, Cowork, and Claude Code. Agents work in Cowork and Claude Code. Ask for `/bioinfo-lab:update` to compare your version with the latest release and get the exact commands: `/plugin marketplace update research_agents`, `/plugin update bioinfo-lab@research_agents`, then `/reload-plugins`.

Slides: ask for a talk and the `slides` skill downloads the newest [slide_template](https://github.com/oumarkme/slide_template) and builds an HTML deck (PDF on request).

## Quick start

Type a request. Skills load by themselves; call one directly as `/bioinfo-lab:<skill>`.

```text
/bioinfo-lab:start-here
Rank my 300 wheat lines for yield with genomic prediction, and tell me how to validate it.
```

Intended behavior (not yet tested end to end): the breeder agent states the objective and validation scheme (`quantitative-genetics`, `genomic-prediction`), asks at most one question, and answers with the baseline model and the metrics to report.

## Usage

| Agent | Model | Effort | Role |
|---|---|---|---|
| `assistant` | Haiku | low | Search, lookups, log checks, test runs |
| `data-steward` | Sonnet | low | Metadata, FAIR, repositories, data plans |
| `translator` | Sonnet | medium | Academic English to or from any language (target from your CLAUDE.md, else it asks) |
| `writer` | Sonnet | medium | Manuscripts, grants, reports, READMEs |
| `bioinformatician` | Sonnet | medium | Sequencing QC, calling, assembly, workflows, long jobs |
| `microbial-genomicist` | Sonnet | medium | Bacterial, fungal, viral, and pathogen genomics, metagenomics, AMR, outbreak trees |
| `evolutionary-genomicist` | Sonnet | medium | Phylogenetics, selection tests, comparative and non-model population genomics |
| `software-engineer` | Sonnet | medium | Reusable tools in Python, R, C++, Rust |
| `breeder` | Sonnet | medium | Plant and animal breeding, genomic selection |
| `statistician` | Sonnet | high | Models, tests, validation |
| `clinical-geneticist` | Sonnet | high | ACMG/AMP classification, physician reports |
| `reviewer` | Opus | high | One independent review before results are reported |
| `literature-reviewer` | Sonnet | medium | Literature search and evidence review with verified citations |
| `figure-maker` | Sonnet | low | Figures, posters, and decks with the legibility check |

| Group | Skills |
|---|---|
| Entry and rules | `start-here`, `lab-rules`, `lab-team`, `agent-brief`, `team-playbooks`, `update` |
| Quantitative | `study-design`, `quantitative-genetics`, `genomic-prediction`, `association-studies` |
| Data and sequencing | `sample-and-assay-planning`, `sequencing-pipelines`, `genomics-pitfalls`, `data-stewardship` |
| Clinical | `variant-interpretation` |
| Code and projects | `coding-style`, `project-readme`, `analysis-log`, `slides` |
| Evidence and writing | `trusted-sources`, `writing`, `humanizer`, `translator`, `plotting` |
| Communication and compliance | `stakeholder-communication`, `research-ethics`, `research-planning` |

## Skills by area

The task skills below load on demand; the agents call them by name (`start-here` has the routing).

| Skill | Purpose |
|---|---|
| `run-qc-and-demultiplexing` | A new Illumina or ONT run arrives and needs demultiplexing, FASTQ or run QC, and a pass or re-run call |
| `short-read-germline-calling` | Aligning short reads and calling, joint genotyping, filtering, or benchmarking germline SNVs and indels from WGS, WES, or panels |
| `exome-and-panel-analysis` | Analyzing WES or targeted panels: capture kit and BED, coverage metrics, per-gene gaps, padding, kit and panel versions, capture CNV |
| `sample-identity-and-contamination` | Confirming sample sex, relatedness, pedigree, cross-sample contamination, or a suspected swap in sequencing or array data |
| `sv-cnv-calling` | Detecting, merging, filtering, or benchmarking structural variants or copy-number changes from short-read, exome, or long-read data |
| `repeat-expansions` | Genotyping short tandem repeats or testing for pathogenic repeat expansions (FMR1, C9orf72, RFC1, HTT) from short or long reads |
| `long-read-ont-pacbio` | Processing ONT or PacBio reads: basecalling, model choice, alignment, small variants, SV, phasing, methylation, assembly, or run metrics |
| `difficult-genes-and-mito` | A gene has a paralog, pseudogene, or segmental duplication (SMN1, GBA1, CYP2D6, HBA1) or a mitochondrial variant needs calling |
| `somatic-calling` | Calling somatic SNVs and indels from tumor-normal, tumor-only, or low-VAF mosaic data and filtering them |
| `reference-genomes-and-liftover` | Choosing a reference build or contig naming, or converting coordinates and VCFs between builds |
| `annotation-and-databases` | Annotating variants or choosing VEP, ANNOVAR, snpEff, transcripts, or gnomAD and ClinVar releases |
| `rare-disease-prioritization` | Ranking candidate variants in a proband, trio, or family: filter ladder, inheritance models, HPO ranking, reanalysis |
| `pharmacogenomics-and-hla` | Calling star alleles, diplotypes, or HLA types from WGS, WES, RNA, or arrays, or reporting CPIC drug-gene results |
| `population-genetics` | Computing PCA, ancestry, admixture, kinship, IBD, Fst, or selection scans, or building a reference panel |
| `array-genotyping-and-imputation` | Processing SNP-array or low-pass data: array QC, strand and build, phasing, imputation, panel choice, info filters |
| `rna-seq-and-splicing` | Analyzing bulk RNA-seq: strandedness, QC, quantification, differential expression, splicing, fusions, or outlier expression for rare disease |
| `methylation-and-epigenomics` | Analyzing methylation arrays, bisulfite, EM-seq, or ONT methylation, ChIP-seq or ATAC-seq peaks, episignatures, or cell-type composition |
| `metagenomics` | Analyzing 16S or shotgun microbiome data: host removal, taxonomic and functional profiling, assembly and binning, contamination controls, compositional statistics, STORMS reporting |
| `proteomics-metabolomics-integration` | Adding proteomics or metabolomics to genomic data: pQTL, colocalization, identifier mapping, normalization, missing values, multi-omics factor models |
| `non-human-genomes-and-polyploidy` | Working on plant or livestock genomes: reference choice, assembly and annotation, polyploid genotype calling, GBS, SNP arrays, marker files |
| `workflow-engines-and-containers` | Choosing, writing, or debugging a Nextflow, Snakemake, or WDL workflow, or setting up Apptainer, Docker, or conda software |
| `hpc-resource-planning` | Sizing cores, memory, disk, GPU, and runtime for a job, or splitting parallel jobs under the host limit |
| `troubleshooting-failed-jobs` | A pipeline step, container, or job fails, hangs, is killed, or leaves empty or truncated output |
| `pipeline-testing-and-ci` | Adding tests, regression checks, or continuous integration to a Nextflow, Snakemake, Python, or R pipeline |
| `performance-profiling` | A step is slower or heavier than expected and you must find the bottleneck and tune threads, I/O, compression, or indexing |
| `storage-and-data-lifecycle` | Planning storage, compression, transfer, checksums, backup, retention, or cleanup of FASTQ, pod5, BAM, CRAM, and VCF |
| `omics-statistics-and-batch` | Testing expression, methylation, or count data, sizing replicates, or detecting and correcting batch effects |
| `omics-data-wrangling` | Reshaping, filtering, or joining large genomic tables and intervals in pandas, polars, R, Bioconductor, bcftools, bedtools, or tabix |
| `deep-learning-genomics` | Training, validating, or applying neural models to genomic data (variant effect predictors, sequence models, basecallers) |
| `genome-browser-review` | Visually reviewing variants, SVs, repeats, or splicing in IGV or a similar browser, or saving screenshots and review decisions |
| `clinical-pipeline-validation` | Validating, freezing, or changing a diagnostic NGS bioinformatics pipeline, or preparing evidence for accreditation |
| `ai-tools-in-analysis` | An AI coding or writing assistant helps with analysis code, numbers, or text: what to delegate, verification, provenance, disclosure |
| `bacterial-genome-assembly-annotation` | Assembling, polishing, annotating, and quality-checking a bacterial isolate genome from long or hybrid reads |
| `amr-genotype-phenotype` | Detecting antimicrobial resistance genes and mutations in bacterial genomes and relating them to phenotype |
| `pangenome-analysis-prokaryote` | Comparing gene content across many bacterial or archaeal genomes: core and accessory genes, method choice, annotation consistency, recombination |
| `pathogen-genomic-epidemiology` | Turning pathogen sequence data into consensus genomes, lineages, phylogenies, time trees, and outbreak reports with metadata and data sharing |
| `fungal-genomics` | Assembling, annotating, or comparing fungal genomes (yeast, molds, plant and human pathogens) |
| `amplicon-metabarcoding-analysis` | Analyzing 16S, 18S, ITS, or other amplicon or eDNA metabarcoding reads: ASV inference, taxonomy, controls, contamination, reporting |
| `phylogenetic-inference` | Building a maximum-likelihood tree from DNA, codon, or protein sequences of any organism: alignment, trimming, model choice, support, rooting, reporting |
| `species-tree-and-selection` | Estimating a species tree from many gene trees, or testing selection on codon alignments (HyPhy) |
| `orthology-comparative-genomics` | Inferring orthogroups, gene-family gain and loss, synteny, or whole-genome duplication across species of any kingdom |
| `model-organism-resources` | Looking up genes, alleles, phenotypes, orthologs, or GO annotations for fly, worm, zebrafish, mouse, rat, frog, or yeast, or citing and downloading these resources |
| `popgen-inbreeding-ne-germplasm` | Estimating structure, inbreeding, ROH, or effective population size in non-model, crop, livestock, or genebank samples |
| `genome-assembly-and-curation` | Assembling a eukaryotic genome from long reads and Hi-C: haplotype strategy, scaffolding, contamination screening, QC, curation, reporting |
| `gene-annotation-te-repeats` | Annotating repeats, transposable elements, and genes on a eukaryotic assembly, or transferring an annotation |
| `pangenome-and-pav` | Building or using a eukaryotic pangenome (graph or linear), calling presence/absence variation, or genotyping SVs across accessions or breeds |
| `reference-genome-selection` | Choosing or recording the reference assembly and annotation for a non-human eukaryote project, or deciding to build a new one |
| `polyploid-genotyping-dosage` | Calling or analyzing genotypes in tetraploid, hexaploid, or other polyploid crops as allele dosage |
| `reduced-representation-genotyping` | Designing or analyzing GBS, RAD, DArT, or skim-sequencing data, with or without a reference, including filters and low-coverage imputation |
| `livestock-genotype-qc-imputation` | Cleaning livestock SNP-array genotypes: parentage and pedigree checks, sex and breed checks, imputation to a denser panel |
| `plant-field-trial-gwas` | Running GWAS or QTL mapping on replicated, spatially modelled field trials, single or multi-environment |
| `agricultural-microbiome` | Planning or reporting rumen, soil, or rhizosphere microbiome studies: sampling, controls, amplicon versus shotgun, host reads, reporting standards |
| `breeding-metadata-and-archives` | Describing or sharing phenotype, sample, and sequence data from breeding or agricultural projects (MIAPPE, BrAPI, ontologies, FAANG, ENA, EVA) |
| `access-benefit-sharing-and-data-governance` | Sample, sequence, or share data from wild, germplasm, microbial, or community-held material across borders |
| `animal-research-ethics-3rs` | Planning or reporting animal experiments or field and wildlife sampling: 3Rs, ARRIVE 2.0, sample size, approvals, and permits |
| `open-science-reproducible-paper` | Assemble the reproducibility package for a paper: code, environment, workflow, deposits with DOIs, preprint, and TOP checks |
| `current-methods-lookup` | A decision depends on version-sensitive facts: choosing a tool, options, thresholds, database releases, benchmarks, or guidelines |

If you run jobs on a shared server or cluster, put its rules (host, limits, read-only paths, scratch) in your global or project `CLAUDE.md`. Otherwise nothing needs setup.

## Methodology

1. Scope: skills map to the ISCB bioinformatics core competencies (Mulder et al., 2018) and to domain standards for breeding, prediction, association studies, sequencing, microbial and evolutionary genomics, clinical genetics, and data stewardship. The map is in `plugins/bioinfo-lab/skills/lab-team/references/competency-map.md`.
2. Evidence: each skill cites primary sources. On 2026-10-22 the 45 cited DOIs were checked in Crossref and 136 resource URLs with live requests; failures are flagged in the catalog.
3. Cost control: each agent preloads `lab-rules` (under 3 KB) and at most one core skill for its role (for example, `writer` preloads `writing`); every other skill, including the 60 task skills, loads on demand when the agent calls it. Detail sits in `references/` files that load on demand. Each agent has a model and effort tier and no hard turn cap; it writes a checkpoint every 30 tool calls (`lab-rules`), and the main session handles small work (`lab-team`).
4. Long work: `analysis-log` keeps a progress file, a claims ledger, and provenance, so a new session resumes from the files and not from memory.
5. Design basis: delegation, context, and testing choices follow Anthropic's published engineering guidance; each choice and its source is listed in `plugins/bioinfo-lab/skills/lab-team/references/design-basis.md`.
6. Layout: `.claude-plugin/marketplace.json`; `plugins/bioinfo-lab/` with `agents/`, `skills/<name>/SKILL.md`, and `.claude-plugin/plugin.json`; `tests/` with the CI checks.

Limits: skills are guidance, not validated pipelines, and no skill has been tested end to end on real data. Instructions are advice, not enforcement: a rule that must never be skipped belongs in a hook or permission rule in your own settings. Policy items taken from secondary sources (ICMJE and Springer Nature AI rules, national data-protection and access-and-benefit-sharing law) must be checked against the official text. Some sites block scripts (OMIM, UK Biobank, TAIR); use a browser.

## Develop

* Add a skill: `plugins/bioinfo-lab/skills/<name>/SKILL.md` with `name` (equal to the folder) and a "Use when ..." `description`. Keep `SKILL.md` near 2.5 KB for new skills and under 3.6 KB for older ones (the trigger, core steps, and pointers), and put long material in `references/`.
* Add an agent: `plugins/bioinfo-lab/agents/<role>.md` with `model`, `effort`, `tools`, and `skills`. Choose the cheapest tier that works.
* Check with `claude plugin validate . --strict`, test with `claude --plugin-dir ./plugins/bioinfo-lab`, run the checks in `tests/` (also run by CI), and raise `version` in `plugin.json` for each release.

## References

Mulder, N. J., et al. (2018). The development and application of bioinformatics core competencies to improve bioinformatics training and education. *PLOS Computational Biology, 14*(2), e1005772. https://doi.org/10.1371/journal.pcbi.1005772

Claude documentation (checked 2026-10-22): [Create a marketplace](https://code.claude.com/docs/en/plugin-marketplaces), [Plugin components](https://code.claude.com/docs/en/plugins/components), [Plugins on claude.ai](https://claude.com/docs/plugins/overview).

## License

MIT. See `LICENSE`.
