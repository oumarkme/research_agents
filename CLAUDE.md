# Maintainer notes (this repository only; not shipped in the plugin)

* Plugin version `vx.x.x` in `plugins/bioinfo-lab/.claude-plugin/plugin.json`, the README, and `marketplace.json` must agree. Bump in the same change: new function +0.1.0, fix +0.0.1, major +1.0.0 only when the owner asks.
* Code style: Google style guides (Python, R, Bash); nf-core conventions for Nextflow.
* The plugin stays generic: no site-specific values, no hooks, no `userConfig`, no plugin `settings.json`, no permission rules. Environment, safety, privacy, and language belong in the user's own `CLAUDE.md`.
* Check before a release: `claude plugin validate .` (in `plugins/bioinfo-lab`) and `python -m pytest plugins/bioinfo-lab/tests -q`.
