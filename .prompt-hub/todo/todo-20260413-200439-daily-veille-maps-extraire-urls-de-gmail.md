# Todo — daily-veille-maps-extraire-urls-de-gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Create this task file before work starts
- [x] Check repo state and restore a clean synced baseline if needed
- [x] Query Gmail label `0---veille-mapping` and extract article URLs
- [x] Update `LIST.md` with normalized/deduped in-scope URLs only
- [x] Review `LIST.md` and remove off-scope/local-noise URLs
- [x] Trash processed Gmail emails
- [x] Update prompt-hub memory/version/releases and finalize review

## Plan
1. Inspect git status and sync only after the working tree is clean, committing/pushing any pending local changes first if needed.
2. Query Gmail label `0---veille-mapping`, extract candidate article URLs, and filter them to mapping/cartography/geospatial domain news while excluding local small-scale initiatives.
3. Normalize, dedupe, and write the resulting queue to `LIST.md`, then trash the processed emails.
4. Update prompt-hub tracking files, commit/push all resulting changes, and record a concise review.

## Review
- Repo was already clean/synced at start (`## main...origin/main` aside from this new todo).
- Gmail query `label:0---veille-mapping` returned 0 messages with `--include-body --json --max 50 --no-input`.
- `LIST.md` was already empty and stayed empty after scope review.
- URLs added: 0.
- URLs removed: 0.
- Emails trashed: 0.
