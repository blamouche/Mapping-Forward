# Todo - daily-veille-maps-extraire-urls-de-gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Check repo status
- [x] Sync repo with `git pull --rebase`
- [x] Query Gmail label `0---veille-mapping`
- [x] Extract and filter article URLs
- [x] Review and update `LIST.md`
- [x] Trash processed emails
- [x] Update veille run tracking files
- [x] Commit and push changes

## Review

- `gog gmail messages search '''label:0---veille-mapping''' --include-body --json --max 100 --no-input` returned no current messages.
- Fallback `in:anywhere label:0---veille-mapping` only surfaced already trashed historical alerts.
- `LIST.md` was empty and stayed unchanged after scope review.
- Added URLs: 0
- Removed URLs: 0
- Trashed emails: 0
