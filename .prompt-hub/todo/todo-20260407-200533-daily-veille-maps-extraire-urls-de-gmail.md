# Todo — daily veille maps extraire urls de gmail

## Objective
Exécuter la séquence quotidienne Gmail -> LIST.md -> nettoyage scope -> corbeille pour le repo Mapping-Forward.

## Plan
- [x] Lire les emails Gmail label `0---veille-mapping`
- [x] Extraire et filtrer les URLs liées à la cartographie/GIS/donnée cartographique
- [x] Restaurer un repo propre si nécessaire, puis mettre à jour `LIST.md` (normalisation + déduplication)
- [x] Supprimer de `LIST.md` les URLs hors scope ou trop locales
- [x] Commit/push les changements requis
- [x] Mettre à la corbeille les emails traités
- [x] Journaliser le run dans `.prompt-hub/*`

## Notes
- Si le repo n'est pas clean, commit/push toutes les modifications locales non synchronisées avant traitement pour repartir proprement.
- Résultat attendu: résumé du run + nombre d'URLs ajoutées/supprimées.

## Review
- 1 email Gmail traité (`Alerte Google : "Here maps"`).
- 2 liens candidats extraits depuis le mail.
- 1 URL conservée: article HERE WeGo sur l'amélioration de la planification bus/train.
- 1 URL filtrée: vidéo YouTube, trop secondaire/bruit pour la file de veille.
- `LIST.md` était vide; 1 URL y a été ajoutée après normalisation/déduplication.
- Revue de scope sur `LIST.md`: 0 URL supprimée.
- Le repo a d'abord été resynchronisé proprement via un commit/push de baseline du todo.
- L'email traité a été déplacé à la corbeille.
