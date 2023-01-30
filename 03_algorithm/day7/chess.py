# 1. 8 * 8
# text = '.F.F...F'
# # 어떻게 바꾼다?
# # ['.', 'F', '.', ..., 'F']
# list(text)

import pprint

# 1-1. 반복문
matrix = []
for _ in range(8):
    # text = '.F.F...F'
    matrix.append(list(input()))

pprint.pprint(matrix)

# 1-2. list comprehension
# line = '.F.F...F'
matrix = [list(input()) for _ in range(8)]

# 2. 3X3
# line = '1 2 3'
# [1, 2, 3]
matrix = [ list(map(int, input().split())) for _ in range(3)]

# matrix = []
# for _ in range(3):
#     matrix.append(__________________)