import pandas as pd
from sklearn import preprocessing
from wikidata.client import Client
import requests
import pycountry
import warnings


API_ENDPOINT = "https://www.wikidata.org/w/api.php"
client = Client()


def get_norm_ranking(ranking: pd.Series) -> pd.Series:
    """
    This method returns ranking pd.Series unified to [0,1] range.
    """
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(ranking.to_numpy().reshape(-1, 1))
    return pd.Series(x_scaled.T[0], index=ranking.index)


def resolve_countries(series: pd.Series) -> pd.Series:
    countries = {}
    for _index, _value in series.items():
        _country = resolve_country(_index)
        if _country is None:
            warnings.warn(f"Couldn't resolve the country '{_index}'! Using 'N/A'.")
        else:
            countries[_country.alpha_3] = _value
    return pd.Series(countries)


def get_data(query):
    params = {
        'action': 'wbsearchentities',
        'format': 'json',
        'language': 'en',
        'search': query
    }
    r = requests.get(API_ENDPOINT, params=params)
    return r.json()['search'][0]['id']


def get_country_code_from_wikidata(country):
    data = get_data(country)
    cv = client.get(data)
    return pycountry.countries.get(
        alpha_3=cv.attributes['claims']['P298'][0]
        ['mainsnak']['datavalue']['value'])


def identity(country: str) -> str:
    return country


def take_first(country: str) -> str:
    return country.split(',')[0]


def take_first_ws(country: str) -> str:
    return country.split(' ')[0]


def reverse_parts(country: str) -> str:
    return ' '.join(country.split(',')[::-1])


def resolve_country(_country_query):
    for _method in [pycountry.countries.lookup, get_country_code_from_wikidata]:
        for _fixing_country_string_method in [identity, take_first, take_first_ws, reverse_parts]:
            try:
                _country = _method(_fixing_country_string_method(_country_query))
                return _country
            except (LookupError, IndexError):
                continue


def resolve_countries_from_alpha_2(series: pd.Series) -> pd.Series:
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