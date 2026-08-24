# Task: GitHub Action — génération quotidienne du site

- **Date**: 2026-08-24 11:21 CEST
- **Statut**: in_progress

## Objectif

Créer une automatisation GitHub Actions qui génère le site statique
(`site/build_site.py` → `site/dist/`) une fois par jour à 9h, et publie le
résultat.

## Contexte

- Générateur : `site/build_site.py` (Python stdlib pur, aucune dépendance)
- Sortie : `site/dist/` (actuellement gitignoré)
- Repo : `https://github.com/blamouche/Mapping-Forward` — aucun `.github/` existant
- Hébergement actuel : `mappingforward.fr` (déploiement manuel rsync/scp)

## Étapes

- [x] Créer `.github/workflows/build-site.yml`
- [x] Décider de la cible de déploiement — **commit `site/dist/` dans le repo** (choix utilisateur)
- [x] Décider de l'interprétation de « 9h » — **9h heure de Paris** (dual cron 07:00/08:00 UTC + garde TZ)
- [x] Tester le workflow localement — build validé (783 articles), YAML validé
- [x] Mettre à jour `.prompt-hub/memory.md`, `releases.md`, `version.md` (0.1.793)
- [x] Commit + push

## Revue

- **Workflow créé** : `.github/workflows/build-site.yml`
  - `schedule` : `0 7 * * *` + `0 8 * * *` (UTC), avec une étape de garde qui ne lance le
    build que si l'heure de Paris est 09 — → exactement une fois par jour à 9h Paris.
  - `push` : branches `main`, paths `src/**` et `site/build_site.py` (pas de boucle : le
    commit du bot ne touche que `site/dist/**`).
  - `workflow_dispatch` : relance manuelle.
  - Le build (`python3 site/build_site.py`) puis commit `git add -f site/dist` + push.
  - `permissions: contents: write` (nécessaire pour le push du token GITHUB_TOKEN).
- **Décision** : `site/dist/` reste gitignoré localement (working copy propre) ; le workflow
  le commit via `git add -f`. Déploiement mappingforward.fr inchangé (rsync manuel).
- **Point d'attention** : le commit initial de `dist` sera fait par la 1ère exécution CI.
  Recommandation : committer d'abord le style refresh en cours (`site/build_site.py`) pour
  que CI génère dist avec le générateur à jour.
- **Limite connue** : autour des transitions d'heure d'été, la garde TZ absorbe le double
  déclenchement (run no-op vert).
