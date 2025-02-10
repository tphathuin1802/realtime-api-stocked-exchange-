import ccxt
import pandas as pd

exchange = ccxt.binance({
    "apiKey": "7q4UD0XOGUJ2pwwctsJ5XJdfJUKpIPVyMcFNP2WXD1pzKxUR768L8bYvo8ioOq1w",
    "secret": "secret api make my repo secret",
    "enableRateLimit": True,
})
exchange.set_sandbox_mode(False)

try:
    all_data = []  # Initialize as a list to store OHLCV data
    price = exchange.fetch_ohlcv("BTC/USDT", "5m", limit=20)
    balance = exchange.fetch_balance()

    # Fetching OHLCV data and converting to a readable format
    for i in price:
        readable_time = pd.to_datetime(i[0], unit="ms").strftime("%Y-%m-%d %H:%M:%S")
        data = {
            "timestamp": readable_time,
            "open": i[1],
            "high": i[2],
            "low": i[3],
            "close": i[4],
            "volume": i[5],
        }
        all_data.append(data)  # Append to the list

    # Create DataFrame from the fetched OHLCV data
    df = pd.DataFrame(all_data, columns=["timestamp", "open", "high", "low", "close", "volume"])
    print(df)

    # Fetch and display balance data separately
    df_balance = pd.DataFrame(balance['total']).reset_index()
    print(df_balance)

except Exception as e:
    print(f"Error fetching data: {e}")
