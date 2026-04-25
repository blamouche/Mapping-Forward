# Todo - daily veille maps extraire urls de gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Create this todo file before starting work
- [x] Restore a clean synced repo state
- [x] Query Gmail label `0---veille-mapping` and extract candidate article URLs
- [x] Update `LIST.md` with normalized, deduped, in-scope URLs only
- [x] Trash processed emails
- [x] Update prompt-hub tracking, commit, and push

## Review
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` returned 0 messages.
- `LIST.md` was already empty and stayed in scope after review.
- No URLs were added, no URLs were removed, and no emails were trashed.
- Repo tracking files were updated for the scheduled empty run.
