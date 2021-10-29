from datetime import datetime
from datetime import timedelta


now = datetime.now()
print(now)
print(f"year = {now.year}")
print(f"month = {now.month}")
print(f"day = {now.day}")
print(f"hour = {now.hour}")
print(f"minute = {now.minute}")
print(f"second = {now.second}")
print(f"microsecond = {now.microsecond}")
print(f"weekday = {now.weekday()}")

print(now.strftime("%d.%m.%Y %H:%M:%S %A %W %j"))


d1 = now + timedelta(days=1, hours=10, minutes=10)
print(d1)
