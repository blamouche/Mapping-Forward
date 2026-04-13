# Todo — daily veille maps extraire urls de gmail

## Context
- Timestamp: 2026-04-13 22:04:38 Europe/Paris
- Trigger: cron daily veille Maps
- Goal: scan Gmail label `0---veille-mapping`, extract in-scope cartography URLs, sync `LIST.md`, remove off-scope/local items, trash processed emails, and report counts.

## Checklist
- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Check repo status / sync prerequisites
- [x] Query Gmail label `0---veille-mapping`
- [x] Review `LIST.md` scope
- [x] Update tracking files
- [x] Review outcome

## Review
- `gog gmail messages search "label:0---veille-mapping" --max 100 --json --no-input` returned no messages.
- Repo was already clean and synced on `main...origin/main`; no baseline cleanup commit was needed.
- `LIST.md` was empty, so no URLs were added or removed.
- No emails were trashed because nothing matched the label at run time.
- Outcome: empty successful run.
