#!/usr/bin/env bash
set -euo pipefail
mkdir -p fixtures/global fixtures/project
cat > fixtures/global/CLAUDE.md <<'EOF'
# Global
* Always reply in Spanish.
* Be careful with data.
* For this repo run `make test-all` before every commit.
EOF
cat > fixtures/project/CLAUDE.md <<'EOF'
# Project
* Reply in English.
* Be careful with data.
* Run `make test-all` before every commit.
* API token: sk-test-0000000000
EOF
