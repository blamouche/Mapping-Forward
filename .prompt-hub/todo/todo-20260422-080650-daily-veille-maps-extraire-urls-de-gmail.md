# Todo - Daily veille maps extraire urls de gmail

## Objective
Exécuter la séquence quotidienne: chercher les emails Gmail `label:0---veille-mapping`, extraire les URLs d'articles, mettre à jour `LIST.md` selon les règles `add-url`, supprimer les URLs hors scope cartographie/donnée cartographique/actualité du domaine (hors petites initiatives locales), puis mettre à la corbeille les emails traités.

## Plan
- [x] Lire les consignes `.prompt-hub` requises et l'état du repo.
- [ ] Vérifier que le repo est propre/synchronisé, sinon commit/push toutes les modifs locales non synchronisées pour repartir d'un état clean.
- [ ] Interroger Gmail sur `label:0---veille-mapping` et extraire les URLs candidates.
- [ ] Filtrer les URLs au scope cartographie/cartographic data/domain news, dédupliquer, puis mettre à jour `LIST.md`.
- [ ] Mettre à jour les fichiers prompt-hub (summary, memory, releases, version, review du todo), commit/push.
- [ ] Mettre à la corbeille les emails traités.

## Review
- Pending
