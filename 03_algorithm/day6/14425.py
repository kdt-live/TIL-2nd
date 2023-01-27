
S = ['baekjoononlinejudge','startlink','codeplus','sundaycoding','codingsh']

words = ['baekjoon','codeplus','codeminus','startlink','starlink','sundaycoding',
'codingsh','codinghs','sondaycoding','startrink','icerink']

# list 탐색 
cnt = 0 

for word in words:
    if word in S: # O(N)
        cnt += 1
print(cnt)

# set 탐색
cnt = 0 

S = set(S)
for word in words: # N
    if word in S: # O(1)
        cnt += 1
print(cnt)

# set 연산!
print(len(set(S) & set(words)))