sumSec = 0
for hour in range(24):
    for minute in range(60):
        if '3' in str(hour) or '3' in str(minute):
           sumSec += 60

print(sumSec)

