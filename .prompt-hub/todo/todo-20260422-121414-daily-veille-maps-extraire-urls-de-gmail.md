# Todo - Daily veille maps extraire urls de gmail

## Objective
Exécuter la séquence quotidienne Gmail -> LIST.md pour la veille mapping.

## Plan
- [ ] Vérifier/synchroniser l’état du repo pour repartir proprement.
- [ ] Lire les emails Gmail `label:0---veille-mapping` et extraire les URLs d’articles.
- [ ] Filtrer les URLs hors périmètre cartographie / donnée cartographique / actualités du domaine, en excluant les petites initiatives locales.
- [ ] Mettre à jour `LIST.md` avec déduplication et normalisation, puis vérifier les ajouts.
- [ ] Mettre à jour les fichiers `.prompt-hub` (memory, summary, version, releases).
- [ ] Commit + push toutes les modifications nécessaires.
- [ ] Mettre à la corbeille les emails traités.

## Notes
- Si le repo n’est pas clean, committer/pusher d’abord toutes les modifications locales non synchronisées pour retrouver un état propre avant la mise à jour de `LIST.md`.
- Vérifier et retirer de `LIST.md` les URLs désormais hors périmètre si besoin.

## Review
- Pending
