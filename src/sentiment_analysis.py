from textblob import TextBlob
import pandas as pd

def get_sentiment_score(text: str) -> float:
    """
    Return sentiment polarity score for a given text.
    Range: -1 (negative) to 1 (positive)
    """
    return TextBlob(text).sentiment.polarity

def apply_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply sentiment analysis to 'headline' column and return updated DataFrame.
    """
    df['sentiment_score'] = df['headline'].apply(get_sentiment_score)
    return df
