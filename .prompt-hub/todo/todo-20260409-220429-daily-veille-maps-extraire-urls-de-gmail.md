# Todo — daily-veille-maps-extraire-urls-de-gmail

## Objective
Exécuter la séquence quotidienne : scanner Gmail label `0---veille-mapping`, extraire les URLs d’articles, mettre à jour `LIST.md` selon les règles `add-url`, supprimer les URLs hors périmètre cartographie/GIS, mettre à la corbeille les emails traités, puis commit/push un état propre.

## Plan
- [x] Vérifier l’état git et nettoyer/synchroniser le repo si nécessaire.
- [x] Scanner Gmail label `0---veille-mapping` et extraire les URLs candidates.
- [x] Filtrer les URLs au périmètre cartographie/GIS/actualités cartographiques (hors petites initiatives locales).
- [x] Mettre à jour `LIST.md` avec normalisation, déduplication et vérification.
- [x] Mettre à la corbeille les emails traités.
- [x] Mettre à jour le suivi `.prompt-hub`, commit, push, puis documenter le résultat.

## Review
- Repo initialement non clean à cause du nouveau fichier todo `.prompt-hub`; baseline commit/push effectué pour repartir d’un état propre.
- `gog gmail messages search 'label:0---veille-mapping' --max 20 --include-body --json` a retourné 0 message.
- `LIST.md` était vide et le reste après revue de périmètre; aucune URL ajoutée, aucune URL supprimée.
- Aucun email traité à mettre à la corbeille.
