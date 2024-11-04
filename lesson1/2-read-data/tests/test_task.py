import unittest
from unittest.mock import MagicMock
from io import StringIO
import pandas as pd

from task import read_data, preview_data, describe_data


# todo: replace this with an actual test
class TestCase(unittest.TestCase):

    def setUp(self):
        self.sample_csv_content = """Name,Platform,Year_of_Release,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales,Critic_Score,Critic_Count,User_Score,User_Count,Developer,Rating
                Game1,PC,2015,Action,Publisher1,0.1,0.2,0.0,0.1,0.4,85,20,8.0,100,Dev1,E
                Game2,PS4,2016,Adventure,Publisher2,0.3,0.4,0.1,0.2,1.0,90,30,9.0,200,Dev2,T
                """

        self.sample_csv_file = StringIO(self.sample_csv_content)

    def test_read_data(self):
        df = read_data(self.sample_csv_file)
        self.assertIsInstance(df, pd.DataFrame)


    def test_df_columns(self):
        df = read_data(self.sample_csv_file)
        expected_columns = [
            'Name', 'Platform', 'Year_of_Release', 'Genre', 'Publisher', 'NA_Sales',
            'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Critic_Score',
            'Critic_Count', 'User_Score', 'User_Count', 'Developer', 'Rating'
        ]
        self.assertListEqual(list(df.columns), expected_columns)

    def test_preview_data(self):
        df = pd.read_csv(self.sample_csv_file)
        result = preview_data(df)

        self.assertIsInstance(result, pd.DataFrame)

        expected_result = df.head()
        pd.testing.assert_frame_equal(result, expected_result)

    def test_describe_data(self):
        df_mock = MagicMock(spec=pd.DataFrame)
        describe_data(df_mock)

        df_mock.describe.assert_called_once()
