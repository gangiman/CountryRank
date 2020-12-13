import pandas as pd

from .utils import IndividualRanking


class MIPEX(IndividualRanking):
    higher_is_better = True

    def __init__(self):
        self.df = pd.read_excel(
            './Raw_Data/policy_indicators_finalwebsite.xlsx',
            sheet_name='Summary 2014', engine="openpyxl", index_col=0).T

    def get_ranking(self, year='2019'):
        return self.df['Overall Score (10-14)']
