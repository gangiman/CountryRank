import pandas as pd

from .utils import IndividualRanking


class FreedomOfInternetReport(IndividualRanking):
    higher_is_better = False

    def __init__(self):
        self.df = pd.read_csv('./Raw_Data/FOTN_2018_Final_Booklet_11_1_2018_global_ranking.csv', index_col=0, names=['Country', 'global_ranking'])

    def get_ranking(self):
        return self.df.global_ranking
