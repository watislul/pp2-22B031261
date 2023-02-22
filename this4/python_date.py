import datetime

# Write a Python program to subtract five days from current date.
res = datetime.date.today()
res = res.replace(day = res.day - 5)
print(res)

# Write a Python program to print yesterday, today, tomorrow.

today = datetime.date.today()
yesterday = today.replace(day = today.day - 1)
tomorrow = today.replace(day = today.day + 1)
print(yesterday, today, tomorrow)

# Write a Python program to drop microseconds from datetime.

print(datetime.datetime.now().isoformat(timespec='milliseconds'))

# Write a Python program to calculate two date difference in seconds.

date1 = datetime.datetime.today()
epochtime = datetime.datetime(1970, 1, 1)
deltatime = date1 - epochtime
print(f"Time difference in seconds: {deltatime.total_seconds()}")