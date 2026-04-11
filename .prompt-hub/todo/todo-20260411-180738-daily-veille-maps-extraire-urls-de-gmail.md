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
- Repo already clean and synced (`git pull --rebase` up to date).
- Gmail label returned 0 messages; no candidate URL was extracted.
- `LIST.md` was empty and unchanged after scope review.
- No Gmail trash action was needed because nothing was processed from Gmail.
