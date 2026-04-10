# Todo — daily veille maps extraire urls de gmail

- [x] Read .prompt-hub/lessons.md
- [x] Read .prompt-hub/memory.md
- [x] Read .prompt-hub/releases.md
- [x] Check repo status and existing LIST.md state
- [x] Create clean baseline if repo is dirty, then sync
- [x] Search Gmail label `0---veille-mapping` and extract article URLs
- [x] Filter mapping/cartography/geospatial candidates and dedupe into `LIST.md`
- [x] Remove off-scope URLs from `LIST.md` (non-cartography, local small initiatives)
- [x] Trash processed Gmail messages
- [x] Update prompt-hub tracking (`memory.md`, `version.md`, `releases.md`, run summary)
- [x] Commit/push final changes

## Review
- Run time: 2026-04-10 18:11 CEST
- Repo state before URL addition: clean and synced after baseline commit/push.
- Gmail result: 1 message returned for label `0---veille-mapping`.
- Extracted 4 candidate URLs from the Google Alert.
- Kept 2 URLs relevant to cartography/geospatial platform updates:
  - https://www.01net.com/actualites/bing-maps-microsoft-allie-tomtom-rattraper-google-maps.html
  - https://www.generation-nt.com/actualites/bing-maps-tomtom-orbis-microsoft-copilot-donnees-2073589
- Filtered 2 off-scope URLs:
  - GeekWire executive-moves article (Overture Maps only mentioned in passing)
  - AirGuide supersonic-travel article (not about cartography despite the word “Overture”)
- `LIST.md` result: 2 URLs added, 0 URLs removed during whole-list cleanup.
- Emails trashed: 1
- Outcome: successful watchlist update, ready for downstream scan-list processing.
