result = ['1', '5', '3', '4']

# 1534을 출력해야한다...?

# (1) print의 키워드(end)를 써서 출력한다. 
# (2-1) 반복하면서 문자열을 만든다. 

text = ''
for elem in result:
    text = text + elem 
print(text)

# (2-2) join 메서드
print(''.join(result))

# 1 5 3 4
print(' '.join(result))
