import time as T1
import datetime as dt
import calendar

# asctime is a function which converts the time data type to string

localTime = T1.asctime(T1.localtime(T1.time()))
print('Time : ', localTime)

print('Date : ', dt.date.today())

t1 = dt.date.today()
print('Year', int(t1.year))
print('Month', int(t1.month))

print(calendar.month(2021, 1))
