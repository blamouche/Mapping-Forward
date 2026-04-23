# Todo - Daily veille maps extraire urls de gmail

- [x] Read .prompt-hub/lessons.md
- [x] Read .prompt-hub/memory.md
- [x] Read .prompt-hub/releases.md
- [x] Create this todo file
- [x] Inspect repo status and restore a clean synced state if needed
- [x] Query Gmail label `0---veille-mapping` and extract candidate article URLs
- [x] Update `LIST.md` with normalized in-scope URLs and remove off-scope URLs
- [x] Trash processed Gmail messages
- [x] Update prompt-hub tracking files and review

## Notes
- Cron run requested on 2026-04-23 18:45 CEST.
- Must follow `/agents add-url` sync/dedupe/commit+push rules.
- If repo is not clean, commit/push all pending local changes first to return to a clean synced state.

## Review
- Repo was cleaned/synced via a baseline tracking commit before Gmail extraction.
- `gog gmail messages search` returned 0 messages for `label:0---veille-mapping`.
- `LIST.md` remained empty and no off-scope URLs needed removal.
- No Gmail messages were trashed.
