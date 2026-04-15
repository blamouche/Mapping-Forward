# Todo 20260415-020440 daily veille maps extraire urls de gmail

- [x] Lire les consignes projet (.prompt-hub, agents.md)
- [x] Récupérer les emails Gmail label:0---veille-mapping et extraire les URLs
- [x] Nettoyer/synchroniser le repo et ajouter les URLs pertinentes dans LIST.md
- [x] Supprimer de LIST.md les URLs hors périmètre cartographie
- [x] Mettre à la corbeille les emails traités
- [x] Vérifier, commit, push, puis rédiger le résumé

## Review

- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` a retourné 0 message.
- `LIST.md` contenait déjà 7 URLs de veille et aucune suppression supplémentaire n'était nécessaire après revue de périmètre.
- Aucun email à mettre à la corbeille.
- Fichiers de suivi `.prompt-hub` mis à jour pour consigner ce run vide.
