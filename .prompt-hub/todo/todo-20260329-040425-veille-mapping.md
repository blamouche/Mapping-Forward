# Todo: veille-mapping (2026-03-29 04:04 CET)

## Goal
Run daily veille mapping sequence: scan Gmail label 0---veille-mapping, extract mapping-related URLs, update LIST.md (dedupe), clean non-mapping/local items, trash processed emails, and report summary.

## Plan
1. Sync repo state and ensure clean working tree (commit/push any pending changes if needed).
2. Query Gmail label `0---veille-mapping` for messages; extract article URLs from message bodies.
3. Filter URLs to mapping/cartography/spatial data news; exclude small local initiatives.
4. Normalize + dedupe URLs; update `LIST.md` accordingly.
5. Trash processed Gmail messages.
6. Update prompt-hub tracking (memory, version, releases) and finalize this todo.

## Plan Check-in
Scheduled cron run — proceeding with execution.

## Checklist
- [x] Repo clean/synced
- [x] Gmail label scanned
- [x] URLs extracted + filtered (none found)
- [x] LIST.md updated + deduped (no changes)
- [x] Non-mapping/local URLs removed from LIST.md (none)
- [x] Emails trashed (none)
- [x] Prompt-hub logs/version/releases updated
- [x] Commit/push updates
- [x] Summary sent

## Review
- Result: Gmail label empty; LIST.md already empty.
- URLs added: 0
- URLs removed: 0
- Emails trashed: 0
- Notes: No mapping URLs found in label 0---veille-mapping.
