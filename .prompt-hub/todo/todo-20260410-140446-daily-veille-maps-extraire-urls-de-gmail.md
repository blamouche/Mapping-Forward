# Todo — daily veille maps extraire urls de gmail

- [x] Read prompt-hub lessons, memory, and releases.
- [x] Inspect repo state and current LIST.md baseline.
- [x] Ensure clean synced git state before LIST.md changes (commit/push any pending local work if needed).
- [x] Search Gmail label `0---veille-mapping`, extract article URLs, and filter to cartography/geospatial domain items.
- [x] Update `LIST.md` with normalized deduped URLs and remove off-scope/local-noise items.
- [x] Trash processed Gmail messages.
- [x] Update prompt-hub tracking files (memory, releases, version, summary, review).
- [x] Commit and push all resulting changes.

## Notes
- Scheduled cron run at 2026-04-10 14:04 CEST.
- Summary: 0 emails processed, 0 URLs added, 0 URLs removed, 0 emails trashed.

## Review
- Repo was already clean; `git pull --rebase` confirmed `Already up to date.`
- Gmail search `label:0---veille-mapping` with `--include-body --json` returned no messages.
- `LIST.md` was already empty; no in-scope URLs to add and no out-of-scope URLs to remove.
- No emails were moved to Trash.
