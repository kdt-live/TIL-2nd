from pprint import pprint
# 인접 행렬 
# 7 * 7 
# 정점간의 관계를 표현하고 있는 행렬
# 정접의 개수인 N에 의해 크기가 정해짐

N = 7
M = 7 # Input 수이면서 간선의 개수....

graph = [[0] * N for _ in range(N)]

pprint(graph)
# [[0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0]]

# Input 
# 0 1
# 0 2
# 1 3
# 1 4
# 2 4 
# 2 5
# 4 6

# # 1....  0 1
# graph[0][1] = 1
# graph[1][0] = 1
# # 2..... 0 2
# graph[0][2] = 1
# graph[2][0] = 1 
# # 3..... 1 3 
# graph[1][3] = 1
# graph[3][1] = 1

for _ in range(M):
    # input() 예시 : 0 1
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

pprint(graph)