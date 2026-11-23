#!/usr/bin/env bash
# Run the eval suite from outside the plugin folder. Usage: evals/run.sh [claude plugin eval options]
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
plugin="$root/plugins/bioinfo-lab"
[ -e "$plugin/evals" ] && { echo "refusing: $plugin/evals exists" >&2; exit 1; }
ln -s ../../evals "$plugin/evals"
trap 'rm -f "$plugin/evals"' EXIT
cd "$plugin"
claude plugin eval . --scaffold --trust-plugin "$@"
