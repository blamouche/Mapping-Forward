# Task: Déplacer site/ vers docs/

- **Date**: 2026-08-24 11:36 CEST
- **Statut**: in_progress

## Objectif

Renommer le dossier `site/` en `docs/` (tout ce qui concerne le site).

## Contexte

- `site/` contient : `build_site.py`, `README.md`, `.gitignore`, `dist/` (ignoré)
- Le script est relatif à `__file__` → fonctionnera tel quel dans `docs/`
- Le style refresh de `build_site.py` est non commité → ne pas le committer
- `.github/workflows/build-site.yml` référence `site/...` → à mettre à jour

## Étapes

- [x] Créer todo
- [x] `git mv site/* docs/` — renames stages purs (0 ligne), modifs non commitées préservées
- [x] Vérifier que les modifs style restent non commitées sur `docs/build_site.py`
- [x] Mettre à jour `.github/workflows/build-site.yml` (`docs/build_site.py`, `docs/dist`, path filter)
- [x] Mettre à jour `docs/README.md` (4 occurrences `site/` → `docs/`)
- [x] Reconstruire `python3 docs/build_site.py` (783 articles → `docs/dist/`)
- [x] Mettre à jour `.prompt-hub/memory.md`, `releases.md`, `version.md` (0.1.794)
- [ ] Commit + push

## Revue

- Renommage `site/` → `docs/` propre : rename stages pur (0 insertion), le style refresh
  non commité de `build_site.py` est resté en diff non stage sur `docs/build_site.py`.
- Le script est relatif à `__file__` → fonctionne sans changement dans `docs/`.
- Workflow mis à jour : `python3 docs/build_site.py`, `git add -f docs/dist`, path
  filter `docs/build_site.py`, commentaires.
- `docs/README.md` : `cd docs/` partout (util, cron, hook, option A).
- Aucune référence `site/` restante hors `.prompt-hub/`.
- Note : avec `docs/`, GitHub Pages pourrait servir `docs/` directement si activé
  (nécessiterait de déplacer la sortie du build à la racine de `docs/` — non fait).
