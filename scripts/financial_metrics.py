# scripts/financial_metrics.py

import pandas as pd
import numpy as np

def calculate_metrics(df: pd.DataFrame, rf: float = 0.01) -> pd.Series:
    """
    Calculate basic financial metrics:
    - Daily returns
    - Sharpe ratio (annualized)
    - Volatility (annualized)
    """
    df = df.copy()
    daily_returns = df["Close"].pct_change().dropna()

    mean_return = daily_returns.mean()
    std_dev = daily_returns.std()

    # Annualized metrics
    sharpe_ratio = ((mean_return - rf / 252) / std_dev) * np.sqrt(252)
    volatility = std_dev * np.sqrt(252)

    return pd.Series({
        "Sharpe_Ratio": round(sharpe_ratio, 4),
        "Volatility": round(volatility, 4)
    })

if __name__ == "__main__":
    from scripts.stock_data import load_stock_csv
    from scripts.technical_indicators import calculate_indicators

    ticker = "AAPL"
    df = load_stock_csv(ticker)
    df = calculate_indicators(df)

    metrics = calculate_metrics(df)
    print(f"📊 Financial Metrics for {ticker}\n{metrics}")
