# Todo - daily veille maps extraire urls de gmail

- [x] Read prompt-hub lessons, memory, and releases
- [x] Inspect repo status and restore a clean synced baseline if needed
- [x] Query Gmail label `0---veille-mapping` and extract candidate article URLs
- [x] Filter to in-scope cartography/mapping/domain news URLs
- [x] Update `LIST.md` with normalized deduped URLs
- [x] Trash processed emails
- [x] Update prompt-hub tracking, commit, and push

## Review
- Repo cleaned via baseline tracking commit, then `git pull --rebase origin main` confirmed it was up to date.
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` returned no messages.
- `LIST.md` stayed empty after scope review, so 0 URL added and 0 removed.
- No emails needed to be trashed.
