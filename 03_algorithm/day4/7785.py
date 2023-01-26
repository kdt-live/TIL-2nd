# 회사에 있는 사람
# 그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.
# enter / leave
# 현재 사람의 상태가 enter -> 회사에 있음.

"""
4
Baha enter
Askar enter
Baha leave
Artem enter
"""
# input_list = [
#     "Baha enter",
#     "Askar enter",
#     "Baha leave",
#     "Artem enter"
# ]

# # 사람의 상태를 기록할 변수
# log_dict = {}

# n = 4
# for i in range(n): # n 만큼 출입 기록 입력
#     # name, log = input_list[i]
#     # print(input_list[i])
#     name, log = input_list[i].split()
#     # print(name,log)

#     # 사람의 상태(출입) 기록
#     # key(사람) - value(출입 상태)
#     log_dict[name] = log
    
# # print(log_dict)

# # 현재 사람의 상태가 enter만 남긴다.

# # 남긴다 -> enter 리스트에 저장한다.
# enter_name_list = []

# # 이름과 출입 상태를 함께 순회
# for name, log in log_dict.items():
#     if log == "enter":
#         # 저장
#         enter_name_list.append(name)

# # print(enter_name_list)

# # # sorted() 정렬 함수
# enter_name_list = sorted(enter_name_list,reverse=True)

# for name in enter_name_list:
#     print(name)


dict_ = {
    3: ['x','cc'],
    1: ['x','aa'],
    2: ['x','bb'],
}

# print(dict_)
print(dict_.items())

A_sorted = sorted(dict_.items(), key = lambda x: -x[0])
print(A_sorted)

B_sorted = sorted(dict_.items(), key = lambda x: x[1],reverse=True)
print(B_sorted)

C_sorted = sorted(dict_.items(), key = lambda x: x[1][1])
print(C_sorted)