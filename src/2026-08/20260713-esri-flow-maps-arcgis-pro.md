# Flow Maps
**Source**: https://www.esri.com/arcgis-blog/products/arcgis-pro/mapping/flow-maps
**Date**: 2026-07-13
**Author**: Chris Wesson (Esri)
**Keywords**: Esri, ArcGIS Pro, flow maps, Sankey, alluvial charts, migration maps, Map Viewer, XY to Line, cartography, data visualisation

## Elevator pitch
An Esri ArcGIS blog post details multiple methods for creating flow maps — visualising movement between origins and destinations — in both Map Viewer and ArcGIS Pro, filling the gap left by the retired ArcGIS Insights application.

## Takeaways
- Flow maps show movement between places (migration, trade, transport) and are commonly requested by ArcGIS users at conferences
- The blog presents two main solutions: Map Viewer's Find Closest tool for simple all-to-one or all-to-all flows, and ArcGIS Pro's XY to Line / Generate Origin-Destination Links for more complex many-to-many flows
- The ArcGIS Pro workflow involves four steps: creating link lines, adding offset midpoints for curved appearance, smoothing lines with Bezier interpolation, and styling with variable widths and arrowheads
- A legacy "Distributive Flow Lines" tool exists but only works for single-source routing, making it unsuitable for typical many-to-many migration or route maps
- The author demonstrates with ferry crossing data between England and mainland Europe, showing how real-world data can be prepared even when not in ideal format

## Synthesis
On July 13, 2026, Esri's ArcGIS Blog published a detailed technical guide on creating flow maps, written by Principal Product Engineer Chris Wesson. The post addresses a recurring question from ArcGIS users at conferences: how to visualise movement data — migration patterns, flight routes, trade flows — in the absence of the retired ArcGIS Insights application, which previously offered Sankey and alluvial flow map capabilities.

The blog post presents two primary solutions. The first, suited for simpler all-to-one or all-to-all scenarios, uses Map Viewer's Find Closest tool. This approach requires start and end point layers and automatically generates connection lines that appear curved at small scales over long distances. The author notes that barrier features (such as land masses for sea crossings) can be added to improve realism.

The second, more versatile solution is an ArcGIS Pro workflow comprising four steps. Step one creates link lines between origins and destinations using either the XY to Line tool (for single-table datasets) or the Generate Origin-Destination Links tool (for separate origin and destination tables). The author provides practical guidance for data preparation, including a geocoding shortcut using a unique city lookup table. Step two adds offset midpoint vertices to lines, creating a curved appearance — the author shares a Python script for this purpose and references community alternatives. Step three applies Bezier interpolation smoothing via the Smooth Line tool. Step four involves styling: varying line thickness by frequency or volume and adding arrowheads from the Esri Arrowheads font.

The post also discusses the legacy "Distributive Flow Lines" add-in tool, which is hydrology-based and limited to single-source routing. While useful for distributive flow scenarios, it does not meet the common need for many-to-many flow visualisation that conference attendees were requesting. The author's practical, step-by-step approach with real ferry crossing data demonstrates that flow maps are achievable with standard ArcGIS tools, even when source data is not in an ideal format.