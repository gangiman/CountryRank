import pandas as pd

from .utils import IndividualRanking


class DoingBuisnessReview(IndividualRanking):
    higher_is_better = False

    def __init__(self):
        # TODO: fix exclx reading 
        self.df = pd.read_excel('Raw_Data/Doing_buisness_16_12_2020.xlsx', engine="openpyxl", index_col="Economy")

    def get_ranking(self):
        pass
