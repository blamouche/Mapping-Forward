# Todo — daily veille maps extraire urls de gmail

- [x] Read `.prompt-hub/lessons.md`, `.prompt-hub/memory.md`, and `.prompt-hub/releases.md`.
- [x] Check repo cleanliness/sync state and restore a clean baseline if needed.
- [x] Search Gmail label `0---veille-mapping`, extract candidate URLs, and review scope.
- [x] Update `LIST.md` with in-scope URLs only (normalized, deduped).
- [x] Trash processed emails.
- [x] Update prompt-hub tracking (`memory.md`, `releases.md`, `version.md`, summary json, review).
- [ ] Commit and push all resulting changes.

## Notes
- Scheduled run requested: Gmail → URL extraction → clean `LIST.md` update → trash emails.
- Exclude items outside cartography / mapping / spatial data domain, especially small local initiatives.

## Review
- `git pull --rebase --autostash origin main` confirmed the repo was already clean/synced.
- `gog gmail messages search 'label:"0 - Veille/Mapping"' --include-body --json --max 100 --no-input` returned 0 messages.
- `LIST.md` stayed unchanged and empty after scope review; 0 URLs added, 0 removed.
- No processed emails to move to Trash.
- Prompt-hub tracking updated for this empty scheduled run.
