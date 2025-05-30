import pandas as pd

def load_news_data(filepath: str) -> pd.DataFrame:
    """
    Load financial news dataset from a CSV or JSON file.
    Expected columns: headline, url, publisher, date, stock
    """
    df = pd.read_csv(filepath, parse_dates=['date'])
    return df

def preview_data(df: pd.DataFrame, n: int = 5):
    """
    Display the first n rows of the DataFrame.
    """
    print(df.head(n))
