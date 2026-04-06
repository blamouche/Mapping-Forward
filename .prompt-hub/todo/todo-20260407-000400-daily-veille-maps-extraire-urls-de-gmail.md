# Todo - daily-veille-maps-extraire-urls-de-gmail

## Objective
Exécuter la séquence quotidienne: Gmail label `0---veille-mapping` -> extraction d'URLs -> mise à jour/nettoyage de `LIST.md` -> corbeille des emails -> commit/push.

## Checklist
- [x] Lire `.prompt-hub/lessons.md`
- [x] Lire `.prompt-hub/memory.md`
- [x] Lire `.prompt-hub/releases.md`
- [x] Vérifier la version courante
- [x] Vérifier l'état du repo et `LIST.md`
- [x] Inspecter les emails Gmail label `0---veille-mapping`
- [x] Extraire/filtrer les URLs cartographie
- [ ] Assurer un repo propre (commit/push toute modif locale si nécessaire)
- [x] Mettre à jour `LIST.md` (normalisation, déduplication, suppression hors-scope)
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour `.prompt-hub/memory.md`
- [x] Incrémenter `.prompt-hub/version.md` et `.prompt-hub/releases.md`
- [x] Commit + push

## Notes
- Exécution automatique par cron.

## Review
- 1 email Gmail traité.
- 2 URLs conservées et ajoutées à `LIST.md`.
- 3 URLs filtrées (promo/finance hors périmètre).
- 1 email Gmail traité puis mis à la corbeille.
