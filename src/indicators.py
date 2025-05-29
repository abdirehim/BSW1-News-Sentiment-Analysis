# src/indicators.py

import talib
import pandas as pd

def apply_moving_average(df: pd.DataFrame, period: int = 20) -> pd.Series:
    """
    Calculate Moving Average (SMA) using TA-Lib.
    """
    return talib.SMA(df['Close'], timeperiod=period)

def apply_rsi(df: pd.DataFrame, period: int = 14) -> pd.Series:
    """
    Calculate RSI (Relative Strength Index) using TA-Lib.
    """
    return talib.RSI(df['Close'], timeperiod=period)

def apply_macd(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate MACD and signal line using TA-Lib.
    """
    macd, signal, hist = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return pd.DataFrame({
        'MACD': macd,
        'MACD_signal': signal,
        'MACD_hist': hist
    })

def apply_all_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply all relevant indicators to the stock price DataFrame.
    Returns the DataFrame with additional columns.
    """
    df['MA20'] = apply_moving_average(df)
    df['RSI14'] = apply_rsi(df)
    macd_df = apply_macd(df)
    return pd.concat([df, macd_df], axis=1)
