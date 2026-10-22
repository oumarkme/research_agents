---
name: coding-style
description: 'Use before writing, changing, or reviewing code in Python, R, C++, Rust, shell, LaTeX, Nextflow, or Snakemake: Google style, project layout, tests, reproducibility.'
---

# Coding style and project layout

## Style

* Follow the Google style guide for the language strictly in all new and changed lines: naming, formatting, line length, imports, comments and docstrings, type annotations where the guide asks for them. Guides, formatters, and linters per language: `${CLAUDE_SKILL_DIR}/references/languages.md`.
* Where Google has no guide (LaTeX, Nextflow, Snakemake, container recipes), use the convention in `references/languages.md` and say which one you used.
* Google style replaces "match the surrounding style" wherever the two conflict, in new and changed lines only. Do not reformat untouched code. If an existing file deviates heavily, mention it in the report and leave it.
* Comments explain why, not what. Docstrings state inputs, outputs, units, and coordinate conventions (see `genomics-pitfalls`).
* Run the formatter and linter for the language before reporting. A warning you keep needs a one-line reason.

## Layout

* `src/` for core code, `tests/` beside it, one subdirectory per subproject, and `env/` for the environment recipe if you keep one.
* Each project and subproject has a compact `README.md`; load `project-readme` before writing it.
* Software environment: record exact versions in whatever your setup uses (conda or mamba file, renv, pip lock file, module list, container recipe, or a plain versions file). Containers are optional.

## Reproducibility and tests

* Pin versions, set and log random seeds, log all parameters and the command line, and write outputs deterministically.
* Write the expected result before running. Use a truth set where one exists (for example GIAB with `hap.py` for variant calling) or a small input with a known answer, plus edge cases (empty input, one record, multi-allelic site, missing values).
* Keep tests proportional to the code: each behavior and each edge case once, without parametrized expansion or duplicate cases. Tests check behavior, not only that the code runs.
* Test on a small input first. Run heavy jobs where CLAUDE.md says, if it names a place and limits.
* Do not add dependencies, change environments, or delete data without saying so in the report.
