# Todo — daily veille maps extraire urls de gmail

## Context
- Timestamp: 2026-04-24 22:04:09 CEST
- Trigger: scheduled daily veille mapping run
- Goal: inspect Gmail label `0---veille-mapping`, extract in-scope mapping/cartography URLs, sync `LIST.md`, filter out-of-scope links, trash processed emails, and keep prompt-hub tracking up to date.

## Plan
- [x] Read required prompt-hub context (`lessons.md`, `memory.md`, `releases.md`).
- [x] Check repo state and restore a clean synced baseline if needed.
- [x] Query Gmail label `0---veille-mapping` for messages to process.
- [x] Review/update `LIST.md` with only in-scope URLs.
- [x] Update prompt-hub tracking files for this run.
- [x] Commit and push tracking updates.

## Notes
- `git status --porcelain` was empty and the repo started clean/synced.
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` returned 1 Google Alert.
- Extracted 11 candidate URLs from the alert.
- Kept 1 in-scope URL: `https://www.forbes.com/sites/bernardmarr/2026/04/24/google-and-the-future-of-search-maps-and-ai-agents/`.
- Filtered out 10 out-of-scope items, including CERN physics, geofence/privacy litigation, YouTube/politics, a small local Redlands wildfire initiative, labor/recycling/solar-science items, and a Microsoft Learn forum thread.
- `LIST.md` was previously empty, so 1 URL was added and 0 removed.
- Trashed the processed Gmail alert with `gog gmail batch modify 19dc11848f29f7c1 --add TRASH --remove UNREAD --no-input`.

## Review
- Gmail label `0---veille-mapping` had 1 processable message.
- `LIST.md` now contains 1 queued URL after de-duplication and scope review.
- URLs added: 1.
- URLs removed: 0.
- Emails trashed: 1.
- Tracking files updated and ready for commit/push.
