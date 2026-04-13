# Todo — daily veille maps extraire urls de gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Create this todo file before work starts
- [x] Check repo cleanliness/sync state
- [x] Search Gmail label `0---veille-mapping`
- [ ] Extract candidate article URLs
- [ ] Update `LIST.md` with dedupe + scope review
- [ ] Trash processed emails
- [ ] Update tracking files / finalize

## Notes
- Scheduled cron run at 2026-04-13 02:04 Europe/Paris.
- Previous runs were blocked by Gmail OAuth `invalid_grant`; verify first.

## Review
- Repo state at start: clean except for this new todo file.
- Gmail search failed immediately with OAuth `invalid_grant` (`Token has been expired or revoked`).
- Browser fallback unavailable: authenticated `user` browser profile not running.
- No URLs extracted, no changes to `LIST.md`, no emails trashed.
- Tracking files updated and pushed to restore a clean synced repo state.
