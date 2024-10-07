import calendar
from datetime import date

today_date = date.today()
today_date_day = today_date.day
x = calendar.month_name[today_date.month]
print(x + " " + str(today_date_day + 1))








