# Todo — daily-veille-maps-extraire-urls-de-gmail

## Objective
Run the daily sequence: Gmail label scan, article URL extraction, `LIST.md` update with clean sync/dedupe/commit/push, scope cleanup, and trash processed emails.

## Plan
- [x] Check repo state and restore a clean synced baseline if needed.
- [x] Search Gmail label `0---veille-mapping` and extract candidate article URLs.
- [x] Filter to cartography / geospatial / mapping-domain URLs, update `LIST.md`, and remove out-of-scope URLs already present.
- [x] Update prompt-hub tracking files (memory, releases, version, run summary, todo review).
- [x] Commit and push all required changes.
- [x] Trash processed Gmail emails.

## Review
- Repo was cleaned first by committing/pushing the new scheduled todo.
- Gmail label `0---veille-mapping` returned no messages with `--include-body --json --max 100 --no-input`.
- `LIST.md` was already empty and remained unchanged after scope review.
- URLs added: 0
- URLs removed: 0
- Emails trashed: 0
