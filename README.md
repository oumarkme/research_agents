# research_agents

Genomics know-how for Claude: 88 skills that help with bioinformatics, genetics, genomics, and breeding in any organism.

Status: stable · Version: 2.7.0 · License: MIT · Research use only · Plugin: `bioinfo-lab`

Ask Claude a research question in plain language and the matching skill loads. Each skill states the decision criteria and failure modes for its task, looks up version-sensitive facts instead of answering from memory (`current-methods-lookup`), and says how to verify the result. It covers sequencing QC and variant calling, human variant interpretation, breeding and genomic prediction, microbial and pathogen genomics, phylogenetics, omics assays, statistics, data stewardship, and scientific writing.

It adds no servers, hooks, settings, or agents, and it never reads your `CLAUDE.md`.

## Install

Claude Code:

```text
/plugin marketplace add oumarkme/research_agents
/plugin install bioinfo-lab@research_agents
```

Claude web app: Customize > Plugins > Add > Add marketplace, enter `oumarkme/research_agents`, select `bioinfo-lab`. Skills work in chat, Cowork, and Claude Code.

Update: type `/bioinfo-lab:update`. It compares versions and prints the commands to run.

## Quick start

Describe the task. To call a skill directly, use `/bioinfo-lab:<skill>`; `/bioinfo-lab:start-here` lists what is available.

```text
Rank my 300 wheat lines for yield with genomic prediction, and tell me how to validate it.
```

Expected behavior (not yet tested end to end): Claude loads `quantitative-genetics` and `genomic-prediction`, states the objective and a validation scheme that avoids relatives straddling folds, then names the baseline model and the metrics to report.

More examples:

| You ask | Skills that load |
|---|---|
| "Call structural variants from 30x nanopore data." | `sv-cnv-calling`, `long-read-ont-pacbio` |
| "Classify this BRCA2 variant." | `variant-interpretation` |
| "Assemble this bacterial isolate and find resistance genes." | `bacterial-genome-assembly-annotation`, `amr-genotype-phenotype` |
| "Build a species tree and test for selection." | `phylogenetic-inference`, `species-tree-and-selection` |
| "Check my global and project CLAUDE.md files." | `claude-md-setup` |

## What is inside

| Part | Skills |
|---|---|
| Sequencing and calling | QC and demultiplexing, short-read germline, somatic, SV and CNV, repeat expansions, long reads, exome and panels, difficult genes |
| Human genetics | variant interpretation, annotation, rare-disease prioritization, pharmacogenomics, clinical pipeline validation |
| Breeding and non-human genomes | quantitative genetics, genomic prediction, field-trial GWAS, polyploids, livestock QC, reduced representation |
| Microbial and evolution | bacterial and fungal genomes, AMR, pangenomes, pathogen epidemiology, metagenomics, trees, selection, orthology |
| Omics and statistics | RNA-seq, methylation, proteomics, study design, association studies, batch effects |
| Engineering | workflows and containers, HPC sizing, failed jobs, profiling, tests and CI, storage |
| Conduct and writing | ethics, data stewardship, trusted sources, writing, humanizer, translation, plots, slides, README, `git-versioning` |
| Forked skills | `fact-lookup`, `literature-review`, `long-analysis-job`, `independent-review` run in their own context |
| Setup | `claude-md-setup` helps you write your own `CLAUDE.md` |

The full list with example requests is in [`skill-map.md`](plugins/bioinfo-lab/skills/start-here/references/skill-map.md).

### Agents and delegation

The plugin ships no agents. `lab-team` explains when to use Claude Code's built-in `Explore`, `Plan`, `general-purpose`, and `web-fetch`, the forked skills above, `/code-review`, and `/advisor`. A subagent starts with no conversation history, and multi-agent runs used about 15 times the tokens of a chat, so delegate only parallel or bulky work.

### Clean git history

`git-versioning` keeps the version as `vx.x.x` (+0.0.1 for a fix, +0.1.0 for a new function, +1.0.0 only when you ask), gives each project an MIT `LICENSE` and a README written for strangers, and keeps Claude out of commits, pull requests, and tracked files. Claude Code adds attribution by default, so also set this in your own `settings.json`:

```json
{ "attribution": { "commit": "", "pr": "", "sessionUrl": false } }
```

## Design principles

1. As few restrictions as possible; the model does what it is good at.
2. No handling of environment, safety, resource limits, privacy, data governance, or reply language. You set those in your own `CLAUDE.md`.
3. No hooks, `userConfig`, plugin `settings.json`, permission rules, or site-specific values.
4. One setup skill, `claude-md-setup`.
5. You own your data decisions.

## Limits

* Skills are guidance, not validated pipelines. No skill has been tested end to end on real data, and the eval suite in `evals/` has not been run.
* Instructions are advice, not enforcement. A rule that must never be skipped belongs in a hook or permission rule in your own settings.
* Claude Code lists skill descriptions within 1% of the context window and drops the least-used ones first (names stay). With 88 skills, raise `skillListingBudgetFraction` (for example 0.02) in your settings; `/doctor` shows the cost.
* Policy items taken from secondary sources (ICMJE and Springer Nature AI rules, data-protection and access-and-benefit-sharing law) must be checked against the official text.
* Some sites block scripts (OMIM, UK Biobank, TAIR); use a browser.
* Model aliases (`sonnet`, `opus`) in skill frontmatter follow the latest model of that family on purpose.

## Contributing

* Layout: `plugins/bioinfo-lab/skills/<name>/SKILL.md`, `.claude-plugin/`, `tests/`, `evals/` (outside the installed plugin; see `evals/README.md`), `docs/removed-rules.md`, `.github/workflows/ci.yml`.
* A skill needs `name` equal to its folder and a `description` under 400 characters that leads with the trigger and ends with "Not for ... (other-skill)". Keep `SKILL.md` short; put detail in `references/`.
* Check with `claude plugin validate .` in `plugins/bioinfo-lab` and `python -m pytest plugins/bioinfo-lab/tests -q`. CI also checks versions, front matter, and description and line limits.
* Bump the version in `plugin.json` and here together. Open an issue for bugs or requests.

## References

Mulder, N. J., et al. (2018). The development and application of bioinformatics core competencies to improve bioinformatics training and education. *PLOS Computational Biology, 14*(2), e1005772. https://doi.org/10.1371/journal.pcbi.1005772

Claude documentation: [marketplaces](https://code.claude.com/docs/en/plugin-marketplaces), [skills](https://code.claude.com/docs/en/skills), [subagents](https://code.claude.com/docs/en/sub-agents), [plugin evals](https://code.claude.com/docs/en/plugin-evals).

## License

MIT. See `LICENSE`.
