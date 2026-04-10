# Todo - daily veille maps extraire urls de gmail

## Objective
Run the scheduled Gmail -> LIST.md mapping veille sequence.

## Plan
- [x] Verify repo sync/clean state and restore clean baseline if needed
- [x] Scan Gmail label `0---veille-mapping` and extract article URLs
- [x] Update `LIST.md` with dedupe + scope filtering
- [x] Trash processed Gmail messages
- [x] Update prompt-hub tracking files and push changes

## Review
- Repo already clean and synced with origin/main.
- Gmail label returned no messages, including with body extraction enabled.
- LIST.md was empty and stayed empty after scope review.
- No Gmail messages were moved to Trash.
