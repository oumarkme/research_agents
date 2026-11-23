---
name: current-methods-lookup
description: 'Use when a decision depends on version-sensitive facts: choosing a tool, options, thresholds, database releases, benchmarks, or guidelines. Not for stable principles already covered by the domain skill.'
---

# Current methods lookup

Goal: pick methods from today's evidence, not from memory, and record what was found so the next session reuses it.

## When

Look up: tool or method choice, options and flags, thresholds from a release, database releases, benchmark claims, guideline updates.
Skip: stable principles, file-format meaning, statistics, and any dated, unexpired entry in the project `analysis-log`. Reuse that entry.
Stop when two independent reliable sources agree.

## How

Who looks up: any session with web tools, or the forked skill `fact-lookup` to keep page text out of the main context. Check its facts against the page. Return facts only: URL, version or date, a short quote, retrieval date, or "not found".
1. State the question and constraints: organism, data type, scale, platform.
2. Search the keywords in the domain skill's where-to-look file; open the official or most-used current page; official documentation and release notes first. Fetch from the web; keep no local copies of documentation.
3. Then recent independent benchmarks or reviews (PubMed, Crossref; label preprints) over the authors' own.
4. Read the page or paper, not the snippet. Check last release date, maintenance, license.
5. If sources conflict, report both. Never invent a version or option; write "not verified".

Queries: `references/search-recipes.md`.

## Reliability checks

* Recency: set a window by field speed (judgment; label it). Fast fields need months, slow ones years.
* Does the claim hold for the user's data type and organism?
* Conflicts of interest: tool authors, funders, vendors.
* Check retractions and corrections for any paper that carries weight.

## Record

Add one entry per lookup to the `analysis-log` (template: `references/log-entry.md`): question, date retrieved, sources (URL or DOI), choice and version, reason, not verified, recheck date. Label sources `verified`, `snippet`, or `blocked`.

## For domain skills

A domain skill states no tool names or numbers. It ends with a "Find current information" block of three lines: the questions, the source types, the checks. Template: `references/domain-block.md`.

Basis for benchmark reading: `references/sources.md`.
