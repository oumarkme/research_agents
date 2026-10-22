---
name: lab-team
description: 'Use before delegating to an agent or planning multi-step work: the lab roster with model and effort, when not to delegate, and playbooks.'
---

# Lab team

## Default: the main session

A multi-agent run costs about 15 times the tokens of a chat (Anthropic, 2025). Delegate only for isolation (output you will not reread), independence (a check not anchored on your reasoning), parallelism (many independent items), or a long build. Do not delegate a task of a few tool calls, anything that needs this conversation, or the final answer. Run independent agents in one message, chain at most 3, and say in one line which agent you used.

## Roster (cheapest sufficient tier)

| Agent | Model | Effort | Turns | Use for |
|---|---|---|---|---|
| `assistant` | Haiku | low | 15 | Search, lookups by public ID, log and job checks, test runs, exact edits |
| `data-steward` | Haiku | medium | 20 | Layout, metadata, FAIR and MIAPPE checks, repository choice, data management plans |
| `translator` | Sonnet | medium | 30 | zh-TW and English translation |
| `writer` | Sonnet | medium | 30 | Manuscripts, grants, READMEs, reports |
| `bioinformatician` | Sonnet | medium | 40 | Sequencing QC, calling, benchmarking, assembly, pipelines |
| `software-engineer` | Sonnet | medium | 40 | Reusable tools and packages with tests (Python, R, C++, Rust) |
| `breeder` | Sonnet | medium | 30 | Breeding design, trials, selection, genomic selection strategy |
| `statistician` | Sonnet | high | 30 | Method choice, models, number checks |
| `clinical-geneticist` | Sonnet | high | 30 | Variant classification, phenotype fit, physician reports |
| `reviewer` | Opus | high | 20 | One independent review before results are reported |

Escalate only when a cheaper tier fails twice: raise effort first, then model. Opus is for the reviewer and for blind variant classification, nothing else by default.

## Brief every agent with

Objective, exact inputs and paths, output format and length, boundaries, and (for jobs) the CLAUDE.md compute rules. It sees none of this conversation. Name the skill it must load for figures, prose, or translation.

## Playbooks

* Small script or edit: main session with `coding-style`. No agents.
* Sequencing pipeline: `bioinformatician` on a small input, then full run; `reviewer` once only if the output backs a reported result or a shared pipeline.
* Breeding analysis or genomic prediction: `breeder` sets objective and scheme, `statistician` fits and validates (`quantitative-genetics`, `genomic-prediction`), `bioinformatician` prepares genotypes, `writer` reports to the breeder (`stakeholder-communication`).
* GWAS or Mendelian randomization: `bioinformatician` QC, `statistician` model and thresholds (`association-studies`), `reviewer` on the claim.
* Rare disease or diagnostic case: patient-level data stays in the main session and on the machines CLAUDE.md names. `assistant` batches public-ID lookups; `clinical-geneticist` classifies from the evidence table; `reviewer` (variant mode) classifies blind; adjudicate only discordant variants; the report goes to the physician (`stakeholder-communication`).
* Manuscript or grant: main fixes claims and the design statement (`study-design`, `research-planning`); `assistant` collects literature in parallel; `writer` drafts; one `reviewer` claims audit before delivery. Translation after the English text is final. Brief `translator` with source path, direction, audience, output path, and glossary path. For a final submission, add one `reviewer` claims check on Methods and Results of the translation.
* Data release: `data-steward` prepares; the user decides on any consent or sharing question (`research-ethics`).

## Checks and stop rules

* Spot-check key numbers and citations in an agent report before using them. A report is evidence, not a conclusion.
* Ask a reviewer for correctness and requirement gaps only; it will always find optional ones.
* If an agent fails the same way twice, do the task in the main session.
* Skip `reviewer` for exploratory work and for edits you tested yourself.

Competency map and the sources behind this team: `${CLAUDE_SKILL_DIR}/references/competency-map.md`.
