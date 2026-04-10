# Todo — daily-veille-maps-extraire-urls-de-gmail

- [x] Read .prompt-hub/lessons.md
- [x] Read .prompt-hub/memory.md
- [x] Read .prompt-hub/releases.md
- [x] Clarify objective and constraints from cron payload
- [x] Restore a clean synced git state (only the new scheduled todo was pending; no baseline cleanup commit needed)
- [x] Search Gmail label `0---veille-mapping` and extract candidate article URLs
- [x] Filter to mapping/cartography/domain URLs only; remove off-scope URLs from `LIST.md`
- [x] Update tracking files (`memory.md`, `releases.md`, `version.md`, run summary)
- [x] Trash processed Gmail emails
- [ ] Commit and push final changes

## Notes
- Scheduled cron run at 2026-04-10 06:04 CEST.
- Must follow `agents.md` agent `add-url` sync/clean/dedupe/commit+push requirements.
- If repo is dirty, commit/push all pending local changes first to restore a clean baseline.

## Review
- Gmail label `0---veille-mapping` was empty (`gog gmail messages search --include-body --json`).
- `LIST.md` was already empty; no URLs were added or removed after scope review.
- No Gmail messages were trashed.
- Final step pending: commit/push tracking files.
