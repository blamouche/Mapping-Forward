# Daily veille Maps - extraire URLs de Gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Inspect repo status and current `LIST.md`
- [x] Restore a clean synced repo state if needed
- [x] Query Gmail label `0---veille-mapping`
- [x] Extract candidate article URLs
- [x] Keep only mapping/cartography/domain-news URLs, excluding small local initiatives
- [x] Update `LIST.md` with normalized deduped URLs
- [x] Trash processed emails
- [x] Update prompt-hub tracking, commit, and push

## Notes
- Cron run requested 2026-04-30 06:09 Europe/Paris.
- Gmail query returned zero messages, so there were no URLs to extract or emails to trash.

## Review
- Repo was clean/synced after the baseline tracking commit.
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` returned no messages.
- `LIST.md` remained empty and required no scope cleanup.
- URLs added: 0.
- URLs removed: 0.
- Emails trashed: 0.
