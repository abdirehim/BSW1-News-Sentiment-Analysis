# Step 2: Aggregate Sentiment per Day per Stock
# We’ll now:

# Group by stock and publish_day

# Compute the average sentiment per day per stock


import pandas as pd

def aggregate_daily_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group by stock and publish_day, and calculate average sentiment score.
    Returns: DataFrame with stock, publish_day, avg_sentiment.
    """
    daily_sentiment = (
        df.groupby(["stock", "publish_day"])["sentiment_score"]
        .mean()
        .reset_index()
        .rename(columns={"sentiment_score": "avg_sentiment"})
    )
    return daily_sentiment

if __name__ == "__main__":
    from task3_sentiment_prep import load_and_score_news

    df = load_and_score_news()
    daily_sentiment_df = aggregate_daily_sentiment(df)

    daily_sentiment_df.to_csv("output/daily_sentiment.csv", index=False)
    print(daily_sentiment_df.head())
