# Todo — daily-veille-maps-extraire-urls-de-gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Create this task file before execution
- [x] Check repo status and sync (`git pull --rebase`)
- [x] Search Gmail label `0---veille-mapping`
- [x] Extract article URLs from matching emails
- [x] Update `LIST.md` with dedupe/scope review
- [x] Trash processed emails
- [x] Update prompt-hub tracking files

## Plan
1. Confirm repo state, and if dirty commit/push all pending local changes first to restore a clean baseline.
2. Search Gmail label `0---veille-mapping`, extract article URLs from matched messages, and filter to mapping/cartography/geospatial-domain news while excluding small local initiatives.
3. Update `LIST.md` with normalized deduped URLs, then trash processed emails.
4. Update prompt-hub memory/release/version/todo files, commit, and push.

## Review
- Repo was already clean and synced (`git pull --rebase` → already up to date).
- Gmail search for `label:0---veille-mapping` returned no messages, including with `--include-body`.
- No article URLs were extracted.
- `LIST.md` was already empty and remained unchanged after scope review.
- No Gmail emails were trashed because none matched the label.
- Tracking files were updated for this empty run.
