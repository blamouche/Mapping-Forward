# Todo - 2026-04-23 08:04:00 CEST - daily-veille-maps-extraire-urls-de-gmail

## Objective
Exécuter la séquence quotidienne veille mapping: Gmail `label:0---veille-mapping` -> extraction d'URLs -> mise à jour/filtrage de `LIST.md` -> corbeille pour les emails traités -> commit/push.

## Checklist
- [x] Lire `.prompt-hub/lessons.md`
- [x] Lire `.prompt-hub/memory.md`
- [x] Lire `.prompt-hub/releases.md`
- [x] Vérifier l'état initial du repo
- [x] Récupérer les emails Gmail du label veille mapping
- [x] Extraire et filtrer les URLs pertinentes cartographie/géospatial
- [x] Mettre à jour `LIST.md` (normaliser, dédupliquer, retirer hors-scope)
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour la traçabilité prompt-hub
- [x] Commit et push

## Notes
- Si le repo n’est pas clean au démarrage, commit/push toutes les modifications locales non synchronisées avant le traitement Gmail pour repartir d’un état propre.
- Hors scope à exclure: petites initiatives locales, faux positifs autour de `map`, politique locale, promos génériques, vidéos sans matière éditoriale.

## Review
- Repo déjà propre et synchronisé.
- `git pull --rebase` n’a ramené aucun changement.
- Recherche Gmail vide, `LIST.md` reste vide.
- Aucun email à mettre à la corbeille.
- Tracking `.prompt-hub` mis à jour, commit/push effectués.
