from datetime import date, timedelta

def checkio(from_date, to_date):
    # 5 and 6 are weekend
    weekend_days = 0
    cur_date = from_date
    while cur_date <= to_date:
        if cur_date.weekday() > 4:
            weekend_days += 1
        cur_date = cur_date + timedelta(days=1)
    return weekend_days
    
checkio(date(2013, 1, 1), date(2013, 2, 1))
checkio(date(2014, 2, 8), date(2014, 2, 9))
