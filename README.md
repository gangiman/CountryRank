# CountryRank

Simple project that given your preferences for different country attributes returns a ranked list of countries.

The original design was:
1) `rankings` submodule that imports and pre-processes data series.
2) restrict list of countries being compared.
3) join data series into DataFrame using countries as index.
4) rank DataFrame using your preference weights.
5) return ranked list of countries.

There was a original version, but it was lost due to accidentally killed container, all that remained is this screenshot.

![List of my preferences and some links to data](image.png) 
