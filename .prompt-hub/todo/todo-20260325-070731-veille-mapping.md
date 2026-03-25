# Task: Daily veille mapping (Gmail -> LIST.md)

## Objective
Exécuter la séquence quotidienne: Gmail label 0---veille-mapping -> extraire URLs -> filtrer cartographie -> mettre à jour LIST.md via agent add-url (sync propre, dedupe, commit+push) -> supprimer URLs non carto -> corbeille emails -> résumé.

## Plan
1. Vérifier état git du repo; si dirty, ajouter/commit/push toutes les modifs pour repartir propre.
2. Rechercher emails Gmail label:0---veille-mapping, extraire URLs d'articles, filtrer cartographie (exclure initiatives locales).
3. Mettre à jour LIST.md selon l'agent add-url (sync propre, dedupe, commit+push), retirer URLs hors carto.
4. Mettre à la corbeille les emails traités.
5. Mettre à jour version/release + mémoire prompt-hub et fournir résumé (URLs ajoutées/supprimées).

## Status
- [ ] Plan validé
- [ ] Exécution

## Review
- Outcome:
- URLs ajoutées:
- URLs supprimées:
- Emails traités:
- Notes:
