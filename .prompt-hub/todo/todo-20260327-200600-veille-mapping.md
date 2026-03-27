# Todo - 2026-03-27 20:06 CET - veille-mapping

## Objective
Exécuter la veille Gmail -> LIST.md puis nettoyage et clôture.

## Plan
- [ ] Vérifier repo propre / synchroniser si nécessaire.
- [ ] Extraire emails label:0---veille-mapping.
- [ ] Extraire/filtrer URLs (cartographie uniquement, exclure petites initiatives locales).
- [ ] Mettre à jour LIST.md (dedupe) via add-url rules.
- [ ] Supprimer URLs non carto de LIST.md.
- [ ] Mettre à la corbeille les emails traités.
- [ ] Mettre à jour prompt-hub (memory, version, releases) puis commit/push.

## Notes
- Agent: add-url (sync propre, dedupe, commit+push).
- Si repo pas clean: committer/pusher tout le local d'abord.

## Review
- [ ] Résumé + stats URLs ajoutées/supprimées.
