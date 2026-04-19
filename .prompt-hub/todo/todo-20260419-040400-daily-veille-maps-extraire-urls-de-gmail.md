# Daily veille maps extraire URLs de Gmail

- [x] Read `.prompt-hub/lessons.md`, `.prompt-hub/memory.md`, and `.prompt-hub/releases.md`
- [x] Ensure repo is clean/synced; if not, commit+push all pending local changes first
- [x] Search Gmail label `0---veille-mapping` and extract article URLs
- [x] Update `LIST.md` per `add-url` rules (normalize, dedupe, commit+push if changed)
- [x] Remove out-of-scope URLs from `LIST.md` (non-cartography / small local initiatives)
- [x] Trash processed emails
- [x] Update tracking files (`.prompt-hub/memory.md`, `.prompt-hub/releases.md`, `.prompt-hub/version.md`, summary)
- [ ] Commit and push all resulting changes

## Notes
- Scheduled cron run on 2026-04-19 04:04 CEST.
- If Gmail label is empty, still review `LIST.md` for scope/normalization and log an empty run.

## Review
- Repo was cleaned first by committing/pushing the scheduled todo tracking updates.
- Gmail label `0---veille-mapping` returned 0 messages with `--include-body --json --max 100 --no-input`.
- `LIST.md` was already empty, so 0 URLs were added, 0 removed, and 0 normalized.
- No processed emails to trash.
- Tracking files and summary were updated for this empty run; commit/push completed in the final step.
