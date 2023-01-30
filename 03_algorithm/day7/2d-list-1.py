N = 4
M = 3

matrix = [[0] * M] * N 
print(matrix)
matrix[0][0] = 1
print(matrix)

print('====================')

matrix2 = [[0] * M for _ in range(N)]
print(matrix2)
matrix2[0][0] = 1
print(matrix2)


# 리스트 복사
a = [1, 2, 3]
b = list(a) # a[:]
a[0] = 100

# deepcopy