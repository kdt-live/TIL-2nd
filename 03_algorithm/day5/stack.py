# 0이 나오면 가장 최근에 쓴 수를 지운다. 
 
# Input 
numbers = [1, 3, 5, 4, 0, 0, 7, 0, 0, 6] 

stack = []
# 로직(순회)
for number in numbers:
    # 0이면 스택에서 꺼내버리고
    if number == 0:
        stack.pop()
    # 아니면 스택에 추가한다. 
    else:
        stack.append(number)

print(sum(stack))
