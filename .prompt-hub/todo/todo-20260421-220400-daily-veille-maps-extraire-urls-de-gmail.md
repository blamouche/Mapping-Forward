# Todo - daily veille maps extraire urls de gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Create this task file before starting work
- [x] Check repo status and restore a clean synced baseline if needed
- [x] Query Gmail label `0---veille-mapping` and extract candidate article URLs
- [x] Update `LIST.md` with normalized in-scope URLs only, with de-duplication
- [x] Remove out-of-scope/local URLs already present in `LIST.md`
- [x] Trash processed Gmail messages
- [x] Update prompt-hub tracking (`memory.md`, `releases.md`, `version.md`) and finalize review

## Notes
- Scheduled cron run at 2026-04-21 22:04 CEST.
- Must follow `add-url` sync/verify/commit flow while also cleaning any pending local changes first.

## Review
- Repo was clean apart from this mandatory todo file; no other unsynced local changes were pending.
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` returned 0 message.
- `LIST.md` was empty and stayed empty after scope review, so 0 URL was added and 0 URL was removed.
- No processed email needed to be moved to Trash.
- Prompt-hub tracking updated for this empty scheduled run.
