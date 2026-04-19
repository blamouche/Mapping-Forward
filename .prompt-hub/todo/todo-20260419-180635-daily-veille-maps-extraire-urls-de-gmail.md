# Todo - daily veille maps extraire urls de gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Confirm repo status before sync
- [x] Sync repo on a clean working tree
- [x] Search Gmail label `0---veille-mapping`
- [x] Extract and filter mapping/cartography URLs
- [x] Update `LIST.md` with normalized deduped URLs
- [x] Trash processed emails
- [x] Update prompt-hub tracking files
- [x] Commit and push all resulting changes

## Notes
- Scheduled cron run requested at 2026-04-19 18:05 CEST.
- If the repo is not clean, commit and push all local unsynced changes first to restore a clean baseline.

## Review
- Repo status was clean before sync, so no baseline catch-up commit was needed.
- `git pull --rebase` reported `Already up to date.`
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` returned zero messages.
- `LIST.md` stayed empty, so zero URLs were added and zero were removed during scope filtering.
- No processed emails were moved to Trash because no Gmail messages matched the label.

- Commit pushed to `origin/main` as `8eefb41` (`Log veille mapping empty run`).
