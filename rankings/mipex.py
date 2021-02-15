import pandas as pd
import pycountry
import warnings

from .utils import IndividualRanking


class MIPEX(IndividualRanking):
    higher_is_better = True

    def __init__(self):
        self.df = pd.read_excel(
            './Raw_Data/policy_indicators_finalwebsite.xlsx',
            sheet_name='Summary 2014', engine="openpyxl", index_col=0).T

    def get_ranking(self, year='2019'):
        return self.df['Overall Score (10-14)']

    def resolve_countries(self) -> pd.Series:
        series = self.get_ranking()
        countries = {}
        for _index, _value in series.items():
            if _index == 'UK':
                _index = 'GB'
            try:
                _country = pycountry.countries.get(alpha_2=_index)
            except LookupError:
                _country = None
            if _country is None:
                warnings.warn(f"Couldn't resolve the country '{_index}'! Using 'N/A'.")
            else:
                countries[_country.alpha_3] = _value
        return pd.Series(countries)
