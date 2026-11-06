# Version log and column naming

Keep `annotation_versions.tsv` in the project root, one row per resource:

| Field | Example |
|---|---|
| resource | frequency database |
| version | release label |
| build | genome build |
| subset | population or data type (state which) |
| file and md5 | path, checksum |
| date downloaded | 2026-11-06 |
| used in | script line or rule |

Log: annotation tool and cache release, transcript set release, frequency resources, ClinVar release date, score and constraint tables (with model and gene annotation), local frequencies, HPO release (`rare-disease-prioritization`).

## Column naming
`<resource>_<version>_<subset>_<metric>`. A column without a version is a defect.

## Local population data
* Access terms are set by the data owner; cohort-level data stays on the hosts CLAUDE.md names.
* Use local frequency as an extra column. Do not replace the public resource silently: sample size and ascertainment differ.
* A large gap between a population-matched public subset and the local frequency: check build, allele orientation, and array ascertainment first.

## Where
Use the reference directory, containers, host, and core limit in CLAUDE.md; set thread counts explicitly.
