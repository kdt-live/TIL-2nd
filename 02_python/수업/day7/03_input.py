print('홍엽', '유영', '윤원', '진아')


def add(*numbers):
    # print(type(numbers)) # tuple
    result = 0
    for n in numbers: 
        result += n
    return result

print(add(1, 2, 3, 10, 23))

def movie(**kwargs):
    return kwargs

print(movie(name='더 글로리', writer='김은숙'))

# open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# open('README.md', 'r', encoding='UTF8')
# open('README.md', mode='r', encoding='UTF8')
# open('README.md', 'r', 'UTF8') # 다르게 동작! 왜? buffering이 세번째!