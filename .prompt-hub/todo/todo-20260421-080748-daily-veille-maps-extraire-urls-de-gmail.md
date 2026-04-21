# Todo - daily veille maps extraire urls de gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Check repo status and current branch
- [x] Commit/push any pending local changes to restore a clean synced state if needed
- [x] Pull latest changes on current branch
- [x] Query Gmail label `0---veille-mapping` and extract article URLs
- [x] Normalize, scope-filter, dedupe, and update `LIST.md`
- [x] Trash processed emails
- [x] Update prompt-hub tracking, review, and final summary

## Notes
- Scheduled cron run at 2026-04-21 08:07 CEST.
- Must exclude small local initiatives and non-cartography domain items.

## Review
- Repo tracking changes were committed and pushed first to restore a clean synced baseline.
- `git pull --rebase` reported `Already up to date.`
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` returned no messages.
- `LIST.md` stayed empty after scope review, so 0 URLs were added and 0 removed.
- No emails were moved to Trash because none matched the label.
