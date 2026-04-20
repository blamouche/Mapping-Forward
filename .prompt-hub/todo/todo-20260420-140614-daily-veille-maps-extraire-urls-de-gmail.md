# Todo - Daily veille maps extraire urls de gmail

- [x] Read lessons, memory, releases
- [x] Check repo status
- [x] Sync repo from a clean state
- [x] Search Gmail label `0---veille-mapping`
- [x] Extract and filter article URLs
- [x] Update `LIST.md` with dedupe and scope cleanup
- [x] Trash processed emails
- [x] Update prompt-hub tracking files
- [x] Commit and push

## Notes
- Scheduled cron run on 2026-04-20 14:05 CEST.
- Must commit/push all pending local changes first if repo is not clean before the Gmail extraction phase.

## Review
- Repo synced cleanly with `git pull --rebase origin main` (already up to date).
- Gmail query `label:0---veille-mapping` returned 0 messages, so no URLs were extracted.
- `LIST.md` remained empty after scope review.
- No processed emails to move to Trash.
