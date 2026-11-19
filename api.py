import requests

BASE_URL = 'https://financialmodelingprep.com/stable'

# response = requests.get(url, params={'symbol': symbol, 'apikey': key}, timeout=10)
# data = response.json()[0]

class ApiKeyError(Exception):
  'API key problem'

def load_api_key():
  try:
    with open('API_KEY.txt', 'r', encoding='utf-8') as f:
      return f.readline().strip()
  except FileNotFoundError:
    return '0'

def check_api_key():
  key = load_api_key()
  if key in ('0', ''):
    return 'ApiKeyNotFound'

  try:
    response = requests.get(f'{BASE_URL}/profile', params={'symbol': 'AAPL', 'apikey': key}, timeout=10)
    response.raise_for_status()

  # wrong API key
  except requests.HTTPError as error:
    if error.response is not None and error.response.status_code in (401, 403):
      return 'ApiKeyWrong'

  # Internet issues
  except (requests.ConnectionError, requests.Timeout, requests.RequestException):
    return 'NoConnection'

  try:
    data = response.json()
  except requests.exceptions.JSONDecodeError:
    return 'ApiKeyWrong'

  if not isinstance(data, list):
    return 'ApiKeyWrong'
  
  return '1' #True


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

