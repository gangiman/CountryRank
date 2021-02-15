from rankings import list_of_all_rankings
import numpy as np
import pandas as pd


def get_ranking_df() -> pd.DataFrame:
    series = {}
    for _class in list_of_all_rankings:
        data_source = _class()
        series[_class.__name__] = data_source.get_norm_ranking()
    return pd.DataFrame(series)


def print_all_rankings(weights='equal'):
    if weights == 'equal':
        num_classes = len(list_of_all_rankings)
        weights = np.ones(num_classes) / num_classes
    
    for _class in list_of_all_rankings:
        data_source = _class()
        ranking = data_source.get_ranking()
        print('-' * 80)
        print("Data source {}".format(_class.__name__))
        print("Higher is better" if data_source.higher_is_better else "Lower is better")
        print("Data available for these countries")
        print(ranking.index)
        print("Maximum value is {}, for country {}".format(ranking.max(), ranking.idxmax()))
        print("Minimum value is {}, for country {}".format(ranking.min(), ranking.idxmin()))        


def main():
    df = get_ranking_df()
    df.to_csv('score_dump_v1.csv')
    print(df.describe())


if __name__ == '__main__':
    main()
