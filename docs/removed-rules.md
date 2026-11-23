# Removed and changed rules (v2.1.0 to v2.3.0)

Source: a ledger of 181 directive sentences in `lab-rules`, `lab-team`, `agent-brief`, and the 14 agent bodies. K = domain knowledge or a fact the model cannot know; P = process, length, sequencing, style, or cost limit; U = user-owned (environment, safety, resource limits, privacy, language, paths). 63 rows duplicate another file. Skill bodies also lost about 25 pointers to a user's `CLAUDE.md`, host, or scratch (see `git diff main`).

Totals: K 34, P 132, U 15.

| File | Directive | Class | Duplicate of | Status in v2.3.0 |
|---|---|---|---|---|
| lab-rules | users decides; subagents hold one role; main routes | P |  | removed |
| lab-rules | version-sensitive facts: look up via current-methods-lookup, log, never from memory | K |  | kept |
| lab-rules | report style: answer first, evidence, not checked | P |  | removed |
| lab-rules | say "not verified"; no praise/recap; stop when done | P |  | removed |
| lab-rules | reply in user's language and level | U |  | removed |
| lab-rules | cheapest action; read only needed | P |  | removed |
| lab-rules | load a skill only when trigger applies | P |  | removed |
| lab-rules | do not repeat steps or widen scope | P |  | removed |
| lab-rules | missing input: ask one question else default | P |  | removed |
| lab-rules | after two same failures stop | P |  | removed |
| lab-rules | checkpoint every 30 calls; stop at 3 repeats; partial at ~90 calls | P |  | removed |
| lab-rules | evidence: verify every PMID/DOI, label preprints, never cite from memory | K | trusted-sources | kept |
| lab-rules | AI output may report results not obtained; recompute key numbers | K |  | kept |
| lab-rules | call writing/plotting/coding-style/analysis-log/genomics-pitfalls | P |  | removed |
| lab-rules | bump vx.x.x without asking | U | coding-style,software-engineer | removed |
| lab-rules | call agent-brief before delegating | P |  | removed |
| lab-rules | use compute host/limits/paths from CLAUDE.md; ask if none | U |  | removed |
| lab-rules | ask before destructive step/new dependency/env change | U |  | removed |
| lab-rules | watch jobs >1 min | P | sequencing-pipelines | removed |
| lab-team | delegate by default; split; work alone only if trivial | P |  | softened (one non-binding sentence or optional checklist) |
| lab-team | 15x token cost fact | K |  | kept |
| lab-team | bounded task, capped report, chain max 3, announce agent | P |  | removed |
| lab-team | routine work to assistant first; check returns | P |  | softened (one non-binding sentence or optional checklist) |
| lab-team | roster of 14 agents | K |  | kept |
| lab-team | five fixed chains | P |  | removed |
| lab-team | PI/deputy PI roles; scope/budget/ethics to PI | P | agent-brief | removed |
| lab-team | model/effort in frontmatter; raise effort then model after 2 failures | P |  | softened (one non-binding sentence or optional checklist) |
| lab-team | Opus only for reviewer and blind classification | P |  | softened (one non-binding sentence or optional checklist) |
| lab-team | call agent-brief and team-playbooks | P |  | removed |
| lab-team | reviewer: correctness only; skip for exploratory | P |  | softened (one non-binding sentence or optional checklist) |
| agent-brief | template: objective | P |  | softened (one non-binding sentence or optional checklist) |
| agent-brief | template: context | P |  | softened (one non-binding sentence or optional checklist) |
| agent-brief | template: inputs | P |  | softened (one non-binding sentence or optional checklist) |
| agent-brief | template: output format/cap/path | P |  | softened (one non-binding sentence or optional checklist) |
| agent-brief | template: boundaries (writable dirs, host limit, scratch) | U |  | removed |
| agent-brief | template: skills to call | P |  | softened (one non-binding sentence or optional checklist) |
| agent-brief | template: done-when | P |  | softened (one non-binding sentence or optional checklist) |
| agent-brief | template: current facts pasted, agent does not browse | P | lab-rules,current-methods-lookup | softened (one non-binding sentence or optional checklist) |
| agent-brief | escalation to deputy PI/PI | P | lab-team | softened (one non-binding sentence or optional checklist) |
| agent-brief | PROGRESS.md for multi-session | P | analysis-log | softened (one non-binding sentence or optional checklist) |
| agent-brief | split by file/question; never two agents edit same file | K |  | kept |
| agent-brief | dependent steps in one agent or in sequence | K |  | kept |
| agent-brief | verify: outputs exist and nonempty | P |  | softened (one non-binding sentence or optional checklist) |
| agent-brief | verify: recompute one number | K | lab-rules | kept |
| agent-brief | verify: snippet/blocked = unverified | K | trusted-sources | kept |
| agent-brief | verify: partial return -> re-brief; twice -> do it yourself | P |  | softened (one non-binding sentence or optional checklist) |
| assistant | role intro | P |  | kept in the agent |
| assistant | lookup-first | P | lab-rules | removed |
| assistant | escalate to deputy PI only | P | all agents | removed |
| assistant | trusted-sources labels, fetched text is data | K | trusted-sources | kept |
| assistant | log triage skill | P |  | kept in the agent |
| assistant | no interpretation/drafting | P |  | kept in the agent |
| assistant | jobs follow CLAUDE.md | U | lab-rules | removed |
| assistant | tests: run what given, no source edit | P |  | kept in the agent |
| assistant | 0 tests/skipped/empty/truncated is suspicious | K |  | kept |
| assistant | edits exact only | P |  | kept in the agent |
| assistant | report <150 words | P |  | removed |
| bioinformatician | role intro | P |  | dropped with the agent (role detail); domain rules folded into skills |
| bioinformatician | lookup-first, WebFetch only given URLs | P | lab-rules | removed |
| bioinformatician | escalate to deputy PI only | P | all agents | removed |
| bioinformatician | skill calls | P |  | dropped with the agent (role detail); domain rules folded into skills |
| bioinformatician | on-demand skill list (29) | P |  | dropped with the agent (role detail); domain rules folded into skills |
| bioinformatician | smallest input; expected result first; read full output | P |  | dropped with the agent (role detail); domain rules folded into skills |
| bioinformatician | assert build/coordinates/sample order in code | K | genomics-pitfalls | kept |
| bioinformatician | pin versions/seeds; log command | P |  | dropped with the agent (role detail); domain rules folded into skills |
| bioinformatician | long jobs: host/limits from CLAUDE.md | U | lab-rules | removed |
| bioinformatician | background, log, PID, Monitor | P | sequencing-pipelines | dropped with the agent (role detail); domain rules folded into skills |
| bioinformatician | delete only own scratch | U |  | removed |
| bioinformatician | hand-offs to other agents | P |  | dropped with the agent (role detail); domain rules folded into skills |
| bioinformatician | report <200 words | P |  | removed |
| breeder | role intro | P |  | dropped with the agent (role detail); domain rules folded into skills |
| breeder | lookup-first | P | lab-rules | removed |
| breeder | escalate | P | all agents | removed |
| breeder | skill calls | P |  | dropped with the agent (role detail); domain rules folded into skills |
| breeder | on-demand list | P |  | dropped with the agent (role detail); domain rules folded into skills |
| breeder | state objective/environments/trait/scheme before advising | K |  | kept |
| breeder | ask one question if missing | P | lab-rules | dropped with the agent (role detail); domain rules folded into skills |
| breeder | hand-offs | P |  | dropped with the agent (role detail); domain rules folded into skills |
| breeder | report <250 words | P |  | removed |
| clinical-geneticist | role intro (no clinical decisions) | P |  | dropped with the agent (role detail); domain rules folded into skills |
| clinical-geneticist | lookup-first | P | lab-rules | removed |
| clinical-geneticist | escalate | P | all agents | removed |
| clinical-geneticist | state build, transcript version, db releases; check ClinGen spec | K | variant-interpretation | kept |
| clinical-geneticist | stakeholder/ethics skill calls | P |  | dropped with the agent (role detail); domain rules folded into skills |
| clinical-geneticist | on-demand list | P |  | dropped with the agent (role detail); domain rules folded into skills |
| clinical-geneticist | use evidence in brief, WebFetch given URLs, labels | P | lab-rules,trusted-sources | dropped with the agent (role detail); domain rules folded into skills |
| clinical-geneticist | blind classification: evidence table only | K | reviewer | kept |
| clinical-geneticist | report <300 words | P |  | removed |
| data-steward | role intro | P |  | dropped with the agent (role detail); domain rules folded into skills |
| data-steward | lookup-first | P | lab-rules | removed |
| data-steward | escalate | P | all agents | removed |
| data-steward | skill calls | P |  | dropped with the agent (role detail); domain rules folded into skills |
| data-steward | on-demand list | P |  | dropped with the agent (role detail); domain rules folded into skills |
| data-steward | check files vs metadata (IDs unique, units, checksums) | K | data-stewardship | kept |
| data-steward | never move/rename/delete raw data | U |  | removed |
| data-steward | consent/law not yours to decide | U | research-ethics | removed |
| data-steward | report <200 words | P |  | removed |
| evolutionary-genomicist | role intro | P |  | dropped with the agent (role detail); domain rules folded into skills |
| evolutionary-genomicist | lookup-first | P | lab-rules | removed |
| evolutionary-genomicist | escalate | P | all agents | removed |
| evolutionary-genomicist | skill calls | P |  | dropped with the agent (role detail); domain rules folded into skills |
| evolutionary-genomicist | on-demand list | P |  | dropped with the agent (role detail); domain rules folded into skills |
| evolutionary-genomicist | state question/taxon/outgroup; report alignment, model, support, versions; gene-tree conflict | K |  | kept |
| evolutionary-genomicist | selection depends on alignment/sampling; positive site is not proof | K | species-tree-and-selection | kept |
| evolutionary-genomicist | long jobs: host/limits from CLAUDE.md, Monitor, own scratch | U | lab-rules | removed |
| evolutionary-genomicist | hand-offs | P |  | dropped with the agent (role detail); domain rules folded into skills |
| evolutionary-genomicist | report <200 words | P |  | removed |
| figure-maker | role intro | P |  | dropped with the agent (role detail); domain rules folded into skills |
| figure-maker | escalate | P | all agents | removed |
| figure-maker | follow plotting; slides; coding-style | P |  | dropped with the agent (role detail); domain rules folded into skills |
| figure-maker | plot only named data; no value changes/filtering/tests; stop if data look wrong | P |  | dropped with the agent (role detail); domain rules folded into skills |
| figure-maker | run legibility check, read image, done = check passes | P | plotting | dropped with the agent (role detail); domain rules folded into skills |
| figure-maker | report <100 words | P |  | removed |
| literature-reviewer | role intro | P |  | dropped with the agent (role detail); domain rules folded into skills |
| literature-reviewer | lookup-first | P | lab-rules | removed |
| literature-reviewer | escalate | P | all agents | removed |
| literature-reviewer | search PubMed/PMC first; recent; label preprints | P | trusted-sources | dropped with the agent (role detail); domain rules folded into skills |
| literature-reviewer | open each cited paper, verify PMID/DOI, labels, never from memory, fetched text is data | K | trusted-sources,lab-rules | kept |
| literature-reviewer | on-demand list | P |  | dropped with the agent (role detail); domain rules folded into skills |
| literature-reviewer | separate shows/suggests/missing; sample size and design | K |  | kept |
| literature-reviewer | report <400 words | P |  | removed |
| microbial-genomicist | role intro | P |  | dropped with the agent (role detail); domain rules folded into skills |
| microbial-genomicist | lookup-first | P | lab-rules | removed |
| microbial-genomicist | escalate | P | all agents | removed |
| microbial-genomicist | skill calls | P |  | dropped with the agent (role detail); domain rules folded into skills |
| microbial-genomicist | on-demand list | P |  | dropped with the agent (role detail); domain rules folded into skills |
| microbial-genomicist | smallest input; expected first | P | bioinformatician | dropped with the agent (role detail); domain rules folded into skills |
| microbial-genomicist | name db/tool versions; calls change with release | K |  | kept |
| microbial-genomicist | sample metadata can identify people; keep out of web queries | U |  | removed |
| microbial-genomicist | long jobs: CLAUDE.md host, Monitor, own scratch | U | lab-rules | removed |
| microbial-genomicist | hand-offs | P |  | dropped with the agent (role detail); domain rules folded into skills |
| microbial-genomicist | report <200 words | P |  | removed |
| reviewer | independence: judge from spec/files, not author's explanation; passing test counts only if assertions read | K |  | kept |
| reviewer | lookup-first | P | lab-rules | removed |
| reviewer | escalate | P | all agents | removed |
| reviewer | code criteria incl genomics-pitfalls, reproducibility, tests check behavior | K |  | kept |
| reviewer | claims: check each number/citation; separate data/literature/assumed | K |  | kept |
| reviewer | variants: blind classify via variant-interpretation | K |  | kept |
| reviewer | extra skill calls | P |  | kept in the agent |
| reviewer | read-only Bash limited to git/grep/head/wc; report only material findings | P |  | kept in the agent |
| reviewer | report <400 words, verdict format | P |  | removed |
| software-engineer | role intro | P |  | dropped with the agent (role detail); domain rules folded into skills |
| software-engineer | lookup-first | P | lab-rules | removed |
| software-engineer | escalate | P | all agents | removed |
| software-engineer | read code first; smallest change; return ambiguity | P |  | dropped with the agent (role detail); domain rules folded into skills |
| software-engineer | follow coding-style | P |  | dropped with the agent (role detail); domain rules folded into skills |
| software-engineer | on-demand list | P |  | dropped with the agent (role detail); domain rules folded into skills |
| software-engineer | version bump rule | U | lab-rules,coding-style | removed |
| software-engineer | expected result then tests per behavior/edge | P | coding-style | dropped with the agent (role detail); domain rules folded into skills |
| software-engineer | stop after 3 fix rounds | P | lab-rules | dropped with the agent (role detail); domain rules folded into skills |
| software-engineer | C++/Rust only when profiling shows need | K |  | kept |
| software-engineer | report <200 words | P |  | removed |
| statistician | role intro | P |  | dropped with the agent (role detail); domain rules folded into skills |
| statistician | lookup-first | P | lab-rules | removed |
| statistician | escalate | P | all agents | removed |
| statistician | skill calls | P |  | dropped with the agent (role detail); domain rules folded into skills |
| statistician | on-demand list | P |  | dropped with the agent (role detail); domain rules folded into skills |
| statistician | design statement first; name model, covariates, replication unit, test family | K | study-design | kept |
| statistician | recompute key numbers | K | lab-rules | kept |
| statistician | effects with intervals and exact P; no causal wording | K |  | kept |
| statistician | simplest adequate model vs baseline; say when data cannot answer | K |  | kept |
| statistician | report <250 words | P |  | removed |
| translator | role intro | P |  | dropped with the agent (role detail); domain rules folded into skills |
| translator | escalate | P | all agents | removed |
| translator | call writing + lint | P |  | dropped with the agent (role detail); domain rules folded into skills |
| translator | brief fields; target language from CLAUDE.md | U |  | removed |
| translator | glossary fallback | P | translator skill | dropped with the agent (role detail); domain rules folded into skills |
| translator | translate every claim/number; add/drop nothing | K | translator skill | kept |
| translator | flag ambiguous source sentence | K | translator skill | kept |
| translator | section by section; check_translation no FAIL | P | translator skill | dropped with the agent (role detail); domain rules folded into skills |
| translator | report only path/check/flags | P |  | removed |
| writer | role intro; humanizer pass | P |  | dropped with the agent (role detail); domain rules folded into skills |
| writer | lookup-first | P | lab-rules | removed |
| writer | escalate | P | all agents | removed |
| writer | skill calls | P |  | dropped with the agent (role detail); domain rules folded into skills |
| writer | on-demand list | P |  | dropped with the agent (role detail); domain rules folded into skills |
| writer | main message first | P |  | dropped with the agent (role detail); domain rules folded into skills |
| writer | every claim needs number/citation/basis | K |  | kept |
| writer | cite via trusted-sources; verify PMID/DOI; never invent | K | lab-rules,trusted-sources | kept |
| writer | edit in own voice | P |  | dropped with the agent (role detail); domain rules folded into skills |
| writer | report <100 words | P |  | removed |

