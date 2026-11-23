# CLAUDE.md scopes

Check these against the current Claude Code memory documentation if behavior differs.

| Scope | File | Shared with | Put here |
|---|---|---|---|
| Managed | set by an administrator | everyone on the machine | organization policy (not edited here) |
| Global (user) | `~/.claude/CLAUDE.md` | only you, all projects | personal preferences that hold in every project |
| Project | `./CLAUDE.md` or `./.claude/CLAUDE.md` | the team, through git | project facts, build and test commands, conventions |
| Local | `./CLAUDE.local.md` | only you, this project | personal notes for this project; git-ignore it |
| Subdirectory | `CLAUDE.md` in a subfolder | as the project | loads on demand when files there are read |

* All discovered files are concatenated, not overridden. Files closer to the working directory are read last.
* The file is delivered as context in a user message. It guides the model; it does not enforce anything.
* Aim for under 200 lines per file. Longer files cost context and lower adherence.
* `@path` imports (up to four hops) organize content; the imported text still loads.
* `.claude/rules/*.md` (or `~/.claude/rules/`) with `paths` frontmatter load only when matching files are read.
* `/memory` lists what loaded; `/init` suggests improvements to an existing file.
* Anything that must always happen belongs in a hook or a permission rule in `settings.json`, not in CLAUDE.md.
