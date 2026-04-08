# Todo — daily veille maps extraire urls de gmail

## Objective
Exécuter la séquence quotidienne : Gmail label `0---veille-mapping` → extraire les URLs d’articles → mettre à jour `LIST.md` selon le scope cartographie/GIS/mapping → mettre à la corbeille les emails traités → repo clean/synced avec commit+push.

## Plan
- [x] Vérifier/synchroniser l’état du repo (et pousser toute modif locale non synchronisée si besoin).
- [x] Chercher les emails Gmail label `0---veille-mapping`.
- [x] Extraire et filtrer les URLs d’articles pertinentes.
- [x] Mettre à jour `LIST.md` (normalisation, déduplication, suppression des URLs hors scope).
- [x] Mettre à jour tracking `.prompt-hub` (memory/version/releases/todo).
- [x] Commit + push.
- [x] Mettre à la corbeille les emails traités.

## Notes
- Scope retenu : cartographie, donnée cartographique, GIS, géospatial, navigation/maps platforms, actualités mapping sectorielles.
- Exclure les petites initiatives locales et le bruit non cartographique.
- Gmail a retourné 0 message pour le label `0---veille-mapping`; aucune URL candidate à évaluer.
- `LIST.md` était déjà vide, donc aucune normalisation/suppression supplémentaire nécessaire.

## Review
- Repo initialement sale uniquement à cause du todo courant; tracking mis à jour puis commit/push pour restaurer un état propre.
- Gmail label `0---veille-mapping`: 0 email traité.
- URLs ajoutées à `LIST.md`: 0.
- URLs supprimées de `LIST.md`: 0.
- Emails mis à la corbeille: 0.
