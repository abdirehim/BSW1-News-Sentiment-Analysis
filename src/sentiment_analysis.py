# src/sentiment_analysis.py

from textblob import TextBlob
import pandas as pd

def get_sentiment_score(text: str) -> float:
    """
    Calculate sentiment polarity of text using TextBlob.
    Returns a float between -1.0 (negative) and 1.0 (positive).
    """
    if not isinstance(text, str) or text.strip() == "":
        return 0.0
    return TextBlob(text).sentiment.polarity

def apply_sentiment(df: pd.DataFrame, text_column: str = "headline") -> pd.DataFrame:
    """
    Apply sentiment analysis on a column (default: 'headline') in the DataFrame.
    Adds a new column called 'sentiment_score'.
    """
    df['sentiment_score'] = df[text_column].apply(get_sentiment_score)
    return df
