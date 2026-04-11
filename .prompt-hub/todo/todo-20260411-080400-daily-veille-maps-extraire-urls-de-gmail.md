# Todo — daily veille maps extraire urls de gmail

- [x] Lire `.prompt-hub/lessons.md`
- [x] Lire `.prompt-hub/memory.md`
- [x] Lire `.prompt-hub/releases.md`
- [x] Vérifier l’état du repo et la synchro git
- [x] Chercher les emails Gmail label `0---veille-mapping`
- [x] Extraire les URLs d’articles
- [x] Mettre à jour `LIST.md` selon l’agent `add-url`
- [x] Retirer de `LIST.md` les URLs hors périmètre cartographie / donnée cartographique / actualités du domaine (hors petites initiatives locales)
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour les fichiers `.prompt-hub/*`
- [x] Commit + push

## Notes
- Run planifié du 2026-04-11 08:04 Europe/Paris.
- Hypothèse de départ: le label Gmail peut être vide; dans ce cas la routine doit tout de même vérifier `LIST.md`, journaliser l’exécution, puis pousser l’état.

## Review
- Gmail `label:0---veille-mapping` renvoie 0 message avec `--include-body --json`.
- `LIST.md` est vide et reste inchangé après revue de périmètre.
- Aucune URL ajoutée, aucune URL supprimée, aucun email mis à la corbeille.
- Repo déjà propre et synchronisé; seuls les fichiers de suivi `.prompt-hub/*` ont été mis à jour avant commit/push.
