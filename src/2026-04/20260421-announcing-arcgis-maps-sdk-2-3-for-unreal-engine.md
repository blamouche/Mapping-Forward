# Announcing ArcGIS Maps SDK 2.3 for Unreal Engine
**Source**: https://www.esri.com/arcgis-blog/products/unreal-engine/announcements/announcing-arcgis-maps-sdk-2-3-for-unreal-engine
**Date**: April 21, 2026
**Author**: Mike Branscomb, Rex Hansen, Shimona Lahiri
**Keywords**: ArcGIS, Unreal Engine, 3D point scene layers, digital twins, geospatial developers

## Elevator pitch
Esri's ArcGIS Maps SDK 2.3 for Unreal Engine adds performant point scene layer rendering, better building-scene identification, and a smaller runtime to support more interactive 3D geospatial apps.

## Takeaways
- Version 2.3 adds support for high-performance visualization of 3D point scene layers in Unreal Engine.
- Developers can use data-driven styling, including simple, unique-value, and class-break renderers with 3D model symbols.
- Identify workflows now include building scene layers, improving interaction with detailed architectural content.
- Esri says the native SDK component is 25% smaller, reducing deployment size and startup overhead across supported platforms.
- The release strengthens Unreal Engine as a target for immersive geospatial applications, especially those using large 3D datasets.

## Synthesis
This release note outlines a focused but meaningful update to Esri’s ArcGIS Maps SDK for Unreal Engine, with improvements that target both rendering performance and developer ergonomics. The headline capability is support for 3D point scene layers, a data type well suited to dense collections of objects that can be represented as points in 3D space, such as trees, street furniture, sensors, and infrastructure assets. By adding this layer type, Esri is making it easier to build Unreal applications that need to display large real-world datasets while preserving performance.

The article emphasizes that point scene layers are not just about scale but about representation. Developers can now apply data-driven styling through simple, unique-value, and class-break renderers, and can use 3D model symbols to express those categories visually. Combined with hierarchical level-of-detail behavior, this means applications can transmit and render large point collections efficiently while preserving semantic differences between assets. The example of the Open 3D Trees layer, sourced from Overture-derived data and updated monthly, shows how this capability fits into broader efforts to make large open geospatial datasets usable in interactive 3D environments.

A second improvement concerns identification workflows. Methods introduced in the previous release now support building scene layers, allowing developers to retrieve attributes from complex architectural content. That matters because immersive 3D applications increasingly require more than passive visualization. Users need to click, query, compare, and highlight features in digital twins, operational models, and simulation environments. By extending identify support, Esri reduces the need for custom interaction workarounds and makes richer exploratory workflows easier to implement.

The final major change is infrastructural rather than visible: the native component of the SDK is now 25 percent smaller. That has practical consequences for deployment size, download time, storage usage, and application startup performance, especially across the SDK’s multiple supported platforms. For teams targeting Android, iOS, Linux, macOS, and Windows, footprint reduction can meaningfully improve development and distribution efficiency.

Taken together, the release shows Esri continuing to position Unreal Engine as a serious destination for geospatially enabled 3D and XR applications. The improvements are not framed as experimental features but as enablers for more scalable, more interactive, and more production-ready geospatial experiences. In that sense, the update reflects the growing convergence of GIS content, game-engine rendering, and digital twin workflows.
