# scripts/visualization.py
# Plot MA20, RSI, MACD to output/project-root level

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Ensure headless environments won't break

import pandas as pd
import os
from stock_data import load_stock_csv
from technical_indicators import calculate_indicators

def plot_ma(df: pd.DataFrame, ticker: str, output_dir: str = "output"):
    os.makedirs(output_dir, exist_ok=True)
    save_path = os.path.join(output_dir, f"{ticker}_ma_plot.png")
    print(f"📤 Saving MA plot: {save_path}")
    plt.figure(figsize=(12, 5))
    plt.plot(df['Close'], label='Close Price', color='blue')
    plt.plot(df['MA20'], label='20-Day MA', linestyle='--', color='orange')
    plt.title(f"{ticker} - Close Price vs 20-Day MA")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_rsi(df: pd.DataFrame, ticker: str, output_dir: str = "output"):
    os.makedirs(output_dir, exist_ok=True)
    save_path = os.path.join(output_dir, f"{ticker}_rsi_plot.png")
    print(f"📤 Saving RSI plot: {save_path}")
    plt.figure(figsize=(12, 4))
    plt.plot(df['RSI14'], label='RSI14', color='purple')
    plt.axhline(y=70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(y=30, color='green', linestyle='--', label='Oversold (30)')
    plt.title(f"{ticker} - RSI14")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_macd(df: pd.DataFrame, ticker: str, output_dir: str = "output"):
    os.makedirs(output_dir, exist_ok=True)
    save_path = os.path.join(output_dir, f"{ticker}_macd_plot.png")
    print(f"📤 Saving MACD plot: {save_path}")
    plt.figure(figsize=(12, 5))
    plt.plot(df['MACD'], label='MACD', color='blue')
    plt.plot(df['MACD_signal'], label='Signal Line', color='orange')
    plt.bar(df.index, df['MACD_hist'], label='Histogram', color='gray', alpha=0.3)
    plt.title(f"{ticker} - MACD Indicator")
    plt.xlabel("Date")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

if __name__ == "__main__":
    tickers = ["AAPL", "GOOG", "AMZN", "MSFT", "TSLA", "NVDA", "META"]
    output_dir = "output"

    for ticker in tickers:
        # Load data and calculate indicators
        df = load_stock_csv(ticker)
        if df.empty:
            print(f"Skipping {ticker} due to data load failure.")
            continue
        df = calculate_indicators(df)

        # Generate plots
        plot_ma(df, ticker, output_dir)
        plot_rsi(df, ticker, output_dir)
        plot_macd(df, ticker, output_dir)

    print(f"All visualizations saved to '{output_dir}/' directory.")