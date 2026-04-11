# Todo — daily veille maps extraire urls de gmail

## Contexte
- Horodatage: 2026-04-11 04:04 Europe/Paris
- Source: cron `Daily veille Maps Extraire urls de gmail`
- Objectif: scanner Gmail label `0---veille-mapping`, extraire les URLs d'articles, mettre à jour `LIST.md` selon les règles `add-url`, retirer les URLs hors périmètre cartographie/cartographic data/domain news (hors petites initiatives locales), puis mettre à la corbeille les emails traités.

## Plan
- [x] Vérifier l’état Git et rétablir un repo propre/synchronisé si nécessaire.
- [x] Chercher les emails Gmail label `0---veille-mapping`.
- [x] Extraire et normaliser les URLs candidates.
- [x] Filtrer les URLs hors périmètre cartographie / donnée cartographique / actualités du domaine cartographique (exclure petites initiatives locales).
- [x] Mettre à jour `LIST.md` en respectant dedupe + ordre stable.
- [x] Mettre à jour les fichiers de suivi `.prompt-hub`.
- [x] Commit + push toutes les modifications nécessaires.
- [x] Mettre à la corbeille les emails Gmail traités.

## Review
- Gmail: 0 email trouvé dans `label:0---veille-mapping`.
- URLs candidates extraites: 0.
- URLs ajoutées à `LIST.md`: 0.
- URLs supprimées de `LIST.md`: 0.
- Emails mis à la corbeille: 0.
- `LIST.md` vérifié vide en shell (`wc -l = 0`) et laissé inchangé.
- Repo déjà propre/synchronisé avant commit final.
