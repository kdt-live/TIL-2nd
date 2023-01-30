import sys

# heapq 모듈 import
from heapq import heapify,heappop,heappush

sys.stdin = open("input.txt")

# input() 보다 빠른 입력 방법
N = int(sys.stdin.readline().strip())

# 연산의 개수
# print(N)

# 연산을 저장할 리스트
number_list = []

for _ in range(N):
    number = int(sys.stdin.readline().strip())

    # 입력받은 연산
    # print(number)

    # heappop
    if number == 0:
        # heap이 비어있을때
        if len(number_list) == 0:
            pass
            
        # heap이 비어있지 않을 때
        elif len(number_list) != 0:
            pass
        

    # heappush
    elif number != 0:
        # (절대값, 원본값) push
        heappush(number_list, (abs(number), number))
        # print(number,number_list)