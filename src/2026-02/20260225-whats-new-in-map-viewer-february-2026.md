# What's New in Map Viewer (February 2026)
**Source**: https://www.esri.com/arcgis-blog/products/arcgis-online/announcements/whats-new-in-map-viewer-february-2026
**Date**: 2026-02-25
**Author**: Lily Wydra, Jennifer Bell, Megan Arreola
**Keywords**: ArcGIS Online, Map Viewer, visualization, editing, analysis, collaboration

## Elevator pitch
Esri’s February 2026 update to ArcGIS Online Map Viewer focuses on richer temporal visualization, more precise editing, and smoother sharing, signaling a push to make Map Viewer the default end-to-end workspace for cartography and analysis.

## Takeaways
- Map Viewer adds tighter label placement, time visibility controls, and symbol animation to improve cartographic clarity and storytelling.
- New exploration tools like Calendar Heat Charts and enhanced attachment viewing make temporal patterns and evidence easier to analyze in-map.
- Editing upgrades, including true curve support and shared template management, target higher-precision data creation workflows.
- Analysis tools expand ModelBuilder sharing and raster analysis to support more advanced, repeatable spatial workflows.
- Sharing improvements like dynamic print legends, URL parameters, and routing waypoints focus on clarity and audience-specific outputs.

## Synthesis
The February 2026 release positions ArcGIS Online Map Viewer as a more comprehensive environment for both map design and analytical workflows. Esri’s emphasis on visualization and styling improvements is notable: label positioning now dynamically adjusts for partially visible polygons, a practical fix for a common cartographic annoyance where labels drift off-screen or anchor to invisible centroids. Complementary styling updates introduce visible time ranges for layers, allowing non–time-enabled data to be filtered by temporal windows, and symbol animation across vector symbols, which adds expressive movement for time-sensitive or attention-critical features. Together, these changes encourage mapmakers to use the web viewer for presentation-grade cartography without detouring to desktop tooling.

Exploration tools lean into temporal analytics and evidence-rich workflows. The new Calendar Heat Chart organizes date-field records into calendar layouts by day, week, or month, which is especially helpful for spotting rhythms in incident data, service requests, or seasonal activity. An upgraded attachment viewer inside the attribute table keeps imagery and documents within the mapping context; users can now inspect and manage photos without bouncing across tabs, reducing friction for review or QA processes. Imagery layer pop-ups powered by Arcade add another dimension: pixel values and imagery attributes can be transformed on the fly into narrative-ready insights, which is useful for environmental monitoring and remote sensing workflows.

Editing gets a precision upgrade with true curve support. Instead of converting curves into dense collections of straight segments, the editor now preserves native geometry when creating or modifying curved features. This is a meaningful quality improvement for engineering, transportation, or utility datasets where geometric fidelity matters. The addition of shared template management in Map Viewer is a broader workflow improvement: team-defined templates can be reviewed and updated directly in the web interface, allowing organizations to standardize data creation while lowering the barrier for contributors who don’t use ArcGIS Pro.

On the analysis side, ModelBuilder enhancements make it easier to publish models as web tools, broadening how workflows can be shared and reused across organizations. The expansion of raster analysis with tools like Geomorphon Landforms and Summarize Categorical Raster indicates a continued push toward web-based surface analysis, useful for land-cover change studies, terrain characterization, and environmental reporting. These changes align with a trend in enterprise GIS: moving analytical pipelines into hosted environments where they can be versioned, automated, and accessed by non-specialists.

Sharing and collaboration improvements focus on output clarity and situational responsiveness. Printing now includes dynamic legends that reflect only what is visible in the map extent, improving readability for audiences who need concise outputs. URL parameter support, route layer waypoints, and expanded reverse geocoding controls provide power users with more flexibility to tailor experiences without custom development. The retirement of Map Viewer Classic in this release is also a strategic signal: Esri is consolidating user behavior around the modern viewer, betting that feature parity and performance are now sufficient to make the transition stick.

Overall, the February 2026 update blends quality-of-life refinements with capability expansions that reflect Map Viewer’s evolving role: not just a viewer, but a primary environment for exploration, editing, analysis, and dissemination. The throughline is workflow efficiency—keeping users inside one interface while offering enough power to produce polished, analytically sound maps.
