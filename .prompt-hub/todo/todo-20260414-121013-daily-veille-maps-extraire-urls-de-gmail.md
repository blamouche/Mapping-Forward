# Todo - daily veille maps extraire urls de gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Restore a clean synced repo state (commit/push pending local changes if needed)
- [x] Search Gmail label `0---veille-mapping` and extract article URLs
- [x] Update `LIST.md` with normalized/deduped in-scope URLs and remove off-scope URLs
- [x] Trash processed Gmail messages
- [x] Update prompt-hub tracking (`memory`, `releases`, `version`, todo review)
- [ ] Commit and push final changes

## Review
- Repo state: clean except for the new scheduled todo/tracking files; no baseline cleanup commit was needed before the Gmail check.
- Gmail result: `label:0---veille-mapping` returned no messages with `--include-body --json --max 20 --no-input`.
- LIST.md result: file stayed empty after scope review; no URLs added or removed.
- Email cleanup: no processed emails to trash.
