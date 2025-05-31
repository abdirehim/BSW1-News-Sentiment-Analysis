# scripts/task2_analysis.py
import os
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from scripts.stock_data import load_stock_csv
from scripts.technical_indicators import calculate_indicators
from scripts.visualization import plot_ma, plot_rsi, plot_macd




# List of tickers (adjust if needed)
TICKERS = ["AAPL", "GOOG", "AMZN", "MSFT", "TSLA", "NVDA", "META"]
DATA_DIR = "data/yfinance_data"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_task2_pipeline():
    for ticker in TICKERS:
        print(f"\n🔍 Processing {ticker}...")
        df = load_stock_csv(ticker, data_dir=DATA_DIR)
        if df.empty:
            print(f"⚠️  Skipping {ticker}, no data found.")
            continue
        
        indicators_df = calculate_indicators(df)
        out_path = os.path.join(OUTPUT_DIR, f"{ticker}_indicators.csv")
        indicators_df.to_csv(out_path)
        print(f"✅ Saved indicators to {out_path}")

if __name__ == "__main__":
    run_task2_pipeline()
