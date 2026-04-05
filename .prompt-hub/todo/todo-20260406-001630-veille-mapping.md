# Todo — veille-mapping — 2026-04-06 00:16:30 CEST

## Objective
Exécuter la séquence quotidienne : Gmail label `0---veille-mapping` → extraction d’URLs → mise à jour/filtrage de `LIST.md` → corbeille Gmail → commit/push.

## Checklist
- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Inspect repo state and Gmail label
- [ ] If repo dirty, commit/push all pending local changes to restore a clean state
- [ ] Extract article URLs from Gmail messages in label `0---veille-mapping`
- [ ] Normalize/dedupe and update `LIST.md`
- [ ] Remove non-cartography / local-noise URLs from `LIST.md`
- [ ] Trash processed emails
- [ ] Update prompt-hub tracking (`memory`, `version`, `releases`)
- [ ] Commit and push final changes
- [ ] Add review section

## Notes
- Cron run autonome.
- Si le dépôt n’est pas clean, tout pousser d’abord pour repartir propre.
