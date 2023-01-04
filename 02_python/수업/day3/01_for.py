# for의 기본!
# 반복가능한 객체...
# 숫자통 
target_number = int(input())
result = 0

for n in range(1, target_number+1):
   result = n + result

print(result)