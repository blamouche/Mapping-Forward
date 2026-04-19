# Todo - Daily veille Maps Extraire urls de gmail

## Context
- Trigger: cron `e86a7434-db99-44fe-8c2c-6c13463de00f`
- Time: 2026-04-19 22:04:40 CEST
- Goal: Gmail label `0---veille-mapping` -> extract article URLs -> update `LIST.md` -> filter out-of-scope URLs -> trash processed emails -> commit/push.

## Checklist
- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Create this todo file before work
- [x] Check git status and restore clean synced state if needed
- [x] Query Gmail label and extract candidate URLs
- [x] Review scope and update `LIST.md`
- [x] Trash processed emails
- [x] Update prompt-hub tracking files
- [x] Commit and push

## Notes
- If repo is dirty, commit/push all unsynced local changes first to restore a clean baseline before Gmail extraction.
- Scope: cartography, mapping, GIS, geospatial data, domain news. Exclude small local initiatives.

## Review
- Repo restored to a clean baseline, Gmail label `0---veille-mapping` returned 1 message, 13 candidate URLs were extracted, 1 in-scope URL was kept and added to `LIST.md`, 0 existing URLs were removed, and 1 processed email was moved to Trash.
