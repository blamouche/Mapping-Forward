# Todo - daily-veille-maps-extraire-urls-de-gmail

## Context
- Trigger: cron `Daily veille Maps Extraire urls de gmail`
- Goal: chercher les emails Gmail `label:0---veille-mapping`, extraire les URLs d'articles, mettre à jour `LIST.md`, retirer les URLs hors scope cartographie/donnée cartographique/actualité du domaine (hors petites initiatives locales), puis mettre à la corbeille les emails traités.
- Constraints: suivre `agents.md` et l'agent `add-url`, garder le repo propre/synchronisé, journaliser chaque action significative, versionner toute modification, commit/push.

## Plan
- [x] Lire le contexte prompt-hub requis et vérifier l'état du repo.
- [x] Créer ce fichier todo avant exécution.
- [x] Rechercher les emails Gmail du label ciblé et extraire les URLs candidates.
- [x] Mettre à jour `LIST.md` avec normalisation, déduplication et filtrage de scope.
- [x] Mettre à jour les fichiers prompt-hub (`memory`, `releases`, `version`, éventuel résumé de run).
- [x] Committer et pousser les changements.
- [x] Mettre à la corbeille les emails traités.

## Review
- Gmail `label:0---veille-mapping` était vide à 06:16 CEST.
- Aucune URL candidate détectée, donc aucun ajout dans `LIST.md`.
- `LIST.md` était déjà vide, donc aucune suppression hors scope à faire.
- Aucun email à déplacer vers la corbeille.
