# Todo: veille mapping (daily Gmail -> LIST.md)

## Plan
- [ ] Sync repo and ensure clean status (if dirty, commit/push all pending changes first).
- [ ] Fetch Gmail messages with label `0---veille-mapping` and extract article URLs.
- [ ] Filter URLs to keep only mapping/cartography/spatial data news (exclude local small initiatives).
- [ ] Update `LIST.md` via add-url rules (dedupe, one per line), remove non-mapping URLs already in list.
- [ ] Commit/push changes (update version + releases).
- [ ] Trash processed Gmail messages.
- [ ] Log actions in `.prompt-hub/memory.md` and complete review.

## Notes
- Requires plan check-in before execution (per agents.md).
