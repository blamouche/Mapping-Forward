# Todo — daily veille maps extraire urls de gmail

## Objective
Exécuter la séquence quotidienne : extraire les URLs des emails Gmail label `0---veille-mapping`, mettre à jour `LIST.md`, retirer les URLs hors périmètre cartographie/GIS/data cartographique (hors petites initiatives locales), puis mettre les emails traités à la corbeille.

## Plan
- [x] Vérifier l’état git du repo et le remettre propre/synchronisé si nécessaire.
- [x] Chercher les emails Gmail du label `0---veille-mapping` et extraire les URLs candidates.
- [x] Mettre à jour `LIST.md` selon les règles de l’agent `add-url` (normalisation, déduplication, commit+push).
- [x] Repasser `LIST.md` pour supprimer les URLs hors périmètre.
- [x] Mettre à la corbeille les emails traités.
- [x] Mettre à jour le suivi `.prompt-hub` (memory, releases, version, summary, review) et pousser les changements.

## Review
- Repo baseline re-cleaned first via a dedicated prompt-hub commit/push.
- Gmail label `0---veille-mapping`: 3 messages processed, 29 candidate URLs extracted.
- Kept 4 in-scope URLs and filtered 25 off-scope/local/noise items.
- `LIST.md` moved from 0 to 4 URLs after dedupe.
- 3 processed Gmail alerts moved to Trash.
