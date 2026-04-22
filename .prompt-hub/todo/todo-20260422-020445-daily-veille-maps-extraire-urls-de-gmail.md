# Todo - daily veille maps extraire urls de gmail

## Context
- Scheduled run at 2026-04-22 02:04:45 CEST.
- Objective: scan Gmail label `0---veille-mapping`, extract article URLs, sync/update `LIST.md`, remove off-scope URLs, trash processed emails, and log per repo rules.

## Checklist
- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Restore clean synced repo state
- [x] Query Gmail label and extract candidate URLs
- [x] Update `LIST.md` with dedupe/normalization and scope filtering
- [x] Trash processed Gmail messages
- [x] Update prompt-hub tracking files
- [x] Commit and push

## Review
- Added 1 new in-scope URL from 1 Gmail alert, removed 1 off-scope existing URL from `LIST.md`, trashed 1 processed email, and updated prompt-hub tracking before commit/push.
