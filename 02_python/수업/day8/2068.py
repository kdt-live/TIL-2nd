import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    # 코드 구현
    print(f'#{test_case} {max(map(int, input().split()))}')
