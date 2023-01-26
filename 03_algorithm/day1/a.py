numbers = [10, 2, 5, 7]

for number in numbers: 
    if number % 2 == 0:
        numbers.pop()
    print(number)


# 1. number 10 => pop => [10, 2, 5]
# 2. number 2 => pop => [10, 2]

# (1) 
# 별도의 리스트에 추가를 하거나, 관리를 하는 형태
# (2)
# 인덱스로 접근해서 값을 변화시켜..
# (3)
# 리스트를 copy해서 쓴다. 
