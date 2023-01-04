word = 'banana'

# a를 만나면 1을 출력하고 종료하세요.
# break : 반복 종료
for char in word:
    if char == 'a':
        print(1)
        break

print('============')
# a를 제외하고 모두 출력하세요.

# continue : 다음 반복을 실행
for char in word:
    if char == 'a':
        continue
    print(char)

for char in word:
    if char != 'a':
        print(char)