# Todo - veille mapping

## Objective
Exécuter la séquence quotidienne Gmail label 0---veille-mapping -> LIST.md, filtrer les URLs hors périmètre, puis vider les emails traités.

## Checklist
- [x] Read .prompt-hub/lessons.md
- [x] Read .prompt-hub/memory.md
- [x] Read .prompt-hub/releases.md
- [x] Commit/push any pending local changes to restore a clean repo state
- [x] Pull/rebase latest main
- [x] Inspect Gmail label 0---veille-mapping and extract article URLs
- [x] Update LIST.md with dedupe + scope filtering
- [x] Trash processed emails
- [x] Update prompt-hub memory/version/releases and review

## Notes
- Scheduled cron run at 2026-04-06 06:11 Europe/Paris.
- Repo was made clean first via tracking commit/push, then `git pull --rebase`.
- Gmail query `label:0---veille-mapping` returned no messages.
- LIST.md was already empty after the 06:01 scan-list run, so no scope cleanup was needed.

## Review
- Completed: repo synced, Gmail label empty, LIST.md already empty, no emails trashed.

## Outcome
- Added URLs from Gmail: 0
- Removed URLs from LIST.md: 0
- Emails trashed: 0
