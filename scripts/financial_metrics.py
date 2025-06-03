# scripts/financial_metrics_all.py
import pandas as pd
import numpy as np
from stock_data import load_stock_csv  # Correct import
from technical_indicators import calculate_indicators

def calculate_metrics(df: pd.DataFrame, rf: float = 0.005, period: str = "2020-01-01/2020-06-30") -> pd.Series:
    """
    Calculate basic financial metrics:
    - Daily returns
    - Sharpe ratio (annualized)
    - Volatility (annualized)
    """
    start_date, end_date = period.split('/')
    df = df.copy().loc[pd.Timestamp(start_date):pd.Timestamp(end_date)]
    
    # Ensure the index is a DatetimeIndex
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)

    daily_returns = df["Close"].pct_change().dropna()

    mean_return = daily_returns.mean()
    std_dev = daily_returns.std()

    # Annualized metrics
    sharpe_ratio = ((mean_return - rf / 252) / std_dev) * np.sqrt(252)
    volatility = std_dev * np.sqrt(252)

    return pd.Series({
        "Sharpe_Ratio": round(sharpe_ratio, 4),
        "Volatility": round(volatility, 4)
    })

if __name__ == "__main__":
    # List of tickers to process
    tickers = ["AAPL", "GOOG", "AMZN", "MSFT", "TSLA", "NVDA", "META"]

    # Dictionary to store metrics for all tickers
    all_metrics = {}

    for ticker in tickers:
        # Load stock data and calculate indicators
        df = load_stock_csv(ticker)
        if df.empty:
            print(f"Skipping {ticker} due to data load failure.")
            continue
        df = calculate_indicators(df)

        # Calculate metrics
        metrics = calculate_metrics(df, rf=0.005, period="2020-01-01/2020-06-30")
        all_metrics[ticker] = metrics

    # Convert metrics to DataFrame
    if all_metrics:
        metrics_df = pd.DataFrame(all_metrics).T
        print("\n📊 Financial Metrics for Tickers:\n", metrics_df)

        # Save to CSV
        metrics_df.to_csv("metrics_all_tickers.csv")
        print("\nMetrics saved to 'metrics_all_tickers.csv'")
    else:
        print("No metrics calculated due to data issues.")