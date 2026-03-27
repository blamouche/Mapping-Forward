# Todo - 2026-03-27 20:06 CET - veille-mapping

## Objective
Exécuter la veille Gmail -> LIST.md puis nettoyage et clôture.

## Plan
- [x] Vérifier repo propre / synchroniser si nécessaire.
- [x] Extraire emails label:0---veille-mapping.
- [x] Extraire/filtrer URLs (cartographie uniquement, exclure petites initiatives locales).
- [x] Mettre à jour LIST.md (dedupe) via add-url rules.
- [x] Supprimer URLs non carto de LIST.md.
- [x] Mettre à la corbeille les emails traités.
- [ ] Mettre à jour prompt-hub (memory, version, releases) puis commit/push.

## Notes
- Agent: add-url (sync propre, dedupe, commit+push).
- Si repo pas clean: committer/pusher tout le local d'abord.

## Review
- [x] Résumé + stats URLs ajoutées/supprimées.

### Summary
- Gmail label 0---veille-mapping: 0 message.
- LIST.md: removed 1 non-mapping/local URL; 0 added.
- Emails trashed: 0.
