# Esri Expert Voices: Unlocking the Power of Open Data for Basemaps
**Source**: https://www.esri.com/arcgis-blog/products/arcgis-living-atlas/decision-support/esri-expert-voices-unlocking-the-power-of-open-data-for-basemaps
**Date**: 2026-03-17
**Author**: Steven Moore, Nicte Hernandez
**Keywords**: Esri, open data, basemaps, OSM, Overture

## Elevator pitch
Esri détaille comment l’ouverture des données (OSM, Overture) alimente ses fonds de carte 2D/3D et comment l’entreprise assure la qualité et les mises à jour.

## Takeaways
- Esri s’appuie sur OSM et Overture pour ses basemaps open data.
- Les pipelines mettent à jour des tuiles 2D/3D mensuellement.
- L’énorme volume de données impose une ingestion et un partitionnement avancés.
- La validation repose sur contrôles OSM et Overture.
- Esri prévoit des feature layers Overture en 2026.

## Synthesis
L’article “Esri Expert Voices” présente un entretien avec Steve Moore, Senior GIS Engineer chez Esri, centré sur l’intégration des données ouvertes (OpenStreetMap et Overture Maps Foundation) dans les basemaps d’Esri. L’objectif est de fournir des fonds de carte fiables, actualisés et multi‑formats (2D, 3D, feature layers).

L’entretien explique que les basemaps open data d’Esri s’appuient sur des pipelines complexes. Les tuiles vectorielles 2D sont mises à jour chaque mois, tandis que les couches 3D utilisent des outils internes pour intégrer rapidement les données ouvertes. La volumétrie est considérable : un “planet file” OSM dépasse 2 To, et Overture ajoute des milliards d’empreintes de bâtiments. Pour gérer cette échelle, Esri prétraite les données, partitionne géographiquement les traitements et exécute les pipelines dans des environnements cloud co‑localisés.

Un point clé est la qualité. Esri mise sur les processus de validation d’OSM et d’Overture, hérités notamment du projet Daylight Map Distribution, pour réduire les erreurs et améliorer la fiabilité. L’entreprise insiste sur l’importance des licences de données et sur la nécessité de comprendre les contraintes juridiques associées aux datasets ouverts.

L’article souligne que la diversité des sources est un avantage : les utilisateurs peuvent choisir entre données ouvertes et données commerciales selon leurs besoins. Esri considère que l’ouverture favorise l’innovation, la transparence et la collaboration, tout en offrant une base solide pour les applications cartographiques.

Enfin, Esri annonce un plan pour 2026 : publier des feature layers dérivées d’Overture (bâtiments, routes, POIs) afin de permettre des analyses plus avancées, au‑delà des seuls basemaps.

En résumé, l’article décrit comment Esri industrialise l’usage des données ouvertes pour ses fonds de carte. La stratégie combine pipelines de mise à jour, validation rigoureuse et expansion des produits open data, montrant que l’ouverture devient centrale dans l’offre cartographique d’Esri.