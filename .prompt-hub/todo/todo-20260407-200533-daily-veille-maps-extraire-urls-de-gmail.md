# Todo — daily veille maps extraire urls de gmail

## Objective
Exécuter la séquence quotidienne Gmail -> LIST.md -> nettoyage scope -> corbeille pour le repo Mapping-Forward.

## Plan
- [ ] Lire les emails Gmail label `0---veille-mapping`
- [ ] Extraire et filtrer les URLs liées à la cartographie/GIS/donnée cartographique
- [ ] Restaurer un repo propre si nécessaire, puis mettre à jour `LIST.md` (normalisation + déduplication)
- [ ] Supprimer de `LIST.md` les URLs hors scope ou trop locales
- [ ] Commit/push les changements requis
- [ ] Mettre à la corbeille les emails traités
- [ ] Journaliser le run dans `.prompt-hub/*`

## Notes
- Si le repo n'est pas clean, commit/push toutes les modifications locales non synchronisées avant traitement pour repartir proprement.
- Résultat attendu: résumé du run + nombre d'URLs ajoutées/supprimées.

## Review
- Pending
