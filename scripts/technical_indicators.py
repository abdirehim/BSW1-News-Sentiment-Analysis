# scripts/technical_indicators.py

import pandas as pd
import talib

def calculate_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute technical indicators using TA-Lib and return a DataFrame with added columns.
    """
    df = df.copy()
    close = df['Close'].values

    # Calculate MA, RSI, MACD
    df['MA20'] = pd.Series(talib.SMA(close, timeperiod=20), index=df.index)
    df['RSI14'] = pd.Series(talib.RSI(close, timeperiod=14), index=df.index)
    
    macd, signal, hist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
    df['MACD'] = pd.Series(macd, index=df.index)
    df['MACD_signal'] = pd.Series(signal, index=df.index)
    df['MACD_hist'] = pd.Series(hist, index=df.index)

    return df

if __name__ == "__main__":
    # Standalone test
    from stock_data import load_stock_csv

    ticker = "AAPL"
    df = load_stock_csv(ticker)
    indicators_df = calculate_indicators(df)

    indicators_df.to_csv(f"output/{ticker}_indicators.csv")
    print(f"✅ Indicators calculated and saved to output/{ticker}_indicators.csv")
