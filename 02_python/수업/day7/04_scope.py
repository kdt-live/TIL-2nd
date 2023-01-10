print(sum)

# global scope
a = 10 

# local scope
def foo():
    b = 10 

foo()
print(b) # NameError!