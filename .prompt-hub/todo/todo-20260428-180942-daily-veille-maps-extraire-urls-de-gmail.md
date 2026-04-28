# Todo - Daily veille maps extraire urls de gmail

- [x] Vérifier l'état du repo et restaurer un état propre/synchronisé si nécessaire
- [x] Chercher les emails Gmail label:0---veille-mapping
- [x] Extraire les URLs candidates
- [x] Filtrer les URLs hors périmètre cartographie / donnée cartographique / actualités du domaine, exclure petites initiatives locales
- [x] Mettre à jour LIST.md (normalisation, déduplication, une URL par ligne)
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour le tracking prompt-hub (memory, releases, version, summary)
- [x] Commit + push toutes les modifications

## Notes
- Cron: daily veille Maps Extraire urls de gmail
- Timestamp: 2026-04-28 18:09:42 Europe/Paris

## Review
- Repo nettoyé via commit/push de baseline, puis `git pull --rebase` confirmé à jour.
- `gog gmail messages search` sur `label:0---veille-mapping` n'a retourné aucun email.
- `LIST.md` est resté vide après revue de périmètre.
- Aucun email à mettre à la corbeille.
