# (1, 1)
# 위와 같은 조합이 들어왔을 때 상하좌우를 모두 출력하는 코드!

# 상 (i-1, 0)
# 하 (i+1, 0)
# 좌 (0, j-1)
# 우 (0, j+1)

x = 0 
y = 0
print(x, y)

# 상하좌우
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for dx, dy in delta:
    print(x + dx, y + dy)