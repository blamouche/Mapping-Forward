# Todo — Daily veille Maps extraire urls de gmail

- [x] Lire `.prompt-hub/lessons.md`
- [x] Lire `.prompt-hub/memory.md`
- [x] Lire `.prompt-hub/releases.md`
- [x] Créer ce fichier de tâche
- [x] Restaurer un repo propre et synchronisé
- [x] Chercher les emails Gmail `label:0---veille-mapping`
- [x] Extraire et filtrer les URLs cartographie/carto data/actualité du domaine
- [x] Mettre à jour `LIST.md` (normalisation, déduplication, nettoyage du hors-scope)
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour le tracking prompt-hub, commit, push

## Notes
- Contrainte agent `add-url`: repo clean avant sync, une URL par ligne, déduplication exacte, commit+push.
- Si le repo n'est pas clean, commit/push d'abord toutes les modifs locales non synchronisées pour repartir d'un état propre.
- Exclure les petites initiatives locales et les faux positifs autour de `map`.

## Review
- 1 email Gmail traité.
- 1 URL candidate extraite, 0 URL ajoutée, 0 URL supprimée.
- L’unique lien a été exclu car il pointait vers une vieille vidéo Frandroid, hors du flux d’actualité cartographie retenu.
- `LIST.md` est resté vide et propre.
