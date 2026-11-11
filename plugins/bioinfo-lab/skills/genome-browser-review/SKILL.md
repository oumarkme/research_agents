---
name: genome-browser-review
description: 'Use when visually reviewing variants, SVs, repeats, or splicing in a genome browser, or saving screenshots and review decisions. Not for figure design (plotting) or variant classification (variant-interpretation).'
---

# Genome browser review

## Capability
Confirm or reject calls by eye with a recorded, repeatable decision. Correct: each reviewed call has evidence counts, a call, a reason, and a screenshot tied to build and settings.

## Decide
1. Match the browser build to the data (contigs, header); load alignments with index, calls, gene annotation, repeat and duplication tracks, and a population-frequency track.
2. Know which display settings hide or distort evidence (downsampling, mapping-quality shading, filters, grouping).
3. Read per variant class: strand balance, read ends, mismatch clusters, repeats, clips, mapping quality, allele fraction against expectation, relatives.
4. Call true, artifact, or uncertain with a reason code. Uncertain goes to orthogonal confirmation; a second reviewer checks reported calls.
5. One window per variant, whole family in one image; sample IDs stay in the project.

## Find current information
Follow `current-methods-lookup`. Questions:
* What do the browser's current docs say about downsampling, filters, batch scripts, and long-read or modification display?
* Which tracks (annotation, frequency, repeats) are current for this build?
* Is a validated visualization tool available for this variant class?
Sources, in order: browser docs and release notes; track provider pages; recent independent papers (PubMed, Europe PMC); preprints, labeled.
Check: release date, build, fit to our platform.

## Verify
* Review known true and known false calls first; the reviewer must separate them.
* Compare calls with caller metrics; disagreement needs a note.
* Two reviewers agree on a sample; if not, revise the criteria.

## Failure modes
* Downsampled view read as low support; hollow reads counted.
* Wrong build or contig names; one read taken as proof.

## Record and report
Table row: key (chrom, pos, ref, alt, build), sample, reviewer, date, browser version, tracks, settings, evidence counts, call, reason, screenshot path. Append; never overwrite. `analysis-log`: question, date, sources, version, not verified, recheck date.

Seeds: `references/`.
