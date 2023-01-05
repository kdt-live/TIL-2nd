number_list = [-12, -10, -1, -20, -3, -4, -5]

# max_value = 0
# 만약, 수 제한이 없다면? 초기값을 첫번째 값으로!
max_value = number_list[0]
# number_list 반복, number!
for number in number_list:
    # 만약에 max_value보다 number가 크면!
    if max_value < number:
        # 값 교체 
        max_value = number

print(max_value)