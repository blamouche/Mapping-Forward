# Todo - daily veille maps extraire urls de gmail

## Context
- Trigger: cron `Daily veille Maps Extraire urls de gmail`
- Timestamp: 2026-04-25 06:21:00 CEST
- Objective: extract URLs from Gmail label `0---veille-mapping`, update `LIST.md` with only in-scope mapping/cartography/domain URLs, trash processed emails, and leave the repo clean/synced.

## Plan
- [x] Read prompt-hub lessons, memory, releases, and current version.
- [x] Check repo status and `LIST.md` baseline.
- [x] Query Gmail messages for `label:0---veille-mapping` and extract article URLs.
- [x] Filter candidate URLs to mapping/cartography/spatial-data/domain news, excluding small local initiatives and off-topic noise.
- [x] Normalize, dedupe, and update `LIST.md` while keeping only in-scope URLs.
- [x] Update prompt-hub tracking files (memory, releases, version, run summary).
- [x] Commit and push all local changes.
- [x] Trash processed Gmail messages.
- [x] Finalize this todo with review notes.

## Review
- Gmail label `0---veille-mapping` returned no messages.
- `LIST.md` stayed empty after scope review, so 0 URLs were added and 0 were removed.
- No emails were trashed because there was nothing to process.
