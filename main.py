import datetime as dt

import requests

from api import *
from helpful import *
from stock import Stock
from tickers import *
from reports import *

tickers_list = []
stocks_list = []
#working_api = check_api_key()
working_api = '1'

current_prices_report = []
week_prices_report = []

today_date = dt.date.today()
week_ago_date = today_date - dt.timedelta(days=7)

while True:
  main_menu(working_api)
  mainchoice = userinput()

  match mainchoice:
    # 0. close everything
    case '0' | '7':
      break

    # 1. enter data
    case '1':
      separator()
      print('''select input (or "stop"):
      \t1.only terminal
      \t2.only txt
      \t3.both''')
      inputchoice = userinput()

      match inputchoice:
        # 1.0. back to menu
        case '0':
          pass

        # 1.1. only terminal
        case '1':
          add_ticker_from_input(tickers_list)

        # 1.2. only txt
        case '2':
          add_ticker_from_txt(tickers_list)

        # 1.3. both
        case '3':
          add_ticker_from_txt(tickers_list)
          add_ticker_from_input(tickers_list)

#      |\      _,,,---,,_
#ZZZzz /,`.-'`'    -.  ;-;;,_
#     |,4-  ) )-,_. ,\ (  `'-'
#    '---''(_/--'  `-'\_)

    # 2. remove ticker
    case '2':
      show_list(tickers_list)
      remove_ticker(tickers_list)

    # 3. print the list
    case '3':
      show_list(tickers_list)
    
    # 4. update prices and sectors
    # only with working api
    case '4' if working_api == '1':
      separator()
      print('''Select or "stop"
      \t1. Current prices + sectors
      \t2. Week-ago prices + sectors
      \t3. Both''')
      
      # update stocks list
      stocks_list = [Stock(ticker) for ticker in tickers_list] 
      
      inputchoice = userinput()

      separator()

      match inputchoice:
        # 4.0. back to menu
        case '0':
          pass

        # 4.1. current prices
        case '1':
          make_report(stocks_list, current_prices_report, today_date, False)

        #4.2 week-ago prices
        case '2':
          make_report(stocks_list, week_prices_report, week_ago_date, True)

        #4.3. both
        case '3':
          make_report(stocks_list, current_prices_report, today_date, False)
          make_report(stocks_list, week_prices_report, week_ago_date, True)

    # calculate average price
    # only with working api
    case '5':
      # update stocks list
      stocks_list = [Stock(ticker) for ticker in tickers_list]
      
      # avg current prices
      avg_price(stocks_list, tickers_list, today_date)

        
