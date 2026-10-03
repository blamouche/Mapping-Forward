# Tech for Earth: Methane, Penguins, and a Volcano Nobody Was Watching

**Source**: https://geoawesome.com/tech-for-earth-methane-penguins-and-a-volcano-nobody-was-watching/
**Date**: 2026-09-30
**Author**: Sebastian Walczak (Geoawesome)
**Keywords**: MAPL-EMIT, methane plumes, Google Research, NASA, PNAS, WeatherNext 3, Sentinel-1, emperor penguins, NISAR, volcano monitoring, Overture Maps, satellite imagery, remote sensing, Earth observation, Vega-C, FLEX, Sentinel-3C

## Elevator pitch
Geoawesome's monthly Earth observation roundup covers Google and NASA's AI model that found 23,000 methane plumes from space, Sentinel-1 radar tracking of emperor penguin colonies in Antarctic darkness, NISAR's nine-month volcano time-lapse, and the latest Overture Maps data release.

## Takeaways
- Google Research and NASA JPL published MAPL-EMIT in PNAS, a vision transformer model that identified approximately 23,000 methane plumes from EMIT hyperspectral data on the ISS, including plumes at 24 of the 25 worst-emitting landfills globally
- The model combines spectral and spatial information in a single vision transformer (trained on 3.6 million synthetic plumes), recovering 84% of hand-annotated NASA plume complexes and flagging ~1.5x more plausible plumes than human analysts
- Google DeepMind released WeatherNext 3 with 5km grid resolution (down from 25km) and hourly refresh, layering live geostationary satellite mosaics to cut forecast lag from ~7 hours to 3-4 hours
- Durham University researchers tracked emperor penguin colonies in Antarctic winter using Sentinel-1 SAR imagery, detecting bright clusters of pixels (1.2m-tall birds in dense huddles) against smooth fast ice, across eight breeding seasons
- NASA's NISAR satellite captured 17 frames of Krasheninnikov volcano on Kamchatka erupting for the first time since ~1550, assembling a time-lapse showing lava filling and overflowing the caldera
- Vega-C flight VV30 launched both FLEX and Copernicus Sentinel-3C on September 15, ESA's first dual Earth observation satellite launch
- Overture Maps shipped its September data release with addresses, buildings, places, transportation, and divisions data free to download

## Synthesis
Geoawesome's September Earth observation roundup spans methane detection, weather forecasting, wildlife tracking, volcano monitoring, and satellite launches. The standout piece is MAPL-EMIT, a Google Research and NASA JPL model published in PNAS that reads the full radiance spectrum from the EMIT hyperspectral instrument on the International Space Station. The vision transformer architecture combines spectral and spatial information to identify methane plumes at 60 metres per pixel, recovering 84% of hand-annotated NASA plume complexes and flagging approximately 23,000 additional plumes globally, including at 24 of the 25 largest-emitting landfills.

Google DeepMind's WeatherNext 3 represents a structural shift in AI weather forecasting: a 5km grid (down from 25km) refreshed hourly, using live geostationary satellite mosaics to cut the lag between observation and forecast from roughly seven hours to three or four. The model also outputs wind speed at 100 metres (turbine hub height), cloud cover, and solar radiation, targeting grid operators and renewables forecasting.

The penguin tracking from Durham University is a elegant application of routinely collected SAR data: emperor penguins, standing 1.2 metres tall in dense huddles, scatter enough microwave signal to appear as bright moving clusters against smooth fast ice in Sentinel-1 winter imagery. The team tracked three colonies across eight breeding seasons at sub-weekly resolution. Meanwhile, NISAR captured a nine-month time-lapse of Krasheninnikov volcano erupting for the first time in five centuries, and Overture Maps shipped its September data release of open base map data.