# Todo: veille-mapping (20260329-180836)

## Objective
Run daily Gmail veille mapping sequence: extract URLs, update LIST.md (dedupe/filter), sync repo, commit/push, and trash processed emails.

## Plan
1. Check repo status; if dirty, commit/push pending local changes to restore clean state.
2. Pull/rebase latest main.
3. Fetch Gmail label `0---veille-mapping`, extract URLs from messages, filter to mapping/cartography domain (exclude local initiatives), normalize and dedupe.
4. Update LIST.md with kept URLs; remove non-mapping URLs already in LIST.md.
5. Commit/push LIST.md + prompt-hub tracking updates if changes.
6. Trash processed Gmail messages.
7. Update prompt-hub memory/version/releases; finalize this todo with review notes.

## Check-in
Proceeding now per scheduled cron instruction.

## Checklist
- [ ] Repo clean or synced with commit/push
- [ ] Gmail label scanned and URLs extracted
- [ ] LIST.md updated (add/dedupe/remove non-mapping)
- [ ] Commit/push completed (if changes)
- [ ] Gmail messages trashed
- [ ] Prompt-hub tracking updated (memory/version/releases)
- [ ] Todo review completed

## Review
- Outcome: 
- URLs added: 
- URLs removed: 
- Emails trashed: 
- Notes: 
