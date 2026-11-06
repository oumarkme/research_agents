---
name: run-qc-and-demultiplexing
description: 'Use when a new Illumina or ONT run arrives and needs demultiplexing, FASTQ or run QC, and a pass or re-run call. Not for alignment-level QC (short-read-germline-calling) or sample identity (sample-identity-and-contamination).'
---

# Run QC and demultiplexing

## Capability
Turn a raw run into per-sample FASTQ and a pass, pass-with-note, or re-run call before alignment. Correct: yield, read share, and index assignment match the plan; each deviation has a cause.

## Decide
1. Record instrument, flow cell, kit, read length, planned yield, sample sheet version. Stop if one is missing.
2. Demultiplex with the vendor-supported tool. Index pairs must be unique per lane; record allowed mismatches and orientation.
3. A high Undetermined fraction usually means a sheet error. Fix the sheet and re-demultiplex before judging the run.
4. Estimate index hopping from valid pairs absent from the sheet.
5. Review quality, adapter, duplication, GC, length, lane and tile effects. Trim only for a stated reason.
6. ONT: yield, read length, quality per barcode; record basecaller, model; keep raw signal.
7. Cause first: one lane or tile points to the flow cell, a uniform drop to the library. Limits come from lab history.
8. Ask when a failure is borderline or a re-run uses a scarce sample.

## Find current information
Follow `current-methods-lookup`. Ask: which demultiplexer and QC tools the instrument supports; the index design and orientation the kit needs; the vendor's yield and quality expectations for this chemistry; the current basecaller and model. Search vendor and tool documentation and release notes, then independent papers (PubMed, Europe PMC; preprints labeled). Check release date, maintenance, fit to instrument and kit.

## Verify
* Assigned plus Undetermined reads equal total reads; read share matches plan.
* Control library (for example PhiX) gives the expected error rate.
* Re-demultiplex a subset with a second tool; assignments agree.
* Failing: counts do not reconcile or hopping exceeds the project norm. Fix and repeat.

## Failure modes
* Trimming that breaks R1 and R2 order.
* Lanes merged despite different read-group IDs.
* Adapter or UMI settings from another kit.

## Record and report
Log per `analysis-log`: question, date, sources, versions, not verified, recheck. Report per-sample metrics, run-level Undetermined and hopping, decision and reason.

Seeds: `${CLAUDE_SKILL_DIR}/references/where-to-look.md`.
