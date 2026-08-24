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
- [x] Mettre à jour `.prompt-hub/memory.md`, `releases.md`, `version.md` (0.1.795)
- [x] Commit + push (a19fa72, rebase sur le commit bot `0e67c75`)
- [x] Déclencher `workflow_dispatch` et vérifier que le déploiement Pages réussit
- [x] Vérifier https://blamouche.github.io/Mapping-Forward/

## Revue

- **Pages activé** par API : `build_type: workflow` → https://blamouche.github.io/Mapping-Forward/
- **Workflow** : perms `pages: write` + `id-token: write`, garde Paris séparée en
  step avec output, steps `upload-pages-artifact` (docs/dist) + `deploy-pages`.
- **Run de validation** (workflow_dispatch 32713332955) : **success**, site vérifié :
  index 200, archives 200, feed.xml 200, page article 200.
- **Constat** : le push du move (`docs/build_site.py` rename) a déclenché le workflow
  qui a commité `docs/dist` (0e67c75). Mon commit Pages a été rebasé dessus.
- **⚠️ Style** : le site Pages affiche pour l'instant l'ANCIEN style — le workflow
  build avec `docs/build_site.py` commité (sans le style refresh non commité).
  Une fois le style refresh commité, le push sur `docs/build_site.py` re-déclenchera
  build + redéploiement automatique.
- **État local** : `main` local est 1 commit derrière `origin/main` (le commit bot
  `d026307`) — un `git pull` le récupérera (les fichiers `docs/dist` deviennent
  trackés, écrasant le `dist` local gitignoré).
