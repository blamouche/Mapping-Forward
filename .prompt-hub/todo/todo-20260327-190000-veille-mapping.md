# Todo 20260327-190000 - veille-mapping

## Objective
Exécuter la veille quotidienne: extraire les URLs des emails Gmail label 0---veille-mapping, mettre à jour LIST.md (filtrer cartographie), dédupliquer, commit+push, puis mettre les emails traités à la corbeille.

## Plan
1. Vérifier l’état du repo et nettoyer si nécessaire (committer/pusher toute modif locale non synchronisée).
2. Récupérer les emails Gmail label 0---veille-mapping et extraire les URLs d’articles.
3. Filtrer les URLs non cartographie / non données carto / non actualités carto (exclure petites initiatives locales).
4. Mettre à jour LIST.md (dedupe) et supprimer les URLs non pertinentes si présentes.
5. Commit + push selon les règles add-url (sync propre + vérifications).
6. Mettre à la corbeille les emails traités.
7. Journaliser dans .prompt-hub/memory.md, mettre à jour version/release, puis commit/push.

## Check-in
User request received via cron trigger; proceed with execution.

## Progress
- [ ] Repo clean/sync
- [ ] Gmail search + URL extraction
- [ ] Filtering (mapping relevance)
- [ ] Update LIST.md (dedupe + removals)
- [ ] Commit/push changes
- [ ] Trash processed emails
- [ ] Log memory + version/release updates, commit/push

## Review
- [ ] Summary provided to user
- [ ] URLs added/removed counted
- [ ] Emails trashed confirmed
