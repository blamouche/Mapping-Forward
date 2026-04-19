# Todo - daily-veille-maps-extraire-urls-de-gmail

## Objective
Exécuter la veille quotidienne Gmail -> LIST.md pour la file cartographie.

## Checklist
- [x] Lire `.prompt-hub/lessons.md`
- [x] Lire `.prompt-hub/memory.md`
- [x] Lire `.prompt-hub/releases.md`
- [x] Vérifier l'état du repo
- [x] Synchroniser le repo avec `origin/main`
- [x] Chercher les emails Gmail `label:0---veille-mapping`
- [x] Extraire et filtrer les URLs cartographie/GIS/maps
- [x] Mettre à jour `LIST.md` (normalisation, dédoublonnage, nettoyage)
- [x] Mettre à jour les fichiers de suivi prompt-hub
- [x] Mettre les emails traités à la corbeille
- [x] Commit et push

## Notes
- Si le repo n'est pas clean, commit/push toutes les modifs locales non synchronisées avant le run.
- Exclure les petites initiatives locales et les URLs hors cartographie / donnée cartographique / actualité du domaine.

## Review
- Repo clean et synchronisé avec `origin/main`.
- 2 emails Gmail `label:0---veille-mapping` traités.
- 18 URLs candidates extraites, 2 gardées après filtrage de pertinence.
- `LIST.md` était vide, 2 URLs en scope y ont été ajoutées, 0 URL retirée.
- 2 emails déplacés vers la corbeille.
