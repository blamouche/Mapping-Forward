# Todo — daily veille maps extraire URLs de Gmail

## Objective
Exécuter la séquence quotidienne Gmail -> LIST.md -> nettoyage de scope -> corbeille -> résumé.

## Plan
- [x] Read repo rules and prompt-hub context.
- [x] Check git status and repo baseline.
- [ ] Search Gmail label `0---veille-mapping` and extract candidate article URLs.
- [ ] Normalize, dedupe, and merge relevant mapping/cartography URLs into `LIST.md`.
- [ ] Review `LIST.md` and remove off-scope / small local initiative URLs.
- [ ] Update prompt-hub tracking files.
- [ ] Commit and push all resulting changes.
- [ ] Trash processed Gmail messages.
- [ ] Add review notes and final counts.

## Notes
- If the repo is dirty before LIST update, commit/push all pending local changes first to restore a clean synced state.
- Keep only URLs relevant to cartography, mapping data, GIS, navigation platforms, or domain news; exclude small local initiatives.
