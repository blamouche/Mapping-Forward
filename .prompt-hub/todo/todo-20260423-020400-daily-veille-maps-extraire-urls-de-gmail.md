# Todo - 2026-04-23 02:04:00 CEST - daily-veille-maps-extraire-urls-de-gmail

## Objective
Exécuter la séquence quotidienne veille mapping: Gmail `label:0---veille-mapping` -> extraction d'URLs -> mise à jour/filtrage de `LIST.md` -> corbeille pour les emails traités -> commit/push.

## Checklist
- [x] Lire `.prompt-hub/lessons.md`
- [x] Lire `.prompt-hub/memory.md`
- [x] Lire `.prompt-hub/releases.md`
- [x] Vérifier l'état initial du repo
- [x] Récupérer les emails Gmail du label veille mapping
- [x] Extraire et filtrer les URLs pertinentes cartographie/géospatial
- [x] Mettre à jour `LIST.md` (normaliser, dédupliquer, retirer hors-scope)
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour la traçabilité prompt-hub
- [x] Commit et push

## Notes
- Hypothèse de travail: le repo était déjà clean/synced au démarrage, donc pas de commit baseline supplémentaire requis avant l'extraction.
- Hors scope à exclure: faits divers, politique de redistricting, YouTube, initiatives locales/petits événements locaux, faux positifs `map`.

## Review
- Gmail: 3 alertes traitées, 20 URLs candidates extraites.
- Ajouts retenus dans `LIST.md`: 3 URLs (TechCrunch sur l'IA dans Google Maps, Airbus sur la cartographie satellite des plantations de café, 01net sur Maps Imagery Grounding / Street View pour décors).
- Suppressions de `LIST.md`: 0, les 3 URLs déjà présentes sont restées dans le scope carto/géo.
- Emails: 3 messages déplacés vers `TRASH` et sortis de `UNREAD`.
- Commit/push: à inclure dans le commit `Add URL(s) to processing queue`.
