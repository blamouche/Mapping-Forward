# Task: Remove picto from site header

## Context
- `site/build_site.py` renders two header pictos 🗺️: hero `<h1>` on index and navbar brand (all pages).
- User request: remove the picto in the site header.

## Plan
1. Remove 🗺️ from hero h1 in `generate_index`.
2. Remove 🗺️ from navbar brand in `page_html`.
3. Rebuild `site/build_site.py`, verify no 🗺️ in `site/dist/`.

## Done
- [x] Hero h1 picto removed
- [x] Navbar brand picto removed
- [x] Rebuilt; `grep 🗺️ site/dist/` returns nothing

## Review
- Change is CSS/HTML-source only; no JS. Archives page header keeps its 📚 (out of scope).
- Note: `site/build_site.py` also carries an uncommitted style-refresh change (todo-20260824-105913).
- 2026-08-24 12:00 CEST: Committed + pushed (site moved to `docs/` meanwhile).
