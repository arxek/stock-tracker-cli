




import datetime as dt

from api import *
from helpful import *
from reports import *
from stock import Stock
from tickers import *

tickers_list = []
stocks_list = []
working_api = check_api_key()
#working_api = '1'

current_prices_report = []
week_prices_report = []

today_date = dt.date.today()
week_ago_date = today_date - dt.timedelta(days=7)
today_date = today_date.strftime('%d.%m.%Y')
week_ago_date = week_ago_date.strftime('%d.%m.%Y')

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

      # update stocks list
      stocks_list = [Stock(ticker) for ticker in tickers_list] 

#      |\      _,,,---,,_
#ZZZzz /,`.-'`'    -.  ;-;;,_
#     |,4-  ) )-,_. ,\ (  `'-'
#    '---''(_/--'  `-'\_)

    # 2. remove ticker
    case '2':
      show_list(tickers_list)
      remove_ticker(tickers_list)

      # update stocks list
      stocks_list = [Stock(ticker) for ticker in tickers_list]

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
      avg_price(stocks_list, tickers_list, today_date)

    # reports
    case '6':
      separator()
      print('Select or "stop"')
      print('''\t1. Save current report\n\t   to output.txt
      \t2. Save week-ago report\n\t   to output2.txt
      \t3. Save both
      \t4. Print current report
      \t5. Print week-ago report''')

      inputchoice = userinput()

      match inputchoice:
        # 6.0. back to menu
        case '0':
          pass

        # 6.1. current price report
        case '1':
          save_report(stocks_list, current_prices_report, today_date, 'output.txt', False)

        # 6.2. week-ago price report
        case '2':
          save_report(stocks_list, week_prices_report, week_ago_date, 'output2.txt', True)

        # 6.3. both report
        case '3':
          save_report(stocks_list, current_prices_report, today_date, 'output.txt', False)
          save_report(stocks_list, week_prices_report, week_ago_date, 'output2.txt', True)

        # 6.4. print current
        case '4':
          separator()
          if current_prices_report:
            for i in current_prices_report:
              print(i)

          else:
            print('No report found, update first')

        # 6.5. print week-ago
        case '5':
          separator()
          if week_prices_report:
            for i in week_prices_report:
              print(i)

          else:
            print('No report found, update first')



