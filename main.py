import datetime as dt
#import yfinance as yf
from helpful import *
from tickers import *

tickers_list = set()

while True:
  separator()
  print('wha u want to do')    #change
  print('\t1. Enter data\n\t2. another')
  mainchoice = userinput()

  match mainchoice:
    case 'q' | 'stop':
      break

    # enter data
    case '1':
      separator()
      print('select input:\n\t1.only terminal\n\t2.only txt\n\t3.both')
      inputchoice = userinput()
      
      match inputchoice:
        case 'q' | 'stop':
          pass

        # only terminal
        case '1':
          while True:
            separator()
            print(f'enter your data or "stop" ({len(tickers_list)})')
            tickerinput = userinput()

            if tickerinput in ('q', 'stop'):
              break

            else:
              add_ticker_from_input(tickers_list, tickerinput)

        # only txt
        case '2':
          pass

    case '2':
      print('bye')
