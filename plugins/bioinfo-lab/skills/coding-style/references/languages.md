# Languages, guides, and tools

Read the row for the language you touch. The Google guides are at https://google.github.io/styleguide/ (checked 2026-10-22). Read the guide itself for any rule not listed here.

| Language | Standard | Format and lint |
|---|---|---|
| Python | Google Python Style Guide (`pyguide.html`): Google-style docstrings, type annotations, 4-space indent, 80 columns | `pyink` or `yapf` with the Google style; `pylint` with the Google `pylintrc`; `ruff` for fast checks |
| R | Google R Style Guide (`Rguide.html`, built on the tidyverse guide) | `styler`, `lintr` |
| C++ | Google C++ Style Guide (`cppguide.html`): 2-space indent, 80 columns | `clang-format -style=Google`, `clang-tidy`, `cpplint` |
| Rust | Google Rust Style Guide (`rustguide.html`), which defers to the official Rust Style Guide and API Guidelines: `rustfmt` with 100 columns, no glob imports, `SAFETY:` comment on every `unsafe` block, no `.clone()` to dodge borrowing | `cargo fmt`, `cargo clippy -- -D warnings`, `cargo test` |
| Shell (bash) | Google Shell Style Guide (`shellguide.html`): bash only, 2-space indent, 80 columns, functions documented, `main` function for longer scripts | `shfmt -i 2`, `shellcheck` |
| Markdown (README, notes) | Google Markdown style guide (`docguide/style.html`) | none |
| JSON and YAML configs | Google JSON Style Guide (`jsoncguide.html`) for JSON; two-space indent for YAML | none |
| LaTeX | No Google guide. Use one sentence per source line, `\label` prefixes by type (`fig:`, `tab:`, `sec:`), `siunitx` for numbers and units, `booktabs` for tables, BibTeX or BibLaTeX with APA, no hard-coded figure numbers | `latexindent`, `chktex`; build with `latexmk` |
| Nextflow | No Google guide. Follow the nf-core guidelines: DSL2, one process per module, `meta` maps, containers pinned per process, parameters in `nextflow.config` | `nextflow lint`, `nf-core pipelines lint` for nf-core layouts |
| Snakemake | No Google guide. Follow the Snakemake best practices and the workflow catalog layout (`workflow/`, `config/`, `results/`) | `snakemake --lint`, `snakefmt` |
| Container recipes (optional) | No Google guide. Follow the Apptainer or Docker documentation: pinned base image and package versions, one step per concern, a version label | build plus a test step |

Notes

* Cross-language rules (coordinates, builds, sample order) are in `genomics-pitfalls`; do not restate them in code comments.
* Performance-critical or memory-critical code goes to C++ or Rust; write the same behavior test in Python or R against both, and compare outputs on a small input before benchmarking.
* A language may be unavailable in the project environment. Check with `which` or `cargo --version` before writing code that needs it, and say so if you install anything.
