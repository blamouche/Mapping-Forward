# Todo: veille-mapping (daily run)

## Plan
- [x] Check repo clean; if dirty, commit/push all local changes to reset clean state.
- [x] Pull latest changes.
- [x] Fetch Gmail label `0---veille-mapping` messages and extract article URLs.
- [x] Filter out non-mapping / local initiatives; dedupe and normalize URLs.
- [x] Update LIST.md (one URL per line, no blanks, dedupe).
- [x] Remove unrelated URLs already in LIST.md (non-cartography, local initiatives).
- [x] Commit/push LIST.md updates if any.
- [x] Trash processed Gmail messages.
- [x] Log actions in .prompt-hub/memory.md, update version/release, finalize todo review.

## Review
- Added URLs: 6
- Removed URLs: 0
- Trashed Gmail messages: 2

## Check-in
- User requested cron execution; proceeding per explicit instruction.
