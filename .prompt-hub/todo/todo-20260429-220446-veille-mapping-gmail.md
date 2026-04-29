# Todo - veille mapping gmail

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

- Gmail label `0---veille-mapping` returned no messages with `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input`.
- Cross-check on threads with `gog gmail search 'label:0---veille-mapping' --json --max 20 --no-input` also returned no results.
- `LIST.md` remained empty after scope review, so 0 URLs were added and 0 removed.
- No emails were moved to trash because none were available to process.
