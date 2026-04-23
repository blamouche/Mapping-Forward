# Todo - daily-veille-maps-extraire-urls-de-gmail

## Context
- Trigger: cron `Daily veille Maps Extraire urls de gmail`
- Goal: chercher les emails Gmail `label:0---veille-mapping`, extraire les URLs d'articles, mettre à jour `LIST.md`, retirer les URLs hors scope cartographie/donnée cartographique/actualité du domaine (hors petites initiatives locales), puis mettre à la corbeille les emails traités.
- Constraints: suivre `agents.md` et l'agent `add-url`, garder le repo propre/synchronisé, journaliser chaque action significative, versionner toute modification, commit/push.

## Plan
- [x] Lire le contexte prompt-hub requis et vérifier l'état du repo.
- [x] Créer ce fichier todo avant exécution.
- [ ] Rechercher les emails Gmail du label ciblé et extraire les URLs candidates.
- [ ] Mettre à jour `LIST.md` avec normalisation, déduplication et filtrage de scope.
- [ ] Mettre à jour les fichiers prompt-hub (`memory`, `releases`, `version`, éventuel résumé de run).
- [ ] Committer et pousser les changements.
- [ ] Mettre à la corbeille les emails traités.

## Review
- Pending.
