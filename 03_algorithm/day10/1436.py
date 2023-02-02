# https://www.acmicpc.net/problem/1436
# 백준 1436 영화감독 숌 

N = 500

# N번째
count = 0

movie_number = 666
while True:  
    # 숫자에 666 이 있는지?
    if '666' in str(movie_number):
        count += 1
 
    # 무한 반복문을 종료할 조건
    # N번째 나온 영화이름을 찾을 때
    if count == N:
        break

    # 3
    movie_number += 1



# N번째 영화 이름 출력
print(movie_number)