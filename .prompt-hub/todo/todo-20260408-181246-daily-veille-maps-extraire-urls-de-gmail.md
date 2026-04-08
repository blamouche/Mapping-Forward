# Todo — daily veille maps extraire urls de gmail

- [x] Read .prompt-hub/lessons.md
- [x] Read .prompt-hub/memory.md
- [x] Read .prompt-hub/releases.md
- [x] Restore clean git state (commit/push any pending local changes if needed)
- [x] Search Gmail label `0---veille-mapping`
- [x] Extract article URLs and filter to mapping/cartography domain
- [x] Update `LIST.md` (normalize, dedupe, remove off-scope URLs)
- [x] Trash processed emails
- [x] Update prompt-hub tracking files, commit, and push

## Plan
1. Create and keep this task log updated.
2. If the repo is dirty, commit/push all pending local changes first to restore a clean baseline.
3. Fetch Gmail messages for label `0---veille-mapping`, extract candidate URLs, keep only mapping/cartography/data/map-industry news, and exclude small local initiatives.
4. Update `LIST.md` per add-url rules (clean sync, normalize, dedupe) and remove any off-scope URLs already present.
5. Trash processed Gmail messages, then update memory/version/releases and push the final state.

## Review
- Baseline sync required because the repo was dirty at start (.prompt-hub/memory.md pending).
- Gmail label `0---veille-mapping` returned no messages.
- `LIST.md` stayed unchanged after scope review.
- No emails were trashed.
