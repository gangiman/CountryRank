import pandas as pd

from .utils import IndividualRanking


class GDPperCapita(IndividualRanking):
    higher_is_better = True

    def __init__(self):
        self.df_imf_gdp_per_capita = pd.read_csv(
            'Raw_Data/imf-dm-export-20181120.csv',
            sep=';',
            encoding="ISO-8859-1",
            index_col=0,
            na_values='no data',
            decimal=',')

    def get_ranking(self, year='2019'):
        return self.df_imf_gdp_per_capita[year]
