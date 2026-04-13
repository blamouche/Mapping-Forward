
## 2026-03-14 07:05 CET
- actor: openclaw
- action: Extracted mapping-related URLs from Gmail veille-mapping alerts, filtered out non-mapping/local items, and updated LIST.md (added 13 URLs).
- files: LIST.md
- commands: gog gmail messages search/get; git pull --rebase; git commit; git push
- status: success
- next: None

## 2026-04-06 06:01 CET
- actor: openclaw
- action: scan-list processed 8 URLs from LIST.md; created 7 synthesis files, recorded 1 FETCH_ERROR (Nature readability returned references only), updated README stats/April list, emptied LIST.md, and created synthesis/2026-04-06 - 060142 - batch recap.md.
- files: LIST.md, README.md, src/2026-04/*.md, synthesis/2026-04-06 - 060142 - batch recap.md
- commands: git pull --rebase; git commit per article; git push
- status: success
- next: none

## 2026-04-13 18:01 CEST
- actor: openclaw
- action: scan-list run checked `LIST.md` after `git pull --rebase`; the queue was empty, so no URLs were processed and no batch recap was created.
- files: LIST.md, .prompt-hub/todo/todo-20260413-180100-scan-list.md, .prompt-hub/memory.md, .prompt-hub/releases.md, .prompt-hub/version.md
- commands: git pull --rebase
- status: success
- next: commit and push tracking updates
