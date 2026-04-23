# Todo - daily veille maps extraire urls de gmail

## Objective
Exécuter la séquence quotidienne: extraire les URLs des emails Gmail `label:0---veille-mapping`, mettre à jour `LIST.md`, supprimer les URLs hors périmètre, puis mettre à la corbeille les emails traités.

## Plan
- [x] Lire le contexte prompt-hub requis
- [x] Vérifier l'état git initial
- [x] Extraire les messages Gmail et les URLs candidates
- [x] Mettre à jour `LIST.md` avec déduplication et filtrage de périmètre
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour le suivi prompt-hub, commit et push

## Notes
- Repo initialement clean sur `main...origin/main`.

## Review
- Gmail `label:0---veille-mapping` vide au moment du run.
- `LIST.md` inchangé, toujours vide après revue de périmètre.
- Aucun email à mettre à la corbeille.
