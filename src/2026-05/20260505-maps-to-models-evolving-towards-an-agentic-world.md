# Maps to Models: Evolving Towards an Agentic World
**Source**: https://www.tomtom.com/newsroom/product-focus/maps-to-models-evolving-towards-an-agentic-world
**Date**: May 5, 2026
**Author**: Arpana Honap
**Keywords**: TomTom, agentic AI, Agent Toolkit, MCP, spatial intelligence, Maps SDK, AI agents, Orbis Maps

## Elevator pitch
TomTom introduces its Agent Toolkit for Maps SDK, a plugin that gives any AI agent spatially intelligent capabilities — routing, geocoding, reachable area calculation, and nearby search — all triggered by plain English prompts and chained together automatically across 53 tools.

## Takeaways
- The Agent Toolkit bridges the gap from MCP servers (which connect interfaces to data) to structured workflow capabilities for complex decision-making
- TomTom's competitive advantage is its proprietary data: 2.8 trillion km of global distance data, trillions of GPS points, and continuous live traffic data that ground AI agents in reality
- The toolkit handles "invisible correlation" — interpreting user intent, sequencing tasks, keeping everything in sync — so developers don't have to rebuild workflows for each request
- Example use cases include insurance claims analysis against flood zones, city planning with travel time impact analysis, and dynamic truck rerouting with depot capacity constraints
- The toolkit is available through TomTom's Maps SDK for JavaScript

## Synthesis
TomTom's announcement of the Agent Toolkit represents a strategic pivot from being a map data provider to becoming a spatial intelligence layer for the emerging agentic AI ecosystem. The core insight is that while MCP (Model Context Protocol) servers solve the connection problem — letting AI agents access geographic data and APIs — they don't solve the workflow problem. An MCP server might tell an agent there's a flood zone, but the Agent Toolkit can chain together flood zone detection, claims location matching, coverage area analysis, and distance calculation into a single coherent response to "Which open claims sit within 500 meters of last night's flood zone?"

The article makes a clear distinction between AI assistants (front-end tools like TomTom's TAIA) and AI agents (deeply embedded systems that answer complex questions). The Agent Toolkit is for the latter — it's what someone else's agent uses to become spatially intelligent, not a standalone product.

TomTom's unique position comes from its data assets. The company has accumulated 2.8 trillion kilometers of global distance data and trillions of GPS points over decades of mapmaking, plus continuous live traffic data feeds. This proprietary data foundation addresses AI's fundamental "hallucination" problem by grounding agents in validated, continuously updated real-world information. The Orbis Maps platform is built on this strategy of fresh, validated data.

The toolkit packages 53 different spatial tools that can be chained automatically. When a dispatcher types "Reroute the trucks stuck behind the A12 incident through depots with capacity before 4pm," the Agent Toolkit handles geocoding, incident location, routing with live traffic, reachable area calculation for depots, and time window constraints — without the developer needing to manually orchestrate each step.

This positions TomTom at an interesting inflection point. The company is essentially betting that the future interface for geographic information isn't a map on a screen — it's a conversation. The map becomes a capability behind the interface, and TomTom wants to be the spatial reasoning engine that makes those conversations accurate and useful.
