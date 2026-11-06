---
name: slides
description: 'Use when the user asks for a slide deck, presentation, talk, or PDF slides: builds it from the newest copy of the oumarkme/slide_template (HTML by default, PDF on request).'
---

# Slides

The default template is `https://github.com/oumarkme/slide_template`: one design (white pages, Noto fonts, 16:9, Okabe-Ito colors) in two formats, a reveal.js HTML file and a Beamer (XeLaTeX) file. A template named in CLAUDE.md overrides it. Build from the newest copy, never from an older one.

## Workflow

1. Format: HTML (`html/index.html`) unless the user asks for PDF. For PDF, use the LaTeX route.
2. Fetch the template into a new, empty folder in the project (not the scratchpad if the deck is a deliverable): `python ${CLAUDE_SKILL_DIR}/scripts/fetch_template.py <project>/slides_build`. Report the template version it prints. If the download fails, say so and ask; do not substitute another design.
3. Read the template's `README.md` (usage tables) and the demo file for the chosen format. Copy the demo to a descriptive name, for example `my-talk.html`. Keep the theme (`<style>` and `<script>` in HTML; part 1 in LaTeX) unchanged. Replace only the title block and the slides. Do not recolor the template.
4. Plan first: one message per slide, a title that states the point, at most about 40 words per slide, speaker notes for detail. Author line: author and affiliation from the user's CLAUDE.md, else ask.
5. Write slide text with `writing` (humanizer pass, lint the text). Slides in another language follow `translator`.
6. Figures: make each with `plotting` (JPEG 300 dpi by default) and place it with the template's figure and `credit` pattern. Colors follow `${CLAUDE_SKILL_DIR}/../plotting/references/color.md` ("Slides and posters"; do not repeat hex codes here): white background, color only where it clarifies, blue accent, viridis for continuous scales. Template names: `oiBlue`, `oiVermillion`, `oiGreen`, `oiPurple` (LaTeX) and `--oi-blue`, `--oi-vermillion`, `--oi-green`, `--oi-purple` (CSS).
7. HTML: copy images next to the file and fix `src` paths (the demo path `../figures/` works only in the template repository). The deck needs a network connection for reveal.js, KaTeX, and fonts; say so when the user will present offline.
8. PDF: run `bash fonts/download.sh` once (about 36 MB; say so first), then `cd latex && latexmk <name>.tex`. If XeLaTeX or `latexmk` is missing, offer HTML with `?print-pdf` printed from Chrome, margins none.
9. Check before reporting: render the deck (headless Chromium screenshot for HTML, `pdftoppm -r 100` for PDF), view at least five slides including the densest, and confirm no text overflows, no figure is cut, and numbers and footer are right. Never report a deck you have not viewed.
10. Report the path of the deck, the template version, the slide count, and what was checked. Remove the demo slides, `.git`, and unused files only if the user asks.

