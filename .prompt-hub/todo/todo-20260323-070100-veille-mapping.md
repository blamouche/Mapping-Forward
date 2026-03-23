# Todo 20260323-070100 - veille-mapping

## Objective
Exécuter la séquence quotidienne veille mapping Gmail -> LIST.md, filtrer, dédupliquer, nettoyer le repo, et archiver les emails traités.

## Plan
1. Vérifier l'état du repo; si non clean, commit/push toutes les modifications locales.
2. Récupérer les emails Gmail label:0---veille-mapping (messages) et extraire les URLs.
3. Filtrer URLs (cartographie only, exclure petites initiatives locales), dédupliquer, nettoyer LIST.md.
4. Mettre à la corbeille les emails traités.
5. Mettre à jour version/release/prompt-hub mémoire et commit/push.

## Progress
- [x] Repo clean sync
- [x] Gmail scan + extraction URLs
- [x] Filtering/dedupe + LIST.md update
- [x] Trash emails
- [x] Versioning + releases + commit/push

## Notes
Plan exécuté directement selon la demande explicite (cron) de Ben.

## Review
- Outcome: Added mapping URLs from veille Gmail alerts.
- URLs added: 5
- URLs removed: 0
- Emails trashed: 3
- Notes: Excluded non-mapping/local/news noise (YouTube, local traffic survey, finance ticker, etc.).
