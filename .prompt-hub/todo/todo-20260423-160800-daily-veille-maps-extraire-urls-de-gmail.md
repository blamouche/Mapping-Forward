# Todo - Daily veille Maps extraire urls de Gmail

## Context
- Requested at: 2026-04-23 16:08 CEST
- Goal: process Gmail label `0---veille-mapping`, extract article URLs, sync/update `LIST.md`, remove off-scope URLs, trash processed emails, and commit/push all repo changes.

## Plan
- [x] Inspect repo status and restore a clean synced baseline if needed.
- [x] Query Gmail label `0---veille-mapping` and extract candidate article URLs.
- [x] Filter to mapping/cartography/geospatial-domain URLs, normalize/dedupe, update `LIST.md`, and remove off-scope existing URLs.
- [x] Update prompt-hub tracking files for this run.
- [x] Commit and push all local changes.
- [x] Trash processed Gmail messages.

## Review
- Repo baseline committed and pushed first to restore a clean synced state.
- Gmail label `0---veille-mapping` returned 0 messages with `--include-body --json --max 100 --no-input`.
- `LIST.md` remained empty and no existing URL needed removal after scope review.
- Added 0 URLs, removed 0 URLs, trashed 0 emails.
- Tracking files updated for the empty scheduled run.
