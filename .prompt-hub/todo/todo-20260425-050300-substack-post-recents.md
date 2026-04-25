# Todo - substack-post-recents

## Context
- Timestamp: 2026-04-25 05:03:00 Europe/Paris
- Agent: substack-post-recents
- Objective: Create a new English Substack post from the 15 most recent articles listed in `README.md`, save it in `substack/`, copy it to `substack/latest.md`, then commit and push all required tracking updates.

## Plan
- [x] Read the 15 most recent article files referenced from `README.md`.
- [x] Identify the main narrative, title, subtitle, and source list.
- [x] Draft the new Substack post in `substack/YYYYMMDD-post-<slug>.md` and copy it to `substack/latest.md`.
- [x] Update `.prompt-hub/memory.md`, `.prompt-hub/version.md`, and `.prompt-hub/releases.md`.
- [x] Review changes, commit, and push.

## Review
- Created `substack/20260425-post-maps-are-becoming-workflow-infrastructure.md`.
- Copied the article to `substack/latest.md`.
- Confirmed the article body is within the 1500-2000 word target.
- Updated prompt-hub tracking files and prepared the repo for commit/push.
