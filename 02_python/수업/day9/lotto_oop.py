# Input : 
    # n 로또 번호 세트 수
# Output :
    # 오늘 지른 로또 금액
    # 번호 
# ===========================
# Data :
    # N 세트 수 
    # Lotto 번호 
# 기능 : 
    # 로또 구매 금액 계산
import random

class Lotto:

    def __init__(self, n):
        self.n = n 
        self.lotto_numbers = []
        for i in range(n):
            self.lotto_numbers.append(sorted(random.sample(range(1, 46), 6)))

    def update_numbers(self):
        self.lotto_numbers = []
        for i in range(self.n):
            self.lotto_numbers.append(sorted(random.sample(range(1, 46), 6)))
        return self.lotto_numbers

    def pprint(self):
        print('여러분의 행운번호-!')
        for numbers in self.lotto_numbers:
            print(numbers)
            print('=================')

    def get_price(self):
        return self.n * 1000