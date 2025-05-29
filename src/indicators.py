def calculate_moving_average(df, window=10):
    return df['Close'].rolling(window=window).mean()

def calculate_rsi(df, window=14):
    # Placeholder logic, TA-Lib preferred
    return None

def calculate_macd(df):
    # Placeholder logic
    return None
