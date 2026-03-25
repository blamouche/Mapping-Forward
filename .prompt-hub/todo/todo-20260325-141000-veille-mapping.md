# Todo — veille-mapping (2026-03-25 14:10 CET)

## Objective
Exécuter la séquence quotidienne Gmail -> LIST.md (mapping only), nettoyer la liste, puis trash les emails traités.

## Plan
1. Vérifier repo propre + sync.
2. Extraire les emails Gmail label:0---veille-mapping, collecter les URLs.
3. Filtrer les URLs: cartographie / données spatiales / actus du domaine (exclure petites initiatives locales).
4. Mettre à jour LIST.md (dedupe + remove non-mapping), commit+push.
5. Mettre à la corbeille les emails traités.
6. Renseigner le récap et fermer la tâche.

## Check-in
Plan confirmé par la demande explicite de l’utilisateur ("Exécute la séquence quotidienne").

## Progress
- [x] Repo sync + clean
- [x] Gmail extraction + filtering
- [x] LIST.md update + dedupe + prune non-mapping
- [x] Commit + push (incl. version/release)
- [x] Trash processed emails
- [x] Review + close

## Review
- Added 12 URLs from Gmail veille; removed 3 non-mapping URLs from LIST.md.
- Trashed 9 processed Gmail messages.
