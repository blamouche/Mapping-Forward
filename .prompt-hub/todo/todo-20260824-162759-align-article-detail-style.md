# Task: Align the article detail page style with the home page article card style

## Context
- Home page articles are cards (`.article-card`): `background: var(--bg-card)`, `border: 1px solid var(--border)`, `border-radius: var(--radius)`, padding, muted 0.95rem elevator pitch, small meta row.
- Article detail page (`.article-full`) is a plain text page: no card container, larger meta (0.88rem), italic prominent pitch.
- User request: align the detail page style with the home card style.

## Plan
1. `.article-full` → card container (bg-card, border, radius, padding).
2. `.article-meta-full` → match `.article-meta` (font-size 0.82rem, align-items center).
3. `.elevator-pitch-section .elevator-pitch` → match card pitch (muted, 0.95rem, no italic).
4. Rebuild, verify.

## Done
- [x] `.article-full` card container
- [x] `.article-meta-full` aligned
- [x] `.elevator-pitch-section .elevator-pitch` aligned
- [x] Rebuilt + verified

## Review
- Kept h1 prominent (page title) and the source-link-full CTA button.
- Also aligned `.takeaways-section` to the card's takeaways box (bg-hover, border-soft) and added mobile padding override (768px).
- 2026-08-24 16:30 CEST: committed + pushed (auto-redeploy Pages).
