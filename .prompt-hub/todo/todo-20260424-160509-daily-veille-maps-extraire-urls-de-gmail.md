# Todo — daily veille maps extraire urls de gmail

## Context
- Timestamp: 2026-04-24 16:05:09 CEST
- Trigger: scheduled daily veille mapping run
- Goal: inspect Gmail label `0---veille-mapping`, extract in-scope mapping/cartography URLs, sync `LIST.md`, filter out-of-scope links, trash processed emails, and keep prompt-hub tracking up to date.

## Plan
- [x] Read required prompt-hub context (`lessons.md`, `memory.md`, `releases.md`).
- [x] Check repo state and restore a clean synced baseline if needed.
- [x] Query Gmail label `0---veille-mapping` for messages to process.
- [x] Review/update `LIST.md` with only in-scope URLs.
- [x] Update prompt-hub tracking files for this run.
- [x] Commit and push tracking updates.

## Notes
- `gog gmail messages search 'label:0---veille-mapping' --max 100 --json --no-input` returned no messages.
- `git status --porcelain` was empty and `git pull --rebase` was already up to date.
- `LIST.md` was already empty, so no URLs were added or removed.
- No emails needed trashing.

## Review
- Gmail label `0---veille-mapping` had no messages.
- `LIST.md` stayed empty after scope review.
- URLs added: 0.
- URLs removed: 0.
- Emails trashed: 0.
- Tracking files updated for commit/push.