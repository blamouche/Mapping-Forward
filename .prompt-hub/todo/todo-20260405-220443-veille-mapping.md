# Todo - veille-mapping - 2026-04-05 22:04:43

## Plan
- [x] Inspect Gmail label `0---veille-mapping` and extract article URLs from current messages.
- [x] Sync repo to a clean state; if local unsynced changes exist, commit/push them all first.
- [x] Update `LIST.md`: normalize/dedupe, add kept URLs, remove non-mapping/local URLs.
- [x] Trash processed Gmail messages.
- [x] Update prompt-hub tracking (`memory`, `releases`, `version`, todo review) and push.

## Notes
- Cron run requested full daily sequence without extra confirmation.
- Kept URLs (5): TomTom GO Navigation article, Nature GIS/spatial modelling paper, Matchy Maps hiking app article, Google Maps EV charging IA article, GIM International mobile mapping case study.
- Filtered out local event/news items, finance tickers, YouTube shorts, generic wildfire/local incident maps, astronomy/medical/biomedical false positives, and other non-cartography noise.

## Review
- Repo was initially dirty because this run created a new todo file; committed/pushed tracking baseline first to restore a clean state before `git pull --rebase`.
- `LIST.md` updated with 5 added URLs and 0 removed URLs.
- 8 Gmail messages moved to Trash.
