import sys
from pathlib import Path

# Add src/ directory to path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

import pandas as pd
from sentiment_analysis import apply_sentiment  # ⬅️ corrected here

def load_and_score_news(news_path: str = "data/raw_analyst_ratings/raw_analyst_ratings.csv") -> pd.DataFrame:
    """
    Load financial news data, normalize date, and compute sentiment scores.
    Returns a DataFrame with columns: stock, publish_day, sentiment_score.
    """
    df = pd.read_csv(news_path)

    # ✅ Step 1: Force date parsing
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # ✅ Step 2: Drop invalids (NaT)
    df = df.dropna(subset=['date'])

    # ✅ Step 3: Normalize to just date (no time)
    df['publish_day'] = df['date'].dt.date

    # ✅ Step 4: Apply sentiment
    df = apply_sentiment(df, text_column="headline")

    return df



if __name__ == "__main__":
    df = load_and_score_news()
    print(df[["headline", "stock", "publish_day", "sentiment_score"]].head())
