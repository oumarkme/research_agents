# Evals for bioinfo-lab

Not part of the installed plugin: this folder sits outside `plugins/bioinfo-lab/`, and the marketplace entry installs only that folder. `claude plugin eval` requires the eval folder inside the plugin and rejects `..`, so `run.sh` links it in for the run and removes the link afterwards.

All fixtures are synthetic and are written by each case's `fixture.sh` (needs `--scaffold`; the scripts are in this repository). Free graders: `regex`, `tool_used`, `file_exists`. Cases `claude-md-setup-no-project-file` has one `llm` grader (judge model: Haiku). Cases tagged `paid-web` need `--allow-tools WebSearch WebFetch Agent`.

Run (costs money; set a ceiling and pin the model):

    evals/run.sh --model <model-id> --runs 3 --max-cost-usd <ceiling> --ablation none

Notes: eval workspaces load no CLAUDE.md, so the `claude-md-setup` cases read fixture files by path. In two-arm runs, `tool_used: Skill` graders are indicators, not score. Granting `Write` and `Edit` is not done here, so the no-write checks also rely on `file_exists`.

## Model experiments

* Lookup accuracy (Haiku vs Sonnet): run `lookup-accuracy-release-facts` once with the subagent's `model` set to `haiku` and once to `sonnet` (state it in the prompt). Facts are in that case's `FACTS.md`; refresh them first.
* Judgment roles: run the `gp-validation-leakage`, `planted-coordinate-bugs`, and `independent-review-number-mismatch` cases with `--model` set to Sonnet at `--effort`-equivalent settings versus Opus; the effort of a main session is set in the session, not in the suite.
* Compare arms with `--ablation none`: tag `v2.1.0` (14 agents, 84 skills) against the current `main` (no agents, 88 skills). Check out the tag in a separate worktree to run it. Run the two-arm mode once on one arm to confirm the plugin adds value over no plugin.
