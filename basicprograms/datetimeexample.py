'''
import datetime
import time
print(time.time())
print(time.asctime())

samhitha=datetime.datetime.now()
print(samhitha)
print("year:",samhitha.year)
'''
'''
import calendar
s=calendar.prcal(3023)
s2=calendar.month(1999,5)
s1=calendar.isleap(2005)
print(s2)
'''
'''
import datetime
x=datetime.datetime.now()
from datetime import timedelta
print(x+ timedelta(days=-89))
'''
import time
from datetime import datetime
import pytz
time1=pytz.timezone('America/New_york')
print("current time is:",datetime.now(time1))