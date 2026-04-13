# Todo — Daily veille maps extraire urls de gmail

## Context
- Scheduled run at 2026-04-13 06:04 CEST.
- Goal: search Gmail label `0---veille-mapping`, extract article URLs, sync/update `LIST.md`, remove off-scope URLs, trash processed emails, then log/commit/push per repo rules.

## Plan
- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Create this task file before execution
- [x] Check repo status and restore a clean synced baseline if needed
- [x] Query Gmail label `0---veille-mapping` and extract candidate URLs
- [ ] Update `LIST.md` with normalized, deduped, in-scope URLs only
- [ ] Trash processed Gmail messages
- [x] Update prompt-hub tracking (`memory`, `releases`, `version`, run summary)
- [ ] Commit and push all required changes

## Notes
- Recent runs were blocked by Gmail OAuth `invalid_grant`; retry first, then test browser fallback if needed.

## Review
- Repo state at start: dirty only because of this new scheduled todo file (`git status --short --branch` showed `?? .prompt-hub/todo/todo-20260413-060400-daily-veille-maps-extraire-urls-de-gmail.md`).
- Gmail search failed immediately with OAuth `invalid_grant` (`Token has been expired or revoked`).
- Browser fallback unavailable: the authenticated `user` browser profile is not running.
- No URLs extracted, no changes to `LIST.md`, and no emails trashed.
- Tracking files updated; commit/push still required to restore a clean synced repo state.
