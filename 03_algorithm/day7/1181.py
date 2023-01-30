import sys

sys.stdin = open("input.txt")

N = int(input())

# 단어의 수
# print(N)

# 딕셔너리
# 키 : 단어 / 밸류 : 단어의 길이
word_len = dict()

# 단어의 수만큼 반복문
for _ in range(N):
    word = input()
    
    # 입력받은 단어
    # print(word)
    word_len[word] = len(word)


# 단어와 단어의 길이를 저장한 딕셔너리
# print(word_len)

# 정렬은 어떤 함수를 사용해야하나?
# sorted(값, 정렬 기준)

# 딕셔너리를 정렬할 때 출력해야하는 값
# print(word_len.items())

# sorted 정렬 기준이 2개 이상일 때 -> 튜플 형태
sorted_word_len = sorted(word_len.items(), key = lambda x:(x[1],x[0]))
# print(sorted_word_len)

# 정렬한 값을 순회하며 출력
for value in sorted_word_len:
    print(value[0])