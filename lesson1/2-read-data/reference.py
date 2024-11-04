# These are the reference answers.

import pandas as pd


def read_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def preview_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.head()


def describe_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()