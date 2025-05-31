# scripts/stock_data.py

import pandas as pd
import os

def load_stock_csv(ticker: str, data_dir: str = "data/yfinance_data") -> pd.DataFrame:
    """
    Load a stock CSV file and prepare it for indicator analysis.
    Adds a 'DateOnly' column for alignment with news sentiment data.
    """
    path = os.path.join(data_dir, f"{ticker}_historical_data.csv")
    try:
        df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")
        df = df[["Open", "High", "Low", "Close", "Volume"]].copy()
        df["DateOnly"] = df.index.date  # Strip time for date alignment
        return df
    except Exception as e:
        print(f"❌ Failed to load {ticker}: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    # Quick test
    tickers = ["AAPL", "GOOG", "AMZN", "MSFT", "TSLA", "NVDA", "META"]

    for t in tickers:
        df = load_stock_csv(t)
        print(f"{t}: {df.shape}")
