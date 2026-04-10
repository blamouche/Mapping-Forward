# Todo — daily veille maps extraire urls de gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Clarify task scope and constraints from `agents.md`
- [x] Restore clean synced repo state (commit/push any pending local changes if needed)
- [x] Search Gmail label `0---veille-mapping` and extract candidate article URLs
- [x] Normalize, filter, dedupe, and update `LIST.md`
- [x] Remove off-scope URLs from `LIST.md`
- [x] Trash processed Gmail messages
- [x] Update prompt-hub tracking files (`memory.md`, `releases.md`, `version.md`, run summary if used)
- [x] Commit and push resulting changes

## Plan
1. Check repo cleanliness and, if dirty, commit/push all local pending changes first to restore a clean baseline.
2. Query Gmail label `0---veille-mapping`, extract article URLs from returned messages, and keep only mapping/cartography/geospatial-industry items while excluding small local initiatives.
3. Update `LIST.md` as plain text with normalized deduped URLs, re-review existing entries for scope, then trash processed emails.
4. Update prompt-hub tracking, bump version, commit, and push.

## Review
- Repo started dirty only because of the newly created scheduled todo; final state recorded and committed/pushed; Gmail trash step corrected in a follow-up tracking commit.
- Gmail label returned 1 message. Extracted 1 URL from the Google Alert body, then filtered it out as a false positive unrelated to mapping/cartography.
- `LIST.md` stayed unchanged after scope review.
- Processed Gmail message was moved to Trash.
