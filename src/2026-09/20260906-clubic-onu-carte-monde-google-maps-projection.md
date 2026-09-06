# Why the UN's New World Map Won't Change Google Maps Anytime Soon

**Source**: https://www.clubic.com/actualite-628429-pourquoi-la-nouvelle-carte-du-monde-adoptee-par-l-onu-ne-va-pas-changer-google-maps-tout-de-suite.html
**Date**: 2026-09-06
**Author**: Clubic
**Keywords**: UN General Assembly, Correct the Map, Mercator, Equal Earth, Eckert IV, Google Maps, cartography, projection, France, Togo

## Elevator pitch
The UN's adoption of the Equal Earth projection resolution won't change Google Maps because the app's tiling system depends on Mercator's angle-preserving properties, and the resolution is nonbinding.

## Takeaways
- The UN resolution passed with 164 votes in favour, 1 against (US), and 6 abstentions, but is nonbinding
- France announced it will switch official maps from Mercator to Eckert IV projection
- Google Maps uses a square-tile system since 2005 that requires Mercator's angle-preserving properties at all zoom levels
- Equal Earth and Eckert IV preserve surface areas but sacrifice angular accuracy, making them incompatible with current tile-based mapping infrastructure
- Togo plans to meet with Google, the African Union, and UNESCO within six months to discuss practical implementation

## Synthesis
The United Nations General Assembly adopted the "Correct the Map" resolution by 164 votes to 1, encouraging the replacement of the Mercator projection with equal-area alternatives like Equal Earth. Yet the resolution's nonbinding nature means the world's most widely used digital mapping platform, Google Maps, will not change its projection anytime soon.

The core technical obstacle is Google's tiling system. Since 2005, Google Maps has divided the world into square tiles that must maintain their shape at every zoom level, including near the poles. The Mercator projection preserves angles at all scales — a property that equal-area projections like Equal Earth and Eckert IV do not share. This same tiling architecture is used by OpenStreetMap, Bing Maps, Mapbox, and Esri, meaning the entire web mapping ecosystem is built around Mercator's mathematical properties.

France's Foreign Minister Jean-Noël Barrot announced that France would abandon Mercator in favour of Eckert IV for its official maps, calling the correction "an exercise of truth." Eckert IV and Equal Earth differ in detail but share the principle of preserving surface areas at the cost of angles. The Equal Earth projection, created in 2018, was itself derived from a blend of Eckert IV and another equal-area projection.

Togo's Foreign Minister Robert Dussey, who led the resolution on behalf of the African Union, linked the campaign to broader efforts to move beyond colonial-era representations. He announced plans to meet with technology companies including Google, along with UNESCO and African Union members, within six months to discuss implementation. The resolution explicitly preserves Mercator's use for maritime and aerial navigation, where angle preservation is critical.