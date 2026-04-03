# Todo — veille-mapping (2026-04-03 09:56 CET)

## Plan
- [x] Sync repo (clean check + pull --rebase)
- [x] Scanner Gmail label `0---veille-mapping`, extraire les URLs carto/GIS
- [x] Ajouter URLs dans LIST.md (dedupe, commit+push)
- [x] Supprimer URLs non-carto de LIST.md (filtrage à la source)
- [x] Mettre à la corbeille les emails traités
- [x] Update memory + version/release, commit+push

## Execution Notes
- Running as cron job 2026-04-03 10:06 CET
- 17 emails processed
- 42 URLs added (cartography, GIS, Google Maps AI/EV, TomTom/Bing Maps data, mapping tools)
- Filtered out: local events (video mapping festivals), stock market news, social media, YouTube, off-topic articles

## Review
- All emails trashed
- LIST.md: 43 URLs total (1 pre-existing + 42 new)
- Repo clean, committed, pushed at v0.1.126
