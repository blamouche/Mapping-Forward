# Todo - 2026-04-23 08:04:00 CEST - daily-veille-maps-extraire-urls-de-gmail

## Objective
Exécuter la séquence quotidienne veille mapping: Gmail `label:0---veille-mapping` -> extraction d'URLs -> mise à jour/filtrage de `LIST.md` -> corbeille pour les emails traités -> commit/push.

## Checklist
- [x] Lire `.prompt-hub/lessons.md`
- [x] Lire `.prompt-hub/memory.md`
- [x] Lire `.prompt-hub/releases.md`
- [x] Vérifier l'état initial du repo
- [ ] Récupérer les emails Gmail du label veille mapping
- [ ] Extraire et filtrer les URLs pertinentes cartographie/géospatial
- [ ] Mettre à jour `LIST.md` (normaliser, dédupliquer, retirer hors-scope)
- [ ] Mettre à la corbeille les emails traités
- [ ] Mettre à jour la traçabilité prompt-hub
- [ ] Commit et push

## Notes
- Si le repo n’est pas clean au démarrage, commit/push toutes les modifications locales non synchronisées avant le traitement Gmail pour repartir d’un état propre.
- Hors scope à exclure: petites initiatives locales, faux positifs autour de `map`, politique locale, promos génériques, vidéos sans matière éditoriale.

## Review
- En cours.
