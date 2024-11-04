from pathlib import Path
import pandas as pd


def read_data(path: Path | str) -> pd.DataFrame:
    # Write a function to return a dataframe from csv filepath.
    ...


def preview_data(df: pd.DataFrame) -> pd.DataFrame:
    # Write a function to preview the dataframe.
    ...


def describe_data(df: pd.DataFrame) -> pd.DataFrame:
    # Write a function to describe the dataframe.
    ...


def main():
    data_path = Path("../data/Video_Games_Sales_as_at_22_Dec_2016.csv")
    # Feel free to run and test the functions here!
    df = read_data(data_path)


if __name__ == '__main__':
    main()
