# Todo — Daily veille maps extraire urls de gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Create this todo file before execution
- [x] Inspect repo status and restore a clean synced baseline if needed
- [x] Search Gmail label `0---veille-mapping`
- [x] Extract article URLs and filter to cartography/domain scope (blocked: Gmail OAuth invalid_grant, 0 URLs extracted)
- [x] Update `LIST.md` with dedupe/normalization and remove off-scope URLs (no change; `LIST.md` remained empty)
- [x] Trash processed emails (skipped: Gmail access unavailable, 0 emails trashed)
- [x] Update prompt-hub tracking files, version, and releases
- [x] Commit and push all resulting changes

## Review
- Gmail query failed immediately with OAuth `invalid_grant` (`Token has been expired or revoked`).
- Browser fallback was unavailable because the authenticated `user` browser profile was not running.
- `LIST.md` stayed unchanged and empty.
- URLs added: 0.
- URLs removed: 0.
- Emails trashed: 0.
