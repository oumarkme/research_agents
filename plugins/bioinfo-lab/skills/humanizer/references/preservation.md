# Protected content

The humanizer pass must not change these. No study has measured how often humanizer tools alter numbers, units, symbols, or citations, so the check is mechanical.

| Kind | Examples | Script kind |
|---|---|---|
| Numbers with units | 32.4×, 5 kb, 95%, 1e-8 | `numbers` |
| P values and intervals | P = 0.003, OR = 1.8 | `comparisons` |
| Variant strings | c.743G>A, p.Arg248Gln, g.7675088C>T | `hgvs` |
| rs numbers | rs11540652 | `rsid` |
| Accessions | NM_000546.6, ENST00000269305, GCA_000001405.29, SRR1234567, VCV000012345 | `accession` |
| DOIs, PMIDs, URLs | 10.1038/gim.2015.30, PMID: 25741868 | `doi`, `pmid`, `url` |
| Citation keys | `[@smith2024]`, `\cite{smith2024}` | `citation_key` |
| Author and year | Smith et al., 2024 | `author_year` |
| Code | inline code and fenced blocks | `code` |
| Headings | `## Variant filtering` | `heading` |
| Figure and table references | Table 2, Figure S3 | `figref` |
| Symbols and abbreviations | BRCA2, GRCh38, GWAS | `symbol` |

## Procedure

1. Before editing, read the file once and note the protected spans in the sentences you will touch.
2. Edit around them. Do not retype a protected span; leave it in place.
3. Run `scripts/preserve_diff.py ORIGINAL EDITED`. Each LOST or ADDED line is a stop. Restore the span, or ask the author if the change is intended. Use `--skip heading` only when the headings were meant to change.

## What the script cannot see

* Numbers written as words ("three samples").
* A weaker or stronger claim ("suggests" to "shows").
* A moved sentence that changes what a citation supports.
* A swapped gene symbol of the same shape (BRCA1 for BRCA2 appears as LOST and ADDED, but a swap inside a mixed list still needs a read).
* A reference that was never real. Verify identifiers through `trusted-sources`.

Read the word-level diff after the script passes.