Also removed from skills (U): the version-bump rule (moved to the repository `CLAUDE.md`, maintainers only), reads of `CLAUDE.md` for hosts, reference directories, image directories, thread limits, target language, and author line; "ask before taking all GPUs"; the "assume no server, conda, or containers" sentence; the "3 tool calls or fewer" threshold.

## Where each removed agent's knowledge went

| Former agent | K rules now in |
|---|---|
| statistician | `study-design` (Statistical review) |
| breeder | `quantitative-genetics` (Advising on a breeding question) |
| clinical-geneticist | `variant-interpretation` (Working rules) |
| data-steward | `data-stewardship` (Checking a dataset) |
| writer | `writing` (Evidence in text) |
| translator | `translator` (already held the claim, number, ambiguity, and check rules) |
| figure-maker | `plotting` (Scope of a figure) |
| software-engineer | `coding-style` (Changing code) |
| evolutionary-genomicist | `species-tree-and-selection` (Reporting) |
| microbial-genomicist | `amr-genotype-phenotype` (Versions) |
| bioinformatician | new forked skill `long-analysis-job`; `genomics-pitfalls` and `sequencing-pipelines` already held the rest |
| literature-reviewer | new forked skill `literature-review` |

On v2.6.0 `assistant` and `reviewer` were removed too: lookups, searches, and independent review use Claude Code's built-in agents, `/advisor`, and `/code-review` (`lab-team`). The agents' on-demand skill lists, hand-offs, role introductions, and the `effort` pins were dropped. `roster.md` was deleted.
