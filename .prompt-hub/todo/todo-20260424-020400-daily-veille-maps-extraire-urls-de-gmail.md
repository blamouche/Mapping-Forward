# Todo - daily-veille-maps-extraire-urls-de-gmail

## Objective
Exécuter la séquence quotidienne Gmail -> LIST.md -> nettoyage scope -> corbeille -> commit/push.

## Plan
- [x] Lire `.prompt-hub/lessons.md`
- [x] Lire `.prompt-hub/memory.md`
- [x] Lire `.prompt-hub/releases.md`
- [x] Vérifier l'état du repo et les consignes `agents.md`
- [x] Restaurer un repo clean/synced (commit/push toutes les modifs locales non synchronisées si nécessaire)
- [x] Récupérer les emails Gmail `label:0---veille-mapping`
- [x] Extraire et normaliser les URLs candidates
- [x] Filtrer les URLs hors scope cartographie/donnée cartographique/actu du domaine, exclure petites initiatives locales
- [x] Mettre à jour `LIST.md` (one URL per line, dedupe, no blanks)
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour `.prompt-hub` (memory, releases, version, summary)
- [x] Commit + push

## Review
- Repo local sale au départ uniquement à cause du nouveau todo planifié; commit/push de baseline effectué avant l'accès Gmail.
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` a retourné 0 message.
- 0 URL candidate, 0 URL ajoutée, 0 URL supprimée.
- `LIST.md` conservait 3 URLs existantes, revues et gardées car toujours dans le scope cartographie/domain news.
- 0 email mis à la corbeille.
