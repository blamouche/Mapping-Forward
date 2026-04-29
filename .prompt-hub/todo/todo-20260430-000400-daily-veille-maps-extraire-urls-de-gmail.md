# Todo - daily veille maps extraire urls de gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Ensure repo is clean and synced
- [x] Fetch Gmail messages for `label:0---veille-mapping`
- [x] Extract candidate article URLs
- [x] Update `LIST.md` with normalized, deduplicated, in-scope URLs only
- [x] Trash processed emails
- [x] Update `.prompt-hub/memory.md`
- [x] Update `.prompt-hub/version.md`
- [x] Update `.prompt-hub/releases.md`
- [x] Commit and push

## Review

- Repo was restored to a clean synced state with the baseline tracking commit before Gmail extraction.
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` returned no messages.
- `LIST.md` remained empty after scope review, so 0 URLs were added and 0 removed.
- No emails were moved to trash because none were available to process.
