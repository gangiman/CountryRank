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


## Currently downloaded rankings

1) Social mobility by WorldBank [source](http://www.worldbank.org/en/topic/poverty/brief/what-is-the-global-database-on-intergenerational-mobility-gdim), [data](./Raw_Data/GDIMMay2018.csv)
2) IMF GDP per Capita [source](https://www.imf.org/external/datamapper/NGDPDPC@WEO/OEMDC/ADVEC/WEOWORLD), [data](./Raw_Data/imf-dm-export-20181120.csv)
3) MIPEX Immigrant Integration ranking 2015 [source](http://mipex.eu), [data](./Raw_Data/policy_indicators_finalwebsite.xlsx)
4) Human development report [source](http://hdr.undp.org/en/data), [data](./Raw_Data/2018_statistical_annex_all.xlsx)
5) Freedom of the Internet report 2018 [source](https://freedomhouse.org/sites/default/files/FOTN_2018_Final%20Booklet_11_1_2018.pdf), [data](./Raw_Data/FOTN_2018_Final_Booklet_11_1_2018_global_ranking.csv)
6) Passport Index Data [original source](https://www.passportindex.org/), [source](https://github.com/ilyankou/passport-index-dataset), [data](./Raw_Data/passport-index-country-names.csv)

## Other rankings

We are aware of the following rankings, but they have not been integrated yet:

1. Corruption Perception Index by Transparency International: [source](https://www.transparency.org/cpi)
