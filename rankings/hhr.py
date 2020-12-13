import pandas as pd

from .utils import IndividualRanking


class HumanHappinesReport(IndividualRanking):
    higher_is_better = True

    def __init__(self):
        self.df_human_happiness_report = pd.read_excel(
            'Raw_Data/2018_statistical_annex_all.xlsx',
            header=2, usecols='B:O', engine='openpyxl')

    def get_ranking(self):
        rk = self.df_human_happiness_report['Human Development Index (HDI) '].iloc[3:201]
        rk = pd.to_numeric(rk, errors='coerce')
        return rk[rk.notna()]
