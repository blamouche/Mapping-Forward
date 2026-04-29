# Todo - daily veille maps extraire urls de gmail

## Context
- Timestamp: 2026-04-29 16:05:15 CEST
- Trigger: cron:e86a7434-db99-44fe-8c2c-6c13463de00f
- Goal: chercher les emails Gmail `label:0---veille-mapping`, extraire les URLs d'articles, mettre à jour `LIST.md` via les règles de l'agent `add-url`, retirer les URLs hors périmètre, puis mettre les emails traités à la corbeille.

## Plan
- [x] Lire les consignes `.prompt-hub` et `agents.md`
- [x] Vérifier l'état git initial
- [ ] Restaurer un repo clean/sync si nécessaire
- [ ] Récupérer les emails Gmail ciblés
- [ ] Extraire et filtrer les URLs candidates
- [ ] Mettre à jour `LIST.md` (normalisation, déduplication, nettoyage du scope)
- [ ] Mettre à jour le tracking `.prompt-hub`
- [ ] Commit et push
- [ ] Ajouter une review finale

## Review
- Pending
