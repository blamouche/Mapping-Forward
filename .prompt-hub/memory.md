# Memory Log

- 2026-03-08 21:43:49 CET | agent | Added 23 mapping-related URLs from Gmail label 0---veille-mapping to LIST.md (filtered non-mapping/local items). | Files: LIST.md | Status: success | Next: none
- 2026-03-09 07:02:00 CET | agent | Scanned Gmail label 0---veille-mapping; no mapping-relevant URLs found; LIST.md unchanged. | Files: none | Status: success | Next: none
- 2026-03-10 07:08:09 | agent: openclaw | action: added mapping-related URLs from Gmail veille; updated LIST.md; commands: gog gmail search/get, git pull --rebase | files: LIST.md | status: success | next: none
- 2026-03-11 07:05 CET | agent | Extracted mapping-related URLs from Gmail label 0---veille-mapping; added 5 URLs to LIST.md (deduped). | Files: LIST.md | Status: success | Next: none
- 2026-03-12 07:05 CET | agent | Extracted mapping-related URLs from Gmail label 0---veille-mapping; added 7 URLs; removed 1 non-mapping URL from LIST.md; deduped. | Files: LIST.md | Status: success | Next: none

## 2026-03-13 17:23
- actor: claude-code
- action: scan-list — processed 54 URLs from LIST.md; 37 synthesis files created (36 in src/2026-03/, 1 in src/2026-02/); 17 FETCH_ERRORs (MSN JS-only, paywalled/blocked sites); LIST.md emptied; batch recap created at synthesis/2026-03-13 - 172316 - batch recap.md; README.md updated (March: 51 articles, Feb: 34); all committed and pushed.
- files: src/2026-03/*.md, src/2026-02/*.md, README.md, LIST.md, synthesis/2026-03-13 - 172316 - batch recap.md
- commands: article-synthesis × 54, git commit × 38+
- status: success
- next: /monthly-synthesis 2026-03 when month is complete; /newsletter-maps-agent 2026-03 for maps newsletter

## 2026-03-13 07:05
- actor: openclaw
- action: Extracted URLs from Gmail veille-mapping alerts, filtered non-mapping/local items, and updated LIST.md (added 16 URLs, removed 2 local items).
- files: LIST.md
- commands: gog gmail messages search --include-body; git diff
- status: success
- next: None
