# Todo - 20260421-140500 - daily-veille-maps-extraire-urls-de-gmail

## Objective
Executer la veille mapping quotidienne: sync propre, extraction Gmail label `0---veille-mapping`, filtrage cartographie, mise a jour de `LIST.md`, suppression des emails traites, puis commit/push.

## Checklist
- [x] Lire le contexte prompt-hub et verifier l'etat du repo
- [x] Rendre le repo propre/synchronise si necessaire
- [x] Extraire les emails Gmail label `0---veille-mapping`
- [x] Extraire et filtrer les URLs in-scope
- [x] Mettre a jour `LIST.md` (dedupe + nettoyage)
- [x] Supprimer de `LIST.md` les URLs hors scope
- [x] Mettre a jour version, releases, memory et resume du run
- [x] Commit + push toutes les modifications
- [x] Mettre a la corbeille les emails traites

## Review
- Repo remis a un etat propre via un commit/push de baseline avant extraction Gmail.
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` a retourne 0 message.
- `LIST.md` est reste vide et inchange apres revue du scope.
- URLs ajoutees: 0. URLs supprimees: 0. Emails mis a la corbeille: 0.
