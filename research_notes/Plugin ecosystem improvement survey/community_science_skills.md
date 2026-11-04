# Community science and bioinformatics agent skills and plugins (as of 2026-11-04)

Method note: pages were read through WebFetch (summarized by a small model, not raw files) on 2026-11-04. GitHub API was rate-limited, so no exact last-commit dates. I did NOT read any individual SKILL.md (the one attempt, K-Dense peer-review, returned 404; tree listing also 404). Star counts are from rendered repo pages unless stated.

## K-Dense-AI/scientific-agent-skills and related repos

### Takeaway
K-Dense is the largest and most active science skill library (about 56k stars, 177 skills, MIT, weekly security scans), breadth-first with database and Python-package wrappers. Its strengths are the scale, security reporting and writing/peer-review/grant skills; weaknesses are breadth over depth, mixed per-skill licenses, vendor promotion, and self-reported claims.

### Cited Findings
- Repo stats: about 56k stars, 4.9k forks, MIT for the repo, 763 commits, 177 skills (v2.72.0 removed bundled docx/pdf/pptx/xlsx). Per-skill licenses live in each SKILL.md metadata and may differ. Last-commit date not shown on page. Read: README via WebFetch (not raw file) — [GitHub](https://github.com/K-Dense-AI/claude-scientific-skills) (redirects to scientific-agent-skills), 2026-11-04
- Structure: root `skills/` with one SKILL.md per skill, plus `docs/`, `scripts/`, `tests/` (one suite per skill that ships scripts), `plugin.json`, `pyproject.toml`, `AGENTS.md`; loads in hosts supporting Agent Skills or the Agent Plugins format — same README
- Wrapping: one "Database Lookup" skill documents 80 databases (endpoint choice, pagination, provenance; headline "100+" databases); about 70 Python-package skills with version-aware workflows (RDKit, Scanpy, scikit-learn); multi-database wrappers (BioServices, Biopython, gget); 9 platform-integration skills (Benchling, Opentrons) — same README
- About 20 overlapping domain groups (bioinformatics, cheminformatics, clinical, ML, materials, data analysis, scientific communication) — same README
- CI validates skills on relevant PRs, but full scientific-dependency tests run only before releases; "250,000+ scientists" and "58x speedup" for optimize-for-gpu are self-reported marketing claims — same README
- Security: README warns skills can run code and install packages; recommends reading SKILL.md, checking contribution history, scanning with Cisco AI Defense Skill Scanner. Weekly scan, full rescan at least every 30 days — same README
- Latest published security report (scan 2026-11-02, cisco-ai-skill-scanner 2.3.2 plus an LLM review): 177 skills, 472 findings, 159 safe, 18 not (9 CRITICAL, 9 HIGH); most CRITICAL flags were env-var and network-call patterns judged "declared credential use"; residual risk is user-editable endpoints; LOW findings are self-citation instructions telling the agent to add and fetch the vendor's arXiv paper (flagged as policy/social-engineering). Report's own header counts (21 high) differ from row sum (20). Read via WebFetch summary — [security-report.md](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/docs/security-report.md), 2026-11-02
- K-Dense/claude-scientific-writer: about 2.6k stars, 297 forks, MIT, 244 commits; Claude Code plugin with 26 skills pinned in `skills.lock.json` (research-lookup, peer-review, citation-management, research-grants, latex-posters, scientific-slides); outputs papers (IMRaD), clinical reports, LaTeX posters, grants (NSF, NIH, DOE, DARPA), literature reviews; BibTeX handling, optional Zotero DOCX editing; also a pip CLI and async API; `CLAUDE.md` and byte-identical `AGENTS.md`; needs Parallel CLI/API auth for lookup and a LaTeX install for PDF; README promotes hosted K-Dense Web; `allowed-tools`, `hooks`, `version` frontmatter are Claude Code-only — [GitHub](https://github.com/K-Dense-AI/claude-scientific-writer), 2026-11-04
- Third-party mirrors of K-Dense skills (Smithery, skillstore, agent-skills.md) report conflicting skill counts (128+ to 140), i.e. stale copies circulate — [search result](https://smithery.ai/skills/Microck/claude-scientific-skills), 2026-11 (snippet only)

### Inferences
- The lockfile (`skills.lock.json`), per-skill tests, a published scan report with LLM triage, and a byte-identical AGENTS.md are cheap, transferable practices.
- Telling the agent to cite or fetch the vendor's paper is a pattern to avoid in our own skills.
- Our 24 skills with depth in lab-specific rules are not competing on breadth; K-Dense is a source of reference ideas only (cherry-pick, do not vendor).

### Gaps
- No last-commit date, no raw SKILL.md read, no independent quality review of K-Dense skills found.

## Other GitHub collections and comparable ecosystems

### Takeaway
Bioinformatics-specific libraries exist at scale (bioSkills 561, SciAgent-Skills about 199) but quality signals are mostly self-reported; the official Anthropic life-sciences repo is small and has shrunk to four skills.

### Cited Findings
- GPTomics/bioSkills: 1.2k stars, 270 forks, MIT, 250 commits, 561 skills in 63 categories, ARCHIVED (no further updates; owner encourages forking). Skill conventions: description must start "Use when...", one `primary_tool` per skill, Version Compatibility block, Goal/Approach sections, version header in example scripts, installers with `--validate`, converters for Codex/Gemini/OpenCode layouts; evaluated on Bio-Task Bench (chart only); no test suite described. Page notes Gemini CLI being replaced by Antigravity CLI, sunset 2026-06-18. Read README via WebFetch — [GitHub](https://github.com/GPTomics/bioSkills), 2026-11-04
- jaechang-hits/SciAgent-Skills: 385 stars, 45 forks, CC-BY-4.0 (skills note underlying tool licenses), 155 commits; skill count inconsistent within README (197/199/198); categories: Genomics 65, Structural/Drug discovery 26, Scientific computing 24, Scientific writing 21, Cell biology 15, Biostatistics 12, multi-omics 11, Proteomics 10, Lab automation 6, Data viz 5, Molecular biology 3; typed as 72 toolkits, 53 database connectors, 37 guides, 37 pipelines. Claims 92.0% vs 65.3% baseline on BixBench-Verified-50 (Claude Code Opus 4.6); no methodology, runs, variance or other systems shown (self-reported) — [GitHub](https://github.com/jaechang-hits/SciAgent-Skills), 2026-11-04
- anthropics/life-sciences (marketplace): 640 stars, 112 forks, 85 commits; refocused on skills, MCP connectors removed; remaining plugins: clinical-trial-protocol, scientific-problem-selection (Fischbach and Walsh, Cell 2024), clinical-trial-forecast, binder-gauntlet; removed nextflow-development, scvi-tools, single-cell-rna-qc, instrument-data-to-allotrope. License and last commit not captured — [GitHub](https://github.com/anthropics/life-sciences), 2026-11-04. (Our host still lists some removed ones as bio-research:* skills, so installed copies may be stale.)
- anthropics/skills: 187.1k stars, 22.1k forks, 61 commits; docx/pdf/pptx/xlsx are source-available, not open source; no science skills; README says skills are for demonstration, test before relying; spec at agentskills.io; minimal frontmatter is `name` + `description` — [GitHub](https://github.com/anthropics/skills), 2026-11-04
- ComposioHQ/awesome-claude-skills: 78.7k stars, Apache-2.0 with per-skill licenses possible; no science category (closest: deep-research, recursive-research with source tiering); claims "1000+ skills" but lists far fewer; promotional toward Composio; stale model name in README example — [GitHub](https://github.com/ComposioHQ/awesome-claude-skills), 2026-11-04
- Other repos seen only in search snippets (not opened): ClawBio (OpenClaw; local-first pharmacogenomics, ancestry PCA, metagenomics), windysky/Bioinformatics_ClaudeSkills (MCP-server approach), dannon/taxonomy-resolver and iwc-workflow-recommender (Galaxy-oriented genomic skills), lifangda/claude-plugins, eavae/bioSkills (fork) — [search](https://awesome.ecosyste.ms/projects/github.com%2FGPTomics%2FbioSkills), 2026-11
- OpenAI: a free open-source Codex "life-science-research" plugin launched alongside GPT-Rosalind (reported 2026-04-16), orchestrating 50+ public multi-omics databases; repo path (github.com/openai/plugins/life-science-research) taken from a secondary blog, NOT verified — [pulse.bot](https://www.pulse.bot/ai/news/openai-debuts-gpt-rosalind-a-new-limited-access-model-for-life-sciences-and-broader-codex-plugin-on-b3c6a23c-7142-401f-be39-eacf00e4c731/), 2026-04
- Biomni (Stanford): published in Science 2026 (Huang et al.); links 150+ tools, 59 databases, 100+ packages (counts vary by outlet: 68 databases, 108 packages, 82 tools); Claude "Biomni" skills on skillstore etc. are third-party repackaging, not official — [Stanford News](https://news.stanford.edu/stories/2026/07/biomni-ai-powered-biomedical-co-scientist), [Lab Manager](https://www.labmanager.com/biomedical-ai-agent-connects-more-than-150-research-tools-35884), 2026-07
- Directories/marketplaces: aggregator sites (skills.sh, ClawHub, Smithery, skillstore, openskillindex) mirror repos with inconsistent stats; none were examined for curation quality. Gemini CLI extensions, BioAgents: not researched (see gaps).

### Inferences
- Quality distinguishers seen: active maintenance (K-Dense weekly scans vs archived bioSkills), published methodology for benchmarks (missing in SciAgent-Skills), pinned versions of tools, a validator script, explicit licensing per skill.
- Ideas that transfer: "Use when..." descriptions (we already do), Version Compatibility blocks, `--validate` installer, AGENTS.md mirror for Codex/Gemini portability, lockfile.
- Avoid: inflated counts, unverified benchmark numbers, one-skill-per-package bulk generation.

### Gaps
- Last-commit dates for all repos; awesome-claude-code; Gemini CLI extensions; BioAgents; OpenAI repo verification; marketplace popularity ranking (stars only available for repos above).

## Skill ideas possibly absent from a lab plugin

### Takeaway
Existing collections cover, in some form: peer review, citation management, grants, LaTeX posters, scientific slides, literature lookup, problem selection, statistics (biostatistics 12 skills in SciAgent), and workflow pipelines. Only K-Dense/SciAgent coverage is confirmed by listing; skill contents unread.

### Cited Findings
- Writer plugin names: research-lookup, peer-review, citation-management, research-grants, latex-posters, scientific-slides; also literature reviews and schematics — [claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer), 2026-11-04
- SciAgent-Skills has Scientific Writing (21), Biostatistics (12), Data Visualization (5), Lab Automation (6) categories — [SciAgent-Skills](https://github.com/jaechang-hits/SciAgent-Skills), 2026-11-04
- bioSkills has a workflows category (41 skills) — [bioSkills](https://github.com/GPTomics/bioSkills), 2026-11-04
- Anthropic scientific-problem-selection skill (based on Fischbach and Walsh, Cell 2024) — [anthropics/life-sciences](https://github.com/anthropics/life-sciences), 2026-11-04

### Inferences
- Candidate additions for bioinfo-lab (my judgment, not from sources): (1) peer-review response letter (point-by-point, tracked claims), (2) literature-review workflow with PubMed-verified citations and a screening log, (3) reproducible-environment skill (conda lock, Apptainer, pinned versions), (4) statistical analysis checklist/reporting (we have study-design; maybe a pre-submission checklist), (5) preprint/submission checklist (bioRxiv, data and code availability, ICMJE AI disclosure), (6) BibTeX validation (bibtools:bibtidy already exists in host). Lab notebook logging overlaps our analysis-log. Prioritise those tied to our concrete workflows rather than breadth.

### Gaps
- Did not read any competing SKILL.md for peer review, grant, or literature review, so quality and depth are unknown.

## Risks: quality, injection, supply chain, license, staleness

### Takeaway
Third-party skills are a measured supply-chain risk; use only by reading and adapting, not installing blindly.

### Cited Findings
- Snyk ToxicSkills (2026-02-05): 3,984 skills from ClawHub and skills.sh scanned; 13.4% (534) with a critical issue; 36.82% (1,467) any issue; 76 confirmed malicious payloads; 91% of malicious skills combined prompt injection with malicious code; hardcoded secrets in 10.9% of ClawHub skills; remote-instruction patterns in 2.9% (21% of malicious); recommends treating skills as software supply chain and reviewing agent memory files. Vendor scanner and vendor products promoted — [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub), read 2026-11-04
- arXiv technical report 2605.28588 on agent-skill threats and the SkillInject benchmark (202 injection-task pairs): seen via search snippet only, not read — [arXiv](https://arxiv.org/pdf/2605.28588), 2026-11
- License: K-Dense repo MIT but per-skill licenses vary; SciAgent CC-BY-4.0 with tool-license notes; Anthropic docx/pdf/pptx/xlsx source-available only; Composio per-skill — pages cited above
- Staleness: bioSkills archived; removed Anthropic skills persist in mirrors; star/skill counts disagree across aggregators; Gemini CLI to Antigravity sunset note

### Inferences
- For us: do not copy text verbatim without license check; do not auto-update from external skills; keep our own scan (for example cisco skill-scanner or mcp-scan) in CI; avoid skills that fetch remote instructions or urge citing a vendor.

### Gaps
- No independent audit of K-Dense or bioSkills beyond vendor self-scan; Snyk number is a vendor snapshot of general (non-science) registries.
