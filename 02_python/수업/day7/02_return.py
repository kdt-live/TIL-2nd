def foo():
    return 1, 2, 3

print(foo())
print(type(foo()))

def boo():
    a = 1 + 2

print(boo())


# return
# 명시적인 return문 없는 경우 : None
# 여러 값을 return 하는 경우 : tuple

a = divmod(4, 2)
print(a)