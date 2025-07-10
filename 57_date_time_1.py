import datetime

current_date = datetime.datetime.now()
print(current_date)
print("current year",current_date.year)
print("current month",current_date.month)

print("current day",current_date.day)

from datetime import date
date1 = date(1200,3,21)
print(date1)