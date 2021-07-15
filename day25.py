from datetime import datetime, date , timedelta
print("______________________________________________")
# 1.	Write a Python program to convert a string to datetime


date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
print(date_object)
print("______________________________________________")
# 2.	Write a Python program to subtract five days (last working day) from current date


dt = date.today() - timedelta(5)
print('Current Date :', date.today())
print('5 days before Current Date :', dt)
print("______________________________________________")
# 3.	Write a Python program to convert the date to datetime using a function


dt = date.today()
print(datetime.combine(dt, datetime.min.time()))
print("______________________________________________")
# 4.	Write a Python program to print next 7 days (week) starting from today

import datetime
base = datetime.datetime.today()
for x in range(0, 7):
      print(base + datetime.timedelta(days=x))
