# Daily veille maps extraire URLs de Gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Verify repo sync/cleanliness and restore a clean baseline if needed
- [x] Query Gmail label `0---veille-mapping` and extract candidate article URLs
- [x] Update `LIST.md` with dedupe + mapping-scope filtering
- [x] Trash processed Gmail messages
- [x] Update prompt-hub tracking, version, releases, and review

## Notes
- Triggered by cron at 2026-04-24 18:09:00 Europe/Paris.
- Need to commit/push all local unsynced changes first if the repo is not clean, then proceed with the add-url flow from a clean baseline.

## Review
- Repo was already clean/synced before this run.
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` returned no messages.
- `LIST.md` was already empty and stayed empty after scope review.
- URLs added: 0.
- URLs removed: 0.
- Emails trashed: 0.
- Prompt-hub tracking files updated for commit/push.
