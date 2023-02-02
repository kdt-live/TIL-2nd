# https://www.acmicpc.net/problem/1526
# 백준 1526 가장 큰 금민수

max_number = 0

# 파이썬은 1초에 1억번 연산(반복문)
N = 474747
for number in range(4, N + 1):
    string_temp = str(number)

    # 어떤 수가 4와 7을 제외한 숫자가 있는지 확인
    if not('0' in string_temp or 
        '1' in string_temp or
        '2' in string_temp or
        '3' in string_temp or
        '5' in string_temp or
        '6' in string_temp or
        '8' in string_temp or
        '9' in string_temp):
        # print(number,"금민수 입니다.")  
        max_number = number

print(max_number)
