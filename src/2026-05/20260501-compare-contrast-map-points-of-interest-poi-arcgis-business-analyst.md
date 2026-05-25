# Compare and contrast: Map points of interest (POI) in ArcGIS Business Analyst
**Source**: https://www.esri.com/arcgis-blog/products/bus-analyst/mapping/compare-and-contrast-map-points-of-interest-poi-in-arcgis-business-analyst
**Date**: May 2026
**Author**: Unknown (Esri Blog – Compare and Contrast series)
**Keywords**: ArcGIS Business Analyst, POI (Points of Interest), Web App vs Pro, Data Axle, SafeGraph, Foursquare, ArcGIS Places, spatial analysis, aggregation, POI search, nearby analysis

## Elevator pitch
A side-by-side comparison of how points of interest (POI) search works in ArcGIS Business Analyst Web App versus the ArcGIS Pro extension, covering data sources, search types, filtering, aggregation, and results visualization — part of Esri's ongoing "Compare and contrast" series bridging the two companion products.

## Takeaways
- Both Business Analyst Web App and Pro support POI search via keywords, categories, codes, advanced conditions, and "all points" — but Web App adds semantic search, top retailers, and saveable advanced searches, while Pro can query up to 1 million points using local data.
- POI data sources include Data Axle, SafeGraph, Foursquare, and Esri's ArcGIS Places dataset; Pro uniquely supports local/offline data, avoiding ArcGIS Online credit consumption and enabling larger queries.
- Filtering in Web App is dynamic (real-time map updates) and post-search; Pro applies filters upfront with Preview Map/Table to verify before exporting results as feature classes, shapefiles, or tables.
- Aggregation (summarizing points by sites, geographies, or hexagons) is available in both environments, but Pro supports additional attributes like square footage; Web App aggregation disables filters and bubble charts while active.
- Results exploration differs significantly: Web App provides an interactive Results pane with summary, histogram, bubble chart, and Excel export; Pro relies on ArcGIS Pro's native charting and visualization tools for post-hoc analysis.

## Synthesis
L'article s'inscrit dans la série "Compare and contrast" du blog Esri, qui compare systématiquement les fonctionnalités entre Business Analyst Web App (l'application web, mise à jour 3 fois par an) et l'extension Business Analyst pour ArcGIS Pro (mise à jour 2 fois par an). L'objectif est d'aider les utilisateurs à choisir le bon outil en fonction de leurs besoins, ou à comprendre comment transposer un workflow d'une plateforme à l'autre.

Le cœur de l'article porte sur la recherche de points d'intérêt (POI), une fonctionnalité clé pour l'analyse spatiale business. Les deux plateformes partagent les mêmes types de recherche (mot-clé, catégorie, code NAICS, recherche avancée, tous les points) et exploitent les mêmes sources de données commerciales : Data Axle, SafeGraph, Foursquare et le dataset ArcGIS Places d'Esri. Les catégories Esri unifiées offrent une classification cohérente entre les sources.

Les différences commencent avec la recherche avancée, sauvegardable dans le Web App mais pas dans Pro. Le Web App propose aussi la recherche par "top retailers" (une liste curatoriale des 25 plus grands détaillants US par volume de ventes) et la recherche sémantique, absentes de Pro. En revanche, Pro offre une capacité inégalée avec les données locales : jusqu'à un million de points interrogeables sans consommer de crédits ArcGIS Online.

Le filtrage illustre bien la divergence philosophique entre les deux outils. Le Web App applique les filtres dynamiquement après la recherche initiale, avec mise à jour en temps réel de la carte et du panneau Results. Pro, plus traditionnel, applique les filtres avant l'exécution et propose des aperçus (Preview Map, Preview Table) pour itérer sans créer de couche définitive.

L'agrégation (synthèse des points par site, géographie standard ou hexagone) existe dans les deux environnements avec des attributs similaires (nombre de points, volume de ventes, effectifs). Pro ajoute la surface en pieds carrés (min/max). La granularité des calculs est la même — count, sum, average, min, max.

Là où le Web App excelle, c'est dans l'exploration interactive des résultats : un panneau Results dédié avec résumé statistique, histogramme, bubble chart/scatterplot et tableau exportable en Excel. Pro délègue cette étape aux outils de visualisation natifs d'ArcGIS Pro (pie charts, bar charts, etc.), ce qui offre plus de flexibilité mais demande plus d'effort manuel.

Un détail intéressant : l'article annonce la suppression prochaine des codes SIC (juin 2026) comme type de recherche, confirmant la transition continue vers les standards NAICS plus modernes. L'article se termine par des ressources pour approfondir, typique de la stratégie de contenu Esri qui utilise le blog comme porte d'entrée vers la documentation, les formations et la communauté.

Pour un analyste géospatial, le message est clair : utilisez le Web App pour la rapidité, l'interactivité et le partage ; passez à Pro quand vous avez besoin de volumes massifs, d'analyse offline, ou d'intégration dans des workflows géotraitement plus complexes.
