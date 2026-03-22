# Todo 20260322-070000 - veille-mapping

## Plan
- [ ] Sync repo (ensure clean state; if dirty, commit/push all changes)
- [ ] Pull Gmail messages with label 0---veille-mapping
- [ ] Extract URLs, filter to mapping-related (exclude small local initiatives), dedupe
- [ ] Update LIST.md (add mapping URLs, remove non-mapping URLs)
- [ ] Commit/push per add-url rules + update prompt-hub version/release
- [ ] Trash processed emails
- [ ] Log actions in .prompt-hub/memory.md and finalize review

## Check-in
User request explicitly instructs execution of daily sequence (cron). Proceeding.

## Progress
- [x] Start
- [x] Sync repo (clean + pull --rebase)
- [x] Extract Gmail URLs + filter
- [x] Update LIST.md (dedupe)
- [x] Commit/push
- [x] Trash processed emails

## Review
- Outcome: success
- URLs added: 10
- URLs removed: 0
- Emails trashed: 6
- Notes: Excluded non-mapping/local items from Gmail alerts; LIST.md already mapping-focused.
