---
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill]
runs: 3
tags: ['claude-md']
append_system_prompt: "The user invoked /claude-md-setup. Fixture files under ./fixtures stand in for the global and project scopes."
---

Run claude-md-setup in audit mode. Treat ./fixtures/global/CLAUDE.md as my global file and ./fixtures/project/CLAUDE.md as my project file. Do not change anything.
