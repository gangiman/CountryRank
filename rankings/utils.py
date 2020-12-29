import pandas as pd
from sklearn import preprocessing
from wikidata.client import Client
import requests
import pycountry


API_ENDPOINT = "https://www.wikidata.org/w/api.php"


def get_data(query):
    params = {
        'action': 'wbsearchentities',
        'format': 'json',
        'language': 'en',
        'search': query
    }
    r = requests.get(API_ENDPOINT, params=params)
#     print(r.json()['search'][0])
    return r.json()['search'][0]['id']


def get_country_code_from_wikidata(client, country):
    data = get_data(country)
    cv = client.get(data)
    return pycountry.countries.get(alpha_3=cv.attributes['claims']['P298'][0]['mainsnak']['datavalue']['value'])


class IndividualRanking:
    """
    Abstract class for individual ranking
    """

    @property
    def higher_is_better(self):
        """

        :return: bool
        """
        return NotImplementedError()

    def get_ranking(self):
        raise NotImplementedError()

    def get_norm_ranking(self) -> pd.Series:
        """
        This method returns ranking pd.Series unified to [0,1] range.
        """
        ranking = self.get_ranking()
        min_max_scaler = preprocessing.MinMaxScaler()
        x_scaled = min_max_scaler.fit_transform(ranking.to_numpy().reshape(-1, 1))
        return pd.Series(x_scaled.T[0], index=ranking.index)

    def resolve_countries_to_iso_codes(self) -> pd.Series:
        series = self.get_norm_ranking()
        countries = []
        client = Client()
        for _value in series.index:
            try:
                _country = pycountry.countries.lookup(_value)
                countries.append(_country)
            except LookupError:
                countries.append(get_country_code_from_wikidata(client, _value))
        series.index = pd.Index(countries)
        return series
