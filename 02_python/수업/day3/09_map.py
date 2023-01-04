# 함수 객체
# 함수는 그 자체로 객체이다!
print(len)
print(type(len))

# 함수 호출
# Input을 넣어서 함수를 실행시켰다!
print(len([1, 2, 3]))

# map 함수

numbers = ['1', '2', '3']
result = 0
for number in numbers:
    result += int(number)
print(result)

numbers = ['1', '2', '3']
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)

# 첫번째 인자(Input)으로 함수를 받아서
# 두번째 인자(Input)인 반복 가능한 객체의 모든 요소에 적용!
numbers = ['1', '2', '3']
new_new_numbers = map(int, numbers)
print(new_new_numbers)
print(list(new_new_numbers))