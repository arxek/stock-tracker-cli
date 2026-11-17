def separator(): print('-' * 36)

def userinput():
  stop_words = ('q', 'stop', 'quit', ':q', '0', 'back', 'return', 'exit')
  choice = input('> ').strip().upper()
  if choice.lower() in stop_words:
    return '0'
  else:
    return choice

def main_menu(working_api):
  separator()
  print('Select your action')
  if working_api == '1':
    print('''\t1. Enter data
    \t2. Remove tickers
    \t3. Print the list
    \t4. Update prices and sectors
    \t5. Calculate average price
    \t6. Reports
    \t7. Quit''')

  else:
    print('''\t1. Enter data
    \t2. Remove tickers
    \t3. Print the list
    \tX. Update prices and sectors
    \tX. Calculate average price
    \tX. Reports
    \t7. Quit''')
    separator()
    
    match working_api:
      case 'ApiKeyNotFound':
        print('API key not found.')
      
      case 'ApiKeyWrong':
        print('API key is wrong.')

      case 'NoConnection':
        print('No internet connection or the server\nis unreachable.')

    print('Some functions are off')
    separator()
