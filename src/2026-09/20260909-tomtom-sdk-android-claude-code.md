# Extending the TomTom Maps and Navigation SDK Android Example App with Claude Code
**Source**: https://www.tomtom.com/newsroom/product-focus/extending-the-tomtom-maps-and-navigation-sdk-android-example-app-with-claude-code
**Date**: 2026-09-09
**Author**: TomTom Docs
**Keywords**: TomTom, Android SDK, Claude Code, AI coding agent, navigation, route instructions, Compose

## Elevator pitch
TomTom demonstrates how Claude Code can extend its Android Maps and Navigation SDK example app by building a Route Instructions Panel feature, documenting pitfalls in a reusable skill file.

## Takeaways
- TomTom used Anthropic's Claude Code AI agent to build a Route Instructions Panel — a draggable bottom sheet listing every maneuver on a planned route — on top of their Android SDK example app
- The agent mapped nine routing instruction subtypes (departures, turns, forks, merges, roundabouts, highway exits, tollgates, arrivals) to icons and natural-language phrases
- Key challenges included type-shape surprises in the SDK (e.g., `Road.name` returning `TextWithPhonetics?` not `String?`), packages in unexpected locations, and experimental Compose APIs that compile but crash at runtime
- The experiment is fully reproducible: prompt, CLAUDE.md, and skill file are published in a GitHub repo, pinned to exact app commit and SDK version
- The Superpowers plugin by Jesse Vincent was used to add workflow skills on top of Claude Code

## Synthesis
TomTom's technical blog post documents a case study in using AI coding agents to extend a mapping SDK example app. The team wanted to evaluate how hard it is to add a feature to the TomTom Android example app when an AI coding agent handles the implementation. They chose Claude Code, Anthropic's agentic coding tool, to build a Route Instructions Panel — a UI component that displays every maneuver on a planned route in a draggable Compose bottom sheet, with tap-to-fly camera animations.

The data model turned out to be straightforward: routes contain legs, which contain instructions, each with a maneuver point (GeoCoordinate), route offset (cumulative distance), and optional road name and signpost text. The nine instruction subtypes map cleanly to existing ManeuverType enums and icons already used by the guidance screen. However, several pitfalls emerged during implementation. Some SDK types had type-shape surprises — `Road.name` returns `TextWithPhonetics?` rather than `String?`, requiring unwrapping. Package locations were inconsistent, with some instruction subtypes living outside the `instruction` package they're used alongside. Experimental Jetpack Compose APIs compiled successfully but crashed at runtime, requiring fallbacks to stable alternatives. Empty lines in the maneuver list caused rendering issues.

The team made the experiment repeatable by instructing the coding agent to accumulate learnings in a skill file, which acts as a gotchas table for future attempts. They published the prompt, CLAUDE.md, and skill in a GitHub repository, with all artifacts pinned to the exact app commit and SDK version used. They also ran the agent with Jesse Vincent's Claude Code Superpowers plugin, which adds workflow skills on top of Claude Code's base capabilities. The exercise demonstrates both the potential and the friction of AI-assisted SDK integration: the agent could handle the data model and UI construction competently, but SDK-specific quirks required multiple iterations and manual testing to resolve.