# TODO - Daily veille maps extraire urls de gmail

- [x] Lire `lessons.md`, `memory.md`, `releases.md`
- [x] Vérifier/synchroniser le repo pour repartir d'un état propre
- [x] Scanner Gmail label `0---veille-mapping`
- [x] Extraire, filtrer et dédupliquer les URLs cartographie/GIS/maps
- [x] Mettre à jour `LIST.md`
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour tracking prompt-hub (memory/version/releases)
- [ ] Commit + push

## Review
- Repo déjà propre (`git status --short --branch`: `main...origin/main`).
- Gmail `label:0---veille-mapping` vide avec `gog gmail messages search --include-body --json --max 100 --no-input`.
- `LIST.md` est resté vide, donc 0 URL ajoutée, 0 supprimée, 0 email envoyé à la corbeille.
