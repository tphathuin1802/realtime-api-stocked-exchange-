import ccxt
import pandas as pd

exchange = ccxt.binance({
    "apiKey": "7q4UD0XOGUJ2pwwctsJ5XJdfJUKpIPVyMcFNP2WXD1pzKxUR768L8bYvo8ioOq1w",
    "secret": "b7xl0BDKeI6BRi6r6LFCiImJmrsSyVWkWnlHJlV2WWc9Um6Z3jUZE07I6KUEuPpP",
    "enableRateLimit": True,
})
exchange.set_sandbox_mode(False)

def get_binance_data():
    try:
        price = exchange.fetch_ohlcv("BTC/USDT", "5m", limit=20)

        all_data = []
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
            all_data.append(data)

        df = pd.DataFrame(all_data, columns=["timestamp", "open", "high", "low", "close", "volume"])
        print(df)

    except Exception as e:
        print(f"Error fetching data: {e}")

get_binance_data()
