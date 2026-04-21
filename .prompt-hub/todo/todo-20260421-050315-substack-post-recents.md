# Todo - substack-post-recents

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Confirm current version from `.prompt-hub/version.md`
- [x] Sync repo state (`git fetch` / `git pull --rebase` if needed)
- [x] Gather the 15 most recent article files from `README.md`
- [x] Read the corpus and draft the Substack post
- [x] Save the post to `substack/YYYYMMDD-post-<slug>.md`
- [x] Copy the post to `substack/latest.md`
- [x] Update prompt-hub tracking (`memory`, `version`, `releases`)
- [ ] Commit and push

## Notes
- Trigger: cron `Substack recents (Mapping-Forward)`
- Must follow `agents.md` section `substack-post-recents` exactly.

## Review
- Selected the first 15 article links listed under `README.md` > `## Articles`.
- Wrote a 1,998-word English post titled `Maps are becoming systems of governance`.
- Saved the canonical post to `substack/20260421-post-maps-are-becoming-systems-of-governance.md` and mirrored it to `substack/latest.md`.
- Prompt-hub tracking updated; commit/push still pending at this point.
