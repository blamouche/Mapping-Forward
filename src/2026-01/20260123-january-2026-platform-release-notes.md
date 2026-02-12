# January 2026 Platform Release Notes

**Source**: https://www.here.com/learn/blog/january-2026-platform-release-notes

**Date**: January 20, 2026

**Author**: Mohini Todkari

**Keywords**: HERE Platform, release notes, map content, SDK, API updates, developer tools, vector tiles, raster tiles, navigation

## Elevator pitch

HERE's January 2026 platform release introduces experimental map layers for improved geographic browsing, enhanced API capabilities for truck routing and vehicle restrictions, and SDK updates bringing traffic light visualization and new mobility profiles.

## Takeaways

- Two new experimental layers (Named Areas and Cartography Tile Intersections) enable improved browsing and processing of map partitions across five administrative hierarchy levels
- Raster Tile and Map Image APIs now support truck preferred roads and new vehicle restriction modes with RFC 3339 timestamp parameters
- HERE SDK 4.25.1.0 adds traffic light visualization, vehicle restriction filtering, and route serialization/deserialization capabilities
- Deprecated layers including Road Attributes and Navigation Attributes will be removed by end of Q1 2026
- Real-time traffic improvements targeting Netherlands coverage, European providers, and Cyprus Road Alerts are planned for upcoming releases

## Synthesis

HERE Technologies' January 2026 platform release notes outline a substantial set of updates across the company's map content, APIs, and SDK offerings, reflecting the ongoing evolution of location services infrastructure that developers rely upon for building navigation and mapping applications.

The most notable additions to HERE Map Content v2 are two experimental layers designed to improve how developers interact with geographic data. The Named Areas layer introduces a hierarchical system of tiled references spanning five administrative levels: Built-up Areas and Zones at tile level 12, Cities at level 10, Counties at level 8, States at level 6, and Countries at level 4. This structured approach enables more efficient browsing and processing of map partitions based on administrative boundaries. Complementing this, the Cartography Tile Intersections layer operates at level 12 and allows users to select and render specific cartographic features with greater precision. HERE appropriately flags both layers as experimental, cautioning developers against production deployment until further maturation.

The API enhancements focus on commercial vehicle routing, a critical capability for logistics and fleet management applications. The Raster Tile and Map Image APIs now support visualization of truck preferred roads and introduce two new vehicle restriction modes: active_and_inactive_differentiated and active_only. These modes require RFC 3339 timestamp parameters, enabling time-sensitive restriction queries that reflect real-world conditions such as delivery windows or seasonal road restrictions. The Vector Tile API receives a more modest update with a new border_style property for the boundaries layer, offering developers finer control over how political boundaries are rendered.

HERE SDK version 4.25.1.0 delivers several developer-requested features. Traffic light visualization capabilities enable applications to display traffic signal information to users, enhancing the navigation experience particularly in urban environments. New vehicle restriction filtering methods give developers programmatic control over which restrictions apply to calculated routes. The addition of route serialization and deserialization capabilities facilitates route storage and sharing across sessions or devices. New specification classes for pedestrian, scooter, and taxi profiles expand the SDK's multimodal routing capabilities, reflecting the growing importance of diverse transportation options in urban mobility solutions.

Looking ahead, HERE outlines several planned changes that developers should prepare for. The removal of deprecated layers including Road Attributes, Navigation Attributes, Advanced Navigation Attributes, and Recreational Vehicle Attributes has been delayed until the end of Q1 2026, giving developers additional time to migrate. The CurvatureHeadingAttribute faces deprecation with replacement attributes already introduced. A significant platform change coming in Q3 2026 involves the removal of catalog history for versions older than 18 months, requiring organizations to adjust their data retention strategies accordingly. Q4 2026 will bring a schema redesign for Restricted Driving Maneuvers, while ongoing improvements to HERE Real Time Traffic will expand coverage in the Netherlands, improve European provider integration, and add Cyprus Road Alerts.
