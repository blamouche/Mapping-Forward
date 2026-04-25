# Todo - Daily veille maps extraire urls de gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Clarify scope from cron instructions
- [x] Check repo status and restore clean synced baseline if needed
- [x] Query Gmail label `0---veille-mapping`
- [x] Extract candidate article URLs
- [x] Filter to mapping/cartography/domain-news URLs only
- [x] Review existing `LIST.md` and remove out-of-scope URLs
- [x] Update `LIST.md` with normalized deduped URLs
- [x] Update prompt-hub tracking (`memory.md`, `releases.md`, `version.md`, summary)
- [x] Commit and push all required changes
- [x] Move processed emails to Trash
- [x] Add review notes

## Notes
- Follow agent `add-url` rules: clean sync, normalize/dedupe, verify before commit.
- If repo is dirty, commit/push all unsynced local changes first to restore a clean base.
- Exclude small local initiatives and off-topic false positives.

## Review
- Repo was already clean and synced after the baseline tracking commit.
- Gmail label `0---veille-mapping` returned no messages.
- Reviewed the 5 existing `LIST.md` URLs and kept them all in scope.
- Added 0 URLs, removed 0 URLs, trashed 0 emails.
