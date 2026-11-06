# Liftover failure modes and checks

| Failure | Detection |
|---|---|
| Unmapped (deleted, split) regions | Count rejects by contig; expect more in repeats |
| REF mismatch | Check REF against the target FASTA after normalizing |
| Strand flip, complemented alleles | Compare REF and ALT to the target |
| Indel shift | Left-align and re-normalize |
| SV breakend or END invalid | Lift both ends; check SVLEN |
| Contig renamed | Compare `.fai` before and after |

## Chain file
* Prefer a chain from the reference directory in CLAUDE.md; otherwise download from the assembly provider and record source, date, and checksum.
* The chain must match the exact source and target contig sets.

## Checks
1. Round-trip a random sample and compare; report the fraction recovered.
2. Spot-check known sites in the target build.
3. Count unmapped and rejected records; review records that split.
