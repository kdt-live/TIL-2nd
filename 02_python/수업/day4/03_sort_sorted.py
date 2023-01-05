# .sort() : 메서드
# return : None
# 해당 리스트 자체를 정렬!
numbers = [10, 2, 5]
result = numbers.sort()
print(result) # None
print(numbers)


numbers = [10, 2, 5]
numbers.sort()
print(numbers)

# sorted() : 함수
# return : 정렬된 리스트
numbers = [10, 2, 5]
result = sorted(numbers)
print(result) # [2, 5, 10]