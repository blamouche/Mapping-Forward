# Todo — veille-mapping — 2026-04-06 02:04:28

## Objective
Exécuter la séquence quotidienne veille-mapping : scanner Gmail label `0---veille-mapping`, extraire/filtrer les URLs, maintenir `LIST.md` propre et synchronisé, puis mettre à la corbeille les emails traités.

## Plan
- [x] Lire les consignes repo (`agents.md`, lessons/memory/releases)
- [x] Créer ce fichier de tâche
- [x] Vérifier l’état git du repo et le resynchroniser si nécessaire
- [x] Scanner Gmail label `0---veille-mapping`
- [x] Extraire et normaliser les URLs d’articles
- [x] Ajouter les URLs retenues à `LIST.md` avec déduplication
- [x] Supprimer de `LIST.md` les URLs hors cartographie / données cartographiques / actualités du domaine, en excluant les petites initiatives locales
- [ ] Commit + push de toutes les modifs nécessaires pour revenir à un état propre
- [ ] Mettre à la corbeille les emails traités
- [ ] Mettre à jour mémoire / version / releases / review

## Check-in
Hypothèse opérationnelle: tâche autonome de cron, donc exécution complète sans attendre de validation interactive.

## Review
- Gmail: 2 alertes traitées (`Maps`, `Mapping`).
- Extraction: 17 URLs candidates détectées, 8 retenues pour `LIST.md`.
- Nettoyage de `LIST.md`: suppression de 2 URLs promotionnelles/hors périmètre déjà présentes.
- Git: commit/push final à faire après mise à la corbeille des emails.
