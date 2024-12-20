from binance.client import Client

api_key = "7q4UD0XOGUJ2pwwctsJ5XJdfJUKpIPVyMcFNP2WXD1pzKxUR768L8bYvo8ioOq1w"
api_secret = "b7xl0BDKeI6BRi6r6LFCiImJmrsSyVWkWnlHJlV2WWc9Um6Z3jUZE07I6KUEuPpP"
client = Client(api_key, api_secret)
client.API_URL = 'https://api.binance.com/api/v3/'
client.time_offset = None  # Tự động đồng bộ
