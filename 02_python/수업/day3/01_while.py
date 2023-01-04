
target_number = int(input())
n = 0
result = 0
# 조건 : target_number >= n
# 반복 때마다 n+=1, result 더하기!

while target_number >= n:
    result += n
    n += 1
    # print(result, n)
print(result)