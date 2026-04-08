# Todo — Daily veille maps extraire urls de gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Review current `LIST.md`
- [x] Check git status and restore clean synced repo state
- [x] Search Gmail label `0---veille-mapping`
- [x] Extract article URLs and filter to mapping/cartography/domain-news scope
- [x] Update `LIST.md` with dedupe and remove off-scope/local initiatives
- [x] Trash processed Gmail emails
- [x] Update prompt-hub tracking (`memory.md`, `version.md`, `releases.md`)
- [x] Commit and push all required changes

## Notes
- Scheduled cron run at 2026-04-08 02:04 Europe/Paris.
- Must follow `agents.md` agent `add-url`: clean sync, dedupe, verify, commit+push.
- If repo is dirty at start, commit/push all pending local changes first to restore a clean state.

## Review
- Gmail search returned 0 messages for `label:0---veille-mapping`.
- `LIST.md` already contained 3 relevant mapping/cartography URLs and required no removals.
- No emails were trashed and no URLs were added.
- Tracking files were updated and pushed to keep the repo clean.
