# Todo - Daily veille Maps extraire URLs de Gmail

- [x] Lire `.prompt-hub/lessons.md`
- [x] Lire `.prompt-hub/memory.md`
- [x] Lire `.prompt-hub/releases.md`
- [x] Vérifier les consignes de `agents.md` (agent `add-url`)
- [x] Restaurer un repo clean et synchronisé
- [x] Rechercher les emails Gmail `label:0---veille-mapping`
- [x] Extraire et filtrer les URLs d'articles
- [x] Mettre à jour `LIST.md` (ajout, déduplication, nettoyage hors scope)
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour les fichiers `.prompt-hub` et rédiger la review

## Notes
- Run triggered by cron at 2026-04-21 18:06 CEST.
- Scope: cartographie, donnée cartographique, actualités du domaine cartographique; exclure les petites initiatives locales.

## Review
- Repo clean et synchronisé après commit/push de baseline puis `git pull --rebase origin main`.
- Gmail `label:0---veille-mapping`: 0 email, 0 URL candidate.
- `LIST.md`: 0 URL ajoutée, 0 URL supprimée, 0 URL finale.
- Emails mis à la corbeille: 0.
