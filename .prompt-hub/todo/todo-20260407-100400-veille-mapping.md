# Todo — veille-mapping (2026-04-07 10:04 Europe/Paris)

## Objective
Run the daily sequence: Gmail label `0---veille-mapping` -> extract article URLs -> sync/clean repo -> update and filter `LIST.md` -> trash processed emails -> report counts.

## Plan
- [x] Check and restore a clean git state (commit/push any pending local changes if needed).
- [x] Query Gmail messages for label `0---veille-mapping` and extract article URLs.
- [x] Normalize, de-duplicate, and append kept URLs to `LIST.md`.
- [x] Review `LIST.md` and remove off-scope / small local initiative URLs.
- [x] Trash processed Gmail messages.
- [x] Update prompt-hub tracking (`memory`, `version`, `releases`) and commit/push final state.

## Review
- `git pull --rebase` confirmed the repo was already up to date.
- Gmail label `0---veille-mapping` returned 0 messages, so 0 candidate URLs were extracted.
- `LIST.md` was already empty; 0 URLs were added and 0 were removed during scope review.
- No Gmail messages were moved to Trash.
- Tracking files were updated for the empty run and prepared for commit/push.
