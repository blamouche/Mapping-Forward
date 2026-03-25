# Todo: veille mapping (2026-03-25 14:06)

## Objective
Exécuter la séquence quotidienne Gmail → extraction d’URLs → LIST.md (avec nettoyage/dédoublonnage) → filtrage non-mapping → git sync/commit/push → trash des emails traités.

## Constraints
- Suivre /Users/openclaw/github/Mapping-Forward/agents.md (plan + check-in avant exécution).
- Respecter l’agent add-url (sync propre, dédup, commit+push).
- Si repo pas clean, commit/push toutes modifs locales avant d’ajouter les nouvelles URLs.

## Plan
1. Vérifier l’état git et synchroniser (commit/push si dirty, puis pull --rebase).
2. Rechercher emails Gmail label:0---veille-mapping (messages, incl. body) et extraire URLs.
3. Filtrer: conserver uniquement cartographie/données carto/actualités du domaine carto; exclure initiatives locales.
4. Mettre à jour LIST.md (nettoyage, dedupe, suppression URLs non-mapping) + vérifs.
5. Commit/push + mise à jour prompt-hub (version + releases + memory log).
6. Mettre à la corbeille les emails traités.

## Checklist
- [ ] Git clean/sync OK
- [ ] URLs extraites et filtrées
- [ ] LIST.md mis à jour + dedupe
- [ ] Commit/push faits + version/release bump
- [ ] Emails traités déplacés à la corbeille

## Review
- Summary:
- URLs added:
- URLs removed:
- Emails trashed:
