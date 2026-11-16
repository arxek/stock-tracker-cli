import datetime as dt

import requests

from api import *
from helpful import *
from stock import Stock
from tickers import *
from reports import *

tickers_list = []
stocks_list = []
working_api = check_api_key()

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

          make_report(stocks_list, current_prices_report, False, True)

        #4.2 week-ago prices
        case '2':
          if week_prices_report:
            for row in week_prices_report:
              print(row)

          else:
            for stock in stocks_list:
              if stock.update_week():
                new_stock_line = stock.line(True)
                print(new_stock_line)
                week_prices_report.append(new_stock_line)

        #4.3. both
        case '3':
          print()

    # calculate average price
    # only with working api
    case '5':
      separator()
      print('''Calculate avegare price or "stop"
      \t1. Current prices
      \t2. Week-ago prices''')
      
      # update stocks list
      stocks_list = [Stock(ticker) for ticker in tickers_list]
      
      inputchoice = userinput()

      match inputchoice:
      # 5.0. back to menu
        case '0':
          pass

        # avg current prices
        case '1':
          print('')
          avg_current

        
