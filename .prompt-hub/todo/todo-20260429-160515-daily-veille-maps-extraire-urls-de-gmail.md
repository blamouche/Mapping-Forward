# Todo - daily veille maps extraire urls de gmail

## Context
- Timestamp: 2026-04-29 16:05:15 CEST
- Trigger: cron:e86a7434-db99-44fe-8c2c-6c13463de00f
- Goal: chercher les emails Gmail `label:0---veille-mapping`, extraire les URLs d'articles, mettre à jour `LIST.md` via les règles de l'agent `add-url`, retirer les URLs hors périmètre, puis mettre les emails traités à la corbeille.

## Plan
- [x] Lire les consignes `.prompt-hub` et `agents.md`
- [x] Vérifier l'état git initial
- [x] Restaurer un repo clean/sync si nécessaire
- [x] Récupérer les emails Gmail ciblés
- [x] Extraire et filtrer les URLs candidates
- [x] Mettre à jour `LIST.md` (normalisation, déduplication, nettoyage du scope)
- [x] Mettre à jour le tracking `.prompt-hub`
- [x] Commit et push
- [x] Ajouter une review finale

## Review
- Repo initialement clean, puis baseline tracking commit/push effectué pour respecter le prérequis `add-url` de travail sur un état propre.
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` a renvoyé 0 message.
- `LIST.md` était déjà vide et est resté vide après revue de périmètre.
- Résultat final: 0 URL ajoutée, 0 URL supprimée, 0 email mis à la corbeille.
