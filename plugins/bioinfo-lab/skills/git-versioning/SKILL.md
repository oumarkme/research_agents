---
name: git-versioning
description: 'Use when committing, tagging, versioning, or writing docs, changelogs, or pull requests for a software project that may be pushed to GitHub: the version rule and commit hygiene with no mention of Claude. Not for code style (coding-style).'
---

# Git versioning and clean commits

## Version rule

* Format `vx.x.x` (major.minor.patch). A new project starts at v0.1.0.
* Bug fix: patch +0.0.1. New function: minor +0.1.0 (patch resets to 0). Major +1.0.0 only when the user asks for it; never bump major on your own.
* Apply the bump yourself in the same change as the edit, without asking. Choose the level from the change (fix or new function); ask only for a major bump.
* Keep one source of truth for the version (package file, `VERSION`, or tag) and match it in the README and any changelog. State old and new version in the report. Tag a release (`vx.x.x`) only when the user asks.

## Project defaults

Every project that follows this skill has, at the repository root:

* **`LICENSE`:** MIT unless the user names another license. Copyright line: the current year and the holder's name from the user (or `git config user.name`; ask if neither is known). Mirror the license in the package metadata.
* **`README.md`:** written for strangers who may want to use the project, on GitHub's first screen. Follow `project-readme`: tagline, what and why, install, a tested quick start, usage, status, version, license, and where to get help (issues). Update it in the same change as the code.
* **`.gitignore`** for the language and tooling, with scratch notes, credentials, and large data excluded; never commit secrets.
* **Version file** as the single source of truth for the version rule above.

## Commits, docs, and pull requests

Nothing that reaches GitHub names Claude, Anthropic, or AI assistance. The commit author and committer stay the user's own git identity.

* Commit messages: imperative subject under about 72 characters, then a body that says why. No `Co-Authored-By` trailer for Claude or Anthropic, no "Generated with" line, no session link, no robot emoji. GitHub lists contributors from those trailers, so omit them.
* Pull request descriptions, changelogs, release notes, README, comments, docstrings, branch names, and file names: the same rule. Applies to every file not in `.gitignore`; scratch notes that are git-ignored may say anything.
* A functional reference the project truly needs (for example an API it calls) is not attribution; ask if unsure.
* Before each commit, check the staged text and the message: `git diff --cached | grep -inE "claude|anthropic|co-authored"` and read the message. Fix hits before committing. Do not rewrite or force-push already pushed history unless the user asks.
* Do not push unless asked.

## Claude Code adds attribution by default

Claude Code appends a `Co-Authored-By` trailer to commits, a "Generated with" line to pull requests, and sometimes a session link. A plugin cannot change settings, so write the commit message without them and tell the user once that they can turn the defaults off in their own `settings.json`:

```json
{ "attribution": { "commit": "", "pr": "", "sessionUrl": false } }
```

On Claude Code v2.1.281 or later, `"attribution": false` hides all of it. Check the current key in the Claude Code settings reference if it differs.
