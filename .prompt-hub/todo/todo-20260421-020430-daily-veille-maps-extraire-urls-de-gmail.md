# Todo - Daily veille maps extraire urls de gmail

## Objective
Exécuter la séquence quotidienne: lire les emails Gmail du label `0---veille-mapping`, extraire les URLs d'articles, mettre à jour `LIST.md` avec déduplication/filtrage métier, supprimer les emails traités, puis tracer le run.

## Checklist
- [x] Vérifier l'état du repo et le resynchroniser si nécessaire
- [x] Lire les emails Gmail du label cible
- [x] Extraire, normaliser et filtrer les URLs cartographie/GIS/cartographie data
- [x] Mettre à jour `LIST.md` avec déduplication
- [x] Mettre à jour le suivi `.prompt-hub`
- [x] Commit et push
- [x] Mettre les emails traités à la corbeille

## Review
- Repo d'abord remis à plat avec un commit/push de baseline pour respecter la règle clean-before-sync.
- 1 email Google Alerts traité.
- 10 URLs candidates extraites, 2 URLs gardées, 0 URL existante supprimée.
- URLs ajoutées: `https://www.abondance.com/20260420-2186214-google-maps-suppression-292-millions-avis-frauduleux-2025.html`, `https://www.bbc.com/afrique/articles/cn43ndy7qxzo`.
- Email traité déplacé vers la corbeille via `gog gmail batch modify --add TRASH --remove UNREAD`.
