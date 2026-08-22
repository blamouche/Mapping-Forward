# Gemini plante Waze sur Android Auto : les conducteurs perdent patience
**Source**: https://www.tomsguide.fr/gemini-plante-waze-sur-android-auto-les-conducteurs-perdent-patience/
**Date**: 2026-07-24
**Author**: Aymeric Geoffre-Rouland, Tom's Guide
**Keywords**: Gemini, Waze, Android Auto, Google Maps, voice assistant, navigation bug

## Elevator pitch
Android Auto users report that Google's Gemini assistant consistently fails to launch Waze navigation routes, forcing drivers to switch to Google Maps — raising questions about whether the bug is accidental or strategic.

## Takeaways
- Gemini voice commands on Android Auto systematically fail to launch Waze routes, returning to the map view without error
- Google Maps remains the only navigation app that works reliably with Gemini voice commands on Android Auto
- Standard troubleshooting — clearing cache, reinstalling apps — does not resolve the issue
- The bug follows a pattern of problematic Gemini deployment across Google services
- Users on the official Android Auto forum have documented a reproducible failure scenario

## Synthesis
A growing number of Android Auto users are reporting that Google's Gemini assistant consistently fails to launch navigation routes in Waze, creating a frustrating experience that is pushing drivers toward Google Maps. The issue, documented on the official Android Auto support forum, follows a reproducible pattern: Gemini receives the voice command, Waze begins calculating the route, then the app aborts without any error message and returns to the map view.

The failure appears systematic rather than intermittent. Users report that regardless of the destination or phrasing, Gemini cannot successfully initiate a Waze navigation session. Standard troubleshooting steps — clearing the app cache, purging application data, reinstalling the latest versions of both Gemini and Waze — fail to resolve the situation. This suggests the problem lies at the integration layer between Gemini's voice command processing and Waze's route launching API, rather than in user-side configuration.

The situation is particularly galling for Waze loyalists because Google Maps, which uses the same Gemini voice interface on Android Auto, works flawlessly. This asymmetry has led some users to speculate whether the bug is purely accidental or reflects a strategic prioritization of Google's first-party mapping application over its acquired community-driven navigation platform.

This issue is the latest in a series of problems with Gemini's deployment across Google's ecosystem. While the assistant has gained capabilities — describing traffic jams in natural language, guiding drivers using building facades and visual landmarks, and enriching turn-by-turn instructions — its integration with third-party or non-primary Google apps has been inconsistent.

For Android Auto users who prefer Waze for its community-reported speed cameras, police locations, and real-time hazard alerts, the Gemini failure effectively downgrades the hands-free experience. Drivers must either manually launch Waze before connecting to Android Auto, use Google Maps as a compromise, or wait for Google to address the integration issue — something the company has not yet publicly acknowledged.