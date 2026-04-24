# Todo - daily veille maps extraire urls de gmail

- [x] Lire les consignes prompt-hub et le contexte repo
- [x] Vérifier/synchroniser le repo depuis un état propre
- [x] Chercher les emails Gmail `label:0---veille-mapping`
- [x] Extraire et filtrer les URLs cartographie / données cartographiques / actus du domaine
- [x] Mettre à jour `LIST.md` avec déduplication
- [x] Supprimer de `LIST.md` les URLs hors périmètre
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour mémoire/version/releases et pousser

## Review
- Repo nettoyé via commit/push du todo de suivi, puis `git pull --rebase` (already up to date).
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` a retourné 0 message.
- `LIST.md` était vide et est resté inchangé après revue du périmètre.
- 0 URL ajoutée, 0 URL supprimée, 0 email mis à la corbeille.
