# Todo — daily veille maps extraire urls de gmail

## Context
- Trigger: cron daily veille mapping at 2026-04-12 10:04 CEST
- Goal: scan Gmail label `0---veille-mapping`, extract article URLs, update `LIST.md`, remove off-scope URLs, trash processed emails, then commit/push all changes.

## Plan
- [x] Inspect repo state and restore a clean synced baseline if needed.
- [x] Query Gmail label `0---veille-mapping` and extract candidate article URLs.
- [ ] Update `LIST.md` with normalized/deduped in-scope URLs and remove off-scope/local items.
- [ ] Trash processed emails, then update prompt-hub tracking, version, releases, and memory.
- [ ] Commit and push all resulting changes.

## Review
- Gmail access failed immediately with OAuth `invalid_grant` (`Token has been expired or revoked`).
- No Gmail messages could be read, so no URLs were extracted, `LIST.md` stayed unchanged, and no emails were moved to Trash.
- Prompt-hub tracking files were updated to record the blocked run; commit/push still pending.
