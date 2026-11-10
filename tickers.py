#from yfinance import ticker

from helpful import separator, userinput

def add_ticker_from_input(ls):
  while True:
    separator()
    print(f'enter your data or "stop" ({len(ls)})')
    tickerinput = userinput()

    if tickerinput in ('q', 'stop'):
      break

    else:
      ls.add(tickerinput)

def add_ticker_from_txt(ls, txt='input.txt'):
  rowscount = 0
  with open(txt, 'r') as f:
    for row in f:
      ls.add(row[:-1].lower())
      rowscount += 1
  separator()
  print(f'Found {rowscount} ticker(s) in input.txt')

# unused
def show_list_short(ls):
  separator()
  tickers_short = ''
  for i in ls:
    tickers_short = tickers_short + i.upper() + ' '
  
  print('Availabe tickers:', tickers_short)

def remove_ticker(ls):
  while True:
    separator()
    tickerinput = userinput()

    if tickerinput in ('q', 'stop'):
      break
    
    else:
      try:
        ls.remove(tickerinput)
        print(f'Ticker "{tickerinput.upper()}" was successfuly removed ({len(ls)} left)')
      
      except KeyError:
        print(f'Ticker "{tickerinput.upper()}" was not found ({len(ls)} left)')


def show_list(ls):
  separator()
  print('Available tickers:')
  for i in ls:
    print('\t', i.upper())
