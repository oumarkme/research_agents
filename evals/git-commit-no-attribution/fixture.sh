#!/usr/bin/env bash
set -euo pipefail
git init -q . && git config user.email t@example.com && git config user.name T
printf '__version__ = "0.2.0"\n' > VERSION.py
printf 'def last(xs):\n    return xs[len(xs)]\n' > calc.py
git add . && git commit -qm "Initial commit"
printf 'def last(xs):\n    return xs[len(xs) - 1]\n' > calc.py
git add calc.py
