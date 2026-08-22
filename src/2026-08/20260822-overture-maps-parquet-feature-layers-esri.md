# Overture Maps Data as Parquet Feature Layers (Early Access)
**Source**: https://www.esri.com/arcgis-blog/products/arcgis-online/announcements/overture-maps-data-as-parquet-feature-layers-early-access
**Date**: August 22, 2026
**Author**: Esri
**Keywords**: Overture Maps, Esri, ArcGIS Online, Parquet feature layer, open map data, POIs, buildings, roads, AWS, Azure

## Elevator pitch
Esri announced Early Access Parquet feature layers created from Overture Maps Foundation data, enabling ArcGIS Online users to work with large read-only datasets like addresses, railways, infrastructure, places, and major cities directly through pre-configured web maps.

## Takeaways
- Eight web maps are now available through the Overture Parquet Layers group on ArcGIS Online: addresses, railways, infrastructure points/lines/polygons, places, major cities, and division areas
- The Parquet feature layer is a new layer type released in Beta in the June 2026 ArcGIS Online release, ideal for large read-only datasets
- Overture Maps Foundation generates monthly releases of reference datasets (buildings, roads, POIs) sourced from OpenStreetMap, Esri Community Maps, Microsoft, Meta, and others
- Data is accessible through open AWS S3 or Microsoft Azure endpoints and the Parquet format makes it well-suited for cloud-hosted large datasets
- Basic functionality like filtering, labeling, and modifying symbology is supported despite Beta limitations

## Synthesis
The Overture Maps Foundation, founded in December 2022, aims to create reliable, user-friendly, and interoperable open map data. Esri has been a member since shortly after the project was publicly announced and is now leveraging the new Parquet feature layer technology to make Overture data accessible within the ArcGIS ecosystem. The Parquet format is particularly well-suited for Overture's large, cloud-hosted datasets because it enables efficient querying and rendering of massive read-only geographic data.

For the Early Access release, Esri is sharing eight web maps covering addresses, railways, infrastructure (points, lines, and polygons), places, major cities, and division areas. These are available through a dedicated ArcGIS Online group. Since properties like symbology and popup configuration cannot yet be stored within the Parquet feature layer itself, Esri recommends using the pre-configured web maps which contain copies of the actual Parquet layers with their styling already applied.

During the Early Access period, Esri is actively seeking user feedback to improve and expand the offering. An upcoming blog will outline how these layers were created using ArcGIS Data Pipelines, enabling users to replicate the workflow for their priority layers and areas of interest. This represents a significant step in making open map data more accessible and usable within professional GIS workflows.