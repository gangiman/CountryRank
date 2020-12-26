import pandas as pd

from .utils import IndividualRanking


class DoingBuisnessReview(IndividualRanking):
    higher_is_better = False

    def __init__(self):
        self.series = pd.read_csv('./Raw_Data/Doing_buisness_16_12_2020.csv', delimiter=';', index_col=0
                                  ).globalRank.dropna().astype(int)

    def get_ranking(self):
        return self.series
