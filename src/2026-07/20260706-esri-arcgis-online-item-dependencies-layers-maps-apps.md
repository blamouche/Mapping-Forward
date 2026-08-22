# Esri ArcGIS Online: Discover How Your Layers, Scenes, Maps, and Apps Connect
**Source**: https://www.esri.com/arcgis-blog/products/arcgis-online/announcements/discover-how-your-layers-scenes-maps-and-apps-connect
**Date**: 2026-07-06
**Author**: Laura Busolo and Aditya Allamraju, Esri
**Keywords**: Esri, ArcGIS Online, item dependencies, layers, web maps, web scenes, content management, GIS workflows, data lineage, dependency tracking

## Elevator pitch
Esri's June 2026 ArcGIS Online update introduces item dependency tracking — new "Items used" and "Used by" sections on item pages that reveal how layers, scenes, maps, and apps interconnect, helping organizations manage content chains and avoid breaking dashboards.

## Takeaways
- New "Items used" and "Used by" sections on ArcGIS Online item pages visualize content dependencies
- Feature layers show a "Used by" section in the Usage tab; web maps, scenes, and apps show both sections
- Helps identify how changes to one item (e.g., making a layer private) ripple through dependent maps and dashboards
- Supported item types include feature layers, web maps, web scenes, and multiple ArcGIS app types
- Each connected item is clickable, enabling deep exploration of dependency chains
- Only items the user has permission to access are displayed in dependency lists

## Synthesis
Esri's June 2026 update to ArcGIS Online introduces a long-requested capability: visible dependency tracking between content items. The new "Items used" and "Used by" sections on item pages make it possible to see how layers, web maps, web scenes, and applications depend on one another — addressing a persistent challenge in GIS content management where changes to one item can unknowingly break downstream applications.

The feature addresses a real operational problem. In ArcGIS Online, items form chains of connected content: a feature layer feeds a web map, which powers a dashboard, which is shared with a public audience. If the underlying layer is made private, deleted, or transferred to another owner, the dashboard breaks for its users. Without visibility into these relationships, administrators have had difficulty anticipating the impact of such changes.

For feature layers, the item page's Usage tab now includes a "Used by" section showing all items that directly reference the layer — including item title, type, last modified date, owner, and view count. This helps layer owners understand where their data is consumed across the organization. Web maps and web scenes get both "Items used" (showing the data sources they depend on) and "Used by" (showing what consumes them). Supported app types also receive both sections.

Each item in the dependency list is clickable, opening the corresponding item page for deeper exploration. This enables administrators to trace dependency chains through multiple levels — from a base layer through intermediate maps to end-user applications. Only items the user has permission to access appear in these lists, maintaining appropriate access controls.

Esri recommends making dependency review a regular habit, especially for high-use content, and communicating changes to owners of dependent items before deprecating or deleting content. This feature brings ArcGIS Online's content management capabilities closer to the lineage tracking expected in enterprise data platforms.