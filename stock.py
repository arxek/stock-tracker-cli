import datetime as dt
from functools import wraps

from api import ApiKeyError, get_history, get_profile


def safe_api_call(func):
  @wraps(func)
  def wrapper(self, *args, **kwargs):
    try:
      func(self, *args, **kwargs)
      return True
    except ApiKeyError:
      raise
    except Exception:
      print(f'Wrong ticker or another issue with "{self.ticker}". Ticker skipped.')
      return False
  
  return wrapper


class Stock:
  def __init__(self, ticker):
    self.ticker = ticker
    self.sector = None
    self.price_now = None
    self.price_week = None
  
  @safe_api_call
  def update_current(self):
    profile = get_profile(self.ticker)
    sector = profile.get('sector')
    price = profile.get('price')
    if (not sector) or (price is None):
      raise ValueError('API didn\'t return price or sector')
    self.sector = sector
    self.price_now = round(price, 2)

  @safe_api_call
  def update_week(self):
    target = dt.date.today() - dt.timedelta(days=7)
    if self.sector is None and not self.update_current():
      return False

    start = target - dt.timedelta(days=5)
    history = get_history(self.ticker, start.isoformat(), target.isoformat())

    final_price = None
    for row in history:
      if (row['date'] <= target.isoformat()) and (final_price is None or row['date'] > final_price['date']):
        final_price = row

    if final_price is None:
      raise ValueError('Error while calculating week-ago price')

    self.price_week = round(final_price['close'], 2)

  def line(self, week=False):
    price = self.price_week if week else self.price_now
    try:
      return f'{self.ticker} ({self.sector}) -> {price:.2f} USD'
    except TypeError:
      pass
