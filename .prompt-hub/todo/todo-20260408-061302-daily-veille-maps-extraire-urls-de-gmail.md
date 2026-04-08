# Todo — daily-veille-maps-extraire-urls-de-gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Inspect repo state and restore a clean synced baseline if needed
- [x] Search Gmail label `0---veille-mapping` and extract article URLs
- [x] Update `LIST.md` with normalized/deduped in-scope URLs; remove off-scope/local items
- [x] Trash processed Gmail emails
- [x] Update prompt-hub tracking (`memory`, `version`, `releases`) and review
- [x] Commit and push all resulting changes

## Plan
1. Check git status; if dirty, commit/push all pending local changes first so `/add-url` rules start from a clean synced state.
2. Read Gmail messages in label `0---veille-mapping`, extract candidate URLs, and keep only cartography / geospatial / mapping-domain news (excluding small local initiatives).
3. Rewrite `LIST.md` as a clean one-URL-per-line deduped list, then trash processed emails.
4. Update prompt-hub tracking, bump version/release, commit, and push.

## Review
- Repo state inspected: only the new scheduled todo was pending; `LIST.md` was already empty.
- Gmail search on `label:0---veille-mapping` returned no messages, so no URLs were extracted and no emails were trashed.
- `LIST.md` stayed empty after scope review.
- Prompt-hub tracking updated for this empty run; changes committed and pushed.
