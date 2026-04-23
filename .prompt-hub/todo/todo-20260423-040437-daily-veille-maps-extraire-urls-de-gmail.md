# Todo - Daily veille maps extraire urls de Gmail

## Objective
Exécuter la séquence quotidienne : extraire les URLs des emails Gmail `label:0---veille-mapping`, mettre à jour `LIST.md` avec une queue propre et pertinente, supprimer les emails traités, puis consigner les changements.

## Checklist
- [x] Lire les consignes `.prompt-hub` et l’historique utile.
- [x] Vérifier l’état git initial du repo.
- [x] Synchroniser le repo proprement avant modification.
- [x] Chercher les emails Gmail `label:0---veille-mapping`.
- [x] Extraire les URLs candidates et filtrer le hors sujet.
- [x] Mettre à jour `LIST.md` (normalisation, déduplication, nettoyage du hors périmètre).
- [x] Mettre à la corbeille les emails traités.
- [x] Mettre à jour `.prompt-hub` (memory, releases, version, summary, review).
- [ ] Commit et push toutes les modifications.

## Notes
- Si le repo n’est pas clean, commit/push toutes les modifications locales non synchronisées avant le traitement Gmail pour repartir d’un état propre.
- Exclure les petites initiatives locales et les faux positifs autour de “map”.
- Cette exécution était vide : aucun email trouvé sous `label:0---veille-mapping`, donc aucune URL candidate ni email à mettre à la corbeille.

## Review
- Repo déjà propre et synchronisé.
- `git pull --rebase` n’a ramené aucun changement.
- Recherche Gmail vide, `LIST.md` reste vide.
- Tracking `.prompt-hub` mis à jour, commit/push restant à faire.
