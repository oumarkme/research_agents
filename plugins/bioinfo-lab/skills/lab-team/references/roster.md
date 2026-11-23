# Group roster

The roster lists what each agent is good at and where its work usually goes next. It is a guide, not a routing rule: the main session decides whether to delegate (`lab-team`). "Reviewed by" names who can check that agent's work before it leaves the project.

| Agent | Owns | Needs | Returns | Hands off or escalates to | Reviewed by |
|---|---|---|---|---|---|
| `assistant` | Searches, public-ID lookups, log and job checks, test runs, exact edits | Paths, IDs, exact task | Paths, line numbers, quoted values | Main session when judgment is needed | Main session (spot check) |
| `literature-reviewer` | Literature search and evidence labels | Question, public identifiers, date range | Findings with verified or not labels | `writer`; `statistician` for effect-size disputes | `reviewer` (claims) |
| `data-steward` | Layout, metadata, FAIR and MIAPPE, repository, data plan, consent-scope check | Data inventory, consent and permit documents | Layout, dictionary, plan, consent flags | Main session, then the user, for consent or law; `bioinformatician` for processing | `reviewer` |
| `bioinformatician` | One-off sequencing analyses, long jobs, sample and genotype tables | Raw data paths, reference, organism, scale, host limits | Checked tables, logs, pipeline run record | `statistician` (models); `clinical-geneticist` (variants); `software-engineer` (reusable code) | `reviewer` |
| `microbial-genomicist` | Bacterial, fungal, viral, pathogen, metagenome, amplicon work | Reads or assemblies, isolate metadata | Assemblies, AMR calls, trees, tables | `evolutionary-genomicist` (deep phylogeny, selection); `statistician` | `reviewer` |
| `evolutionary-genomicist` | Trees, selection tests, comparative and non-model population genomics | Assemblies or alignments, taxon sampling | Orthogroups, trees, test results | `statistician` (test checks); `writer` | `reviewer` |
| `breeder` | Breeding design, trials, selection decisions, genetic gain | Objective, population, pedigree, phenotypes | Scheme, selection recommendation | `statistician` (fit); `data-steward` (metadata, permits) | `reviewer` |
| `statistician` | Method choice, models, multiple testing, power, number recomputation | Design statement, clean tables | Model, thresholds, recomputed numbers | `writer`; back to `bioinformatician` if QC fails | `reviewer` |
| `clinical-geneticist` | Germline variant classification, gene-disease fit, report fields | Evidence table, build, transcript, phenotype terms | Classification with evidence, draft report fields | Main session, then the user and physician, for decisions; `literature-reviewer` | `reviewer` (blind variant mode) |
| `software-engineer` | Reusable tools, packages, tests | Spec, language, target platform | Code, tests, README | `bioinformatician` (runs); `writer` (docs) | `reviewer` (code) |
| `writer` | Manuscripts, grants, reports, READMEs | Final numbers, claims, verified references | Draft text, lint result | `translator`; `figure-maker` | `reviewer` (claims audit) |
| `figure-maker` | Figures, posters, decks, legibility check | Final numbers, target size, journal | Figure files, script | `writer` (captions) | `reviewer` if the figure backs a claim |
| `translator` | Translation of final academic text | Final source, language pair, glossary | Translated file, check report | `writer` for source ambiguities | `reviewer` (final submission) |
| `reviewer` | Independent review of code, claims, blind variants | Specification, files, evidence | Correctness and requirement gaps | Main session, then the user | Not applicable |

## Common sequences (not binding)

* Assay planning: `data-steward` (`sample-and-assay-planning`) -> `bioinformatician` -> `statistician` -> `reviewer` -> `writer`.
* Variant questions: `bioinformatician` -> `clinical-geneticist` -> `reviewer` (blind).
* Microbial outbreak: `microbial-genomicist` -> `evolutionary-genomicist` -> `reviewer`.
* Breeding: `breeder` -> `statistician` -> `data-steward`; `reviewer` on the claim.
* Manuscript: `literature-reviewer` -> `writer` -> `reviewer` -> `translator` (if needed).

These are examples; dependent steps often fit better in the main session.

## Gaps (no agent created)

* Experimental and assay design liaison (sampling, replicates, batch layout, wet-lab handover): covered today by `data-steward` with `sample-and-assay-planning` and by `statistician` for power.
* Systems and HPC engineer (queues, containers, storage, job failures): covered by `bioinformatician` and `software-engineer` with `hpc-resource-planning` and `workflow-engines-and-containers`.
* Project coordination (milestones, task tracking across sessions): covered by the main session with `analysis-log` and `research-planning`.
* Ethics and compliance officer (consent, permits, access and benefit sharing): covered by `data-steward` with `research-ethics`; the user decides.
* Single-cell, proteomics, and structural biology specialists: covered by `bioinformatician` with on-demand skills; depth is limited.
