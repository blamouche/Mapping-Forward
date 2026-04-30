# Todo - daily-veille-maps-extraire-urls-de-gmail

## Objective
Exécuter la séquence quotidienne: Gmail `label:0---veille-mapping` -> extraction/filtrage d'URLs -> mise à jour de `LIST.md` -> corbeille des emails traités -> sync git.

## Checklist
- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Create this todo file
- [x] Inspect repo status and restore clean synced baseline if needed
- [x] Query Gmail label and extract candidate URLs
- [x] Update `LIST.md` with dedupe and scope filtering
- [x] Trash processed emails
- [x] Update prompt-hub tracking files
- [x] Commit and push

## Notes
- Scheduled cron run at 2026-04-30 04:04:44 CEST.
- Must follow `agents.md` agent `add-url` requirements and remove off-scope/local-small-initiative items.

## Review
- Gmail `label:0---veille-mapping` returned 1 Google Alert.
- 14 candidate URLs were unwrapped and reviewed manually.
- 0 URLs were kept because every result was off-scope for the cartography/domain news queue.
- `LIST.md` stayed unchanged and the processed email was moved to Trash.
- Prompt-hub tracking files were updated for commit/push.
