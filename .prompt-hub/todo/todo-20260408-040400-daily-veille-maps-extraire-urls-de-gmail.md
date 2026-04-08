# Todo — daily-veille-maps-extraire-urls-de-gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Inspect Gmail label `0---veille-mapping`
- [x] Restore clean git state if needed
- [x] Extract candidate article URLs and filter to mapping/cartography domain
- [x] Update `LIST.md` with normalized/deduped URLs
- [x] Review `LIST.md` and remove off-scope/local-noise URLs
- [x] Trash processed Gmail emails
- [x] Update prompt-hub tracking (`memory`, `version`, `releases`)
- [x] Commit and push changes

## Plan
1. Sync the repo into a clean state, committing any pending local work if required.
2. Extract article URLs from Gmail alerts, keep only cartography/geospatial/mapping-domain items, then normalize/dedupe into `LIST.md`.
3. Re-review `LIST.md`, drop off-scope/local-noise items, trash processed emails, and push tracking updates.

## Review
- Repo cleanup done first via a dedicated baseline commit/push (`Add veille-mapping todo for scheduled run`).
- Processed 1 Gmail alert, extracted 10 candidate links, kept 5 mapping-domain URLs, filtered 5 off-scope/noise items (PUBG, comet/space, LA wildfire map consumer-news angle, Penn State local ArcGIS shortcuts, Big Think strange maps).
- `LIST.md` now contains 5 normalized URLs and no removals were needed after the final scope review.
- Trashed 1 processed Gmail alert.
