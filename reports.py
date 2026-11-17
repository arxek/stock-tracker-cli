from helpful import separator
from tickers import show_list


def make_report(stocks_list, reports_list, date, week=False, print_report=False, print_update=True):
  title = 'week-ago' if week else 'current'
  head_line = f'Stocks prices ({title}) - {date}'
  reports_list.clear()

  reports_list.append(head_line)
  
  count = 0

  # current
  if not week:
    for stock in stocks_list:
      if stock.update_current():
        new_line = stock.line()
        reports_list.append(new_line)
        count += 1
        if print_report:
          print(new_line)

  # week-ago
  else:
    for stock in stocks_list:
      if stock.update_week():
        new_line = stock.line(True)
        reports_list.append(new_line)
        count += 1
        if print_report and new_line is not None:
          print(new_line)
  if print_update:
    print(f'{count} tickers have been updated. ({title})')

def avg_price(stocks_list, tickers_list, date):
  separator()
  print(f'Calculting average stocks prices\non {date} for:')
  show_list(tickers_list, False)
  total = 0
  count = 0
  for stock in stocks_list:
    if stock.price_now is None and not stock.update_current():
      continue
    
    total += stock.price_now
    count += 1

  if count == 0:
    print('No prices available.')
    return

  avg = total / count
  print(f'Average price -> {avg:.2f} USD')

def save_report(stocks_list, reports_list, date, filename, week=False):
  if not reports_list:
    make_report(stocks_list, reports_list, date, week)

  with open(filename, 'w', encoding='utf-8') as f:
    f.write('\n'.join(reports_list) + '\n')


