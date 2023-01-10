a = 5

def foo():
    print(a) # Local scope에 a가 없네?

foo()

a = 5

def boo():
    global a
    a = 3
    print(a) 

boo()
print(a)
# a = 5 + 6
# boo()
# a = foo()