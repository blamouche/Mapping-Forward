# Todo — daily veille maps extraire urls de gmail

- [x] Read lessons, memory, releases
- [x] Create this todo file
- [x] Restore clean synced repo state if needed
- [x] Read Gmail label `0---veille-mapping` and extract candidate article URLs
- [x] Filter URLs to mapping/cartography/geospatial-domain items and remove off-scope/local items from `LIST.md`
- [x] Update `LIST.md` with normalized deduped URLs
- [x] Trash processed emails
- [x] Update prompt-hub tracking (`memory.md`, `releases.md`, `version.md`)
- [x] Commit and push all resulting changes

## Plan
1. Ensure the repo is clean/synced before applying add-url rules.
2. Pull Gmail messages for `label:0---veille-mapping`, extract canonical article URLs, and filter for mapping/cartography relevance.
3. Normalize/dedupe `LIST.md`, remove off-scope/local URLs, then commit/push and trash processed emails.

## Review
- Gmail label `0---veille-mapping` returned no messages.
- `LIST.md` was already empty and remained unchanged after scope review.
- No URLs were added or removed.
- No emails were trashed.
