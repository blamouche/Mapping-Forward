# Todo - daily-veille-maps-extraire-urls-de-gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Check repo state
- [x] Sync repo (`git pull --rebase`)
- [x] Search Gmail label `0---veille-mapping`
- [x] Extract and filter article URLs for mapping/cartography scope
- [x] Update `LIST.md` with normalized deduped URLs
- [x] Remove out-of-scope URLs already present in `LIST.md`
- [x] Trash processed emails
- [x] Update prompt-hub tracking files
- [ ] Commit and push

## Review

- Status: completed pending commit/push
- Notes:
  - Scheduled cron run at 2026-04-20 04:04 CEST.
  - `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` returned 0 messages.
  - `LIST.md` was empty after scope review.
  - URLs added: 0.
  - URLs removed: 0.
  - Emails trashed: 0.
