# How Does Google Maps Know What Time You Will Arrive? The Technology Behind ETA
**Source**: https://en.ara.cat/media/how-does-google-maps-know-what-time-will-arrive_1_5828712.html
**Date**: August 20, 2026
**Author**: Albert Cuesta, Ara.cat
**Keywords**: Google Maps, ETA, GNSS, GPS, Galileo, GLONASS, BeiDou, DeepMind, traffic prediction, graph neural networks, navigation

## Elevator pitch
An in-depth explainer of how Google Maps estimates arrival times by combining multi-constellation GNSS positioning, A-GPS assisted location, real-time crowd-sourced traffic data, and DeepMind-developed graph neural networks processing one million "supersegments" to achieve 97% journey reliability.

## Takeaways
- Google Maps uses multi-constellation GNSS (GPS, Galileo, GLONASS, BeiDou) for positioning, with modern chips receiving signals from multiple systems simultaneously
- A-GPS (Assisted GPS) speeds up localisation by combining satellite signals with mobile network data and Wi-Fi triangulation, achieving 7-13m accuracy outdoors
- Google divides road networks into one million "supersegments" and uses DeepMind-developed graph neural networks to predict traffic and ETA
- The ETA prediction is reliable in over 97% of journeys according to Google product manager Johann Lau
- Google Maps controls 67% of the US navigation market vs Apple Maps (25%) and Waze (8%), with over 2 billion global users

## Synthesis
Google Maps' ability to predict arrival times with remarkable accuracy relies on a sophisticated stack of technologies that combine satellite positioning, crowd-sourced traffic data, and advanced machine learning. At the positioning layer, modern mobile phones receive signals from multiple GNSS constellations simultaneously — the US GPS, European Galileo, Russian GLONASS, and Chinese BeiDou — improving accuracy especially in urban canyons where signals bounce. The European Galileo system offers one-meter accuracy in its open service and up to 20 centimeters in its high-accuracy service launched in 2023.

A crucial clarification is that GNSS is a reception system, not a transmission system: satellites broadcast their position and time, and the device calculates its own location through trilateration. Phones refine this with A-GPS (Assisted GPS), which uses mobile network data to speed up localisation, and combine it with cell tower triangulation and Wi-Fi network databases. A modern device with A-GPS typically achieves 7-13 meters accuracy outdoors.

For ETA calculation, Google divides the world's road network into one million predefined "supersegments" and uses graph neural networks developed with DeepMind to combine real-time traffic data with historical patterns. Millions of devices transmit their position and speed anonymously to Google's servers, enabling measurement of traffic density on each road segment and continuous recalculation of routes and arrival times. Google product manager Johann Lau states the result is reliable in over 97% of journeys, a method detailed in a 2021 CIKM academic paper. Google Maps dominates the navigation market with 67% US market share and over 2 billion global users, while Waze — acquired by Google in 2013 — continues as a separate brand focused on real-time driver participation.