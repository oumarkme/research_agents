---
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
runs: 3
tags: ['quality']
---

Have an independent subagent check the claims in ./report.md against ./data.csv, giving it only the files and not your own conclusion, and tell me the verdict.
