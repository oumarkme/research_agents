---
name: slides
description: 'Use when the user asks for a slide deck, presentation, talk, or PDF slides: builds it from the newest copy of the oumarkme/slide_template (HTML by default, PDF on request).'
---

# Slides

The lab template is `https://github.com/oumarkme/slide_template`: one design (white pages, Noto fonts, Okabe-Ito colors, 16:9) in two formats, a reveal.js HTML file and a Beamer (XeLaTeX) file. Always build from the newest copy; never from memory of an older one.

## Workflow

1. Format: HTML (`html/index.html`) unless the user asks for PDF. For PDF, use the LaTeX route.
2. Fetch the template into a new, empty folder in the project (not the scratchpad if the deck is a deliverable): `python ${CLAUDE_SKILL_DIR}/scripts/fetch_template.py <project>/slides_build`. Report the template version it prints. If the download fails, say so and ask; do not improvise a different design.
3. Read the template's `README.md` (usage tables) and the demo file for the chosen format. Copy the demo to a descriptive name, for example `my-talk.html`. Keep the theme (`<style>` and `<script>` in HTML; part 1 in LaTeX) unchanged. Replace only the title block and the slides.
4. Plan first: one message per slide, a title that states the point, at most about 40 words per slide, speaker notes for detail. Author line: Jen-Hsiang Ou, Ph.D. unless the user says otherwise (see CLAUDE.md for affiliation).
5. Write slide text with `writing` (humanizer pass, lint the text). Chinese slides follow `translator` rules; technical terms stay in English.
6. Figures: make each with `plotting` (JPEG 300 dpi by default) and place it with the template's figure and `credit` pattern. Colors come only from Okabe-Ito plus grays; use the template's `oiBlue`, `oiVermillion`, `oiGreen` or the CSS variables.
7. HTML: copy images next to the file and fix `src` paths (the demo path `../figures/` works only in the template repository). The deck needs a network connection for reveal.js, KaTeX, and fonts; say so when the user will present offline.
8. PDF: run `bash fonts/download.sh` once (about 36 MB; say so before downloading), then `cd latex && latexmk <name>.tex`. Check that TeX Live with XeLaTeX and `latexmk` exist; if not, offer the HTML route with `?print-pdf` printed from Chrome with margins set to none.
9. Check before reporting: render the deck (headless Chromium screenshot for HTML, `pdftoppm -r 100` for PDF), view at least five slides, including the densest, and, confirm no text overflows, no figure is cut, and slide numbers and footer are right. Never report a deck you have not viewed.
10. Report the path of the deck, the template version, the slide count, and what was checked. Remove the template's demo slides, `.git`, and unused files from the delivered folder only if the user asks.

Patient-level data never goes on a slide that leaves the project (see `lab-rules`).
