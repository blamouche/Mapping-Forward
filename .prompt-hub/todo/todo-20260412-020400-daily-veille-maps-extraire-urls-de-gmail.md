# Todo — daily veille maps extraire urls de gmail

- [x] Lire les consignes repo (`agents.md`, lessons, memory, releases).
- [x] Vérifier l’état git et remettre le repo dans un état propre/synchronisé si nécessaire.
- [x] Chercher les emails Gmail `label:0---veille-mapping`.
- [x] Extraire et filtrer les URLs mapping/cartographie/GIS ; mettre à jour `LIST.md` (dedupe, une URL par ligne). *(bloqué par Gmail OAuth invalid_grant ; aucune modification métier)*
- [x] Retirer de `LIST.md` les URLs hors périmètre (non carto / petites initiatives locales). *(non applicable : `LIST.md` déjà vide et run bloqué avant extraction)*
- [x] Mettre à la corbeille les emails traités. *(impossible : aucun email accessible pendant l’échec OAuth)*
- [x] Mettre à jour le suivi `.prompt-hub` (memory, releases, version, review), commit, push.

## Notes
- Exécution cron du 2026-04-12 02:04 CEST.
- Si Gmail OAuth échoue (`invalid_grant`), arrêter avant toute modification métier et journaliser l’échec.

## Review
- Repo propre au départ (`## main...origin/main`).
- Gmail bloqué sur `invalid_grant` avec `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 20`.
- `LIST.md` inchangé (0 URL ajoutée, 0 supprimée).
- 0 email mis à la corbeille faute d’accès Gmail.
