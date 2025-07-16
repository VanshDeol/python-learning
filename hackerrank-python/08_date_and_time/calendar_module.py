import calendar
month , day , year = map(int, input().split())

day_index = calendar.weekday(year,month,day)

print(calendar.day_name[day_index].upper())
