# Todo — daily veille maps extraire urls de gmail

## Objective
Exécuter la veille quotidienne Gmail -> LIST.md en respectant `agents.md` (agent `add-url`) et remettre le repo dans un état propre/synchronisé.

## Plan
- [x] Vérifier l’état git et remettre le repo dans un état clean/synced (commit+push tout le local en attente si nécessaire).
- [x] Chercher les emails Gmail label `0---veille-mapping` et extraire les URLs candidates.
- [x] Filtrer les URLs pour ne garder que les sujets cartographie / données cartographiques / actualités du domaine (hors petites initiatives locales).
- [x] Mettre à jour `LIST.md` (normalisation, déduplication, suppression des hors-scope), puis commit+push si changement.
- [x] Mettre à la corbeille les emails traités.
- [x] Mettre à jour prompt-hub (`memory.md`, `version.md`, `releases.md`, review du todo) et pousser l’état final.

## Review
- `git pull --rebase` : repo déjà à jour.
- Gmail label `0---veille-mapping` : 0 message trouvé sur ce run, donc 0 nouvelle URL extraite.
- `LIST.md` revu manuellement : suppression de `https://chipfm.com/en/new-flood-zone-mapping-in-quebec` car article local / assurance habitation Québec, hors périmètre veille cartographie domaine.
- 4 URLs conservées dans `LIST.md` après déduplication / revue de scope.
- Aucun email à mettre à la corbeille sur ce run.
