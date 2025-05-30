# scripts/run_technical_analysis.py

import os
import yfinance as yf
from src.indicators import apply_all_indicators

# List of stock tickers provided in the challenge
TICKERS = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]  # Add more if needed
OUTPUT_DIR = "output"
START_DATE = "2022-01-01"
END_DATE = "2023-01-01"

def run_analysis():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for ticker in TICKERS:
        try:
            print(f"📥 Downloading data for {ticker}...")
            df = yf.download(ticker, start=START_DATE, end=END_DATE)

            if df.empty:
                print(f"⚠️ No data found for {ticker}, skipping.")
                continue

            print(f"📊 Applying indicators to {ticker}...")
            df = apply_all_indicators(df)

            output_path = os.path.join(OUTPUT_DIR, f"{ticker}_indicators.csv")
            df.to_csv(output_path)
            print(f"✅ Saved {ticker} indicators to {output_path}\n")

        except Exception as e:
            print(f"❌ Error processing {ticker}: {e}")

if __name__ == "__main__":
    run_analysis()
