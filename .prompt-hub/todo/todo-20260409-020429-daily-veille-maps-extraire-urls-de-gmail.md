# Todo — daily-veille-maps-extraire-urls-de-gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Inspect repo status and restore a clean synced state if needed
- [x] Search Gmail label `0---veille-mapping` and extract article URLs
- [x] Update `LIST.md` with normalized/deduped in-scope URLs only
- [x] Remove off-scope/local URLs from `LIST.md`
- [x] Trash processed emails
- [x] Update prompt-hub tracking (`memory.md`, `version.md`, `releases.md`, todo review)
- [x] Commit and push all required changes

## Notes
- User requested clean-state recovery before URL insertion if repo is dirty.
- Must follow `add-url` rules for `LIST.md` and repo sync/commit/push.

## Review
- Repo had one pending local tracking file at start; committed/pushed a baseline first to restore a clean state.
- Gmail label `0---veille-mapping` returned 2 Google Alerts messages.
- Extracted 9 new in-scope URLs from the alerts and kept the 1 pre-existing in-scope TomTom URL already in `LIST.md`.
- Filtered out off-scope/local/noise links (video mapping festival local event, gaming/maps noise, Instagram/YouTube/airport map pages, ad-tech/local discovery noise).
- Trashed 2 processed Gmail messages.
- Final `LIST.md` count: 10 URLs.
