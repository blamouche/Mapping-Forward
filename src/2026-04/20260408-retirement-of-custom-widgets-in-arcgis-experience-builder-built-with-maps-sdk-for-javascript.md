# Retirement of custom widgets in ArcGIS Experience Builder built with Maps SDK for JavaScript
**Source**: https://www.esri.com/arcgis-blog/products/apps/announcements/retirement-of-custom-widgets-in-arcgis-experience-builder-built-with-maps-sdk-for-javascript
**Date**: April 8, 2026
**Author**: Sarah Jane O’Keefe and Jianxia Song
**Keywords**: Esri, ArcGIS Experience Builder, JavaScript Maps SDK, web components, migration

## Elevator pitch
Esri is giving Experience Builder developers until Q1 2027 to migrate custom widgets away from legacy JavaScript widget patterns and onto web components.

## Takeaways
- Esri announced that custom Experience Builder widgets built with ArcGIS Maps SDK for JavaScript widgets will retire in Q1 2027.
- Developers are being told to build new custom widgets with JavaScript web components immediately.
- Existing custom widgets should be refactored to use web components before upcoming Experience Builder and ArcGIS Enterprise releases.
- Out-of-the-box Experience Builder widgets will be migrated by Esri and are not expected to break for customers.
- The announcement gives developers a clear transition window and documentation path for migration.

## Synthesis
Esri is using this announcement to warn developers about a specific compatibility break coming to ArcGIS Experience Builder. Custom widgets built with ArcGIS Maps SDK for JavaScript widgets will retire in Q1 2027, and developers are being instructed to move toward JavaScript web components instead. The message is straightforward: teams that extend Experience Builder with custom widgets need to start planning migration work now, not at the point when the change becomes mandatory.

The timeline matters because it is tied to future versions of both ArcGIS Experience Builder and ArcGIS Enterprise. Once those products ship versions that depend on the newer JavaScript Maps SDK implementation built around web components, older custom widgets based on legacy widget patterns will stop working. That creates a fairly typical platform transition problem. Organizations with long-lived internal applications often rely on custom components that receive less attention than customer-facing software, which means migration work can easily be postponed until it becomes urgent. Esri is clearly trying to prevent that delay.

The company draws a distinction between custom widgets and out-of-the-box widgets. Standard Experience Builder widgets will be refactored by Esri and should remain supported, so the burden falls primarily on developers who have built their own extensions. The recommendation is to build all new widgets with web components immediately and to refactor existing ones well before the 2027 deadline. Esri also points developers toward supporting documentation, sample code, and migration guidance, which signals that the ecosystem transition is already underway rather than hypothetical.

For the broader mapping and geospatial software market, this is a reminder that application-builder platforms are still reshaping their underlying component models. Even when the visible feature set remains stable, the technical substrate can change significantly. Teams using low-code or no-code geospatial platforms still need frontend migration capacity if they depend on custom extensions. In that sense, the announcement is less about a single product retirement than about the operational reality of maintaining geospatial applications inside evolving platform ecosystems.
