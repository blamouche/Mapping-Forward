# Todo — Daily veille maps extraire urls de gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Create this todo file before work
- [x] Inspect repo state and restore a clean synced baseline if needed
- [x] Query Gmail label `0---veille-mapping` and extract candidate article URLs
- [x] Update `LIST.md` with normalized, deduped, in-scope URLs only
- [x] Remove out-of-scope / small local initiative URLs from `LIST.md`
- [x] Trash processed Gmail emails
- [x] Update prompt-hub tracking (`memory`, `releases`, `version`, todo)
- [ ] Commit and push all required changes

## Notes
- Scheduled run requested at 2026-04-12 22:04:22 Europe/Paris.
- Need summary with counts for URLs added/removed.

## Review
- Repo state checked: only the new scheduled todo was pending before execution.
- Gmail query failed immediately with OAuth `invalid_grant`.
- Browser fallback was unavailable because no authenticated `user` Chrome session was running.
- No emails were read successfully, no URLs were extracted, `LIST.md` stayed unchanged, and no emails were trashed.
- Prompt-hub tracking updated for the failed run; commit/push still pending at this stage.
