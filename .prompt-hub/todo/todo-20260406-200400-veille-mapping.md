# Todo — veille-mapping — 2026-04-06 20:04 CEST

## Objective
Exécuter la séquence quotidienne Gmail -> LIST.md pour la veille cartographie.

## Plan
- [x] Vérifier les règles prompt-hub et créer la trace de tâche.
- [x] Inspecter l'état git et remettre le repo dans un état propre/synchronisé si nécessaire.
- [x] Lire les emails Gmail label:0---veille-mapping et extraire les URLs d'articles.
- [x] Filtrer les URLs hors périmètre cartographie/GIS/donnée cartographique/actualité du domaine (hors petites initiatives locales).
- [x] Mettre à jour LIST.md avec normalisation + déduplication, puis commit/push selon les règles add-url.
- [x] Mettre à la corbeille les emails traités.
- [x] Mettre à jour la trace prompt-hub (todo, memory, version, releases).

## Notes
- Run cron déclenché automatiquement.
- Si le repo est sale, pousser toutes les modifications locales non synchronisées avant d'ajouter de nouvelles URLs.

## Review
- Run completed successfully. 1 email processed; 4 URLs added; 0 URLs removed; 1 email trashed.
