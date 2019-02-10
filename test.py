import unittest
from rankings import list_of_all_rankings
import pandas as pd


class TestDataSeries(unittest.TestCase):
    def test_all_classes(self):
        for _class in list_of_all_rankings:
            self.assertIsInstance(_class.higher_is_better, bool)
            self.assertIsInstance(_class.get_ranking(), pd.Series)
            