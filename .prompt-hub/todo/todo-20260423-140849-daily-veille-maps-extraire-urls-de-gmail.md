# Todo — Daily veille Maps extraire urls de Gmail

- [x] Lire `agents.md`, `.prompt-hub/lessons.md`, `.prompt-hub/memory.md`, `.prompt-hub/releases.md`
- [x] Vérifier l’état du repo et le resynchroniser proprement si nécessaire
- [x] Rechercher les emails Gmail `label:0---veille-mapping`
- [x] Extraire et filtrer les URLs cartographie / donnée cartographique / actualités du domaine
- [x] Mettre à jour `LIST.md` (normalisation, déduplication, suppression des hors-scope)
- [x] Commit + push toutes les modifications nécessaires
- [x] Mettre à la corbeille les emails traités
- [x] Compléter le bilan et la review

## Notes
- Demande cron du 2026-04-23 14:07 CEST.
- Si le repo n’est pas clean, commit/push toutes les modifications locales non synchronisées avant la mise à jour de `LIST.md`.
- Exclure les petites initiatives locales et les faux positifs autour de `map`.

## Review
- Repo initialement clean, puis baseline tracking commit créé/poussé pour respecter la consigne de repartir d’un état propre après création du todo.
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` a retourné 0 message.
- `LIST.md` était vide et est resté vide après revue éditoriale.
- 0 URL ajoutée, 0 URL supprimée, 0 email mis à la corbeille.
