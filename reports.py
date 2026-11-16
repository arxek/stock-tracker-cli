from stock import Stock

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
        new_line = stock.line()
        reports_list.append(new_line)
        if print_report:
          print(new_line)


