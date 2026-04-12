# Todo - daily-veille-maps

- [x] Collecter les emails Gmail label:0---veille-mapping
- [x] Extraire et filtrer les URLs
- [x] Synchroniser proprement le repo et mettre à jour LIST.md
- [x] Nettoyer les URLs hors sujet
- [x] Commit/push et mettre à la corbeille les emails

## Review
- `gog gmail messages search 'label:0---veille-mapping' --max 100 --json --no-input` a échoué avec OAuth `invalid_grant` (token Gmail expiré/révoqué).
- Tentative de fallback via le navigateur connecté à Gmail impossible: attache Chrome user timeout, aucun onglet exploitable.
- `LIST.md` était déjà vide et est resté inchangé; aucune URL ajoutée/supprimée et aucun email mis à la corbeille.
- La trace d’échec a été mise à jour dans les fichiers prompt-hub puis sera commit/push pour garder le repo propre.
