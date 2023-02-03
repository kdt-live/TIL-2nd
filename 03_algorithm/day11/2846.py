
N = 8
list_ = [12, 20, 1, 3, 4, 4, 11, 1]

# 가장 큰 오르막길 길이를 저장할 변수
max_length = 0

# 첫 번째 숫자(오르막길의 시작 높이)
start = 0

# 마지막 숫자(오르막길의 끝 높이)
end = 0

for i in range(1, N):
    # 뒷 숫자가 앞 숫자보다 큰가요?
    # 오르막길인가요?
    if list_[i] > list_[i-1]:
        # 오르막길 구간

        # start가 0 일 때 
        # 오르막길이 시작을 하지 않았을 때
        # start(시작)을 저장
        if start == 0:
            start = list_[i - 1]

        # 마지막 인덱스도 오르막길일 때
        if i == N - 1:
            end = list_[i]
            length = end - start

            if max_length < length:
                max_length = length

    
    # 오르막길이 끝이날 때
    elif list_[i] <= list_[i-1]:
        # 오르막길이 시작했는지 확인
        # start != 0 ?
        if start != 0:
            end = list_[i-1]
            
            # 오르막길의 길이
            length = end - start

            if max_length < length:
                max_length = length

            # 새로운 오르막길의 시작을 위해서
            start = 0

print(max_length)