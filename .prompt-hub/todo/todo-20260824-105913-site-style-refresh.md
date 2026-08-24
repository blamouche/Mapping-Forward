# Task: Refresh the static site style (prettier, less basic)

## Context
- Site generator: `site/build_site.py` (pure Python stdlib, no JS, relative links).
- Stylesheet is the inline `CSS` variable in `build_site.py`; written to `dist/style.css`.
- Goal: make the site a bit prettier / less basic while keeping constraints:
  - No JavaScript, pure CSS.
  - Dark + light themes (`prefers-color-scheme`).
  - Relative links (works via file:// and web server).
  - Keep structure / generated HTML markup compatible.

## Plan
1. Read current CSS (done) and generated HTML structure.
2. Refined design system: typography (font stack, hierarchy, letter-spacing),
   refined palette + gradient accent, spacing scale, shadows, radius.
3. Polish components: navbar, hero, heatmap, article cards (hover lift), article
   page prose, archives, buttons, footer.
4. Build site (`python3 site/build_site.py`), verify dist renders.
5. Commit + push.

## Review
- 2026-08-24 11:35 CEST: Direction pivoted from "prettier/gradient" to **sober + professional
  (no AI slop)**. Rewrote the stylesheet: flat surfaces, 1px borders, one restrained
  steel-blue accent, 4px radius, system font stack, max-width 860px. Removed gradients,
  shadows, backdrop blur, pills, uppercase letter-spacing, hover lifts, and decorative
  emojis in markup (article meta, section h2, archives, buttons, source links).
- Built `python3 site/build_site.py` → 783 articles, 0 emojis in `dist/`. Constraints
  respected (pure CSS, dark/light, relative links, markup structure unchanged).
- Pending: commit + push (also includes picto removals from earlier requests).
- 2026-08-24 12:00 CEST: Committed + pushed as part of "commit et push tout"
  (site moved to `docs/` meanwhile; rebuild done from `docs/`, 788 dist files updated).