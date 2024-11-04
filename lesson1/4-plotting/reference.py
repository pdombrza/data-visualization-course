import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def read_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def preview_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.head()


def describe_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()


def get_platforms() -> list[str]:
    platforms = ["PC", "XOne", "PS4", "WiiU"]
    return platforms


def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    platforms = get_platforms()
    filtered_df = df.loc[df['Platform'].isin(platforms)]
    genre_platform_counts = filtered_df.groupby(['Platform', 'Genre']).size().reset_index(name='Game_Count')
    return genre_platform_counts


def create_graph(filtered_df: pd.DataFrame) -> None:
    sns.barplot(data=filtered_df, x='Platform', y='Game_Count', hue='Genre', edgecolor='white')
    plt.title("Number of Games by genre for platforms")
    plt.xlabel("Platform")
    plt.ylabel("count")
    plt.xticks(rotation=45)
    plt.legend(title="genre", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def main():
    path = "../data/Video_Games_Sales_as_at_22_Dec_2016.csv"
    df = read_data(path)
    filtered_df = prepare_data(df)
    create_graph(filtered_df)


if __name__ == "__main__":
    main()