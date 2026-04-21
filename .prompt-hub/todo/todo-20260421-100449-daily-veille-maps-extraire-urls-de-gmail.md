# Daily veille Maps - 2026-04-21 10:04:49 CEST

## Objective
Exécuter la séquence quotidienne Gmail -> LIST.md -> nettoyage scope -> corbeille.

## Checklist
- [x] Vérifier le contexte prompt-hub et l'état git
- [x] Si le repo n'est pas clean, commit/push toutes les modifs locales pour repartir proprement
- [x] Lire Gmail label:0---veille-mapping
- [x] Extraire et filtrer les URLs cartographie / donnée cartographique / actualités du domaine
- [x] Mettre à jour LIST.md (normalisation + déduplication + nettoyage hors scope)
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour mémoire / version / releases
- [ ] Commit et push

## Notes
- Exclure les petites initiatives locales et les faux positifs “map/maps/mapping”.
- Respecter l'agent add-url: sync propre, déduplication, vérification, commit+push.

## Review
- Gmail label `0---veille-mapping` vide, donc aucune URL candidate extraite.
- `LIST.md` vérifié vide, donc aucune URL ajoutée ni supprimée lors du nettoyage de scope.
- Aucun email à mettre à la corbeille.
- Tracking prompt-hub mis à jour, commit/push restant à faire.
