from collections import deque 

a = [1, 2, 3, 4, 5]
d = deque(a)
d.rotate(2)
print(d)

a = [1, 2, 3, 4, 5]
d = deque(a)
d.rotate(-2)
print(d)