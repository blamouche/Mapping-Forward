# Todo: veille-mapping (2026-03-29 10:04:34 CET)

## Plan
- [x] Vérifier l'état du repo et le synchroniser si nécessaire.
- [x] Chercher les emails Gmail label:0---veille-mapping et extraire les URLs.
- [x] Filtrer les URLs non liées à la cartographie / données carto / actus du domaine (hors initiatives locales).
- [x] Mettre à jour LIST.md via l’agent add-url (dedupe, nettoyage) et supprimer les URLs non pertinentes.
- [x] Mettre les emails traités à la corbeille.
- [x] Mettre à jour le suivi prompt-hub (memory/version/releases) et consigner le résultat.

## Notes
- Exécution autonome (cron).

## Review
- Gmail label 0---veille-mapping vide; aucune URL extraite.
- LIST.md déjà vide; aucun ajout/suppression.
- Aucun email déplacé vers la corbeille.
