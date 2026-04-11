# Daily veille maps extraire urls de gmail

- [x] Lire lessons/memory/releases et vérifier l’état du repo
- [x] Chercher les emails Gmail label:0---veille-mapping
- [ ] Extraire et filtrer les URLs d’articles
- [ ] Mettre à jour LIST.md (sync propre, dedupe, commit+push)
- [ ] Supprimer de LIST.md les URLs hors périmètre
- [ ] Mettre à la corbeille les emails traités
- [x] Mettre à jour prompt-hub (memory/version/releases) et pousser le résultat

## Review
- Échec bloquant côté Gmail OAuth: `gog gmail messages search 'label:0---veille-mapping' --include-body --json` retourne `invalid_grant` (`Token has been expired or revoked`).
- Repo vérifié propre au départ (`git status --short --branch` → `## main...origin/main`).
- Aucune extraction d’URL, aucune modification de `LIST.md`, aucun email mis à la corbeille.
- Action requise: ré-authentifier `gog` pour Gmail puis relancer la séquence.
