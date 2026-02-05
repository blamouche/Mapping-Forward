# Mapbox Brings Doorway-Level Accuracy to Delivery, Logistics, and Ride-Hailing
**Source**: https://www.prnewswire.com/news-releases/mapbox-brings-doorway-level-accuracy-to-delivery-logistics-and-ride-hailing-302677662.html
**Date**: February 4, 2026
**Author**: Mapbox (PR Newswire)
**Keywords**: Mapbox, geocoding, last-mile delivery, logistics, navigation, entrance data, ride-hailing

## Elevator pitch
Mapbox lance des données d'entrée au niveau de la porte permettant de guider les livreurs à moins de 5 mètres de la bonne entrée pour plus de 100 millions d'adresses américaines, réduisant les échecs de livraison du "dernier mètre".

## Takeaways
- Mapbox lance en preview publique des données de localisation précise des entrées de bâtiments
- Couvre plus de 100 millions d'adresses aux États-Unis avec une précision de 5 mètres ou moins
- 70% des échecs de livraison dans les 100 derniers mètres surviennent dans les 10 derniers mètres
- Les erreurs de localisation peuvent représenter jusqu'à 19% des coûts logistiques (support, temps d'attente, colis perdus)
- Le client dlivrd rapporte 7% de réduction des temps de livraison et 25% de résolution plus rapide des tickets support

## Synthesis
Mapbox annonce le lancement en preview publique de données d'entrée au niveau de la porte (doorway-level entrance data), une fonctionnalité destinée à résoudre le problème persistant du "dernier mètre" dans la livraison et le transport à la demande. Cette nouvelle capacité permet de guider les conducteurs jusqu'à l'entrée exacte d'un bâtiment, et non plus simplement jusqu'à l'adresse générique.

Le problème adressé est significatif : selon l'analyse de Mapbox basée sur les retours de clients en logistique à la demande, près de 70% des échecs de livraison dans les 100 derniers mètres se produisent dans les 10 derniers mètres du trajet. McKinsey estime que les localisations de dépôt inefficaces peuvent représenter jusqu'à 19% des coûts logistiques, incluant les demandes de support, le temps d'attente des chauffeurs, les colis perdus, les rendez-vous manqués et les nouvelles livraisons.

La solution technique s'intègre à l'API Mapbox Geocoding via un nouveau paramètre `entrances`. Lorsqu'activé, l'API retourne les localisations précises des entrées de bâtiments lors de la conversion d'une adresse en coordonnées géographiques. Les développeurs peuvent utiliser ces données pour alimenter une navigation virage par virage qui prend en compte le côté du bâtiment à approcher et où s'arrêter. Les designers peuvent également visualiser les emplacements d'entrée directement sur les cartes.

Les cas d'usage principaux concernent les plateformes de livraison, les prestataires logistiques et les entreprises de mobilité. Le témoignage de dlivrd illustre l'impact concret : réduction de 7% des temps de livraison et résolution 25% plus rapide des questions de support, avec de nombreuses demandes qui n'arrivent plus jamais au service client.

Cette innovation s'inscrit dans la stratégie de Mapbox de fournir une pile géospatiale moderne et flexible. Combinées avec la navigation, le routage, les cartes et le Mapbox Feedback Agent, les données d'entrée permettent de construire des expériences de navigation de bout en bout qui s'améliorent continuellement grâce aux interactions des utilisateurs avec la carte.
