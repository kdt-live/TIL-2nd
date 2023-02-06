import sys
# from pprint import pprint
sys.stdin = open("어디에 단어가 들어갈 수 있을까.txt")

# 2차원 리스트에서 하나의 행을 구분해서 출력
def pprint(arr):
    for row in arr:
        print(*row)

# 테스트케이스 수
T = int(input())

# 테스트케이스 수 만큼 순회
for t in range(1, T+1):
    # print(t)
    # 띄어쓰기로 구분된 정수 2개를 입력
    N, K = list(map(int, input().split()))
    # print(N, K)
    
    # 2차원 리스트 저장 변수
    grid = []
    
    # N x N 입력
    # N번 만큼 입력
    for _ in range(N):
        # 띄어쓰기로 구분된 정수 리스트를 입력
        temp_list = list(map(int, input().split()))
        # print(temp_list)
        grid.append(temp_list)
    
    # pprint(grid)

    # 탐색을 시작하기전에 출력 값을 초기화
    answer = 0

    # 가로 탐색
    # 열(x) -> 행(y)
    for y in range(N):
        empty_count = 0 
        for x in range(N):
            # print(f"행:{y} / 열:{x}")
            # print(grid[y][x])
            
            # K 만큼의 빈 공간이 있는지 확인

            # 흰공간(1)을 만났을 때
            if grid[y][x] == 1:
                # 빈공간의 개수를 1 증가
                empty_count += 1

            # 검은공간(0)을 만났을 때
            if grid[y][x] == 0:
                # 지금까지의 빈공간의 수가 K 확인
                if empty_count == K:
                    # 단어가 들어갈 수 있는 자리 1 증가
                    answer += 1

                # 빈공간의 수를 0 초기화
                empty_count = 0
        
        if empty_count == K:
            answer += 1

    
    # 세로 탐색
    # 행(y) -> 열(x) 
    for x in range(N):
        empty_count = 0 
        for y in range(N):
            # print(f"행:{y} / 열:{x}")
            # print(grid[y][x])
            
            # K 만큼의 빈 공간이 있는지 확인

            # 흰공간(1)을 만났을 때
            if grid[y][x] == 1:
                # 빈공간의 개수를 1 증가
                empty_count += 1

            # 검은공간(0)을 만났을 때
            if grid[y][x] == 0:
                # 지금까지의 빈공간의 수가 K 확인
                if empty_count == K:
                    # 단어가 들어갈 수 있는 자리 1 증가
                    answer += 1

                # 빈공간의 수를 0 초기화
                empty_count = 0
        
        if empty_count == K:
            answer += 1

    # #1 2
    print(f"#{t} {answer}")


