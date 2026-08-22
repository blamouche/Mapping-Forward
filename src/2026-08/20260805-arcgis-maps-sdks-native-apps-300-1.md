# What's New in ArcGIS Maps SDKs for Native Apps 300.1: Gaussian Splats, Overture Maps Labels, and On-Device Analysis
**Source**: https://www.esri.com/arcgis-blog/products/developers/announcements/whats-new-in-arcgis-maps-sdks-for-native-apps-300-1
**Date**: 2026-08-05
**Author**: Esri
**Keywords**: Esri, ArcGIS Maps SDK, Native Apps, 300.1, Gaussian splatting, Overture Maps, 3D Tiles, point cloud, local scenes, on-device analysis, vector tiles

## Elevator pitch
ArcGIS Maps SDKs for Native Apps version 300.1 introduces Gaussian splat layers, Overture Maps-powered 3D place labels in local scenes, expanded point cloud support, improved vector tile performance, and new high-performance on-device spatial analysis tools for slope, aspect, and map algebra.

## Takeaways
- Gaussian splat layers bring photorealistic 3D visualization to local scenes, supporting digital twins of complex infrastructure with both connected and offline workflows
- The Places and Labels layer in local scenes is built using data from the Overture Maps Foundation, updated monthly to align with the latest Overture releases
- 3D Tiles support in local scenes enables textured 3D mesh content including Google Photorealistic 3D Tiles, with dynamic attribution
- Point cloud layer API expanded in local scenes with multiple renderer types and filtering capabilities for buildings, vegetation, and ground surfaces
- Vector tiled layer improvements include support for identify operations and enhanced rendering performance
- New on-device analysis tools for slope, aspect, and map algebra enable high-performance spatial analysis without server connectivity
- Shared editing templates now supported in offline workflows

## Synthesis
Published on August 5, 2026, on the Esri ArcGIS Blog, this announcement covers version 300.1 of the ArcGIS Maps SDKs for Native Apps, a broad update building on the 300.0 release that introduced local scenes and on-device analysis capabilities.

The most notable addition is Gaussian splat layer support in local scenes, mirroring the capability added to the Unreal Engine SDK. Gaussian splatting reconstructs 3D scenes from millions of individual Gaussian splats — soft, ellipsoid-shaped elements defined by position, rotation, size, color, and transparency. This enables highly realistic visualization of complex built and natural environments, particularly for digital twins of utility infrastructure, industrial facilities, and natural features. The implementation supports both connected workflows via ArcGIS Online/Enterprise and offline workflows using local 3D Tiles datasets. In version 300.1, this is available for .NET and Qt SDKs on desktop platforms, with mobile support planned.

The Places and Labels layer integration is particularly significant for the broader mapping ecosystem. Esri's hosted 3D labels layer is built using data curated by the Overture Maps Foundation — a collaborative initiative supported by Meta, Microsoft, Amazon, TomTom, and Esri. The layer combines content from OpenStreetMap and Esri Community Maps to provide current, comprehensive global labeling data for 3D scenes. Updated monthly to align with Overture releases, this gives developers access to high-quality, up-to-date geographic labels. This integration demonstrates the growing impact of the Overture Maps Foundation as a shared data infrastructure across the geospatial industry.

Local scenes receive substantial enhancements beyond Gaussian splats: 3D Tiles support (including Google Photorealistic 3D Tiles with dynamic attribution), blend modes for raster tile layers, and point cloud layers with expanded renderer and filter APIs. The point cloud capabilities mirror those in the Unreal Engine SDK, offering class breaks, unique value, stretch, and RGB renderers with value, return, and bit field filters.

On-device analysis capabilities are expanded with new high-performance tools for slope, aspect, and map algebra analysis, enabling spatial computation without requiring server connectivity. This is particularly valuable for field workflows in disconnected environments. Shared editing templates in offline workflows further strengthen the SDK's field data collection capabilities.