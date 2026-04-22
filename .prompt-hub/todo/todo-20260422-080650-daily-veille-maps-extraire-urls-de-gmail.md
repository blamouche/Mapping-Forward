# Todo - Daily veille maps extraire urls de gmail

## Objective
Exécuter la séquence quotidienne: chercher les emails Gmail `label:0---veille-mapping`, extraire les URLs d'articles, mettre à jour `LIST.md` selon les règles `add-url`, supprimer les URLs hors scope cartographie/donnée cartographique/actualité du domaine (hors petites initiatives locales), puis mettre à la corbeille les emails traités.

## Plan
- [x] Lire les consignes `.prompt-hub` requises et l'état du repo.
- [x] Vérifier que le repo est propre/synchronisé, sinon commit/push toutes les modifs locales non synchronisées pour repartir d'un état clean.
- [x] Interroger Gmail sur `label:0---veille-mapping` et extraire les URLs candidates.
- [x] Filtrer les URLs au scope cartographie/cartographic data/domain news, dédupliquer, puis mettre à jour `LIST.md`.
- [x] Mettre à jour les fichiers prompt-hub (summary, memory, releases, version, review du todo), commit/push.
- [x] Mettre à la corbeille les emails traités.

## Review
- Repo remis dans un état clean/synced via commit/push du todo de run avant l'extraction Gmail.
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` a renvoyé 0 message.
- `LIST.md` est resté vide après revue du scope, donc 0 URL ajoutée et 0 supprimée.
- Aucun email n'a été mis à la corbeille car aucun email n'a été trouvé.
