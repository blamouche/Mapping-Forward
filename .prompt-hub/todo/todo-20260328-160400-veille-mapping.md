# Todo: veille mapping (2026-03-28 16:04 CET)

## Objective
Exécuter la séquence quotidienne: Gmail label 0---veille-mapping → extraire URLs → mettre à jour LIST.md (dedupe + filtre carto) → nettoyer URLs non pertinentes → trash emails.

## Plan
- [ ] Sync et vérifier état repo (doit être clean).
- [ ] Chercher emails Gmail label 0---veille-mapping.
- [ ] Extraire URLs d’articles (dédupe).
- [ ] Filtrer: garder uniquement cartographie/données/cartographie/news domaine (exclure petites initiatives locales).
- [ ] Mettre à jour LIST.md via procédure add-url (sync propre, dedupe, checks).
- [ ] Supprimer de LIST.md les URLs hors scope.
- [ ] Mettre à la corbeille les emails traités.
- [ ] Mettre à jour .prompt-hub (memory, version, releases), commit/push.

## Progress
- [x] Repo clean confirmé.
- [x] Gmail scanné (label vide).
- [x] URLs extraites et filtrées (aucune).
- [x] LIST.md mis à jour (aucun changement).
- [x] Emails traités supprimés (aucun).

## Review
- [x] Résumé + comptage URLs ajoutées/supprimées.
- [x] Todos & prompt-hub mis à jour.
