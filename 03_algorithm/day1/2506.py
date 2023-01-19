N = "10"
answers = "1 0 1 1 1 0 0 1 1 0"
# N = input()
# answers = input()

N = int(N)
# print(type(N), N)

answers = answers.split()
# print(answers)
numbers = []
for answer in answers:
    numbers.append(int(answer))

# print(N)
# print(numbers)

total = 0   # 총합을 저장할 변수
score = 0 # 연속으로 맞춘 개수를 저장할 변수

# for 반복문 -> while 반복문
for number in numbers:
    # 1이면 정답, 0이면 오답
    if number == 1:
        # 정답일 때 연속으로 맞춘 개수 up
        score += 1
        total += score

    else:
        # 오답일 때 연속으로 맞춘 개수 0 초기화
        score = 0

    # print(number, score)
print(total)