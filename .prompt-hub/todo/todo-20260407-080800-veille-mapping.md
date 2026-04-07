# Todo — veille-mapping — 2026-04-07 08:08:00 CEST

## Objective
Exécuter la routine quotidienne: Gmail label `0---veille-mapping` → extraction d’URLs → mise à jour de `LIST.md` → filtrage scope cartographie → corbeille Gmail → commit/push.

## Plan
- [x] Lire `agents.md`, `.prompt-hub/lessons.md`, `.prompt-hub/memory.md`, `.prompt-hub/releases.md`
- [x] Créer ce fichier todo
- [x] Vérifier l’état git et restaurer un état propre si nécessaire
- [x] Chercher les emails Gmail label:0---veille-mapping
- [x] Extraire et filtrer les URLs d’articles
- [x] Mettre à jour `LIST.md` (normalisation, déduplication, retrait off-scope)
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour `.prompt-hub` (memory/version/releases/todo)
- [x] Commit + push

## Notes
- Critère scope: cartographie, GIS, geospatial, spatial data, navigation maps, imagery/cartographic infrastructure, actualités du domaine cartographique.
- Exclure les petites initiatives locales et les liens promo/finance/bruit.

## Review
- Gmail `label:0---veille-mapping`: 0 email trouvé.
- `LIST.md`: inchangée, 0 URL ajoutée, 0 URL supprimée.
- Aucun email à mettre à la corbeille.
- Repo déjà propre; aucun contenu métier à synchroniser hors fichiers de tracking `.prompt-hub`.
