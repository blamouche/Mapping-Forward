# Todo — daily veille maps extraire urls de gmail

## Objective
Exécuter la séquence quotidienne veille-mapping: Gmail label `0---veille-mapping` → extraction d'URLs → mise à jour de `LIST.md` (sync propre, déduplication, filtrage cartographie) → corbeille des emails → commit/push.

## Plan
- [x] Lire les règles prompt-hub et l'historique du repo.
- [x] Vérifier/synchroniser l'état git propre.
- [x] Chercher les emails Gmail `label:0---veille-mapping`.
- [x] Extraire les URLs d'articles et filtrer la veille hors périmètre/locale.
- [x] Mettre à jour `LIST.md` avec déduplication et validation.
- [x] Mettre à jour les fichiers prompt-hub (memory/version/releases + review).
- [x] Commit/push puis mettre les emails traités à la corbeille.

## Notes
- Run cron autonome: j'applique l'hypothèse raisonnable qu'aucun check-in interactif n'est possible.

## Review
- Repo était clean au départ; `git pull --rebase` a confirmé l'état synchronisé.
- Gmail `label:0---veille-mapping` ne contenait aucun message au moment du run.
- `LIST.md` est resté inchangé après revue de périmètre.
- Aucun email à mettre à la corbeille.
- Résultat: 0 URL ajoutée, 0 URL supprimée.
