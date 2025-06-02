# scripts/stock_data.py

import pandas as pd
import os
from pathlib import Path


def load_stock_csv(ticker: str, data_dir: str = "data/yfinance_data") -> pd.DataFrame:
    # Make data path absolute regardless of working directory
    root_dir = Path(__file__).resolve().parent.parent
    abs_data_dir = root_dir / data_dir
    path = abs_data_dir / f"{ticker}_historical_data.csv"

    try:
        df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")
        df = df[["Open", "High", "Low", "Close", "Volume"]].copy()
        df["DateOnly"] = df.index.date
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
