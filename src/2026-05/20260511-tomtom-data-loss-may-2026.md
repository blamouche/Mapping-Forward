# TomTom: Plötzlich alle Daten seit 5. Mai 2026 weg — Restore am Laufen
**Source**: https://borncity.com/blog/2026/05/11/tomtom-ploetzlich-alle-daten-seit-5-mai-2026-weg-restore-am-laufen/
**Date**: May 11, 2026
**Author**: Günter Born
**Keywords**: TomTom, data loss, cloud outage, saved places, favorites, restore, platform migration, navigation

## Elevator pitch
TomTom suffered a major cloud outage starting May 5, 2026, that wiped saved places, favorites, and recent destinations for users across all platforms; data restoration began rolling out by May 10 after the company acknowledged the issue.

## Takeaways
- The outage began May 5, 2026, affecting saved places, home/work addresses, and favorites — new entries were also immediately deleted
- The issue affected all platforms (iOS, Android, web) and was unrelated to operating system
- Users suspected an unannounced platform migration of "plan.tomtom.com" caused the data loss
- TomTom officially acknowledged the problem on May 9 via a help article titled "Temporary loss of saved places and favourites"
- Most users reported data restoration by May 10-11, though the restore process was still ongoing for some

## Synthesis
A significant cloud infrastructure incident at TomTom has highlighted the risks of centralized cloud data storage for navigation services. Starting May 5, 2026, users across all platforms — the TomTom GO app, dedicated navigation devices, and the plan.tomtom.com web interface — found their saved places (My Places), favorites, and recent destinations completely erased. Attempts to re-add locations, including home and work addresses, resulted in the entries being immediately wiped again after logging out and back in.

The incident generated a five-page thread on the German TomTom forum, with users reporting the issue consistently from May 5 onward. The scale suggests a backend platform failure rather than a client-side bug: one user noted that upon being able to log back in, they received a message indicating that "everything is new," leading to speculation that TomTom had migrated or reset its "plan.tomtom.com" platform without properly migrating user data. Interestingly, saved routes were reportedly unaffected on some accounts, suggesting the outage was specific to the places/favorites database rather than a complete infrastructure failure.

TomTom's response timeline reveals a concerning gap. The company did not publicly acknowledge the problem until May 9 — four days after it began — when it published a help article titled "Temporary loss of saved places and favourites." The article confirmed that "some customers recently lost access to their saved places (My Places), favourites, and recent destinations" but characterized it as temporary. By May 10, the first users began reporting that their data had been restored, though the rollout appeared staggered.

The incident raises questions about TomTom's cloud architecture, disaster recovery procedures, and customer communication practices. For a company positioning itself as a provider of mission-critical navigation data to automakers and enterprises, a four-day data access outage — with a multi-day gap before public acknowledgment — represents a significant trust issue. It also serves as a reminder that even established navigation platforms remain vulnerable to cloud infrastructure failures with limited user recourse.
