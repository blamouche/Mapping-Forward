# Todo — daily veille maps extraire urls de gmail

## Objective
Traiter la veille Gmail `label:0---veille-mapping`, extraire les URLs d’articles, mettre à jour `LIST.md`, nettoyer les URLs hors périmètre, puis mettre les emails traités à la corbeille.

## Plan
- [x] Lire les consignes `.prompt-hub` et créer ce todo.
- [x] Vérifier/synchroniser l’état Git du repo pour repartir proprement.
- [x] Lire les emails Gmail du label et extraire les URLs candidates.
- [x] Filtrer/dédupliquer les URLs, mettre à jour `LIST.md`, puis retirer les liens hors périmètre.
- [x] Mettre à jour le tracking `.prompt-hub` (memory/version/releases/summary).
- [x] Commit + push, puis mettre les emails traités à la corbeille.

## Review
- Repo déjà propre et synchronisé (`git status` clean sur `main...origin/main`).
- Gmail `label:0---veille-mapping` ne contenait aucun message (`--include-body --json --max 50 --no-input`).
- 0 URL candidate extraite, 0 URL ajoutée à `LIST.md`, 0 URL supprimée de `LIST.md`.
- Aucun email à mettre à la corbeille.
