# Todo

- [x] Restore repo instructions and context
- [x] Gather Gmail emails for label 0---veille-mapping
- [ ] Extract article URLs and classify mapping-related ones
- [ ] Clean repo state, sync, update LIST.md with dedupe
- [ ] Remove non-mapping / too-local URLs from LIST.md
- [ ] Trash processed emails
- [x] Commit, push, and summarize

## Review

- `gog gmail messages search 'label:0---veille-mapping' --max 100 --json --no-input` failed with Gmail OAuth `invalid_grant` (`Token has been expired or revoked`).
- Browser fallback was checked immediately after: only the `openclaw` profile was running; the authenticated `user` profile was unavailable, so Gmail could not be accessed through the browser either.
- Because the inbox could not be read, no article URLs were extracted, `LIST.md` was left unchanged, and no emails were moved to Trash.
- Repo state was already clean (`git status --short --branch` returned `## main...origin/main`) before tracking this failed run.
