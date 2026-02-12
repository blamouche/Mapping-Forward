# Protomaps Adds Overture Maps Data Source Support

**Source**: https://github.com/protomaps/basemaps/pull/541

**Date**: January 3, 2026

**Author**: Michal Migurski

**Keywords**: Protomaps, Overture Maps, basemaps, PMTiles, OpenStreetMap, vector tiles, MapLibre, open data, mapping infrastructure

## Elevator pitch

Michal Migurski contributes a major pull request to Protomaps basemaps enabling support for Overture Maps as an alternative data source to OpenStreetMap extracts, while maintaining full compatibility with existing MapLibre styles.

## Takeaways

- The PR adds support for Overture Maps input data as an alternative to OpenStreetMap extracts for Protomaps basemaps
- Implementation covers POIs, roads, places, buildings, landuse, and base layers while maintaining compatibility across all five visual style variants
- Data extraction utilizes DuckDB queries against S3-hosted Parquet files, enabling efficient regional data sampling in 1-2 minutes
- Linear referencing is used to split linestrings on bridge, tunnel, and level flags for detailed road rendering
- Future enhancements will incorporate QRank scoring and confidence thresholds to improve POI quality

## Synthesis

Michal Migurski, a prominent figure in the geospatial community, has submitted a significant pull request to the Protomaps basemaps repository that introduces support for the Overture Maps Foundation's datasets as an alternative data source. This development represents an important step in the evolution of open mapping infrastructure, providing map developers with flexibility in choosing their foundational data sources.

The Protomaps project has established itself as a leading solution for serving map tiles efficiently through its PMTiles format, which enables the storage and delivery of map data as single static files. Until now, Protomaps basemaps have relied primarily on OpenStreetMap data extracts. The new implementation expands this foundation by enabling the use of Overture Maps data while maintaining full backward compatibility with existing MapLibre styles across all five visual flavor variants: black, grayscale, white, light, and dark.

The technical implementation is comprehensive, covering the major map layer types needed for typical basemap applications. POIs (points of interest), roads, places, buildings, landuse, and base layers including earth, water, and land cover are all supported in the initial implementation. The PR notes that boundaries and transit layers remain incomplete and are targeted for future work.

One notable technical feature of the implementation involves the use of linear referencing to split linestring geometries based on bridge, tunnel, and level attributes. This approach enables detailed road rendering that matches the quality of output produced from OSM-based data, ensuring that users won't experience degraded visual quality when switching data sources.

The data extraction pipeline leverages DuckDB queries against Overture's S3-hosted Parquet files, a design choice that enables efficient regional data sampling. According to the PR documentation, extracting data for the San Francisco Bay Area takes approximately 1-2 minutes, demonstrating the practical performance of the new data pipeline.

The implementation includes comprehensive test coverage at 82.3% for new code across 56 commits, addressing POI categorization, road classification, and geometry splitting operations. Future planned enhancements include incorporating QRank scoring and confidence thresholds to improve POI quality, as well as extending place rendering to include low-zoom administrative boundaries.

This contribution reflects the growing interoperability between major open mapping data providers and the tools that consume their data, giving developers more options for building mapping applications.
