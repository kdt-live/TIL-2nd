import random

def get_lotto_1(n):
    result = []
    for i in range(n):
        result.append(sorted(random.sample(range(1, 46), 6)))
    return result

def get_lotto_price_1(n):
    return n*1000


# 사용하는 사람.. 
# NUM_OF_LOTTO = 2
# print(get_lotto(2))
# print(get_lotto_price(2))
# [[5, 17, 19, 33, 41, 42], [3, 12, 26, 27, 37, 39]]            
# 2000 