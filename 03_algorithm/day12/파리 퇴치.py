list_ = [
    [1, 3, 3, 6, 7],
    [8, 13, 9, 12, 8],
    [4, 16, 11, 12, 6],
    [2, 4, 1, 23, 2],
    [9, 13, 4, 7, 3],
]
N = 5
M = 2

max_fly_sum = 0

# 파리채의 시작점을 찾기위한 탐색
for y in range(0, N - M + 1):
    for x in range(0, N - M + 1):
        # print(y, x)
        
        # 파리채 영역의 파리의 수
        fly_sum = 0

        # 파리채의 영역 탐색
        for ym in range(y, y + M):
            for xm in range(x, x + M):
                # 죽인 파리의 수
                fly_sum += list_[ym][xm]
        
        # 가장 많이 죽인 파리의 수 갱신
        if max_fly_sum < fly_sum:
            max_fly_sum = fly_sum

print(max_fly_sum)
        