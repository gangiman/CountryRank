from rankings import list_of_all_rankings
import numpy as np


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
    print_all_rankings()    


if __name__ == '__main__':
    main()
