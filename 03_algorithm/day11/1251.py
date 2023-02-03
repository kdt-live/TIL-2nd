
# 가장 작은 값이 index = 0 위치하는 자료구조
from heapq import *

string = "mobitel"

N = len(string)

# string_list = []

string_heap = []

# i 와 j 를 순회하는 이중 for문
for i in range(1, N - 1):
    for j in range(i + 1, N):
        a = string[0:i]
        b = string[i:j]
        c = string[j:N]

        # print(a,b,c)

        reversed_a = a[::-1]
        reversed_b = b[::-1]
        reversed_c = c[::-1]

        join_string = reversed_a + reversed_b + reversed_c

        # 사전적으로 가장 앞에 나오는 단어는 무엇인가요?
        # 모든 합친 문자열을 하나의 리스트에 다 저장
        # string_list.append(join_string)
        heappush(string_heap, join_string)
    

# bometil
# 리스트에 저장된 값 중 가장 작은 값 출력
# print(min(string_list))
print(heappop(string_heap))

