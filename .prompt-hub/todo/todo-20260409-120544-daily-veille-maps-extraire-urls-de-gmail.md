# Daily veille maps extraire URLs de Gmail

## Plan
- [x] Read repo rules: lessons, memory, releases.
- [x] Check repo status and current LIST.md.
- [x] Fetch Gmail messages for label `0---veille-mapping` and extract article URLs.
- [x] Filter to mapping/cartography/cartographic-data domain only; exclude local small initiatives.
- [x] Sync clean repo state; if needed commit/push all pending local changes before LIST.md update.
- [x] Update LIST.md with normalized deduped URLs and remove off-scope URLs already present.
- [x] Trash processed Gmail messages.
- [x] Update prompt-hub tracking (memory, releases, version, todo), commit, and push.

## Notes
- Trigger: cron e86a7434-db99-44fe-8c2c-6c13463de00f
- Current time: 2026-04-09 12:05 UTC / 14:05 Europe/Paris

## Review
- Gmail messages processed: 1
- URLs kept/added: 2
- URLs removed from existing LIST.md as off-scope: 0
- URLs excluded from alert as off-scope/local/noise: 3
- Processed email moved to Trash: yes
