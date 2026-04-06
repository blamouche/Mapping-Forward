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
- Gmail query returned no labeled messages at run start.
- Need to review existing LIST.md entries and remove off-scope links.

## Review
- Completed: Gmail label empty, LIST.md filtered from 12 to 8 URLs, no emails trashed.

## Outcome
- Added URLs from Gmail: 0
- Removed URLs from LIST.md: 4
- Emails trashed: 0
