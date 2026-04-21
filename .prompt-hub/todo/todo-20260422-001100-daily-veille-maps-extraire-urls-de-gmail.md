# Todo - daily veille maps extraire urls de gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Check repo status and agent rules
- [x] Restore a clean synced repo state before Gmail extraction
- [x] Query Gmail label `0---veille-mapping`
- [x] Extract article URLs and filter to cartography/domain scope
- [x] Update `LIST.md` with normalization and de-duplication
- [x] Remove out-of-scope URLs already present in `LIST.md`
- [x] Trash processed emails
- [x] Update prompt-hub tracking, review, version, and releases

## Notes
- Scheduled run requested on 2026-04-22 00:11 CEST.
- If the repo is not clean, commit/push all local unsynced changes first, then continue.
- Kept 5 URLs after filtering out YouTube links, political redistricting pieces, false-positive "map" items, Tom Tom Festival local items, generic market-forecast promo coverage, and duplicate-topic PR coverage.

## Review
- Repo was first restored to a clean synced state via a baseline tracking commit.
- Gmail query returned 2 Google Alerts and 21 candidate URLs.
- Added 5 in-scope URLs to `LIST.md`.
- Removed 0 URLs from the existing queue because `LIST.md` was empty and already in scope.
- Trashed 2 processed emails.
