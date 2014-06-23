# custom time functions

from datetime import datetime, timedelta

def format_time(t):
    return t.strftime("%a %d-%b-%y")

def read_time(s):
    return datetime.strptime(s, "%d/%m/%y")

def now():
    return datetime.now()

def days_ago(days):
    return format_time(now() - timedelta(days=days))

def future(days):
    return format_time(now() + timedelta(days=days))
