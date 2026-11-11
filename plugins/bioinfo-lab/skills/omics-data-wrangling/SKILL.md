---
name: omics-data-wrangling
description: 'Use when reshaping, filtering, or joining large genomic tables and intervals. Not for coordinate and build bug classes (genomics-pitfalls) or code style (coding-style).'
---

# Omics data wrangling

## Capability
Reshape and join genomic tables without silent loss, duplication, or coordinate shifts. Correct: expected row counts at every step, normalized join keys, a toy table with a known answer.

## Decide
1. Coordinates: BED starts are 0-based; VCF positions and tabix regions are 1-based, inclusive. Convert once at input; name columns `start0` and `pos1`.
2. Join variants only on normalized records (split, left-aligned, REF checked), never on rsID.
3. Read with explicit types (IDs as strings, positions as integers); disable default missing-value tokens that IDs or alleles could match.
4. Never open genomic tables in a spreadsheet; gene names become dates.
5. Stream or index rather than load; beyond a fraction of RAM, read lazily or in chunks.
6. Order chromosomes as in the reference index.
7. Join on stable IDs; keep gene symbols as labels.
8. Keep sample tables and matrices in one order.

## Find current information
Follow `current-methods-lookup`. Questions:
* Which library and tool versions handle our formats and interval operations, and what do docs say about coordinates and missing-value defaults?
* Which format specification applies?
* Is a better-supported tool available at our scale?
Sources, in order: tool docs and release notes; the format standards page; recent independent benchmarks (PubMed, Europe PMC); preprints, labeled.
Check: release date, maintenance, scale.

## Verify
* Try each join on a toy table with a hand-computed result.
* After every join assert row counts, key uniqueness on both sides, null counts, and unmatched keys against an expectation.
* Convert coordinates and back for 3 known records.
* Record counts per chromosome match before and after.
* Unexplained count change: stop and trace the step.

## Failure modes
* Multiallelic rows exploded after a join; `chr1` against `1`.
* Renamed gene symbols; interval joins that multiply rows.
* Positions in scientific notation.

## Record and report
`analysis-log`: question, date, sources, versions, not verified, recheck date. Report inputs with checksums, build, key definition, row counts per step, assertions. Ask first if build unknown, key not unique, or memory over plan.

Seeds: `references/`.
