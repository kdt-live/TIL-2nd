import datetime

# print(datetime.datetime.now())
# print(datetime.date(2023, 1, 5))

today = datetime.datetime.today()
# print(today)
# print(type(today))
# print(today.year)
# print(today.day)

end = datetime.datetime(2023, 6, 14)
print(f'우리가 개발자가 되는 시간... {end - today}')



