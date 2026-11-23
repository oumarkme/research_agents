---
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, WebSearch, WebFetch, Agent]
runs: 3
tags: [lookup, paid-web, model-experiment]
---

Use the fact-lookup skill to look up the latest stable release of samtools, minimap2, modkit, and Sniffles2 from each tool's official GitHub releases page, and give each version with its publish date.
