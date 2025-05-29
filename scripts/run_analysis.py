from src.data_loader import load_news_data
from src.sentiment_analysis import apply_sentiment

if __name__ == "__main__":
    df = load_news_data("data/news_sample.csv")
    df = apply_sentiment(df)
    print(df[['headline', 'sentiment_score']].head())
