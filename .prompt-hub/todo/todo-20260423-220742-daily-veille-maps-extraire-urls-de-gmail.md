# Todo - daily-veille-maps-extraire-urls-de-gmail

## Objective
Exécuter la séquence quotidienne Gmail -> LIST.md -> nettoyage scope -> corbeille -> commit/push.

## Plan
- [x] Lire `.prompt-hub/lessons.md`
- [x] Lire `.prompt-hub/memory.md`
- [x] Lire `.prompt-hub/releases.md`
- [x] Vérifier l'état du repo et les consignes `agents.md`
- [ ] Restaurer un repo clean/synced (commit/push toutes les modifs locales non synchronisées si nécessaire)
- [ ] Récupérer les emails Gmail `label:0---veille-mapping`
- [ ] Extraire et normaliser les URLs candidates
- [ ] Filtrer les URLs hors scope cartographie/donnée cartographique/actu du domaine, exclure petites initiatives locales
- [ ] Mettre à jour `LIST.md` (one URL per line, dedupe, no blanks)
- [ ] Mettre à la corbeille les emails traités
- [ ] Mettre à jour `.prompt-hub` (memory, releases, version, summary)
- [ ] Commit + push

## Review
- Pending
