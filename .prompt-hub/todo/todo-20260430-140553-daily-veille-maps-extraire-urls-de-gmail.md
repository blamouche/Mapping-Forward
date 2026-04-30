# Daily veille Maps - 2026-04-30 14:05:53 CEST

## Objective
Exécuter la séquence quotidienne Gmail -> LIST.md, filtrer les URLs hors scope, puis déplacer les emails traités à la corbeille.

## Checklist
- [x] Lire l'état initial du repo et du run
- [x] Remettre le repo dans un état propre/synchronisé si nécessaire
- [x] Chercher les emails Gmail `label:0---veille-mapping`
- [x] Extraire et filtrer les URLs candidates
- [x] Mettre à jour `LIST.md` avec déduplication
- [x] Supprimer de `LIST.md` les URLs hors scope
- [x] Mettre à jour les fichiers prompt-hub
- [ ] Commit + push
- [x] Mettre les emails traités à la corbeille

## Notes
- Conserver uniquement les URLs liées à la cartographie, la donnée cartographique et les actualités du domaine cartographique.
- Exclure les petites initiatives locales et les faux positifs autour de “map/maps/mapping”.
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` a renvoyé 0 message.
- `LIST.md` contenait déjà `https://www.geoweeknews.com/blogs/capture-it-while-the-trench-is-open`, revue et conservée in scope (documentation continue de chantier, GIS / digital twin / reality capture pour l'infrastructure).

## Review
- Repo nettoyé via baseline commit/push avant la lecture Gmail.
- Aucun nouvel email à traiter, aucune URL ajoutée/supprimée.
- Aucun email déplacé à la corbeille.
