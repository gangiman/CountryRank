import pandas as pd
from operator import or_
from functools import reduce
from typing import Optional, Dict

from .utils import IndividualRanking


class PassportIndex(IndividualRanking):
    higher_is_better = True

    def __init__(self):
        self.df = pd.read_csv('./Raw_Data/passport-index-ISO-alpha-3.csv',header=0, index_col=0)

    def get_ranking(self, hold_passports=('Russian Federation',), wights_to_countries: Optional[Dict]=None):
        new_df = reduce(or_, [(self.df.loc[_country] > 0) for _country in hold_passports], (self.df > 0))
        #TODO: add weighting by countries 
        return new_df.sum(axis=1)
