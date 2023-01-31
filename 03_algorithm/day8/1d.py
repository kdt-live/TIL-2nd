a = [1, 2, 3, 4, 5]
N = len(a)

# [1, 2, 3, 4, 5]
# n == 1 : [2, 3, 4, 5, 1]
# n == 2 : [3, 4, 5, 1, 2]

new_a = [None for _ in range(N)]
print(a, new_a)

for i in range(N):
    # 새로운 리스트에 
    new_a[i-5] = a[i]
    print(new_a)

# n == 1 : [5, 1, 2, 3, 4]
# n == 2 : [4, 5, 1, 2, 3]
n = 2
new_a = [None for _ in range(N)]
print(a, new_a)
for i in range(N):
    # 새로운 리스트에 
    print((i+n)%N)
    new_a[(i+n)%N] = a[i]
    print(new_a)

for n in range(5):
    print(a[-n:] + a[:-n])