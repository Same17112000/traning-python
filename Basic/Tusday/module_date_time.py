import datetime

mytime = datetime.time(2,20,20)
print(mytime)

today = datetime.date.today()
print(today)

print(today.ctime())

# /////////////////////////////////////////
from datetime import datetime

mydatetime = datetime(2024,3,19,14,39,59)
print(mydatetime)

# change year
print(mydatetime.replace(year=2021))


# ////////////////////////////////////////
from datetime import date
date1 = date(2024,3,19)
date2 = date(2023,4,19)
result = date1 - date2
print(result)
print(type(result))
print(result.days)



