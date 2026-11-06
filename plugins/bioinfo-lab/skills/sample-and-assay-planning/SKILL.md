---
name: sample-and-assay-planning
description: 'Use when planning sampling, DNA or RNA extraction QC, assay choice, replicates, controls, batch layout, or sample tracking for a genomics study in any organism. Not for analysis.'
---

# Sample and assay planning

## Capability

Plan collection, measurement, and tracking so the data answer the question. See `study-design`, `omics-statistics-and-batch`.

## Decide

1. Assay from question: what must be detected, in how many samples; check reference quality and budget.
2. Sampling: record tissue, time, and context (plants field position and stage; animals breed, sex, age, pedigree; humans consent reference). Separate biological from technical replicates.
3. Extraction QC: named method for quantity, purity, integrity; pass limits set before results, from the kit specification; flag failures, never drop silently.
4. Design: spread samples so batch does not track the main contrast; include positive and negative controls; set replicates from power (`study-design`).
5. Tracking: stable unique IDs, one sample sheet.

## Find current information

Follow `current-methods-lookup`. Ask:
* Which assay now suits our variant class, input, and budget?
* What input and integrity limits does the vendor document?
* Which reference material is a valid control?
* What metadata does the target repository require?

## Verify

* Genotype concordance and sex check against the sheet; flag swaps and contamination.
* The negative control is blank; a repeated sample gives matching genotypes.
* Tabulate batch against the main contrast.

## Failure modes

Relabeling after submission; undocumented pooling; unannounced plan changes.

## Record and report

Kit, lot, instrument, run ID, date, operator per batch; pre-set limits; failed samples. Seeds: `references/where-to-look.md`.
