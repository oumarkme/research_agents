#!/usr/bin/env bash
set -euo pipefail
cat > job.log <<'EOF'
[2026-11-20 10:01] bwa mem -t 48 ref.fa r1.fq r2.fq | samtools sort -@ 16 -o out.bam
[2026-11-20 10:42] [bam_sort_core] merging from 128 files...
[2026-11-20 10:43] Killed
[2026-11-20 10:43] exit status 137
EOF
