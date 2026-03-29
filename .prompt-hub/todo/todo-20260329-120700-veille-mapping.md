# Todo - Veille mapping (daily)

- [ ] Clarify scope and constraints from task
- [ ] Check repo status and sync
- [ ] Fetch Gmail label 0---veille-mapping
- [ ] Extract URLs and filter non-mapping/local items
- [ ] Update LIST.md (normalize, dedupe)
- [ ] Remove non-mapping URLs already in LIST.md
- [ ] Commit and push changes
- [ ] Trash processed emails
- [ ] Update prompt-hub memory/version/releases

## Plan
1. Ensure repo clean; if dirty, commit/push all changes to reset to clean state.
2. Pull latest from origin.
3. Fetch Gmail messages with label 0---veille-mapping.
4. Extract URLs, filter for mapping/cartography domain, exclude small local initiatives.
5. Append normalized URLs to LIST.md, dedupe and clean list.
6. Remove non-mapping URLs from LIST.md.
7. Commit/push per add-url agent rules.
8. Trash processed emails.
9. Log actions in .prompt-hub/memory.md and bump version/releases.

## Review
- [ ] Summary of actions
- [ ] URLs added/removed count
- [ ] Emails trashed count
- [ ] Follow-ups
