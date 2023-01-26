"""
어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.

이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 
여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.

다음과 같은 수 분포가 있으면,

10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3

최빈수는 8이 된다.

최빈수를 출력하는 프로그램을 작성하여라.

(단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).
"""

number_list = [10, 1, 9, 9, 9, 2, 8, 8, 4, 9, 10, 8, 3]

# 숫자 개수 카운팅을 위한 딕셔너리
number_dict = {}

for number in number_list:
    # 숫자(number)가 딕셔너리의 키(Key)
    if number in number_dict.keys():
        number_dict[number] += 1

    # 숫자(number)가 딕셔너리의 키(Key)가 아닐 때
    elif number not in number_dict.keys():
        # 아닐 때 어떤 로직이 필요할까요?
        # 처음 등장한 숫자기 때문에 1로 초기화
        number_dict[number] = 1

# 숫자 개수 확인
# print(number_dict)

# 최빈수를 어떻게 찾을까?
# 최빈수가 몇인지를 우리는 저장해야합니다.
max_count = 0

# 최빈수에 해당하는 점수를 저장할 변수
result_score = 0

# print(number_dict.items())
# 키(숫자) - 값(개수)
for score, count in number_dict.items():
    # print(score, count)
    # 개수(count)가 현재까지의 최빈수(max_count)도 많다면
    if count > max_count:
        max_count = count
        result_score = score

    # 개수(count)가 현재 최빈수와 동일한 경우
    if count == max_count:
        # 현재 점수(score)가 현재 최빈수 점수보다 클 때
        if score > result_score:
            # 현재 정답 점수 갱신
            result_score = score

print(result_score)

# 이 문제에서 우리가 배워야할 점? 얻어야할 점? 얻어야할 스킬?
# 반복문 내부에서 값을 변화 
# 하나의 값이 아니라 두 개 이상의 값을 변화(갱신)


# 숫자 리스트가 있을 때 가장 큰 숫자와 그 숫자의 위치(index)는?
