# Announcing ArcGIS Maps SDK 2.4 for Unreal Engine: Gaussian Splats, Point Clouds, and Enhanced 3D Tiles
**Source**: https://www.esri.com/arcgis-blog/products/unreal-engine/announcements/announcing-arcgis-maps-sdk-2-4-for-unreal-engine
**Date**: 2026-08-05
**Author**: Mike Branscomb, Rex Hansen, and Sneha Suresh, Esri
**Keywords**: Esri, ArcGIS, Unreal Engine, Gaussian splatting, point cloud, 3D Tiles, digital twins, LiDAR, GIS visualization, game engine

## Elevator pitch
Esri's ArcGIS Maps SDK 2.4 for Unreal Engine introduces Gaussian splat layers for photorealistic 3D environment visualization, expanded point cloud rendering and filtering, billboarded marker symbols for 3D point layers, and improved 3D Tiles support with better performance and attribution compliance.

## Takeaways
- Gaussian splat layers enable highly realistic visualization of complex built and natural environments from millions of dense points, ideal for digital twins of utility infrastructure, industrial pipelines, and vegetation
- Point cloud layer API expanded with class breaks, unique value, stretch, and RGB renderers, plus value, return, and bit field filters for precise visualization control
- 3D point scene layers now support billboarded 2D marker symbols that automatically orient toward the camera, complementing existing 3D model symbols
- 3D Tiles improvements include better rendering efficiency, higher visual fidelity, and dynamic attribution that aggregates attribution from visible tiles
- Gaussian splat layers support both connected workflows (ArcGIS Online/Enterprise) and offline workflows (local 3D Tiles datasets)
- Desktop platform support (Windows, Linux, macOS) for Gaussian splats in this release; mobile (Android/iOS) planned for future

## Synthesis
Published on August 5, 2026, on the Esri ArcGIS Blog, this announcement details version 2.4 of the ArcGIS Maps SDK for Unreal Engine, a significant update that brings advanced 3D visualization capabilities to game engine-based GIS applications.

The flagship feature is Gaussian splat layer support. Gaussian splatting is a reality-capture technology that reconstructs 3D scenes from millions of soft, ellipsoid-shaped elements called splats, each defined by position, rotation, size, color, and transparency. Together, these create smooth, photorealistic visualizations that preserve detail more effectively than traditional mesh-based representations. This is particularly valuable for creating high-fidelity digital twins of complex infrastructure like utility power lines, industrial pipelines, construction equipment, and plant facilities. The technology excels at capturing transparency and reflections in glass and metal surfaces while accurately representing vegetation.

The point cloud layer API receives substantial expansion. Developers can now use multiple renderer types — class breaks for quantitative attributes, unique value for categorical data, stretch for color gradients, and RGB for direct color display. Filtering capabilities include value filters (attribute-based), return filters (LiDAR return types), and bit field filters (bit flag classifications). Combined, these allow developers to isolate and analyze features such as buildings, vegetation, and ground surfaces within large point cloud datasets.

Billboarded 2D marker symbols for 3D point scene layers provide a lightweight alternative to 3D model symbols. These markers automatically face the camera, remaining visible and recognizable from any viewing angle, making them well-suited for thematic and attribute-driven visualizations. Support spans simple, unique value, and class breaks renderers.

The 3D Tiles improvements focus on practical deployment concerns. Enhanced rendering efficiency and visual fidelity make large-scale datasets more manageable. Dynamic attribution aggregates and sorts attribution information from visible tiles into a single accessible string, ensuring compliance with data provider requirements — particularly important when using Google Photorealistic 3D Tiles, which have specific application requirements.

This release reflects the broader trend of GIS platforms embracing game engine technology for immersive visualization, with Gaussian splatting representing the cutting edge of reality capture integration into spatial analysis workflows.