description = """
Iterate through a whole year, counting how many days fall on a specific
weekday, and how many working days there are. Manually include
a list of holidays.
"""

from datetime import date, timedelta
from calendar import day_abbr, isleap

WKDAYS = list(day_abbr)

def numberOfWeekdays(year, targetWkdayAbbr):
    targetWkday = WKDAYS.index(targetWkdayAbbr)
    months = [0] * 13
    days = 366 if isleap(year) else 365
    # print("DAYS", days)
    cur = date(year, 1, 1)
    for i in range(DAYS):
        if cur.weekday() == targetWkday:
            months[cur.month] += 1
        cur += timedelta(days=1)
    return months


def test():
    testeql(sum(numberOfWeekdays(2018, 'Mon')), 53)
    testeql(sum(numberOfWeekdays(2018, 'Tue')), 52)
    testeql(sum(numberOfWeekdays(2017, 'Sun')), 53)

def iterateWkday(year):
    for wkday in WKDAYS:
        lst = numberOfWeekdays(year, wkday)
        print(wkday, lst, lst.count(5))
