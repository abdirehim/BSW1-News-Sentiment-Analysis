import pandas as pd
import numpy as np
from stock_data import load_stock_csv
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def calculate_daily_returns(df: pd.DataFrame) -> pd.Series:
    """Calculate daily returns from closing prices.
    
    Args:
        df (pd.DataFrame): DataFrame with 'Close' column.
    
    Returns:
        pd.Series: Daily returns.
    """
    return df['Close'].pct_change().dropna()

def get_sentiment(headline: str) -> float:
    """Compute sentiment score using VADER.
    
    Args:
        headline (str): News headline text.
    
    Returns:
        float: Compound sentiment score.
    """
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(headline)['compound']

def prepare_correlation_data(sentiment_df: pd.DataFrame, stock_df: pd.DataFrame, ticker: str) -> pd.DataFrame:
    """Prepare data for correlation analysis.
    
    Args:
        sentiment_df (pd.DataFrame): DataFrame with sentiment data.
        stock_df (pd.DataFrame): DataFrame with stock data.
        ticker (str): Stock ticker symbol.
    
    Returns:
        pd.DataFrame: DataFrame with aligned sentiment and returns.
    """
    try:
        # Aggregate sentiment by date
        sentiment_df['date'] = pd.to_datetime(sentiment_df['date'])
        daily_sentiment = sentiment_df.groupby(sentiment_df['date'].dt.date)['sentiment'].mean().rename('avg_sentiment')
        
        # Align with stock returns
        stock_returns = calculate_daily_returns(stock_df)
        aligned_data = pd.DataFrame({
            'avg_sentiment': daily_sentiment,
            'daily_return': stock_returns
        }).dropna()
        logger.info(f"Prepared correlation data for {ticker} with {len(aligned_data)} rows")
        return aligned_data
    except Exception as e:
        logger.error(f"Error preparing data for {ticker}: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    # Load sentiment data (assumed FNSPID format: 'date', 'headline', 'stock')
    sentiment_df = pd.read_csv("./data/raw_analyst_ratings/raw_analyst_ratings.csv")  # Adjust path as needed
    sentiment_df['sentiment'] = sentiment_df['headline'].apply(get_sentiment)
    
    # Process all tickers
    tickers = ["AAPL", "GOOG", "AMZN", "MSFT", "TSLA", "NVDA", "META"]
    correlation_results = {}
    
    for ticker in tickers:
        stock_df = load_stock_csv(ticker)
        if stock_df.empty:
            logger.warning(f"Skipping {ticker} due to data load failure.")
            continue
        stock_df = stock_df['2020-01-01':'2020-06-30']  # Limit to Jan-Jun 2020
        
        # Filter sentiment for the ticker and period
        ticker_sentiment = sentiment_df[sentiment_df['stock'] == ticker]
        ticker_sentiment = ticker_sentiment[ticker_sentiment['date'].between('2020-01-01', '2020-06-30')]
        
        # Prepare data and compute correlation
        correlation_data = prepare_correlation_data(ticker_sentiment, stock_df, ticker)
        if not correlation_data.empty:
            correlation = correlation_data['avg_sentiment'].corr(correlation_data['daily_return'])
            correlation_results[ticker] = correlation
            logger.info(f"{ticker} correlation: {correlation}")
    
    # Summary
    correlation_df = pd.DataFrame.from_dict(correlation_results, orient='index', columns=['Pearson_Correlation'])
    print("\n📊 Correlation Results:\n", correlation_df)
    correlation_df.to_csv("output/correlation_results.csv")
    logger.info("Correlation results saved to 'output/correlation_results.csv'")