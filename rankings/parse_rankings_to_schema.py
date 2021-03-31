import json
from operator import or_
from functools import reduce
from typing import Optional, Dict

import pandas as pd


def FreedomOfInternetReport():
    df = pd.read_csv('./Raw_Data/FOTN_2018_Final_Booklet_11_1_2018_global_ranking.csv',
                     index_col=0, names=['Country', 'global_ranking'])

    return {
        'higher_is_better': False,
        'ranking': df.global_ranking
    }


def DoingBuisnessReview():

    series = pd.read_csv('./Raw_Data/Doing_buisness_16_12_2020.csv', delimiter=';', index_col=0
                         ).globalRank.dropna().astype(int)
    return {
        'higher_is_better': False,
        'ranking': series
    }


def HumanHappinesReport():
    higher_is_better = True
    df_hhr = pd.read_excel(
            'Raw_Data/2018_statistical_annex_all.xlsx',
            header=3, usecols='A:C', engine='openpyxl', index_col=0)
    index_numeric = pd.to_numeric(df_hhr.index, errors='coerce')
    df_hhr = df_hhr[index_numeric.notnull()]
    df_hhr = df_hhr.set_index('Country').Value
    return {
        'higher_is_better': True,
        'ranking': df_hhr
    }


def GDPperCapita():
    df_imf_gdp_per_capita = pd.read_csv(
        'Raw_Data/imf-dm-export-20181120.csv',
        sep=';',
        encoding="ISO-8859-1",
        index_col=0,
        na_values='no data',
        decimal=',')
    series = df_imf_gdp_per_capita[2019].iloc[:193]
    return {
        'higher_is_better': True,
        'ranking': series
    }


def MIPEX():
    df = pd.read_excel(
        './Raw_Data/policy_indicators_finalwebsite.xlsx',
        sheet_name='Summary 2014', engine="openpyxl", index_col=0).T
    return {
        'higher_is_better': True,
        'ranking': df['Overall Score (10-14)']
    }


def PassportIndex(hold_passports=('Russian Federation',), wights_to_countries: Optional[Dict]=None):
    df = pd.read_csv('./Raw_Data/passport-index-ISO-alpha-3.csv', header=0, index_col=0)
    new_df = reduce(or_, [(df.loc[_country] > 0) for _country in hold_passports], (df > 0))
    #TODO: add weighting by countries
    return {
        'higher_is_better': True,
        'ranking': new_df.sum(axis=1)
    }


list_of_all_rankings = [
    GDPperCapita,
    HumanHappinesReport,
    MIPEX,
    FreedomOfInternetReport,
    DoingBuisnessReview,
    PassportIndex
]


def main():
    output = [
        {'name': _ranking.__name__, **_ranking()}
        for _ranking in list_of_all_rankings
    ]
    with open('joined_init_rankings.json', 'w+') as fh:
        fh.write(json.dumps(output))


if __name__ == '__main__':
    main()
