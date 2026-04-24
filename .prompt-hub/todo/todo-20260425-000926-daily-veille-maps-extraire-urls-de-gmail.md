# Todo - daily veille maps extraire urls de gmail

## Objective
Exécuter la séquence quotidienne Gmail -> LIST.md pour la veille mapping, en respectant les consignes `agents.md` et `add-url`.

## Checklist
- [x] Lire `.prompt-hub/lessons.md`
- [x] Lire `.prompt-hub/memory.md`
- [x] Lire `.prompt-hub/releases.md`
- [x] Vérifier la version courante `.prompt-hub/version.md`
- [x] Créer ce fichier de tâche
- [x] Vérifier l’état git et rétablir un repo propre/synchronisé si nécessaire
- [x] Chercher les emails Gmail `label:0---veille-mapping`
- [x] Extraire et normaliser les URLs candidates
- [x] Filtrer les URLs hors sujet / petites initiatives locales
- [x] Mettre à jour `LIST.md` avec déduplication et nettoyage
- [x] Committer et pousser toutes les modifications nécessaires
- [x] Mettre à la corbeille les emails traités
- [x] Compléter la review

## Notes
- Timestamp de tâche: 20260425-000926
- Repo: `/Users/openclaw/github/Mapping-Forward`
- Hypothèse: si le repo n’est pas clean, je commit/push d’abord les changements locaux non synchronisés pour repartir d’un état propre, puis j’exécute l’ajout d’URLs.

## Review
- Statut: terminé
- Résultat: 3 emails Google Alerts traités, 18 URLs candidates extraites, 5 URLs retenues et ajoutées à `LIST.md`, 0 URL supprimée de la file existante, 3 emails mis à la corbeille.
- URLs retenues:
  - https://www.letemsvetemapplem.eu/fr/2026/04/24/mapy-com-pridavaji-zasadni-novinku-tohle-vam-zmeni-planovani-vyletu
  - https://android-mt.ouest-france.fr/news/apple-maps-une-experience-f1-immersive-pour-le-grand-prix-de-miami/199991
  - https://global.techradar.com/fr-fr/computing/software/apple-maps-lance-trop-tot-siri-a-la-traine-tim-cook-admet-enfin-lerreur-qui-continue-de-hanter-apple
  - https://www.mapbox.com/location-ai/build
  - https://www.tomtom.com/customers/atkinsrealis-and-tomtom
- Filtrage hors sujet appliqué: YouTube, météo, crypto, carte carburants locale, événements/festival “Tom Tom”, faits divers, et bruit hors cartographie.
