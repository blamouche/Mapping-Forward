# ¿Dónde hay tráfico por el eclipse? Mapbox y DGT muestran los atascos en toda España
**Source**: https://elpais.com/ciencia/2026-08-12/donde-hay-trafico-por-el-eclipse-consulte-los-atascos-en-toda-espana.html
**Date**: 2026-08-12
**Author**: Kiko Llaneras, Sebastián Casse, Pablo Montalvo
**Keywords**: Mapbox, real-time traffic, eclipse, interactive maps, DGT, OpenStreetMap, data visualization

## Elevator pitch
EL PAÍS built a real-time interactive traffic map powered by Mapbox and Spain's DGT traffic authority data showing how eclipse-day travel created massive traffic flows from cities toward the path of totality across Spain.

## Takeaways
- The interactive map combines three data sources: DGT traffic incidents (congestion, roadworks), DGT traffic cameras, and real-time traffic intensity from Mapbox
- The map overlays the eclipse totality band to visualize how traffic patterns correlate with the path of total solar eclipse
- Mapbox provides the base map layer and real-time traffic intensity data (from fluid to very dense)
- The visualization uses OpenStreetMap as a base layer with Mapbox's traffic overlay, demonstrating a production news media use of commercial mapping APIs
- The map includes a feedback mechanism linking to Mapbox's improvement platform, showing the iterative data quality loop

## Synthesis
EL PAÍS created a sophisticated real-time traffic visualization for the August 12, 2026 total solar eclipse in Spain, leveraging Mapbox's mapping platform and data from Spain's Dirección General de Tráfico (DGT). The map serves as a prime example of how news organizations use commercial mapping APIs to create timely, data-driven visualizations for major events.

The map integrates three distinct data layers: DGT-reported traffic incidents (major congestion and roadworks), hundreds of roadside traffic cameras, and real-time traffic intensity data from Mapbox rendered on a scale from "fluido" (fluid) to "muy denso" (very dense). A critical overlay shows the eclipse totality band—the geographic zone where the Moon completely blocks the Sun—enabling users to see how the extraordinary population movements toward this band create traffic patterns radiating from major cities.

The technical stack uses Mapbox as both the base map provider (with OpenStreetMap attribution) and the real-time traffic data source, with DGT providing authoritative government traffic incident data. The map includes a "Improve this map" feedback link to Mapbox's correction platform, demonstrating the data quality feedback loop inherent in modern mapping ecosystems. This project illustrates how Mapbox's API enables newsrooms to rapidly deploy sophisticated interactive maps for breaking events without building mapping infrastructure from scratch.