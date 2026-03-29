# Todo: veille-mapping (2026-03-29 03:08 CET)

## Plan
- [x] Vérifier l’état du repo et synchroniser (nettoyer si nécessaire).
- [x] Scanner Gmail label:0---veille-mapping et extraire les URLs.
- [x] Filtrer URLs non liées à la cartographie (exclure initiatives locales) et dédupliquer.
- [x] Mettre à jour LIST.md via agent add-url (sync propre, dedupe, commit+push).
- [x] Supprimer de LIST.md les URLs hors périmètre si besoin.
- [x] Mettre à la corbeille les emails traités.
- [x] Mettre à jour .prompt-hub (memory/version/releases) + clôturer la todo.

## Progress
- [x] Repo clean + sync
- [x] Gmail scan + extraction URLs
- [x] Filtrage + déduplication
- [x] LIST.md mise à jour + commit/push
- [x] Nettoyage LIST.md (hors périmètre)
- [x] Emails corbeille
- [x] Logs + versioning + release

## Review
- [x] Résumé + métriques (ajout/suppression URLs)
- [x] Risques / limites

## Résultats
- Gmail label vide : aucune URL trouvée.
- LIST.md déjà vide, aucune suppression.
- Aucun email déplacé à la corbeille.

## Risques / limites
- RAS (aucune donnée à traiter).
