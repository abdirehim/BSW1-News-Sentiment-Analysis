# scripts/visualization.py — Plot MA20, RSI, MACD
# 🎯 Goal:
# Use matplotlib to generate:

# Line chart of Close vs MA20

# RSI chart with overbought/oversold zones

# MACD + Signal Line + Histogram

# scripts/visualization.py

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend to avoid display errors

import pandas as pd
import os

def plot_ma(df: pd.DataFrame, ticker: str, output_dir: str = "output"):
    plt.figure(figsize=(12, 5))
    plt.plot(df['Close'], label='Close Price', color='blue')
    plt.plot(df['MA20'], label='20-Day MA', linestyle='--', color='orange')
    plt.title(f"{ticker} - Close Price vs 20-Day Moving Average")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"{ticker}_ma_plot.png"))
    plt.close()

def plot_rsi(df: pd.DataFrame, ticker: str, output_dir: str = "output"):
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
    plt.savefig(os.path.join(output_dir, f"{ticker}_rsi_plot.png"))
    plt.close()

def plot_macd(df: pd.DataFrame, ticker: str, output_dir: str = "output"):
    plt.figure(figsize=(12, 5))
    plt.plot(df['MACD'], label='MACD', color='blue')
    plt.plot(df['MACD_signal'], label='Signal Line', color='orange')
    plt.bar(df.index, df['MACD_hist'], label='Histogram', color='gray', alpha=0.3)
    plt.title(f"{ticker} - MACD Indicator")
    plt.xlabel("Date")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"{ticker}_macd_plot.png"))
    plt.close()
