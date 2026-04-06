# Todo - veille mapping

## Objective
Exécuter la séquence quotidienne Gmail label 0---veille-mapping -> LIST.md, filtrer les URLs hors périmètre, puis vider les emails traités.

## Checklist
- [x] Read .prompt-hub/lessons.md
- [x] Read .prompt-hub/memory.md
- [x] Read .prompt-hub/releases.md
- [x] Commit/push any pending local changes to restore a clean repo state
- [ ] Pull/rebase latest main
- [ ] Inspect Gmail label 0---veille-mapping and extract article URLs
- [ ] Update LIST.md with dedupe + scope filtering
- [ ] Trash processed emails
- [ ] Update prompt-hub memory/version/releases and review

## Notes
- Scheduled cron run at 2026-04-06 06:11 Europe/Paris.
- If repo is dirty, commit/push all pending local changes before add-url sync.
