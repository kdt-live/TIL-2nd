# https://www.acmicpc.net/problem/9455
# 백준 9455 박스

grid = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 1],
    [1, 1],
]

m = 5  # 세로(행)
n = 2  # 가로(열)

# 탐색 방향은???????
# 행 우선 -> y축을 먼저 움직여야하는지
# 열 우선 -> x축을 먼저 움직여야하는지

# 박스 이동
move_dis = 0

for x in range(n):
    for y in reversed(range(m)) :
        # print(y, x, grid[y][x])

        # 박스를 이동시키기위해
        # 박스를 찾자!
        if grid[y][x] == 1:
            # 조건이 만족하면
            # 박스를 이동
            while True:
                # 조건을 작성할 때
                # 최우선 순위는
                # 범위를 체크하는 것

                # 조건 1를 만족하는지?
                # 다음 위치가 범위를 벗어나면 박스 이동 X
                if y+1 == m:
                    break

                # 조건 2을 만족하는지?
                # 다음 위치에 박스가 있을 때 박스 이동 X
                if grid[y+1][x] == 1:
                    break
                
                # 현재 위치는 비우고,
                grid[y][x] = 0

                # 다음 위치로 박스가 이동
                grid[y+1][x] = 1

                # 박스 이동 거리 + 1
                move_dis += 1

                # 다음 위치 탐색
                y += 1

# def pprint(arr):
#     for a in arr:
#         print(*a)

# pprint(grid)
print(move_dis)