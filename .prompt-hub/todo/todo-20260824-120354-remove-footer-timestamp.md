# Task: Remove "Static site generated on ..." line from site footer

## Context
- `docs/build_site.py` renders a footer with two `<p>`: `{SITE_TITLE} — {SITE_SUBTITLE}` and a timestamp + Source link.
- User request: remove the "Static site generated on 24 Aug 2026 at 09:57 — Source" line.

## Plan
1. Remove the timestamp `<p>` (line 222) from `page_html` footer in `docs/build_site.py`. Keep the title/subtitle line.
2. Rebuild `python3 docs/build_site.py`, verify no "Static site generated" in `docs/dist/`.

## Done
- [x] Footer timestamp line removed from generator
- [x] Rebuilt; `grep "Static site generated" docs/dist/` returns nothing

## Review
- Change is HTML-source only; CSS untouched. Footer keeps site title + subtitle.
- Pending: commit + push (auto-triggers workflow → rebuild + redeploy Pages). Awaiting user go-ahead.
