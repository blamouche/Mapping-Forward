# How Does Google Maps Know What Time You Will Arrive?
**Source**: https://en.ara.cat/media/how-does-google-maps-know-what-time-will-arrive_1_5828712.html
**Date**: 2026-08-21
**Author**: Ara.cat
**Keywords**: Google Maps, ETA, GPS, GNSS, trilateration, DeepMind, graph neural networks, traffic prediction, navigation technology

## Elevator pitch
Google Maps achieves over 97% ETA reliability by combining satellite positioning, anonymous real-time traffic data from millions of devices, and DeepMind-developed graph neural networks that process historical and live traffic patterns across one million "supersegments."

## Takeaways
- GPS devices receive signals from multiple GNSS systems (GPS, Galileo, GLONASS, BeiDou) and calculate position via trilateration — satellites don't receive data from phones
- Modern positioning chips capture signals from multiple GNSS simultaneously, improving accuracy in urban canyons; A-GPS with Wi-Fi and cell tower triangulation achieves 7-13 meter accuracy outdoors
- Google Maps divides the road network into one million "supersegments" and uses DeepMind-developed graph neural networks to combine real-time traffic with historical patterns
- Millions of anonymous devices send position and speed data to Google servers, enabling real-time traffic density measurement and dynamic route recalculation
- Google Maps product manager Johann Lau reports ETA predictions are reliable in over 97% of journeys
- Waze dominates short repetitive commutes while Google Maps prevails on longer routes and unfamiliar places

## Synthesis
The article provides a detailed technical explanation of how Google Maps calculates routes and predicts arrival times. The process begins with satellite positioning: contrary to common belief, GNSS satellites (GPS, Galileo, GLONASS, BeiDou) only emit signals — they don't receive anything from mobile phones. The device receives signals from at least four satellites, calculates the time each signal took to arrive, and deduces its position through trilateration. Since 2017, most positioning chips capture signals from multiple GNSS systems simultaneously, improving accuracy especially in cities with tall buildings where signals bounce and distort.

Phones refine this calculation with A-GPS (Assisted GPS), which receives data via the mobile network to speed up localization, combined with cell tower triangulation and Wi-Fi network databases. A modern device with A-GPS typically positions itself with 7-13 meter accuracy outdoors, degrading notably indoors or between skyscrapers.

Once the phone's location is established, it becomes a transmitter: it sends position and speed data anonymously to Google's servers. Multiplied by millions of simultaneously circulating devices, this data flow enables measurement of traffic density on each road segment. Google divides the road network into one million predefined "supersegments" and uses graph neural networks developed with DeepMind to combine real-time traffic with historical patterns. Product manager Johann Lau confirms the system achieves over 97% ETA reliability.

The article also notes the different usage patterns: Waze concentrates activity on short, repetitive commutes, while Google Maps dominates longer routes and unfamiliar destinations — the use case that multiplies in summer travel. The base map itself combines satellite imagery, aerial photogrammetry, Street View data since 2007, and official cartographic sources.