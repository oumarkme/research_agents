#!/usr/bin/env bash
set -euo pipefail
cat > README.md <<'EOF'
# demo-pipeline
Snakemake workflow for read QC. Run `make test` for the tests; `make lint` for ruff.
EOF
printf 'test:\n\tpytest -q\nlint:\n\truff check .\n' > Makefile
mkdir -p tests && echo 'def test_ok(): assert True' > tests/test_ok.py
