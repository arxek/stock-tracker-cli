from helpful import separator
from tickers import show_list


def make_report(stocks_list, reports_list, date, week=False, print_report=False):
  title = 'week-ago' if week else 'current'
  head_line = f'Stocks prices ({title}) - {date}'
  reports_list.clear()

  reports_list.append(head_line)

  # current
  if not week:
    for stock in stocks_list:
      if stock.update_current():
        new_line = stock.line()
        reports_list.append(new_line)
        if print_report:
          print(new_line)

  # week-ago
  else:
    for stock in stocks_list:
      if stock.update_week():
        new_line = stock.line(True)
        reports_list.append(new_line)
        if print_report and new_line is not None:
          print(new_line)

def avg_price(stocks_list, tickers_list, date):
  separator()
  print(f'Calculting average stocks prices on {date} for:')
  show_list(tickers_list, False)
  sum = 0
  count = 0
  for stock in stocks_list:
    if stock.update_current():
      sum += stock.price_now
      count += 1

  avg = sum / count
  print(f'Average price -> {avg:.2f} USD')

