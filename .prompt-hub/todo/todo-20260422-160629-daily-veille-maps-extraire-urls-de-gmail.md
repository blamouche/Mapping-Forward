# Todo - daily veille maps extraire urls de gmail

## Objective
Exécuter la séquence quotidienne Gmail -> LIST.md -> filtrage cartographie -> corbeille -> sync.

## Checklist
- [x] Lire `.prompt-hub/lessons.md`
- [x] Lire `.prompt-hub/memory.md`
- [x] Lire `.prompt-hub/releases.md`
- [x] Vérifier l'état du repo
- [x] Chercher les emails Gmail `label:0---veille-mapping`
- [x] Extraire et filtrer les URLs d'articles
- [x] Mettre à jour `LIST.md` (sync propre, dedupe)
- [x] Supprimer les URLs hors sujet de `LIST.md`
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour `.prompt-hub` puis commit/push

## Notes
- Horodatage de tâche: 20260422-160629
- `git pull --rebase` a confirmé que le dépôt était déjà à jour.

## Review
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` a retourné 0 message actif.
- La vérification `in:anywhere` n'a montré que des alertes déjà en corbeille.
- `LIST.md` est resté inchangé après revue de périmètre.
- Bilan: 0 URL ajoutée, 0 URL supprimée, 0 email mis à la corbeille.
