import pandas as pd

from .utils import IndividualRanking


class HumanHappinesReport(IndividualRanking):
    higher_is_better = True

    def __init__(self):
        self.df_hhr = pd.read_excel(
            'Raw_Data/2018_statistical_annex_all.xlsx',
            header=3, usecols='A:C', engine='openpyxl', index_col=0)

    def get_ranking(self):
        index_numeric = pd.to_numeric(self.df_hhr.index, errors='coerce')
        df_hhr = self.df_hhr[index_numeric.notnull()]
        df_hhr = df_hhr.set_index('Country').Value
        return df_hhr
