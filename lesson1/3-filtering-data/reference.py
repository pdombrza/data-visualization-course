import pandas as pd


def platform_values(df: pd.DataFrame) -> list:
    return df['Platform'].unique()


def get_platforms() -> list[str]:
    platforms = ["PC", "XOne", "PS4", "WiiU"]
    return platforms


def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    platforms = get_platforms()
    filtered_df = df.loc[df['Platform'].isin(platforms)]
    genre_platform_counts = filtered_df.groupby(['Platform', 'Genre']).size().reset_index(name='Game_Count')
    return genre_platform_counts


def main():
    ...


if __name__ == "__main__":
    main()