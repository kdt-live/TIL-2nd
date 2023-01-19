# https://www.acmicpc.net/problem/10988
# 팰린드롬 

# 1. Input
# word = '토마무우마토'
word = input()

# 2. 값 초기화(단어의 인덱스)
# start(시작) : 0
# end(끝) : len(word) - 1
start = 0 
end = len(word) - 1
is_pal = True

# 3. while
# start 값이 end보다 작을 때....
while start < end:
    # word[start], word[end] 비교해서 
    # 다르면, 팰린드롬이 아니다!
    if word[start] != word[end]:
        is_pal = False
        break
    # 매 반복이 끝나면
    # start는 1씩 증가하고
    # end는 1씩 감소
    start += 1
    end -= 1

# 4. 출력 
# 팰린드롬이면 1, 아니면 0을 출력한다.
if is_pal:
    print(1)
else: 
    print(0)

# print(int(is_pal))