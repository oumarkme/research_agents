---
name: long-analysis-job
description: 'Use when a long or heavy sequencing analysis should run in its own context (QC, alignment, calling, assembly, workflows) with a log and a checked result. Not for reusable tools (coding-style) or model choice (study-design).'
context: fork
model: sonnet
background: false
---

# Long analysis job

Task: $ARGUMENTS

You have no conversation history; work from the task above and the files it names. Turn raw data into checked tables.

* Start from the smallest input that shows the behavior. Write the expected result first, run it, and read the full output; do not claim success on output you have not read.
* Assert build, coordinates, and sample order in code (`genomics-pitfalls`); pin versions and seeds; log the command line.
* Run long steps in the background with a log file in the project directory and watch the log; record the command.
* Call `sequencing-pipelines` for sequencing work, `coding-style` before writing code, and the matching domain skill for the data type.
* Done means the expected output files exist and a key number recomputes from the raw input.

Return the files changed, commands and results, versions, what was not tested, and open decisions.
