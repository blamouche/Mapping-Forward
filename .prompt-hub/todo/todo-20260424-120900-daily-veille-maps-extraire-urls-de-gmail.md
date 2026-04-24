# Todo - daily-veille-maps-extraire-urls-de-gmail

## Context
- Timestamp: 2026-04-24 12:09:00 CEST
- Goal: traiter les emails Gmail `label:0---veille-mapping`, extraire les URLs, mettre à jour `LIST.md`, filtrer le hors-sujet, puis mettre à la corbeille les emails traités.

## Checklist
- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Check repo status
- [x] Fetch Gmail messages for label
- [x] Extract and filter candidate URLs
- [x] Update `LIST.md` with dedupe and normalization
- [x] Update prompt-hub tracking files
- [x] Commit and push all pending changes
- [x] Trash processed Gmail messages

## Notes
- Repo was clean before starting.
- One Google Alert message found.
- 6 candidate URLs extracted, 3 retained.
- Retained URLs:
  - https://www.gim-international.com/content/news/geo-business-2026-opens-registration-with-expanded-programme
  - https://www.geoweeknews.com/blogs/to-measure-the-earth-is-to-know-it
  - https://www.geoweeknews.com/news/how-the-florida-wildlife-corridor-foundation-uses-gis-to-save-florida-s-wild-lands

## Review
- Completed successfully.
- `LIST.md` updated with 3 new in-scope URLs.
- 1 processed Gmail alert moved to Trash.
- No existing URL needed removal during this run.
