string = "KARIJERA"

compare_word = "CAMBRIDGE" # 비교 알파벳

# 새로운 결과 문자열
result = ""

# 한 글자씩 비교
# 인덱스 활용 순회
for index in range(len(string)):
    # print(string[index])
    char = string[index]
    
    # 포함되지 않은 문자 찾기
    # print(char, char not in compare_word)
    if char not in compare_word:
        # 포함되지 않은 문자라면
        # 방법 1. end 속성을 활용
        # print(char, end="")
        
        # 방법 2. 새로운 문자열 만들기 (추천)
        result += char

print(result)