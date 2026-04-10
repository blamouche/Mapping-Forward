# Todo — daily veille maps extraire urls de gmail

## Objective
Exécuter la séquence quotidienne Gmail -> LIST.md -> nettoyage scope -> corbeille Gmail.

## Plan
- [x] Vérifier état repo et repartir d'un état propre/synced si nécessaire
- [x] Lire les emails Gmail label:0---veille-mapping et extraire les URLs d'articles
- [x] Mettre à jour LIST.md via l'agent add-url (normalisation/déduplication)
- [x] Retirer de LIST.md les URLs hors scope cartographie / donnée cartographique / actualités du domaine, en excluant les petites initiatives locales
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour prompt-hub (memory/version/releases) puis commit+push

## Review
- Repo déjà propre; `git pull --rebase` non nécessaire avant traitement.
- Gmail `label:0---veille-mapping` vide (`gog gmail messages search --include-body --json --no-input`).
- `LIST.md` déjà vide; aucune URL ajoutée ni supprimée après revue du scope.
- Aucun email à mettre à la corbeille.
