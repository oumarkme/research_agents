---
name: update
description: 'Use when the user asks to update, upgrade, or check the version of this plugin, or after an error that a newer release may fix.'
---

# Update the plugin

A skill cannot install a plugin; Claude Code does that through slash commands. This skill checks and tells the user exactly what to type.

1. Run `python ${CLAUDE_SKILL_DIR}/scripts/check_update.py`. It compares the installed `plugin.json` version with the one on GitHub (`oumarkme/research_agents`, branch `main`), lists the five newest commit subjects, and changes nothing.
2. Exit 0: report "up to date" with the version. Exit 10: report both versions, summarize the commit subjects in one or two lines, and give the commands the script prints. Exit 2: report that GitHub was unreachable and give the same commands.
3. The user types the commands (Claude cannot run slash commands):

```text
/plugin marketplace update research_agents
/plugin update bioinfo-lab@research_agents
/reload-plugins
```

4. Claude web app: Customize > Plugins, open the marketplace, and refresh it.
5. The slide template is not part of the plugin cache. `slides` downloads the newest copy on every use, so it needs no update step.

Do not edit files in the plugin cache; the next update overwrites them. Changes to the plugin belong in the source repository, with `version` raised in `plugin.json`.
