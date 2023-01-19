# 나무 조각

# 입력 문자열
input_numbers = "2 3 4 5 1"
input_numbers = input_numbers.split()

# 숫자 리스트
numbers = []

for number in input_numbers:
    numbers.append(int(number))

# print(numbers)
while True:
    # 시작 : 0 -> 마지막 - 1 : 3
    for i in range(0, len(numbers) -1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

            result = ""
            for number in numbers:
                result += str(number) + " "
            
            print(result)
    
    if numbers == [1,2,3,4,5]:
        break

    # # 첫 번째 조각의 수 > 두 번째 조각의 수 ???
    # if numbers[0] > numbers[1]:
    #     # 조건식이 성립하면 값을 교환
    #     numbers[0], numbers[1] = numbers[1], numbers[0]
        
    #     result = ""
    #     for number in numbers:
    #         result += str(number) + " "

    #     # 값을 확인
    #     print(result)

    # if numbers[1] > numbers[2]:
    #     numbers[1], numbers[2] = numbers[2], numbers[1]
    #     result = ""
    #     for number in numbers:
    #         result += str(number) + " "
    #     # 값을 확인
    #     print(result)

    # if numbers[2] > numbers[3]:
    #     numbers[2], numbers[3] = numbers[3], numbers[2]
        
    #     result = ""
    #     for number in numbers:
    #         result += str(number) + " "

    #     # 값을 확인
    #     print(result)

    # if numbers[3] > numbers[4]:
    #     numbers[3], numbers[4] = numbers[4], numbers[3]
    #     result = ""
    #     for number in numbers:
    #         result += str(number) + " "
    #     # 값을 확인
    #     print(result)

    # if numbers == [1, 2, 3, 4, 5]:
    #     break


# 이중 반복문 해결할 떄
# 처음부터 이중 반복으로 접근하면 어렵습니다.

# 작은 단위로 문제를 해결하기 -> 알고리즘 풀이에서 중요한 팁!