import sys
from pathlib import Path
import pandas as pd

# Add src/ directory to path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))
from stock_data import load_stock_csv

TICKERS = ["AAPL", "GOOG", "AMZN", "MSFT", "TSLA", "NVDA", "META"]
DATA_DIR = "data/yfinance_data"
OUTPUT_PATH = "output/daily_returns.csv"

all_returns = []

for ticker in TICKERS:
    df = load_stock_csv(ticker, data_dir=DATA_DIR)
    if df.empty:
        print(f"⚠️ Skipping {ticker}, no data found.")
        continue

    df = df.sort_index()
    df["daily_return"] = df["Close"].pct_change()
    df["stock"] = ticker
    df["publish_day"] = df.index.date  # To align with sentiment

    # Keep only what's needed
    all_returns.append(df[["stock", "publish_day", "daily_return"]])

# Combine all tickers
returns_df = pd.concat(all_returns)
returns_df = returns_df.dropna(subset=["daily_return"])
returns_df.to_csv(OUTPUT_PATH, index=False)

print(f"✅ Saved daily returns to {OUTPUT_PATH}")
print(returns_df.head())
