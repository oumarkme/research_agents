# README templates

## A. Tool or pipeline

````markdown
# name

One-line tagline: what it does for whom.

Status: stable | experimental | archived · Version: x.y.z · License: MIT

What it does and why it is useful, in 2-3 sentences. Name the inputs and the outputs.

## Install

```bash
<one command that works from a clean machine>
```

Requirements: operating system, language and tool versions, memory and disk. Other routes (source, conda, container) in one line each, if offered.

## Quick start

```bash
<runnable example on the bundled test data>
```

Expected output: <file names and one key number>.

## Usage

| Input | Format | Notes |
|---|---|---|

| Option | Default | Meaning |
|---|---|---|

| Output | Format | Meaning |
|---|---|---|

## Methodology

1. Step, tool and version, key parameters.
2. ...

Validation: <benchmark data, metric, result with interval>. Limits: <what it does not handle>.

References (APA).

## Test

```bash
<test command>
```

## Citation

How to cite, with DOI.

## License and contact

License. Maintainer and where to ask questions.
````

## B. Analysis project

````markdown
# project name

One sentence: the question and the answer.

## Question and data
Question, sample and source, data version, access route and consent scope.

## Methods
Design statement (sample, comparison, model, covariates, multiple testing). Steps with tool versions and seeds.

## Results
Key numbers with intervals. Figure file names. One-line limitation.

## Reproduce
```bash
<commands in order>
```
Versions recorded in <file>. Runtime and memory.

## Layout
`src/`, `tests/`, `results/`, `docs/` with one line each.

## Status, license, contact
````

## C. Dataset

````markdown
# dataset name

What it contains, who produced it, when, and under which consent and license.

## Files
Table: file, content, format, rows, checksum file.

## Data dictionary
Table: column, type, unit, allowed values, missing code.

## Provenance
How it was generated, processing steps, versions.

## Access and citation
How to get it, restrictions, how to cite (DOI).
````
