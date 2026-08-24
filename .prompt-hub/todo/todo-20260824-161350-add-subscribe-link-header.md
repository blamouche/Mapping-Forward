# Task: Add a "Subscribe" link in the site header

## Context
- Navbar (`page_html` in `docs/build_site.py`) has links: Home, Archives, RSS, Substack.
- User request: add a "Subscribe" link pointing to the Substack subscribe URL
  `https://mappingforward.substack.com/subscribe?utm_source=menu&simple=true&next=https%3A%2F%2Fmappingforward.substack.com%2F`.

## Plan
1. Add `<a href="..." target="_blank" rel="noopener">Subscribe</a>` to `.nav-links` (after Substack).
2. Rebuild `python3 docs/build_site.py`, verify the link in `docs/dist/`.

## Done
- [x] Subscribe link added to navbar
- [x] Rebuilt; link present in dist

## Review
- Kept the existing "Substack" link (homepage); "Subscribe" is a separate CTA to the subscribe page.
- 2026-08-24 16:15 CEST: committed + pushed (auto-redeploy Pages).
