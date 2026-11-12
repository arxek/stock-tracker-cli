def separator():
  print('-' * 30)

def userinput():
  stop_words = ['q', 'stop', 'quit', ':q', '0', 'back', 'return', 'exit']
  choice = input('> ').strip().upper()
  if choice.lower() in stop_words:
    return '0'
  else:
    return choice

