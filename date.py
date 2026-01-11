from datetime import datetime
from datetime import timedelta
#from datetime import date
#from datetime import time

# import datetime

simdi = datetime.now()

result = datetime.now()
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y')
result = datetime.strftime(simdi,'%Y %B %A')

t = '7 December 2025 hour 12:12:43'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1983,5,9,12,30,00)

result = datetime.timestamp(birthday) # saniye
result = datetime.fromtimestamp(result) # saniye to datetime
result = datetime.fromtimestamp(0)

result = simdi - birthday # timedelta


# result = result.days
# result = result.seconds
print(simdi)
# result = simdi + timedelta(days=10)
# result = simdi + timedelta(days=730, minutes = 10)
result = simdi - timedelta(days = 10)
print(result)