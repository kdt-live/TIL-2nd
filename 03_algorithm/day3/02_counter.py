from collections import Counter 

print(Counter('pen pineapple apple pen'))
print(Counter('pen pineapple apple pen').most_common())
print(Counter('pen pineapple apple pen').most_common(2))

