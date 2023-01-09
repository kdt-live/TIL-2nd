drama = {'name': '더 글로리', 'writer': '김은숙'}
print(drama['name'])
# print(drama['director']) # KeyError
print(drama.get('director')) # None


students = {'홍엽': 89, '민지': 20, '소담': 47}
print(students['홍엽'])
print(students.get('길동', 0))