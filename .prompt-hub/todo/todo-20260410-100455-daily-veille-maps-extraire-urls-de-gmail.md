# Todo - daily veille maps extraire urls de gmail

## Objective
Exécuter la séquence quotidienne Gmail -> LIST.md -> nettoyage de scope -> corbeille, puis commit/push en respectant `agents.md`.

## Checklist
- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Create this todo file
- [x] Check repo status and restore a clean synced state if needed
- [x] Search Gmail label `0---veille-mapping`
- [x] Extract and filter article URLs
- [x] Update `LIST.md` (dedupe + scope cleanup)
- [x] Trash processed emails
- [x] Update prompt-hub tracking (`memory`, `releases`, `version`, run summary)
- [x] Commit and push all changes

## Notes
- Triggered by cron on 2026-04-10 10:04 Europe/Paris.
- If the repo is dirty, commit/push all pending local changes first to restore a clean state before touching `LIST.md`.

## Review
- Repo was already clean; no baseline sync commit was needed.
- Gmail label `0---veille-mapping` returned 0 messages with `--include-body --json`.
- `LIST.md` stayed empty after scope review, so 0 URLs were added and 0 removed.
- No emails were moved to Trash.
- Tracking files were updated and will be committed/pushed in this run.
