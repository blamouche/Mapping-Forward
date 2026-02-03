# Announcing MapLibre Tile: a modern and efficient vector tile format
**Source**: https://maplibre.org/news/2026-01-23-mlt-release/
**Date**: January 23, 2026
**Author**: Bart Louwers and Ramya Ragupathy
**Keywords**: MapLibre, vector tiles, MLT, MVT, geospatial, open-source, compression, performance

## Elevator pitch
MapLibre introduces MLT, a next-generation vector tile format that delivers up to 6x better compression and faster decoding than the traditional MVT format.

## Takeaways
- MLT (MapLibre Tile) is a redesigned successor to Mapbox Vector Tile (MVT), engineered for modern geospatial data challenges
- The format achieves up to 6x compression improvement on large tiles compared to MVT
- Faster decoding is enabled through lightweight encodings compatible with SIMD instructions
- Future capabilities include 3D elevation data support, GPU-optimized processing, and linear referencing for Overture Maps
- Already supported in MapLibre GL JS and MapLibre Native through the new `encoding` property in style JSON

## Synthesis
MapLibre has announced the release of MapLibre Tile (MLT), a revolutionary new vector tile format designed to replace the aging Mapbox Vector Tile (MVT) standard. This development represents a significant leap forward in how geospatial data is encoded, transmitted, and rendered across mapping applications.

The MLT format addresses critical performance bottlenecks that have plagued the mapping industry for years. By leveraging modern hardware capabilities, MLT achieves remarkable compression ratios - up to six times better than MVT on large tiles. This improvement translates directly into reduced storage costs, lower bandwidth requirements, and more efficient cache utilization. For organizations serving planet-scale basemaps, these gains compound into substantial operational savings.

Perhaps more importantly, MLT introduces faster decoding through lightweight encodings that are compatible with SIMD (Single Instruction, Multiple Data) instructions found in modern processors. This means that map tiles can be decompressed and rendered more quickly, resulting in smoother user experiences and reduced latency in mapping applications.

The format's forward-looking design also positions it well for emerging trends in the geospatial industry. MLT is architected to eventually support 3D elevation data, enabling richer terrain visualizations. GPU-optimized processing paths will allow developers to offload tile decoding to graphics hardware, further improving performance. Support for linear referencing aligns with emerging formats like Overture Maps, ensuring interoperability with next-generation mapping standards. Complex nested data types will enable more sophisticated geographic feature representations.

The development of MLT has been a multi-year collaborative effort involving academic institutions, open-source contributors, and major technology companies including Microsoft and AWS. This broad coalition ensures that the format benefits from diverse perspectives and use cases while maintaining its open-source nature.

Both MapLibre GL JS and MapLibre Native already support MLT through a new `encoding` property in style JSON configurations. Developers can begin experimenting with MLT-based demo tiles immediately, and conversion tools are available for those who want to transform existing tile sets. The upcoming version of Planetiler will generate MLT tiles for production deployments, making adoption straightforward for organizations already in the MapLibre ecosystem.
