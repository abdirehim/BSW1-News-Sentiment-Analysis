import talib
import pandas as pd

def apply_moving_average(df: pd.DataFrame, period: int = 20) -> pd.Series:
    return pd.Series(talib.SMA(df['Close'].values, timeperiod=period), index=df.index)

def apply_rsi(df: pd.DataFrame, period: int = 14) -> pd.Series:
    return pd.Series(talib.RSI(df['Close'].values, timeperiod=period), index=df.index)

def apply_macd(df: pd.DataFrame) -> pd.DataFrame:
    macd, signal, hist = talib.MACD(df['Close'].values, fastperiod=12, slowperiod=26, signalperiod=9)
    return pd.DataFrame({
        'MACD': macd,
        'MACD_signal': signal,
        'MACD_hist': hist
    }, index=df.index)

def apply_all_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df['MA20'] = apply_moving_average(df)
    df['RSI14'] = apply_rsi(df)
    macd_df = apply_macd(df)
    return pd.concat([df, macd_df], axis=1)
