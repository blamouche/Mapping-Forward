# Daily veille Maps extraire URLs de Gmail

- [x] Lire `.prompt-hub/lessons.md`
- [x] Lire `.prompt-hub/memory.md`
- [x] Lire `.prompt-hub/releases.md`
- [x] Vérifier l'état du repo
- [x] Chercher les emails Gmail `label:0---veille-mapping`
- [x] Extraire et filtrer les URLs d'articles
- [x] Nettoyer `LIST.md` (déduplication + suppression hors périmètre)
- [x] Commit + push les changements
- [x] Mettre à la corbeille les emails traités
- [x] Ajouter la review finale

## Notes
- Horodatage demandé par le cron: 2026-04-28 16:04 CEST.
- Repo déjà propre au départ.
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` a retourné 0 message.
- `LIST.md` est resté vide après revue du périmètre.

## Review
- Exécution terminée sans nouvel email à traiter.
- URLs ajoutées: 0.
- URLs supprimées: 0.
- Emails mis à la corbeille: 0.
