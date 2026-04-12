# Todo — Daily veille maps extraire urls de gmail

## Context
- Trigger: cron `e86a7434-db99-44fe-8c2c-6c13463de00f`
- Timestamp: 2026-04-12 08:04 CEST
- Objective: search Gmail label `0---veille-mapping`, extract article URLs, update `LIST.md` via add-url rules, remove off-scope URLs, trash processed emails, then report added/removed counts.

## Plan
- [x] Read prompt-hub lessons, memory, releases, and version.
- [x] Create this task file before execution.
- [x] Inspect repo state and restore a clean synced baseline if needed.
- [x] Query Gmail label and extract candidate URLs.
- [ ] Filter to cartography/GIS/mapping-domain URLs; update `LIST.md` with dedupe.
- [ ] Remove off-scope/local URLs from `LIST.md`.
- [ ] Trash processed emails.
- [x] Update prompt-hub tracking files, commit, and push.

## Review
- `git status --short --branch` showed `## main...origin/main` with only this scheduled todo pending before execution.
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 50` failed immediately with Gmail OAuth `invalid_grant` (`Token has been expired or revoked`).
- Because Gmail access failed, no URLs could be extracted, `LIST.md` was not modified, and no emails were moved to Trash.
- Prompt-hub tracking was updated to log the failed scheduled run; next step remains re-authenticating `gog` for Gmail, then rerunning the sequence.
