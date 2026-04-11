# Daily veille Maps - extraire URLs de Gmail

## Objective
Exécuter la séquence quotidienne Gmail -> LIST.md -> tri -> corbeille en respectant `agents.md`.

## Plan
- [x] Vérifier/synchroniser l'état git propre du repo.
- [x] Lire les emails Gmail `label:0---veille-mapping` et extraire les URLs candidates.
- [x] Filtrer les URLs hors périmètre cartographie/GIS/maps et petites initiatives locales.
- [x] Mettre à jour `LIST.md` avec déduplication, puis vérifier.
- [x] Mettre à jour tracking prompt-hub (memory/version/releases) et commit/push.
- [x] Mettre à la corbeille les emails traités.

## Review
- Gmail label returned 0 message; no new URLs were added.
- Scope review removed 3 out-of-scope URLs from `LIST.md` and kept 2 in-scope URLs.
- No Gmail trash action was needed because nothing was processed from Gmail.
