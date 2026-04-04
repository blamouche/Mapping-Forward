# Todo: Veille Mapping - 2026-04-04 16:04

## Plan
1. [x] Read lessons.md
2. [x] Read memory.md
3. [x] Read releases.md
4. [x] Create todo file
5. [ ] Sync repo (git pull --rebase)
6. [ ] Search Gmail label:0---veille-mapping
7. [ ] Extract URLs, filter, add to LIST.md
8. [ ] Filter non-mapping URLs from LIST.md
9. [ ] Commit + push
10. [ ] Trash processed emails

## Status: FAILED

## Reason
Gmail OAuth token expired/revoked (invalid_grant) for b.lamouche@gmail.com.
Error: `oauth2: "invalid_grant" "Token has been expired or revoked."`

This is a recurring issue (same on 2026-03-27, 2026-04-03 22h04).

## Next
User must re-auth: `gog auth add b.lamouche@gmail.com`
Then rerun the veille-mapping cron job.
