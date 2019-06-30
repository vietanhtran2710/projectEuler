import datetime
count = 0
for year in range(1901, 2001):
	for month in range(1, 13):
		d = datetime.date(year, month, 1)
		if datetime.date.weekday(d) == 6:
			count += 1
print(count)
