# Daily veille Maps - extraire URLs de Gmail

- [x] Lire `.prompt-hub/lessons.md`
- [x] Lire `.prompt-hub/memory.md`
- [x] Lire `.prompt-hub/releases.md`
- [x] Créer ce fichier de tâche avant exécution
- [x] Vérifier/synchroniser l'état Git du repo
- [x] Chercher les emails Gmail `label:0---veille-mapping`
- [x] Extraire et filtrer les URLs cartographie/GIS/donnée cartographique
- [x] Mettre à jour `LIST.md` (normalisation, déduplication, nettoyage)
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour `.prompt-hub` (memory, releases, version, summary)
- [x] Commit + push

## Review
- Repo remis à plat via un commit de baseline, puis `git pull --rebase` a confirmé que `main` était à jour.
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` a renvoyé 0 message.
- `LIST.md` était déjà vide, donc 0 URL ajoutée et 0 URL supprimée après revue de portée.
- Aucun email à mettre à la corbeille.
