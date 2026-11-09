import datetime as dt
import yfinance as yf
from helpful import *
from tickers import *

tickers_list = set()

while True:
  separator()
  print('wha u want to do')    #change
  print('''\t1. Enter data
    \t2. Remove tickers
    \t3. print the list
    \t4.''')
  mainchoice = userinput()

  match mainchoice:
    case 'q' | 'stop':
      break

    # enter data
    case '1':
      separator()
      print('''select input:
        \t1.only terminal
        \t2.only txt
        \t3.both''')
      inputchoice = userinput()
      
      match inputchoice:
        case 'q' | 'stop':
          pass

        # only terminal
        case '1':
          add_ticker_from_input(tickers_list)

        # only txt
        case '2':
          add_ticker_from_txt(tickers_list)

        # both
        case '3':
          add_ticker_from_txt(tickers_list)
          add_ticker_from_input(tickers_list)

#      |\      _,,,---,,_
#ZZZzz /,`.-'`'    -.  ;-;;,_
#     |,4-  ) )-,_. ,\ (  `'-'
#    '---''(_/--'  `-'\_)

    case '2':
      show_list(tickers_list)
      remove_ticker(tickers_list)

    # print the list
    case '3':
      show_list(tickers_list)
