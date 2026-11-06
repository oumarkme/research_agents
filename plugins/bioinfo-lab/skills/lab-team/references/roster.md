# Group roster

The user is the PI and decides. The main session is the deputy PI: it plans, splits work, briefs group members (`agent-brief`), integrates and checks returns, and reports to the PI. The group members below are the 14 agents. Every member escalates to the deputy PI, who passes on to the PI what belongs to the PI: scope, budget, ethics approvals, publication claims, and anything outside the brief. "Reviewer" in the last column names who checks that agent's work before it leaves the project; the reviewer itself is checked by the deputy PI.

| Agent | Owns | Needs | Returns | Hands off or escalates to | Reviewed by |
|---|---|---|---|---|---|
| `assistant` | Searches, public-ID lookups, log and job checks, test runs, exact edits | Paths, IDs, exact task | Paths, line numbers, quoted values | Deputy PI when judgment is needed | Deputy PI (spot check) |
| `literature-reviewer` | Literature search and evidence labels | Question, public identifiers, date range | Findings with verified or not labels | `writer`; `statistician` for effect-size disputes | `reviewer` (claims) |
| `data-steward` | Layout, metadata, FAIR and MIAPPE, repository, data plan, consent-scope check | Data inventory, consent and permit documents | Layout, dictionary, plan, consent flags | Deputy PI, then the PI, for consent or law; `bioinformatician` for processing | `reviewer` |
| `bioinformatician` | One-off sequencing analyses, long jobs, sample and genotype tables | Raw data paths, reference, organism, scale, host limits | Checked tables, logs, pipeline run record | `statistician` (models); `clinical-geneticist` (variants); `software-engineer` (reusable code) | `reviewer` |
| `microbial-genomicist` | Bacterial, fungal, viral, pathogen, metagenome, amplicon work | Reads or assemblies, isolate metadata | Assemblies, AMR calls, trees, tables | `evolutionary-genomicist` (deep phylogeny, selection); `statistician` | `reviewer` |
| `evolutionary-genomicist` | Trees, selection tests, comparative and non-model population genomics | Assemblies or alignments, taxon sampling | Orthogroups, trees, test results | `statistician` (test checks); `writer` | `reviewer` |
| `breeder` | Breeding design, trials, selection decisions, genetic gain | Objective, population, pedigree, phenotypes | Scheme, selection recommendation | `statistician` (fit); `data-steward` (metadata, permits) | `reviewer` |
| `statistician` | Method choice, models, multiple testing, power, number recomputation | Design statement, clean tables | Model, thresholds, recomputed numbers | `writer`; back to `bioinformatician` if QC fails | `reviewer` |
| `clinical-geneticist` | Germline variant classification, gene-disease fit, report fields | Evidence table, build, transcript, phenotype terms | Classification with evidence, draft report fields | Deputy PI, then the PI and physician, for decisions; `literature-reviewer` | `reviewer` (blind variant mode) |
| `software-engineer` | Reusable tools, packages, tests | Spec, language, target platform | Code, tests, README | `bioinformatician` (runs); `writer` (docs) | `reviewer` (code) |
| `writer` | Manuscripts, grants, reports, READMEs | Final numbers, claims, verified references | Draft text, lint result | `translator`; `figure-maker` | `reviewer` (claims audit) |
| `figure-maker` | Figures, posters, decks, legibility check | Final numbers, target size, journal | Figure files, script | `writer` (captions) | `reviewer` if the figure backs a claim |
| `translator` | Translation of final academic text | Final source, language pair, glossary | Translated file, check report | `writer` for source ambiguities | `reviewer` (final submission) |
| `reviewer` | Independent review of code, claims, blind variants | Specification, files, evidence | Correctness and requirement gaps | Deputy PI, then the PI | Not applicable |

## Standard chains

* Assay planning: `data-steward` (`sample-and-assay-planning`) -> `bioinformatician` -> `statistician` -> `reviewer` -> `writer`.
* Variant questions: `bioinformatician` -> `clinical-geneticist` -> `reviewer` (blind).
* Microbial outbreak: `microbial-genomicist` -> `evolutionary-genomicist` -> `reviewer`.
* Breeding: `breeder` -> `statistician` -> `data-steward`; `reviewer` on the claim.
* Manuscript: `literature-reviewer` -> `writer` -> `reviewer` -> `translator` (if needed).

Every chain starts and ends with the deputy PI, who reports to the PI. Chain at most 3 agents per run.

## Gaps (for the owner's decision; no agent created)

* Experimental and assay design liaison (sampling, replicates, batch layout, wet-lab handover): covered today by `data-steward` with `sample-and-assay-planning` and by `statistician` for power.
* Systems and HPC engineer (queues, containers, storage, job failures): covered by `bioinformatician` and `software-engineer` with `hpc-resource-planning` and `workflow-engines-and-containers`.
* Project coordination (milestones, task tracking across sessions): covered by the deputy PI with `analysis-log` and `research-planning`.
* Ethics and compliance officer (consent, permits, access and benefit sharing): covered by `data-steward` with `research-ethics`; the PI decides.
* Single-cell, proteomics, and structural biology specialists: covered by `bioinformatician` with on-demand skills; depth is limited.
