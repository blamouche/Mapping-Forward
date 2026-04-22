# Todo - daily-veille-maps-extraire-urls-de-gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Check repo status
- [x] Sync repo with `git pull --rebase`
- [x] Query Gmail label `0---veille-mapping`
- [x] Extract and filter article URLs
- [x] Review and update `LIST.md`
- [x] Trash processed emails
- [x] Update veille run tracking files
- [x] Commit and push changes

## Review

- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 100 --no-input` returned 1 current Google Alert.
- Extracted 10 candidate URLs from the alert and kept 3 in-scope mapping/geospatial URLs.
- Filtered out 7 off-scope results, mainly investor coverage, festival/community items, and incidental mentions.
- `LIST.md` was empty and now contains the 3 kept URLs.
- Added URLs: 3
- Removed URLs: 0
- Trashed emails: 1
