import time
import calendar
print(time.localtime())
localtime=time.localtime(time.time())
print("current time is",localtime)
cal=calendar.month(2018,9)
print("9th month is")
print(cal)