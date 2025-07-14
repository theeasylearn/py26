from datetime import date
from datetime import datetime
from datetime import time

ts = date.fromtimestamp(1752230841)
print(ts)  # Output: 2012-01-01


#datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2025, 7, 11, 16, 25, 1, 123)
print(b)
print(b.timestamp())


c = time(16,26,0)
print("time =",c)
print("hour = ",c.hour)
print("minute",c.minute)
print("second",c.second)
print("microsecond",c.microsecond)