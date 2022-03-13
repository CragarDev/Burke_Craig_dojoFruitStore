import datetime
from datetime import time

# time().isoformat(timespec='minutes')
# today = datetime.datetime.now()
# print(today.strftime("%B %d, %Y"))
# t = time()
# print(t.hour)
# print(t.minute)
# print(t)

now = datetime.datetime.now()
t = now.strftime('%H:%M:%S')
# print("Current date and time: ")
# print(str(now))

# print(help(time))
# print("Current date and time: ")
# print(now.strftime('%Y-%m-%d %H:%M:%S'))
# print(now.strftime('%I:%M:%S'))


if int(t[0:2])< 12:
    clk = "PM"
else:
    clk = "AM"
    
print(clk)

# t = time()
# for i in t:
#     print(i)

# print(t)
# t = time()

# t.strftime("%I:%M%p")
'Tuesday, 21. November 2006 04:30PM'
# print('The {3} is {0:%I:%M%p}.'.format(t,"time"))
'The day is 21, the month is November, the time is 04:30PM.'


# print(time.asctime())
'Fri Mar  1 12:56:07 2019'

# time(hour=12, minute=34, second=56, microsecond=123456).isoformat(timespec='minutes')

# t = time(hour=12, minute=34, second=56)
# # dt.isoformat(timespec='microseconds')

# # dt.isoformat(timespec='auto')

# print(t)