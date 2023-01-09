locations = ['서울', '서울', '대전', '부산', '대전']
result = []

# 지역을 하나씩 반복
for location in locations:
    # 만약에 결과 통에 없다면,
    if location not in result:
        # 결과 통에 추가
        result.append(location)

print(result)
print(len(result))
print(set(locations))
print(len(set(locations)))

# dictionary : 키와 값의 모음