import datetime as dt
import requests
from helpful import *
from tickers import *
from api import *

tickers_list = [] 

while True:
  separator()
  print('What do you want to do')    #change
  print('''\t1. Enter data
  \t2. Remove tickers
  \t3. Print the list
  \t4. Update prices and sectors
  \t5. Calculate average price
  \t6. Reports
  \t7. Quit''')

  if not check_api_key():#not check_api_key():
    separator()
    print('! API key not found\n! Some functions might not work')
  mainchoice = userinput()

  match mainchoice:
    case '0' | '7':
      break

    # enter data
    case '1':
      separator()
      print('''select input (or "stop"):
      \t1.only terminal
      \t2.only txt
      \t3.both''')
      inputchoice = userinput()

      match inputchoice:
        case '0':
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

    # remove ticker
    case '2':
      show_list(tickers_list)
      remove_ticker(tickers_list)

    # print the list
    case '3':
      show_list(tickers_list)
    
    # update prices and sectors
    case '4':
      separator()
      print('''Select or "stop"
      \t1. Current prices + sectors
      \t2. Week-ago prices + sectors
      \t3. Both''')
      inputchoice = userinput()

