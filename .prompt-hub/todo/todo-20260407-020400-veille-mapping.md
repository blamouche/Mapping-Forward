# Todo — veille-mapping (2026-04-07 02:04 CEST)

## Objective
Exécuter la séquence quotidienne veille-mapping : Gmail label `0---veille-mapping` → extraction URLs → mise à jour/filtrage `LIST.md` → corbeille Gmail → commit/push.

## Plan
- [x] Lire l’état du repo et restaurer un état git propre si nécessaire.
- [x] Extraire les emails Gmail du label `0---veille-mapping` et collecter les URLs candidates.
- [x] Filtrer les URLs hors sujet/locales et mettre à jour `LIST.md` avec déduplication.
- [x] Supprimer de `LIST.md` les URLs hors cartographie/donnée cartographique/actualité carto.
- [x] Mettre à la corbeille les emails traités.
- [x] Mettre à jour le suivi `.prompt-hub` (memory/version/releases/todo), commit et push.

## Review
- Repo initialement dirty: baseline commit+push effectué pour repartir proprement.
- Gmail: 3 email(s) traité(s), 16 URL(s) candidates extraites.
- LIST.md: 2 URL(s) ajoutée(s), 0 supprimée(s), total final 4.
- Emails déplacés à la corbeille: 3.
