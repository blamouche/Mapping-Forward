# Todo - daily veille maps extraire urls de gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Inspect repo status and current `LIST.md`
- [x] Query Gmail label `0---veille-mapping`
- [x] Extract and classify candidate URLs
- [x] Restore a clean synced repo state if needed, then update `LIST.md`
- [x] Remove out-of-scope URLs from `LIST.md`
- [x] Trash processed emails
- [ ] Update prompt-hub tracking files, commit, and push

## Notes
- Cron run started at 2026-04-29 06:05:40 CEST.
- Follow `agents.md` agent `add-url` rules plus prompt-hub versioning/memory requirements.

## Review
- Gmail returned no messages for `label:0---veille-mapping`.
- `LIST.md` was already empty and remained in scope.
- No emails were trashed.
- Prompt-hub tracking files were updated for an empty scheduled run; commit/push still pending.
