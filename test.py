import unittest

import pandas as pd

from rankings import list_of_all_rankings


class TestDataSeries(unittest.TestCase):
    def test_all_classes(self):
        for _class in list_of_all_rankings:
            obj = _class()
            print('Testing {}'.format(_class.__name__))
            self.assertIsInstance(obj.higher_is_better, bool)
            self.assertIsInstance(obj.get_ranking(), pd.Series)


if __name__ == '__main__':
    unittest.main()