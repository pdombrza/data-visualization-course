from multiprocessing.spawn import prepare
from pathlib import Path
import pandas as pd

def read_data(path: Path | str) -> pd.DataFrame:
    return pd.read_csv(path)


def platform_values(df: pd.DataFrame) -> list:
    # Create a function to return all platform values from the Platform column in the DataFrame.
    ...


def get_platforms() -> list[str]:
    # Create a function to return a list of relevant platforms.
    ...


def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    # Create a function to prepare the data.
    # 1. Get the required platforms
    # 2. Filter the dataframe to retain only values with the relevant Platform values.
    # 3. Group platform and genre in the filtered dataframe. Calculate size of each group. Convert groups Platform and Genre
    # into regular columns in a new DataFrame
    ...


def main():
    data_path = Path("../data/Video_Games_Sales_as_at_22_Dec_2016.csv")
    # Feel free to run and test the functions here!
    df = read_data(data_path)

if __name__ == "__main__":
    main()