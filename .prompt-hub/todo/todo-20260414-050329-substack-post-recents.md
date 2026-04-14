# Todo — substack-post-recents

- Created: 2026-04-14 05:03:29 CEST
- Agent: openclaw
- Scope: Run `/substack-post-recents` exactly as defined in `agents.md`.

## Objective
Create a new recent-articles Substack post from the 15 most recent articles listed in `README.md`, save it to `substack/YYYYMMDD-post-<slug>.md`, copy it to `substack/latest.md`, then commit and push with prompt-hub tracking updates.

## Plan
- [x] Read required prompt-hub context (`lessons.md`, `memory.md`, `releases.md`).
- [x] Create this task file before implementation.
- [x] Read the 15 most recent article synthesis files from `README.md`.
- [x] Draft a 1500-2000 word English article with sentence-case title, italic subtitle, narrative structure, and sources list.
- [x] Save the article to `substack/20260414-post-maps-are-starting-to-tell-you-what-to-do.md` and copy it to `substack/latest.md`.
- [x] Update prompt-hub tracking (`memory.md`, `version.md`, `releases.md`) and add a review section here.
- [ ] Commit and push with message `Add substack post: Maps are starting to tell you what to do`.

## Check-in
Proceeding autonomously as explicitly requested by the cron instruction.

## Review
- Status: ready to commit
- Output file: `substack/20260414-post-maps-are-starting-to-tell-you-what-to-do.md`
- Notes:
  - Article written in English with sentence-case title and italic subtitle.
  - Narrative structure follows the required Substack format with 15 numbered sources.
  - `substack/latest.md` synced to the new article.
