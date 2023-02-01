# https://www.acmicpc.net/problem/1652
# 백준 1652 누울 자리를 찾아라

grid = [
    ['.', '.', 'X', '.'],
    ['.', 'X', '.', '.'],
    ['X', '.', '.', '.'],
    ['.', '.', '.', '.'],
]
N = 4

# 가로로 누울 수 있는 자리 수
row_count = 0
for y in range(N):

    # 비어있는 공간 수
    empty_count = 0

    # 좌 -> 우 행 탐색
    for x in range(N):
        # 현재 탐색 좌표가 빈 공간 O
        if grid[y][x] == '.':
            empty_count += 1

        # 현재 탐색 좌표가 빈 공간 X
        if grid[y][x] == 'X':
            # 이전까지 빈 공간의 수가 2 이상이면
            if empty_count >= 2:
                # 누울 수 있는 자리 수 증가
                row_count += 1

            # 빈 공간의 수 초기화
            empty_count = 0

    # 이전까지 빈 공간의 수가 2 이상 이면
    if empty_count >= 2:
        row_count += 1

col_count = 0
for x in range(N):
    empty_count = 0
    for y in range(N):
        if grid[y][x] == '.':
            empty_count += 1

        if grid[y][x] == 'X':
            if empty_count >= 2:
                col_count += 1
            empty_count = 0

    if empty_count >= 2:
        col_count += 1

print(row_count, col_count)