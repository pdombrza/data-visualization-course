import unittest
from unittest.mock import MagicMock
from io import StringIO
import pandas as pd

from task import platform_values, get_platforms, prepare_data

class TestCase(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'Name': ['Game1', 'Game2', 'Game3', 'Game4', 'Game5'],
            'Platform': ['PC', 'PS4', 'XOne', 'WiiU', 'PC'],
            'Year_of_Release': [2015, 2016, 2017, 2018, 2019],
            'Genre': ['Action', 'Adventure', 'Action', 'Puzzle', 'Adventure'],
            'Global_Sales': [0.4, 1.0, 0.3, 0.7, 1.2]
        })
    #
    # def test_platform_values(self):
    #     result = sorted(platform_values(self.df))
    #     expected_result = ['PC', 'PS4', 'PS5', 'WiiU', 'XOne']
    #     self.assertEqual(result, expected_result)
    #
    # def test_get_platforms(self):
    #     result = get_platforms()
    #     expected_result = {'PC', 'PS4', 'WiiU', 'XOne'}
    #     self.assertEqual(set(result), expected_result)

    def test_prepare_data_correct_output(self):
        result = prepare_data(self.df)
        expected_data = {
            'Platform': ['PC', 'PC', 'PS4', 'WiiU', 'XOne'],
            'Genre': ['Action', 'Adventure', 'Adventure', 'Puzzle', 'Action'],
            'Game_Count': [1, 1, 1, 1, 1]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result.sort_values(by=['Platform', 'Genre']).reset_index(drop=True),
                                      expected_df.sort_values(by=['Platform', 'Genre']).reset_index(drop=True))
