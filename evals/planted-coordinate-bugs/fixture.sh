#!/usr/bin/env bash
set -euo pipefail
cat > liftcheck.py <<'EOF'
"""Count variants inside exons. BED is 0-based half-open; VCF is 1-based."""
import csv
EXON_BED = "exons_hg19.bed"      # annotated on hg19
VCF = "sample_hg38.vcf"          # called on hg38

def load_exons():
    exons = []
    for chrom, start, end in csv.reader(open(EXON_BED), delimiter="\t"):
        exons.append((chrom, int(start), int(end)))
    return exons

def in_exon(chrom, pos, exons):
    return any(c == chrom and s <= pos <= e for c, s, e in exons)

def main():
    exons = load_exons()
    n = 0
    for line in open(VCF):
        if line.startswith("#"):
            continue
        chrom, pos = line.split("\t")[:2]
        if in_exon(chrom, int(pos), exons):
            n += 1
    print(n)
main()
EOF
