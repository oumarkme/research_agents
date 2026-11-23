# research_agents

A Claude plugin marketplace with one plugin, `bioinfo-lab`: 88 skills for bioinformatics, genetics, genomics, and breeding in any organism (research use only). It ships no agents; it uses Claude Code's built-in ones. Each skill says where to find current information, looks up version-sensitive facts through `current-methods-lookup`, and states how to verify results.

Status: stable · Version: 2.7.0 · License: MIT · Install as `bioinfo-lab@research_agents`

Ask in plain language and the right skill loads: genomic prediction for breeders, outbreak phylogenetics for pathogen work, species trees and selection tests for evolutionary biology, ACMG/AMP classification for variant work, pipeline QC for sequencing. No server, conda, container, hook, or setting is needed.

## Install

Claude Code:

```text
/plugin marketplace add oumarkme/research_agents
/plugin install bioinfo-lab@research_agents
```

Claude web app: Customize > Plugins > Add > Add marketplace, enter `oumarkme/research_agents`, select `bioinfo-lab`. Skills work in chat, Cowork, and Claude Code.

Update: ask for `/bioinfo-lab:update`. It prints `/plugin marketplace update research_agents`, `/plugin update bioinfo-lab@research_agents`, and `/reload-plugins`.

## Quick start

Type a request; skills load by trigger, or call one with `/bioinfo-lab:<skill>`. `/bioinfo-lab:start-here` lists what is available.

```text
Rank my 300 wheat lines for yield with genomic prediction, and tell me how to validate it.
```

Intended behavior (not tested end to end): Claude states the objective and validation scheme (`quantitative-genetics`, `genomic-prediction`), then gives the baseline model and the metrics to report.

## What is in it

| Part | Contents |
|---|---|
| Built-in agents | No custom agents. `lab-team` says when to use Claude Code's `Explore` (search, log and test checks), `Plan`, `general-purpose` (lookups, independent review), `web-fetch`, `/advisor`, and `/code-review`. |
| Forked skills | `fact-lookup`, `literature-review`, `long-analysis-job`, and `independent-review` run in their own context on a built-in agent (`general-purpose`), with the model and effort set in each skill. |
| Method skills | 68 method skills: calling and QC, assembly and annotation, human variants, breeding, microbial, evolution, omics, engineering, statistics. Full map: `plugins/bioinfo-lab/skills/start-here/references/skill-map.md`. |
| Support skills | `lab-rules`, `lab-team`, `trusted-sources`, `current-methods-lookup`, `analysis-log`, `coding-style`, `writing`, `humanizer`, `translator`, `plotting`, `slides`, `project-readme`, `research-ethics`, `git-versioning`, `update`. |
| `claude-md-setup` | Audits and sets up your `CLAUDE.md` at global, project, and local scope. Runs only when you call it; writes only after you approve a diff. |

## Design principles

1. As few restrictions as possible; the model does what it is good at.
2. The plugin does not handle environment, safety, resource limits, privacy, data governance, or reply language, and never reads or asks about your `CLAUDE.md`. You set those yourself.
3. No hooks, `userConfig`, plugin `settings.json`, permission rules, or site-specific values.
4. One setup skill (`claude-md-setup`).
5. You own your data decisions.

## Clean git history

`git-versioning` applies the `vx.x.x` rule (+0.0.1 fix, +0.1.0 new function, +1.0.0 only when you ask), gives each project an MIT `LICENSE` by default and a stranger-friendly README (`project-readme`), and keeps Claude out of commits, pull requests, and docs that reach GitHub: no `Co-Authored-By` trailer, no "Generated with" line, no mention in tracked files. Claude Code adds those by default, so also set `"attribution": {"commit": "", "pr": "", "sessionUrl": false}` in your own `settings.json` (v2.1.281 or later accepts `"attribution": false`).

## What v2.3 changed

* **Skills:** descriptions lead with the trigger and carry a "Not for" pointer; process and environment rules are gone and domain knowledge is kept (`docs/removed-rules.md`); `update` and `claude-md-setup` are user-invoked only; five skills were rewritten as compact decision criteria.
* **Agents:** 14 agents became none. 12 roles became skills, with their domain rules folded into the matching skill; the lookup and review jobs use Claude Code's built-in agents and `/advisor`. The 14-agent layout is tag `v2.1.0`.
* **Delegation:** optional guidance in `lab-team`. A subagent starts with no history and multi-agent runs used about 15 times the tokens of a chat, so delegate parallel, breadth-first, or bulky work and keep dependent steps in the main session.
* **Models and effort:** the plugin pins none. The forked skills use model aliases (`opus`, `sonnet`), which follow the latest model of that family on purpose. A plugin cannot set the main model; pass `model` or `effort` per subagent call.

Example model guidance (not prescribed): Sonnet at `medium` by default; `opusplan` or `/model opus` for judgment-heavy sessions such as study design or claim audits; `xhigh` and `max` rarely. In Opus sessions, `CLAUDE_CODE_SUBAGENT_MODEL=sonnet` keeps subagents on Sonnet (Claude Code v2.1.251 or later).

## Limits

Claude Code lists skill descriptions within a budget of 1% of the context window and drops the descriptions of the least used skills first (names always stay). With 88 skills, raise `skillListingBudgetFraction` in your own settings (for example 0.02) or set `SLASH_COMMAND_TOOL_CHAR_BUDGET`; `/doctor` shows the cost. Subagents can load any plugin skill with the Skill tool, so name the skill in the brief (`lab-team`).

Skills are guidance, not validated pipelines, and no skill has been tested end to end on real data. The eval suite in `evals/` has not been run. Instructions are advice, not enforcement: a rule that must never be skipped belongs in a hook or permission rule in your own settings. Policy items taken from secondary sources (ICMJE and Springer Nature AI rules, data-protection and access-and-benefit-sharing law) must be checked against the official text. Some sites block scripts (OMIM, UK Biobank, TAIR); use a browser.

## Develop

* Layout: `.claude-plugin/marketplace.json`; `plugins/bioinfo-lab/` with `agents/`, `skills/<name>/SKILL.md`, `tests/`, and `.claude-plugin/plugin.json`; `evals/` (outside the installed plugin, see `evals/README.md`); `docs/removed-rules.md`; `.github/workflows/ci.yml`.
* Add a skill: a folder with `SKILL.md`, `name` equal to the folder, and a "Use when ..." `description` under 400 characters that states the trigger first and ends with "Not for ... (other-skill)". Keep `SKILL.md` short and put detail in `references/`.
* Prefer skills and Claude Code's built-in agents; add an agent only when a skill cannot give the isolation you need.
* Check: `claude plugin validate .` in `plugins/bioinfo-lab`, then `python -m pytest plugins/bioinfo-lab/tests -q`. CI also checks versions, front matter, description and line limits, and counts.
* Version `vx.x.x` in `plugin.json`, this README, and the marketplace entry must agree: +0.1.0 for a new function, +0.0.1 for a fix, major only on request.

## References

Mulder, N. J., et al. (2018). The development and application of bioinformatics core competencies to improve bioinformatics training and education. *PLOS Computational Biology, 14*(2), e1005772. https://doi.org/10.1371/journal.pcbi.1005772 (basis of `plugins/bioinfo-lab/skills/lab-team/references/competency-map.md`).

Claude documentation: [Create a marketplace](https://code.claude.com/docs/en/plugin-marketplaces), [Plugin components](https://code.claude.com/docs/en/plugins/components), [Plugin evals](https://code.claude.com/docs/en/plugin-evals).

## License

MIT. See `LICENSE`.
