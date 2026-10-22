# research_agents

A Claude plugin marketplace that adds a bioinformatics, genetics, and breeding lab to Claude: 10 agents as lab members and 21 skills as shared methods.

Status: stable · Version: 1.0.0 · License: MIT · Plugin: `bioinfo-lab` (install as `bioinfo-lab@research_agents`)

Ask in plain language, and the right method loads: genomic prediction for breeders, ACMG/AMP variant classification for clinicians, sample planning for the bench, pipeline QC for bioinformatics. No server, conda, or container is required.

## Install

Claude web app: Customize > Plugins > Add > Add marketplace, enter `oumarkme/research_agents`, then select `bioinfo-lab` and Add. For a private repository, connect GitHub and allow the Claude GitHub App when asked.

Claude Code:

```text
/plugin marketplace add oumarkme/research_agents
/plugin install bioinfo-lab@research_agents
```

Skills work in chat, Cowork, and Claude Code. Agents work in Cowork and Claude Code. Update with `/plugin marketplace update research_agents`, then `/reload-plugins`.

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
| `data-steward` | Haiku | medium | Metadata, FAIR, repositories, data plans |
| `translator` | Sonnet | medium | Taiwan Traditional Chinese and American English |
| `writer` | Sonnet | medium | Manuscripts, grants, reports, READMEs |
| `bioinformatician` | Sonnet | medium | Sequencing QC, calling, assembly, pipelines |
| `software-engineer` | Sonnet | medium | Reusable tools in Python, R, C++, Rust |
| `breeder` | Sonnet | medium | Plant and animal breeding, genomic selection |
| `statistician` | Sonnet | high | Models, tests, validation |
| `clinical-geneticist` | Sonnet | high | ACMG/AMP classification, physician reports |
| `reviewer` | Opus | high | One independent review before results are reported |

| Group | Skills |
|---|---|
| Entry and rules | `start-here`, `lab-rules`, `lab-team` |
| Quantitative | `study-design`, `quantitative-genetics`, `genomic-prediction`, `association-studies` |
| Data and sequencing | `sample-and-assay-planning`, `sequencing-pipelines`, `genomics-pitfalls`, `data-stewardship` |
| Clinical | `variant-interpretation` |
| Code and projects | `coding-style`, `project-readme` |
| Evidence and writing | `trusted-sources`, `writing`, `translator`, `plotting` |
| People and compliance | `stakeholder-communication`, `research-ethics`, `research-planning` |

If you run jobs on a shared server or cluster, put its rules (host, limits, read-only paths, scratch) in your global or project `CLAUDE.md`. Otherwise nothing needs setup.

## Methodology

1. Scope: skills map to the ISCB bioinformatics core competencies (Mulder et al., 2018) and to domain standards for breeding, prediction, association studies, sequencing, clinical genetics, and data stewardship. The map is in `plugins/bioinfo-lab/skills/lab-team/references/competency-map.md`.
2. Evidence: each skill cites primary sources. On 2026-10-22 the 45 cited DOIs were checked in Crossref and 136 resource URLs with live requests; failures are flagged in the catalog.
3. Cost control: only `lab-rules` plus at most one role skill is preloaded per agent. Detail sits in `references/` files that load on demand. Each agent has a model and effort tier and a turn cap, and the main session handles small work (`lab-team`).
4. Layout: `.claude-plugin/marketplace.json`; `plugins/bioinfo-lab/` with `agents/`, `skills/<name>/SKILL.md`, and `.claude-plugin/plugin.json`.

Limits: skills are guidance, not validated pipelines, and no skill has been tested end to end on real data. Policy items taken from secondary sources (ICMJE and Springer Nature AI rules, Taiwan data-protection law) must be checked against the official text. Some sites block scripts (OMIM, UK Biobank, TAIR); use a browser.

## Develop

* Add a skill: `plugins/bioinfo-lab/skills/<name>/SKILL.md` with `name` (equal to the folder) and a "Use when ..." `description`. Keep the body under about 3 KB, and put long material in `references/`.
* Add an agent: `plugins/bioinfo-lab/agents/<role>.md` with `model`, `effort`, `maxTurns`, `tools`, and `skills`. Choose the cheapest tier that works.
* Check with `claude plugin validate . --strict`, test with `claude --plugin-dir ./plugins/bioinfo-lab`, and raise `version` in `plugin.json` for each release.

## References

Mulder, N. J., et al. (2018). The development and application of bioinformatics core competencies to improve bioinformatics training and education. *PLOS Computational Biology, 14*(2), e1005772. https://doi.org/10.1371/journal.pcbi.1005772

Claude documentation (checked 2026-10-22): [Create a marketplace](https://code.claude.com/docs/en/plugin-marketplaces), [Plugin components](https://code.claude.com/docs/en/plugins/components), [Plugins on claude.ai](https://claude.com/docs/plugins/overview).

## License

MIT. See `LICENSE`.
