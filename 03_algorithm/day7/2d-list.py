import pprint
# 1. 손수 만들기
# matrix = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]

# 2. for문 활용 
# print([0] * 10)
# 4X3 행렬 만든다고 하면
N = 4 # 행
M = 3 # 열

matrix = []
for _ in range(N):
    # [0, 0, 0, ... 0] 
    matrix.append([0] * M)

pprint.pprint(matrix)

# 3. 리스트 컴프리헨션
# 반복하면서 append 특정 값을 할 때
# 어떠한 요소로 구성된 리스트 만들 때 

matrix = [[0] * M for _ in range(N)]
pprint.pprint(matrix)