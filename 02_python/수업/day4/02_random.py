# 1. 모듈을 가져오는 것!
import random

menu = ['햄버거', '국밥', '초밥']
print(random.choice(menu))

# 로또 추첨 코드 작성
# random.sample(population, k)
# Return a k length list   6개 숫자
# the population sequence. 1~45개 숫자 중 : range(1, 46)

for i in range(5):
    numbers = range(1, 46)
    lucky_numbers = random.sample(numbers, 6)
    print(sorted(lucky_numbers))

students = ['민욱', '홍엽', '현석', '정은']
print(students)
random.shuffle(students)
print(students)