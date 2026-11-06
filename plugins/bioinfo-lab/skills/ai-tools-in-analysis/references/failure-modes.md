# Failure modes and tests

Named by Sharpton 2026: hallucination (confident content with no basis), sycophancy (agreeing with the user), overconfidence, plausible but wrong reasoning, and syntactically correct code with wrong logic. The genomics items are judgment from practice, not cited; each has a test.

| Failure | Test |
|---|---|
| Off-by-one from 0-based BED versus 1-based VCF/GFF | Convert 3 known records by hand; check lengths and a known SNV position |
| Build mismatch (hg19 versus GRCh38) assumed or switched silently | Print build from headers; check a known variant's position in both builds |
| Contig names `chr1` versus `1`; unplaced contigs dropped | Compare contig sets of inputs; count records before and after |
| REF/ALT swap, strand flip, multiallelic split or left-alignment ignored | Run on a handful of indels and a multiallelic site with known answers |
| Sample order differs between tables | Join by ID, never by position; assert equal sets |
| Hallucinated flag, function, or package | Look it up in the installed `--help` or docs; run once with `--version` |
| Plausible but wrong statistics (wrong test, no correction, leakage) | Reproduce with a second method; permutation or simulation with known effect |
| Fabricated citation or number | Resolve DOI and PMID; recompute from raw input |
| Silent filtering (NAs, duplicates, failed rows) | Log row counts at each step |
| Code works on the toy case only | Add one real-size run and a spot check |

## Known-answer inputs

Use a public truth set (for example GIAB benchmark records; see `trusted-sources`), a simulated dataset with a planted effect, or a 20-record file solved by hand. Store the file and expected output in the repository as a test.

## Prompt habits

State build, coordinate system, tool versions, and expected output form. Ask for tests with the code. Ask it to list assumptions. Start a new session for review so it does not defend its own code (judgment).

## Log entry

```
Date:
Model/tool and version:
Task:
Prompt file or text:
Output used where:
Verification (test, recompute, doc check):
Reviewer:
```
