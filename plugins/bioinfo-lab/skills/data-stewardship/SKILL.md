---
name: data-stewardship
description: 'Use when planning, organizing, documenting, or sharing research data in any organism: layout, metadata, provenance, FAIR, repositories, data management plans. Not for analysis.'
---

# Data stewardship

## Capability

Keep data findable, traceable, and shareable under consent and law. See `breeding-metadata-and-archives`, `research-ethics`.

## Decide

* Layout: read-only `raw/` with checksums, `processed/`, `results/`, `metadata/`, README with data dictionary (column, type, unit, values, missing code). Every result traces to a command and versions.
* Metadata: one record per sample and file; stable IDs, species, tissue, assay, platform, build, date; domain community standard.
* FAIR (findable, accessible, interoperable, reusable): persistent identifiers, open formats, license, access route.
* Repository by data type and consent; controlled human data never public.
* Plan: formats, backup, access, retention, sharing date, owner.

## Find current information

Follow `current-methods-lookup`. Ask:
* What does the funder's data management plan template require now?
* Which repository takes this data, with what metadata?
* Which standard version fits our domain?
* What does consent allow?

## Verify

* Restore from backup; checksums match.
* A colleague regenerates one result from README alone.
* Dictionary matches headers; repository validator passes.

## Failure modes

Edited raw data; credentials in files; renaming after release without a mapping table; no license.

## Record and report

Checksums, dictionary, accessions, license, access terms. Seeds: `references/where-to-look.md`.
