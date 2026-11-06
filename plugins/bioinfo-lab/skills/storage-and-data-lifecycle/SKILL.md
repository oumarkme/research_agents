---
name: storage-and-data-lifecycle
description: 'Use when planning storage, compression, transfer, checksums, backup, retention, or cleanup of sequencing data. Not for directory layout and metadata (data-stewardship).'
---

# Storage and data lifecycle

## Capability
Keep data recoverable, verifiable, and no larger than needed. Correct: copies verified by checksum, conversions checked, deletions approved and logged.

## Decide
1. Raw data are read-only; read-only locations named in CLAUDE.md are never modified, moved, or cleaned. Copy to the project; record source, size, checksum.
2. Checksum at creation, after each transfer, and before deletion, in a manifest (path, bytes, checksum, date). An unverified copy is not a backup.
3. Keep raw signal until the user states a retention rule; ask before deleting.
4. Reference-based formats need the exact reference they were written against; archive it with checksum beside the data.
5. Lossless by default; lossy needs written approval and a concordance test.
6. After conversion, check integrity, record counts, and a sample record-level checksum.
7. Tiers, backup, and retention come from the user; consent and accreditation set retention for human data (`research-ethics`).
8. Delete intermediates only after final outputs pass checks and the user agrees.

## Find current information
Follow `current-methods-lookup`. Questions:
* Which formats and compression options are current, and what do they lose?
* What do current docs say about reference lookup and integrity checks?
* Which transfer and encryption tools does the destination accept?
* What do funder, repository, and institution require for retention?
Sources, in order: format specification and tool docs; repository or funder policy page; recent independent benchmarks (PubMed, Europe PMC); preprints, labeled.
Check: release date, maintenance, fit.

## Verify
* Manifest check at the destination; a mismatch is a bad copy.
* Convert one file; compare counts and a record-level checksum. Failing: keep the source and investigate.
* Restore test with only the archived reference.

## Failure modes
* Reference deleted or replaced after conversion.
* Glob cleanup in shared directories.

## Record and report
`analysis-log`: question, date, sources, version, not verified, recheck date. Report sizes before and after, manifest path, verification, deletions and approver. Ask first: raw or only-copy deletion, lossy compression, external destinations.

Seeds: `references/`.
