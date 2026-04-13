# Todo — Daily veille Maps extraire URLs de Gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Check repo state and restore a clean synced baseline if needed
- [x] Search Gmail label `0---veille-mapping` and extract candidate article URLs
- [x] Filter to cartography / mapping / geospatial domain URLs and remove off-scope or small local items from `LIST.md`
- [x] Update `LIST.md` with deduped normalized URLs
- [x] Trash processed Gmail messages
- [x] Update prompt-hub tracking files (`memory`, `releases`, `version`, review)
- [x] Commit and push all required changes

## Review
- Repo was already clean/synced (`git pull --rebase` up to date).
- Gmail label `0---veille-mapping` returned 3 alerts.
- 25 candidate URLs extracted from alert bodies.
- 12 URLs kept after de-duplication and scope filtering; 0 existing URLs removed from `LIST.md`.
- 3 processed Gmail alerts moved to Trash.
- Changes are ready to be committed and pushed as `Add URL(s) to processing queue`.
