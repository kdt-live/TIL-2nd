# 정수형 숫자 다섯 개를 입력 받고, 입력할 때 마다 입력한 정수형 숫자들의 합을 출력하세요.

# 출력 예시
# 첫 번째 정수형 숫자를 입력해주세요 > 1  # 사용자 입력
# 1
# 두 번째 정수형 숫자를 입력해주세요 > 2  # 사용자 입력
# 3
# 세 번째 정수형 숫자를 입력해주세요 > 3  # 사용자 입력
# 6
# 네 번째 정수형 숫자를 입력해주세요 > 4  # 사용자 입력
# 10
# 다섯 번째 정수형 숫자를 입력해주세요 > 5 # 사용자 입력
# 15

n1 = int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
print(n1)
n2 = int(input('두 번째 정수형 숫자를 입력해주세요 > '))
print(n1 + n2)
n3 = int(input('세 번째 정수형 숫자를 입력해주세요 > '))
print(n1 + n2 + n3)
n4 = int(input('네 번째 정수형 숫자를 입력해주세요 > '))
print(n1 + n2 + n3 + n4)
n5 = int(input('다섯 번째 정수형 숫자를 입력해주세요 > '))
print(n1 + n2 + n3 + n4 + n5)

# result = 0
# n1 = int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
# result = result + n1
# print(result)
# n2 = int(input('두 번째 정수형 숫자를 입력해주세요 > '))
# result = result + n2
# print(result)
# n3 = int(input('세 번째 정수형 숫자를 입력해주세요 > '))
# result = result + n3
# print(result)
# n4 = int(input('네 번째 정수형 숫자를 입력해주세요 > '))
# result = result + n4
# print(result)
# n5 = int(input('다섯 번째 정수형 숫자를 입력해주세요 > '))
# result = result + n5
# print(result)

# result = 0
# n1 = int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
# result += n1
# print(result)
# n2 = int(input('두 번째 정수형 숫자를 입력해주세요 > '))
# result += n2
# print(result)
# n3 = int(input('세 번째 정수형 숫자를 입력해주세요 > '))
# result += n3
# print(result)
# n4 = int(input('네 번째 정수형 숫자를 입력해주세요 > '))
# result += n4
# print(result)
# n5 = int(input('다섯 번째 정수형 숫자를 입력해주세요 > '))
# result += n5
# print(result)

# MESSAGE = ' 번째 정수형 숫자를 입력해주세요 > '
result = 0
result += int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
print(result)
result += int(input('두 번째 정수형 숫자를 입력해주세요 > '))
print(result)
result += int(input('세 번째 정수형 숫자를 입력해주세요 > '))
print(result)
result += int(input('네 번째 정수형 숫자를 입력해주세요 > '))
print(result)
result += int(input('다섯 번째 정수형 숫자를 입력해주세요 > '))
print(result)