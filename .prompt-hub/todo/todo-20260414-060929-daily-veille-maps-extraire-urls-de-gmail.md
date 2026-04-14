# Todo — Daily veille Maps extraire URLs de Gmail

- [x] Read .prompt-hub/lessons.md
- [x] Read .prompt-hub/memory.md
- [x] Read .prompt-hub/releases.md
- [x] Inspect repo status and restore a clean synced state if needed
- [x] Search Gmail label `0---veille-mapping` and extract article URLs
- [x] Update `LIST.md` with normalized/deduped in-scope mapping URLs
- [x] Remove off-scope/local URLs from `LIST.md`
- [x] Trash processed Gmail messages
- [x] Update prompt-hub tracking files
- [x] Commit and push all required changes

## Review
- Repo had pending local changes; committed and pushed them first to satisfy the clean-sync prerequisite.
- Gmail label `0---veille-mapping` returned 0 messages, so no new URLs were extracted.
- `LIST.md` stayed empty after scope review; 0 URLs added, 0 removed, 0 emails trashed.
- Prompt-hub tracking files updated for the empty run.
