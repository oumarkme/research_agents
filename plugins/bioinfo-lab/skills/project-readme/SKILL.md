---
name: project-readme
description: 'Use when creating or updating a README.md for a tool, pipeline, analysis project, dataset, or repository: a compact structure that answers what it is, how to install and run it, and how it works.'
---

# Project README

Goal: a first-time visitor knows within one screen what the project is, how to install it, how to run it, and how it works. GitHub asks a README to say what the project does, why it is useful, how to get started, where to get help, and who maintains it. Google asks for a short summary with examples and links to the full documentation. Keep to that: compact, and link out for depth.

## Rules

1. Order: name and one-line tagline; what and why (at most 3 sentences); Install; Quick start; Usage; Methodology; Test; Citation; License and contact. Templates: `${CLAUDE_SKILL_DIR}/references/templates.md` (tool or pipeline, analysis project, dataset).
2. The first screen (about 25 lines) holds the tagline, what and why, Install, and Quick start.
3. Quick start is one runnable example with the expected output. Test every command in a clean copy before you write it down. Pin versions.
4. Methodology: numbered steps, each with tool, version, and key parameters; validation or benchmark results with numbers; known limits; references in APA, verified (`trusted-sources`). Add one diagram or figure only if it explains the flow.
5. Cut: badges that carry no information, project history, a table of contents in a short file, text copied from other docs, marketing language, TODO lists. Move detail to `docs/` or a `references/` folder and link it.
6. Length: tool or pipeline up to about 150 lines; analysis project up to about 100; subproject up to about 50.
7. State status (stable, experimental, archived), version, and license near the top.
8. Update the README in the same change as the code.
9. Never put patient-level data, credentials, machine names, or local paths in it.

Write the prose with `writing` (American English, humanizer pass, lint). Follow the Google Markdown style (`coding-style`). For datasets, add the data dictionary from `data-stewardship`.
