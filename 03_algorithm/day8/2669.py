import sys
sys.stdin = open("input.txt")

def pprint(list_):
    for row in list_:
        print(*row)

# 101 * 101 이차원 리스트
graph = []
for _ in range(101):
    temp = [0] * 101
    graph.append(temp)


# 입력 줄 수
N = 4

for _ in range(N):
    number_list = input().split()

    x_s = int(number_list[0])
    y_s = int(number_list[1])
    x_e = int(number_list[2])
    y_e = int(number_list[3])
    # print(x_s,y_s,x_e,y_e)

    for y in range(y_s, y_e):
        for x in range(x_s, x_e):
            # print(x,y)
            graph[y][x] = 1

# pprint(graph)
# 점의 개수
# 1의 개수
# sum(리스트)

# 방법 1
# 점의 개수
# count = 0
# for y in range(10):
#     for x in range(10):
#         # 점이 찍혀있으면 점의 개수 + 1
#         if graph[y][x] == 1:
#             count += 1
# print(count)


# 방법 2
# 점의 개수
# count = 0 

# for y in range(10):
#     count += sum(graph[y])
# print(count)


# 선택 과제 : 셋을 활용한 방법