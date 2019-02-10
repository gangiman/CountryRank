import pandas as pd
from .utils import IndividualRanking




class HumanHappinesReport(IndividualRanking):
    higher_is_better = True

    def __init__(self):
        self.df_human_happiness_report = pd.read_excel('Raw_Data/2018_statistical_annex_all.xlsx', header=2, usecols='B:O')

    def get_ranking(self, year='2019'):
        return self.df_human_happiness_report
