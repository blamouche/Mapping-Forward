# Todo — daily-veille-maps-extraire-urls-de-gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Check repo status and Gmail access
- [x] Attempt Gmail extraction for `label:0---veille-mapping`
- [x] Attempt quick browser fallback check
- [ ] Update `LIST.md` with new in-scope URLs
- [ ] Remove out-of-scope URLs from `LIST.md`
- [ ] Trash processed emails
- [ ] Commit and push any resulting changes

## Notes
- `gog gmail messages search 'label:0---veille-mapping' --include-body --json --max 50 --no-input` failed with `invalid_grant` (`Token has been expired or revoked`).
- Browser fallback check showed only the `openclaw` profile is available/running; `user` profile is not running, so no authenticated Gmail session was available to reuse.
- No Gmail messages were read, so no URLs could be extracted, no `LIST.md` update/review was possible, and no emails were trashed.

## Review
- Status: failed
- Outcome: blocked by Gmail OAuth failure before step (1) completed.
