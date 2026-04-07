# Todo — Daily veille Maps extraire urls de Gmail

- [x] Read .prompt-hub/lessons.md
- [x] Read .prompt-hub/memory.md
- [x] Read .prompt-hub/releases.md
- [x] Create this task file
- [x] Check repo status and restore clean synced state if needed
- [x] Search Gmail label `0---veille-mapping`
- [x] Extract and filter article URLs
- [x] Update `LIST.md` (normalize + dedupe + scope cleanup)
- [x] Trash processed Gmail emails
- [x] Update prompt-hub tracking (`memory.md`, `version.md`, `releases.md`)
- [x] Commit and push all required changes

## Notes
- Scheduled cron run at 2026-04-08 00:04 CEST.
- Kept URLs:
  - https://www.tomtom.com/newsroom/product-focus/why-accurate-speed-limits-are-crucial-for-drivers-and-automation/
  - https://www.itsinternational.com/news/tomtom-integrates-traffic-info-locus-platform
  - https://www.generation-nt.com/actualites/bing-maps-tomtom-orbis-microsoft-copilot-donnees-2073589
- Filtered candidates: 13 (astronomy/Youtube/local initiatives/reviews/finance/PR noise).

## Review
- Repo was already clean and synced.
- Gmail label returned 2 messages / 16 candidate URLs.
- Added 3 URLs to `LIST.md`; removed 0 existing URLs from `LIST.md` during scope cleanup.
- Trashed 2 processed Gmail messages.
- Prompt-hub tracking updated and ready for commit/push.
