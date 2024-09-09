import requests

API_KEY = '4IM6NYB49J4EUERE'
API_URL = "https://www.alphavantage.co/query"

def get_real_time_price(symbol):
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(API_URL, params=params)
    
    # Parse the response to JSON
    data = response.json()
    
    # Print the API response to inspect its structure
    print(data)
    
    # Now, try to access the real-time stock price (after inspecting the keys)
    if 'Global Quote' in data:
        stock_price = data['Global Quote'].get('05. price', 'N/A')  # Use .get() to avoid KeyError
    else:
        stock_price = 'N/A'
    
    return stock_price

