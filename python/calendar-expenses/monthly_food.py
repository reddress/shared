from datetime import date, timedelta
from calendar import day_abbr, monthrange

def restaurant_expenses(year, month):
    first_day = date(year, month, 1)
    # last_day = date(year, month, monthrange(year, month)[1])
    days_to_count = monthrange(year, month)[1]

    weekday_expense = 12 * 2  # cheap lunch
    weekend_expense = 45 * 2  # expensive dinner for two

    total = 0
    
    for i in range(days_to_count):
        d = first_day + timedelta(days=i)
        wkdy = day_abbr[d.weekday()]

        if wkdy == "Sat" or wkdy == "Sun":
            total += weekend_expense
        else:
            total += weekday_expense

    print(total)
