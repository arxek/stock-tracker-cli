import datetime as dt
#import yfinance as yf
from helpful import *



while True:
  separator()
  print('wha u want to do')    #change
  print('\t1. Enter data\n\t2. another')
  mainchoice = userinput()

  match mainchoice:
    case 'q' | 'stop':
      break
    case '1':
      separator()
      print('select input:\n\t1.only txt\n\t2.only terminal\n\t3.both')
      inputchoice = userinput()
      print(inputchoice)

    case '1':
      print('ok1')

    case '2':
      print('bye')
