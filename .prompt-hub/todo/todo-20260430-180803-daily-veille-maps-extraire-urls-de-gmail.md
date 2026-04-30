# Todo - daily veille maps extraire urls de gmail

## Objective
Traiter les emails Gmail label:0---veille-mapping, extraire les URLs d’articles, maintenir LIST.md propre et synchronisé, puis corbeiller les emails traités.

## Plan
- [x] Inspecter l’état du repo et le synchroniser
- [x] Chercher les emails Gmail ciblés et extraire les URLs
- [x] Ajouter/dédupliquer/filtrer les URLs dans LIST.md
- [x] Committer, pousser, puis corbeiller les emails traités

## Review
- Gmail `label:0---veille-mapping` a retourné 0 email.
- `LIST.md` était déjà vide et aucune URL hors périmètre n’a dû être retirée.
- 0 URL ajoutée, 0 URL supprimée, 0 email corbeillé.
- Run journalisé dans les fichiers prompt-hub, avec bump de version et release note.
