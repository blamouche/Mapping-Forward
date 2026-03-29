# Todo: veille-mapping (daily Gmail -> LIST.md)

## Objective
Run daily veille mapping sequence: scan Gmail label 0---veille-mapping, extract/clean mapping URLs, update LIST.md with dedupe, remove non-mapping/local items, sync git clean state, commit/push, trash processed emails, report summary.

## Plan
1. Sync repo state: ensure clean; if not clean, commit/push all pending changes to restore clean baseline.
2. Scan Gmail label 0---veille-mapping (messages, include body), extract candidate URLs.
3. Filter to mapping/cartography/spatial-data related items (exclude local initiatives).
4. Normalize/dedupe URLs and update LIST.md accordingly.
5. Remove non-mapping URLs already in LIST.md if found.
6. Commit/push changes per add-url rules.
7. Trash processed Gmail messages.

## Plan check-in
Cron run: proceeding with plan per scheduled automation.

## Progress
- [x] Verify repo clean or commit/push pending changes
- [x] Fetch Gmail messages and extract URLs
- [x] Filter mapping-relevant URLs + normalize
- [x] Update LIST.md (add/dedupe/remove)
- [x] Commit/push updates
- [x] Trash processed Gmail messages
- [x] Log actions in prompt-hub memory
- [x] Update version/releases and finalize review

## Review
- [ ] Summary added in task file
- [ ] Actions logged in .prompt-hub/memory.md
- [ ] Version/release bumped and committed

## Summary
- Gmail label empty; no URLs added; LIST.md unchanged (1 URL retained).
- No emails trashed.
- Prompt-hub tracking updated (memory, version, releases).
