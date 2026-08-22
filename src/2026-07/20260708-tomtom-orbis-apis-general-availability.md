# TomTom Orbis APIs Are Now in General Availability
**Source**: https://www.tomtom.com/newsroom/product-focus/tomtom-orbis-apis-are-now-in-general-availability
**Date**: 2026-07-08
**Author**: TomTom Newsroom
**Keywords**: TomTom, Orbis, APIs, general availability, routing, map display, traffic, geocoding, places search, MCP Server, Overture Maps, MapLibre

## Elevator pitch
TomTom launches six generally available APIs built on Orbis Maps — covering routing, map display, traffic, geocoding, places search, and reverse geocoding — with a unified convention set, MapLibre compatibility, and an MCP Server for AI agent integration.

## Takeaways
- Six APIs now GA: Map Display, Traffic, Routing, Places Search, Geocoding, and Reverse Geocoding — all built on Orbis Maps
- Routing API supports up to 150 waypoints per request, more than any other provider
- Traffic API refreshes flow and incidents every 30 seconds from 5+ billion kilometers of driving data daily across 80+ countries
- Places Search replaces mode-specific endpoints with three intuitive actions: discover, suggest, and details
- TomTom MCP Server exposes the full Orbis portfolio through a single integration for AI agents and LLM-based interfaces
- Open data at the core: Orbis combines open data with TomTom proprietary content across 235+ countries and territories; map content updated weekly

## Synthesis
TomTom has reached general availability for six newly built APIs on its Orbis Maps platform, marking a significant milestone in the company's transition to an API-first, open-standards-based location platform. The six APIs — Map Display, Traffic, Routing, Places Search, Geocoding, and Reverse Geocoding — share a single foundation in Orbis Maps, one set of conventions, and come with a Maps SDK for JavaScript and a TomTom MCP Server.

The APIs are designed around REST delivery with JSON responses and GeoJSON-compatible geometry. Map Display treats vector and raster as separate resources with 23 zoom levels (0–22) and MapLibre compatibility out of the box. The Routing API offers traffic-aware car routes with up to 150 waypoints per request — more than any other provider. The Traffic API delivers real-time flow and incident tiles refreshed every 30 seconds, drawing from more than 5 billion kilometers of driving data processed daily across 80+ countries.

Places Search represents a significant redesign, replacing a constellation of mode-specific endpoints (fuzzy search, POI search, nearby search) with three actions that follow how people actually search: discover (fully resolved results from complete input), suggest (as-you-type suggestions), and details (full information for a POI). The Geocoding API tolerates typos and incomplete input, while Reverse Geocoding turns coordinates into structured, human-readable addresses.

Orbis combines open data — developed in collaboration with the Overture Maps Foundation (backed by Meta, Microsoft, and Amazon) — with TomTom's proprietary content including address points, speed limits, traffic restrictions, and traffic signs. Coverage spans 235+ countries and territories with weekly map content updates. The TomTom MCP Server brings the full API portfolio into AI agents and LLM-based interfaces through a single integration, positioning Orbis for the emerging agentic computing paradigm.