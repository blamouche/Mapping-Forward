# Todo — daily veille maps extraire URLs de Gmail

## Objective
Exécuter la séquence quotidienne Gmail -> LIST.md -> nettoyage de scope -> corbeille -> résumé.

## Plan
- [x] Read repo rules and prompt-hub context.
- [x] Check git status and repo baseline.
- [x] Search Gmail label `0---veille-mapping` and extract candidate article URLs.
- [x] Normalize, dedupe, and merge relevant mapping/cartography URLs into `LIST.md`.
- [x] Review `LIST.md` and remove off-scope / small local initiative URLs.
- [x] Update prompt-hub tracking files.
- [x] Commit and push all resulting changes.
- [x] Trash processed Gmail messages.
- [x] Add review notes and final counts.

## Review
- Gmail label `0---veille-mapping` returned no messages (`--include-body --json`).
- `LIST.md` already contained 2 in-scope Bing Maps/TomTom URLs; both were kept.
- URLs added: 0.
- URLs removed: 0.
- Emails trashed: 0.

## Notes
- If the repo is dirty before LIST update, commit/push all pending local changes first to restore a clean synced state.
- Keep only URLs relevant to cartography, mapping data, GIS, navigation platforms, or domain news; exclude small local initiatives.
