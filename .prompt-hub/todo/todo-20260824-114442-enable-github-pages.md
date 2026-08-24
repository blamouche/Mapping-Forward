# Task: Activer GitHub Pages pour le site

- **Date**: 2026-08-24 11:44 CEST
- **Statut**: in_progress

## Objectif

Publier le site sur GitHub Pages (`https://blamouche.github.io/Mapping-Forward/`)
via la GitHub Action existante.

## Décisions

- **Approche** : déploiement via GitHub Actions (`upload-pages-artifact` +
  `deploy-pages`) plutôt que déplacer `DIST_DIR` à la racine de `docs/`.
  Raisons : pas de mélange source/généré dans `docs/`, pas de modification de
  `build_site.py` (le style refresh non commité reste intact), `dist/` reste
  gitignoré localement.
- **Pages activé par API** : `POST /repos/blamouche/Mapping-Forward/pages`
  avec `build_type: workflow` (fait).

## Étapes

- [x] Activer Pages (build_type=workflow) via `gh api`
- [x] Mettre à jour `.github/workflows/build-site.yml` : perms `pages` + `id-token`,
      step de garde Paris séparé (output), steps upload/deploy Pages
- [x] Ajouter note Pages dans `docs/README.md`
- [x] Mettre à jour `.prompt-hub/memory.md`, `releases.md`, `version.md`
- [ ] Commit + push
- [ ] Déclencher `workflow_dispatch` et vérifier que le déploiement Pages réussit
- [ ] Vérifier https://blamouche.github.io/Mapping-Forward/

## Revue

_à remplir à la fin_
