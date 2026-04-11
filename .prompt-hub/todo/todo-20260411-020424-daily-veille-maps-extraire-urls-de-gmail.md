# Todo — daily veille maps extraire urls de gmail

## Objective
Exécuter la séquence quotidienne : extraire les URLs des emails Gmail label `0---veille-mapping`, mettre à jour `LIST.md`, retirer les URLs hors périmètre cartographie/GIS/data cartographique (hors petites initiatives locales), puis mettre les emails traités à la corbeille.

## Plan
- [ ] Vérifier l’état git du repo et le remettre propre/synchronisé si nécessaire.
- [ ] Chercher les emails Gmail du label `0---veille-mapping` et extraire les URLs candidates.
- [ ] Mettre à jour `LIST.md` selon les règles de l’agent `add-url` (normalisation, déduplication, commit+push).
- [ ] Repasser `LIST.md` pour supprimer les URLs hors périmètre.
- [ ] Mettre à la corbeille les emails traités.
- [ ] Mettre à jour le suivi `.prompt-hub` (memory, releases, version, summary, review) et pousser les changements.

## Review
- Pending
