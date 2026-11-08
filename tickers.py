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
  with open(txt, 'r') as f:
    for row in f:
      ls.add(row[:-1])

def show_list(ls):
  separator()
  print('Available tickers:')
  for i in ls:
    print('\t', i.upper())
