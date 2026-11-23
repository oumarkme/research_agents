---
name: claude-md-setup
description: 'Use when the user asks to set up, audit, or fix their CLAUDE.md files at global, project, or local scope. User-invoked only.'
disable-model-invocation: true
---

# CLAUDE.md setup

Helps the user get a correct, compact `CLAUDE.md` at the right scope. Read and write local files only; fetch nothing. Scope and topic details: `${CLAUDE_SKILL_DIR}/references/scopes.md` and `${CLAUDE_SKILL_DIR}/references/topics.md`.

1. **Scope.** Ask which the user wants, or a combination: **global** (`~/.claude/CLAUDE.md`, all projects, personal), **project** (`./CLAUDE.md` or `./.claude/CLAUDE.md`, shared through git), **local** (`./CLAUDE.local.md`, personal to this project, to be git-ignored). For large or file-specific guidance, offer path-scoped rule files (`~/.claude/rules/` or `.claude/rules/` with `paths` frontmatter).
2. **Read, do not edit yet.** Read the existing files at each chosen scope and the other scopes that apply. Report how they combine: all discovered files are concatenated, not overridden; content closer to the working directory is read last; contradictions may be resolved arbitrarily.
3. **Audit.** Report findings ranked blocker, major, minor: over 200 lines; contradictions within or across scopes; vague rules that cannot be verified; content duplicated across scopes; rules in the wrong scope (cross-project personal preferences belong in global, project facts and commands in project, personal project notes in local); content better as a path-scoped rule, a skill, or a hook; stale facts; secrets or credentials.
4. **Missing project file.** Draft a first version from a read-only look at the project (README, build and test files), or suggest `/init`. Ask at most four questions. Offer the optional topics in `topics.md` (reply language, environment and data paths, preferences, anything else); prescribe none.
5. **Propose a minimal diff** that keeps the user's wording and stays under about 200 lines per file. `@path` imports organize content but do not reduce context.
6. **Write only after explicit approval.** First copy each file to `<file>.bak-<date>` and show the diff. Add `CLAUDE.local.md` to `.gitignore` only with approval.
7. **Confirm.** Tell the user to run `/memory` to see what loaded.
8. **Limits.** CLAUDE.md is advisory context, not enforcement. If the user wants hard enforcement, offer to draft rules for their own `settings.json`, applied only on approval.
