# Todo — Daily veille maps extraire urls de gmail

- [x] Read repo rules: `.prompt-hub/lessons.md`, `.prompt-hub/memory.md`, `.prompt-hub/releases.md`
- [x] Check repo cleanliness and sync baseline
- [x] Search Gmail label `0---veille-mapping`
- [x] Extract article URLs and filter to mapping-domain relevance
- [x] Update `LIST.md` with clean deduped URLs
- [x] Remove off-scope/local URLs from `LIST.md`
- [x] Trash processed emails
- [x] Update prompt-hub logs/version/release notes
- [x] Commit and push all required changes

## Plan
1. Ensure repo is clean or commit/push pending local changes first, then sync with origin.
2. Read Gmail messages under the veille label, extract candidate article URLs, and keep only mapping/cartography/geospatial/domain-news links (exclude small local initiatives).
3. Apply add-url rules to `LIST.md`, then do a final scope cleanup over the whole list.
4. Trash processed emails, update prompt-hub tracking files, commit, and push.

## Review
- Repo was already clean and `git pull --rebase` reported up to date.
- Gmail label `0---veille-mapping` returned no messages, so no article URLs were extracted.
- `LIST.md` was already empty, so 0 URLs were added and 0 removed during the scope cleanup.
- No emails were trashed because nothing was processed.
