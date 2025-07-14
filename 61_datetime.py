from datetime import datetime, date
#gap between date using date class
t1 = date(year = 1999, month = 3, day = 18)
t2 = date(year = 2025, month = 7, day = 11)
t3 = t2 -t1 #different is returned in days & hour minute and second

print("t3 =", t3)
#gap between date using datetime class
t4 = datetime(year = 1999, month = 3, day = 18, hour = 5, minute = 30, second = 33)
t5 = datetime(year = 2025, month = 7, day = 11, hour = 16, minute = 35, second = 13)
t6 = t5 - t4 #different is returned in days & hour minute and second
print("t6 =", t6)
print("total seconds =", t6.total_seconds()) #different in second
