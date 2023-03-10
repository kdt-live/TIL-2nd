"""
0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 
먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고,
그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
 다음 예를 보자.

26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 
새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.
"""

# N 기준 / 반복문을 끝낼 기준 
# 기준은 바뀌면 X
N = input()

# N을 복사한 변수
given_n = N

# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만든다.
if int(given_n) < 10:
    given_n = "0" + given_n # 앞에 0붙여서 두 자리수로 만든다.

# 사이클 횟수
cnt = 0
while True:
    #  각 자리의 숫자를 더한다. 
    first = given_n[-1] # 1의 자리 수 
    second = given_n[0] # 10의 자리 수
    sum_number = int(first) + int(second)

    # 주어진 수의 가장 오른쪽 자리 수와 
    # 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
    # 주어진 수 N 
    # 구한 합 sum_number
    new_number = given_n[-1] + str(sum_number)[-1]
    
    # print(new_number)

    # 연산 횟수 증가(사이클 횟수 증가)
    cnt += 1

    # 새로운 수가 기준과 같으면 반복문을 종료
    if int(new_number) == int(N):
        break

    # new_number를 다시 N에 넣어줘요.
    # N의 값을 새로운 수를 저장하면?
    given_n = new_number

print(cnt)