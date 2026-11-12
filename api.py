import requests
import datetime as dt

BASE_URL = 'https://financialmodelingprep.com/stable'

# response = requests.get(url, params={'symbol': symbol, 'apikey': key}, timeout=10)
# data = response.json()[0]

def load_api_key():
  with open('API_KEY.txt', 'r', encoding='utf-8') as f:
    return f.readline().strip()

def get_profile(symbol):
  response = requests.get(f'{BASE_URL}/profile', params={'symbol': symbol, 'apikey': load_api_key()}, timeout=10)
  
  #response.raise_for_status()
  data = response.json()

  if not isinstance(data, list) or not data:
    raise ValueError('Ticker not found')

  return data[0] # get dictionary

def get_history(symbol, from_date, to_date):
  response = requests.get(f'{BASE_URL}/historical-price-eod/full', params={"symbol": symbol, "from": from_date, "to": to_date,"apikey": load_api_key()},timeout=10)

  response.raise_for_status()
  data = response.json()

  if not isinstance(data, list) or not data:
    raise ValueError('Ticker not found')

  return data

print(get_history('AAPL', '2026-10-31', '2026-11-05'))
