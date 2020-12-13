from wikidata.client import Client
import requests
import pycountry
import pandas as pd


API_ENDPOINT = "https://www.wikidata.org/w/api.php"


def get_data(query):
# query = "wikipedia"
    params = {
        'action': 'wbsearchentities',
        'format': 'json',
        'language': 'en',
        'search': query
    }
    r = requests.get(API_ENDPOINT, params=params)
#     print(r.json()['search'][0])
    return r.json()['search'][0]['id']


def convert_to_iso_codes(series: pd.Series):
    countries = []
    # not_found_countries = []
    client = Client()
    for _value in series.index:
        try:
            _country = pycountry.countries.lookup(_value)
            # print(_country)
            countries.append(_country)
        except:
            countries.append(get_country_code_from_wikidata(client, _value))
            # print("cannot parse '{}'".format(_value))
            # not_found_countries.append(_value)


def get_country_code_from_wikidata(client, country):
    data = get_data(country)
    cv = client.get(data)
    return pycountry.countries.get(alpha_3=cv.attributes['claims']['P298'][0]['mainsnak']['datavalue']['value'])
