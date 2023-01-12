import random

def get_lotto(n):
    # Input : 
     # n 로또 번호 세트 수
    # Output :
     # 오늘 지른 로또 금액
     # 번호 
    result = []
    for i in range(n):
        result.append(sorted(random.sample(range(1, 46), 6)))
    return n*1000, result

# # 사용하는 사람..
# print(get_lotto(2))
# (2000, [[3, 4, 24, 29, 41, 45], [18, 20, 26, 33, 39, 45]])   