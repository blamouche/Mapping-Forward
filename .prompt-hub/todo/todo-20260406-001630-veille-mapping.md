# Todo — veille-mapping — 2026-04-06 00:16:30 CEST

## Objective
Exécuter la séquence quotidienne : Gmail label `0---veille-mapping` → extraction d’URLs → mise à jour/filtrage de `LIST.md` → corbeille Gmail → commit/push.

## Checklist
- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Inspect repo state and Gmail label
- [x] If repo dirty, commit/push all pending local changes to restore a clean state
- [x] Extract article URLs from Gmail messages in label `0---veille-mapping`
- [x] Normalize/dedupe and update `LIST.md`
- [x] Remove non-cartography / local-noise URLs from `LIST.md`
- [x] Trash processed emails
- [x] Update prompt-hub tracking (`memory`, `version`, `releases`)
- [x] Commit and push final changes
- [x] Add review section

## Notes
- Cron run autonome.
- Si le dépôt n’est pas clean, tout pousser d’abord pour repartir propre.

## Review
- Repo was dirty at start because a pending `scan-list` todo file was untracked; committed/pushed first to restore a clean baseline.
- Gmail label `0---veille-mapping`: 1 message processed.
- URLs extracted from Gmail: 1.
- URLs added to `LIST.md`: 1.
- URLs removed from `LIST.md`: 0 (the 5 existing entries were still in-scope for cartography/geospatial/maps coverage; no local initiative noise found).
- Processed emails moved to Trash: 1.
